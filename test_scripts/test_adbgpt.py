#!/usr/bin/env python3
"""
Test all bugs against AdbGPT and write adbgpt_log.txt into each Dataset bug folder.

AdbGPT approach:
  1. Extract S2R entities from bug report using LLM (few-shot + CoT)
  2. For each step, capture GUI hierarchy, encode as HTML
  3. Use LLM to match entity to GUI component
  4. Execute action via ADB

AdbGPT supports: tap, input, scroll, double tap, long tap
AdbGPT CANNOT do: pinch, drag_and_drop, edge_swipe, quick_tap, swipe_region,
                   tap_screen (coordinate), home, open_notifications

Usage:
    python3 test_adbgpt.py
    python3 test_adbgpt.py --dry-run
    python3 test_adbgpt.py --category swipe
"""

import os, re, sys, shutil, subprocess, time
from pathlib import Path
from datetime import datetime

WORKSPACE    = Path(__file__).resolve().parent.parent
ADBGPT_DIR   = WORKSPACE / "test_repo" / "AdbGPT"
DATASET_DIR  = WORKSPACE / "Dataset"
ADB          = Path.home() / "Library" / "Android" / "sdk" / "platform-tools" / "adb"
AAPT         = Path.home() / "Library" / "Android" / "sdk" / "build-tools"

# AdbGPT can only attempt these gesture categories
ADBGPT_CAN_DO = {'swipe', 'scroll', 'long_press', 'orientation'}
# These require CARBON-only actions
ADBGPT_CANNOT_DO = {'double_tap', 'pinch_zoom', 'drag_and_drop', 'quick_tap'}

ADBGPT_MISSING = {
    'double_tap': ('double_tap_screen (real multi-touch)',
        'AdbGPT has a double_tap action via two sequential ADB taps, but it lacks '
        'real simultaneous multi-touch double-tap that apps with custom gesture '
        'detectors require. It also has no visual context to identify coordinate targets.'),
    'pinch_zoom': ('pinch (multi-touch)',
        'AdbGPT has no pinch/zoom gesture. It cannot send simultaneous two-finger '
        'touch events. Only supports tap, input, scroll, double tap, long tap.'),
    'drag_and_drop': ('drag_and_drop',
        'AdbGPT has no drag-and-drop action. It cannot perform long-press-then-drag '
        'gestures needed for reordering items or moving widgets.'),
    'quick_tap': ('quick_tap (timing-sensitive)',
        'AdbGPT has no timing-sensitive tap. It processes each step sequentially with '
        'LLM calls between steps, adding seconds of delay that prevents triggering '
        'race-condition bugs.'),
}


def find_aapt():
    if AAPT.is_dir():
        for v in sorted(AAPT.iterdir(), key=lambda p: p.name, reverse=True):
            c = v / "aapt"
            if c.exists(): return str(c)
    return "aapt"


def run_adb(*args, timeout=60):
    return subprocess.run([str(ADB)] + list(args),
                          capture_output=True, text=True, timeout=timeout)


def detect_device():
    result = run_adb("devices")
    for line in result.stdout.splitlines():
        line = line.strip()
        if line.startswith("emulator-") and "device" in line:
            serial = line.split()[0]
            port = serial.replace("emulator-", "")
            return serial, port
    print("ERROR: No emulator running.")
    sys.exit(1)


def go_home(serial):
    run_adb("-s", serial, "shell", "input", "keyevent", "KEYCODE_HOME")
    time.sleep(1)


def get_package_from_apk(apk_path):
    aapt_bin = find_aapt()
    try:
        result = subprocess.run([aapt_bin, "dump", "badging", str(apk_path)],
                                capture_output=True, text=True, timeout=30)
        for line in result.stdout.splitlines():
            if line.startswith("package:"):
                m = re.search(r"name='([^']+)'", line)
                if m: return m.group(1)
    except: pass
    return None


def uninstall_package(serial, package):
    if package:
        run_adb("-s", serial, "shell", "pm", "uninstall", package, timeout=30)
        time.sleep(2)


def parse_bug_report(path):
    fields = {}
    if not path.exists(): return fields
    for line in path.read_text(errors="replace").splitlines():
        for key in ("App", "Version", "Issue", "Primary Gesture"):
            if line.startswith(f"{key}:"):
                fields[key] = line.split(":", 1)[1].strip()
                break
    # Extract steps text
    text = path.read_text(errors="replace")
    steps = []
    in_steps = False
    for line in text.splitlines():
        if "Steps to Reproduce:" in line:
            in_steps = True; continue
        if in_steps and re.match(r'^\s+\d+\.', line):
            steps.append(line.strip())
        elif in_steps and line.strip() and not re.match(r'^\s+\d+\.', line):
            if any(k in line.lower() for k in ['expected', 'actual', '---']): break
    fields['steps_text'] = '\n'.join(steps)
    return fields


def run_adbgpt_test(bug_description, serial, device_port, save_path):
    """Run AdbGPT's main pipeline on a bug description."""
    # Write a runner script that imports AdbGPT and runs it
    script = f'''#!/usr/bin/env python3
import sys, os, time
sys.path.insert(0, "{ADBGPT_DIR}")
os.chdir("{ADBGPT_DIR}")

from loguru import logger
import uiautomator2 as u2
from extract_step import Extract_Steps
from guided_replay import UI, Guided_Replay
import adb

save_path = "{save_path}"
os.makedirs(save_path, exist_ok=True)
logger.add(os.path.join(save_path, "adbgpt.log"))

bug_description = """{bug_description}"""

action_prompt = """Available actions: [tap, input, scroll, double tap, long tap]\\n"""
primtive_prompt = """Action primitives: [Tap] [Component], [Scroll] [Direction], [Input] [Component] [Value], [Double-tap] [Component], [Long-tap] [Component]\\n"""
example_prompt = """Question: Extract the entity from the following ->
    "1. Open bookmark
    2. Tap \\"add new bookmark\\" and create a name with \\"a\\"
    3. Create another one with name \\"b\\"
    4. Click \\"a\\"
    5. Go back to bookmark after changing name \\"a\\" to \\"b\\"
    6. App crash"\\n"""
cot_prompt = """Answer:
    1st step is \\"Open bookmark\\". The action is \\"open\\" and the target component is \\"bookmark\\". However, there is no explicit \\"open\\" in the Available actions list. Therefore, we select the closest semantic action \\"tap\\". Following the Action primitives, the entity of the step is [Tap] [\\"bookmark\\"].
    2nd step is \\"Tap 'add new bookmark' and create a name with 'a'\\". Due to the conjunction word \\"and\\", this step can be separated into two sub-steps. For the first sub-step, the entity is [Tap] [\\"add new bookmark\\"]. For the second sub-step, the entity is [Input] [\\"name\\"] [\\"a\\"].
    3rd step is \\"Create another one with name 'b'\\". This repeats the previous steps: [Tap] [\\"add new bookmark\\"] and [Input] [\\"name\\"] [\\"b\\"].
    4th step is \\"Click 'a'\\". The entity is [Tap] [\\"a\\"].
    5th step is \\"Go back to bookmark after changing name 'a' to 'b'\\". The entity is [Input] [\\"name\\"] [\\"b\\"] then [Tap] [\\"back\\"].
    6th step is \\"App crash\\". No operations.
    Overall: 1.[Tap][\\"bookmark\\"] 2.[Tap][\\"add new bookmark\\"] 3.[Input][\\"name\\"][\\"a\\"] 4.[Tap][\\"add new bookmark\\"] 5.[Input][\\"name\\"][\\"b\\"] 6.[Tap][\\"a\\"] 7.[Input][\\"name\\"][\\"b\\"] 8.[Tap][\\"back\\"]\\n"""

question_prompt = """Question: Extract the entity from the following -> \\"{{}}\\"\\n Answer: """.format(bug_description)
prompt = action_prompt + primtive_prompt + example_prompt + cot_prompt + question_prompt

es = Extract_Steps()
step_outputs = es.infer(prompt)
print(f"Extracted {{len(step_outputs)}} steps")

d = u2.connect("emulator-{device_port}")
print(d.info)

step_i = 0
missing_i = 0
max_missing = 10
gr = Guided_Replay()
start_time = time.time()

while step_i < len(step_outputs) and missing_i < max_missing:
    logger.debug(step_outputs[step_i].step_text)
    try:
        page_source = d.dump_hierarchy(compressed=True, pretty=True)
        xml_file = open(os.path.join(save_path, f'step_{{step_i}}_hierarchy.xml'), 'w', encoding='utf-8')
        xml_file.write(page_source)
        xml_file.close()
        adb.screen_shot(f'step_{{step_i}}', save_path)
    except Exception as e:
        print(f"Error capturing state: {{e}}")
        break

    if step_outputs[step_i].action.lower() != "scroll":
        ui = UI(os.path.join(save_path, f'step_{{step_i}}_hierarchy.xml'))
        html_code = ui.encoding()

        if step_outputs[step_i].action.lower() == "input":
            step = "[{{}}] [{{}}] [{{}}]".format(step_outputs[step_i].action, step_outputs[step_i].target, step_outputs[step_i].input)
        else:
            step = "[{{}}] [{{}}]".format(step_outputs[step_i].action, step_outputs[step_i].target)

        with open(os.path.join("{ADBGPT_DIR}", 'utils/gui-1.xml'), 'r') as f:
            example_ui = f.read()

        title_prompt = "Question:\\n"
        example_ui_prompt_1 = "GUI screen: \\n{{}}\\n\\n".format(example_ui)
        example_question_prompt_1 = 'If I need to [Tap] [\\"Sign in\\"], which component id should I operate on the GUI? ->\\n'
        example_cot_prompt_1 = 'Answer: There is no explicit \\"Sign in\\" component. However, there is \\"Log in\\" button with id=6. So operate on [id=6].\\n'
        example_ui_prompt_2 = "GUI screen: \\n{{}}\\n\\n".format(example_ui)
        example_question_prompt_2 = 'If I need to [Tap] [\\"Settings\\"], which component id should I operate on the GUI? ->\\n'
        example_cot_prompt_2 = 'Answer: No explicit \\"Settings\\". Could be related to \\"drawer\\" id=0. So operate on [id=0]. [MISSING] step.\\n'

        ui_prompt = "GUI screen: \\n{{}}\\n\\n".format(html_code)
        question_prompt = "If I need to {{}}, which component id should I operate on the GUI? ->\\nAnswer:".format(step)

        prompt = title_prompt + example_ui_prompt_1 + example_question_prompt_1 + example_cot_prompt_1 + title_prompt + example_ui_prompt_2 + example_question_prompt_2 + example_cot_prompt_2 + title_prompt + ui_prompt + question_prompt

        recursive_flag, target_id = gr.infer(prompt)
        logger.info("Operate on id={{}} in the GUI screen.".format(target_id))

        if target_id is None:
            adb.back()
            missing_i += 1
            continue

        bounds = [ui.elements[target_id].bounding_box.x1, ui.elements[target_id].bounding_box.y1,
                  ui.elements[target_id].bounding_box.x2, ui.elements[target_id].bounding_box.y2]

        if step_outputs[step_i].action.lower() == "tap":
            adb.click(bounds)
        elif step_outputs[step_i].action.lower() == "double tap":
            adb.double_click(bounds)
        elif step_outputs[step_i].action.lower() == "long tap":
            adb.long_click(bounds)
        elif step_outputs[step_i].action.lower() == "input":
            adb.input_text(bounds, step_outputs[step_i].input)

        if recursive_flag:
            missing_i += 1
        else:
            step_i += 1
    else:
        direction = 'up' if 'up' in step_outputs[step_i].target else 'down'
        adb.scroll(direction)
        step_i += 1

    time.sleep(1)

elapsed = time.time() - start_time
print(f"AdbGPT completed: {{step_i}}/{{len(step_outputs)}} steps in {{elapsed:.1f}}s")
print(f"Missing steps: {{missing_i}}")
'''
    tmp = WORKSPACE / "_adbgpt_run.py"
    tmp.write_text(script)

    start = time.time()
    try:
        proc = subprocess.run(
            ["python3", str(tmp)],
            capture_output=True, text=True, timeout=600,
            cwd=str(ADBGPT_DIR),
            env={**os.environ, 'PYTHONUNBUFFERED': '1'},
        )
        elapsed = time.time() - start
        return {
            "stdout": proc.stdout, "stderr": proc.stderr,
            "elapsed": elapsed, "returncode": proc.returncode,
        }
    except subprocess.TimeoutExpired as e:
        stdout = (e.stdout or b"").decode(errors="replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
        return {
            "stdout": stdout, "stderr": "TIMEOUT after 600s",
            "elapsed": time.time() - start, "returncode": -1,
        }
    except Exception as e:
        return {
            "stdout": "", "stderr": str(e),
            "elapsed": time.time() - start, "returncode": -1,
        }
    finally:
        try: tmp.unlink()
        except: pass


def write_adbgpt_log(bug_dir, info, result):
    """Write adbgpt_log.txt with full test results."""
    status = 'SUCCESS' if result.get('success') else 'FAIL'
    logcat_section = ""
    if result.get('logcat_excerpt'):
        logcat_section = f"""
{'='*60}
LOGCAT (crash detected)
{'='*60}
{result['logcat_excerpt']}
"""
    
    log = f"""AdbGPT Test Log
{'='*60}
App:              {info.get('App', 'unknown')}
Issue:            {info.get('Issue', 'N/A')}
Version:          {info.get('Version', 'N/A')}
Primary Gesture:  {info.get('Primary Gesture', 'N/A')}
Category:         {info.get('category', 'N/A')}
Test Result:      {status}
Execution Time:   {result['elapsed']:.1f}s
Return Code:      {result.get('returncode', '?')}
{'='*60}

Result Reason:
  {result.get('fail_reason', '(no reason)')}

{'='*60}
FULL EXECUTION LOG (stdout)
{'='*60}
{result['stdout'] if result['stdout'].strip() else '(empty)'}
{logcat_section}
{'='*60}
STDERR
{'='*60}
{result['stderr'] if result['stderr'].strip() else '(none)'}
"""
    (bug_dir / "adbgpt_log.txt").write_text(log, encoding="utf-8")


def write_adbgpt_skip_log(bug_dir, info, category):
    """Write adbgpt_log.txt for bugs AdbGPT cannot attempt."""
    missing_action, reason = ADBGPT_MISSING.get(category, ('unknown', 'Unknown gesture category'))
    log = f"""AdbGPT Test Log
{'='*60}
App:              {info.get('App', 'unknown')}
Issue:            {info.get('Issue', 'N/A')}
Version:          {info.get('Version', 'N/A')}
Primary Gesture:  {info.get('Primary Gesture', 'N/A')}
Test Result:      FAIL
Execution Time:   0s
{'='*60}

AdbGPT FAILED — lacks required gesture capability.

Missing Action:   {missing_action}

Failure Reason:
  {reason}

AdbGPT's Action Set:
  tap, input, scroll, double tap, long tap

AdbGPT does NOT support:
  pinch, drag_and_drop, edge_swipe, quick_tap, tap_screen (coordinate),
  swipe_region, home, open_notifications, two_finger_swipe, rotate_gesture

{'='*60}
"""
    (bug_dir / "adbgpt_log.txt").write_text(log, encoding="utf-8")


def main():
    dry_run = "--dry-run" in sys.argv
    cat_filter = None
    for i, arg in enumerate(sys.argv):
        if arg == "--category" and i + 1 < len(sys.argv):
            cat_filter = sys.argv[i + 1]

    if not dry_run:
        serial, port = detect_device()
        print(f"Device: {serial} (port {port})")
    else:
        serial, port = "emulator-5554", "5554"

    # Collect bugs — skip already tested (resume support)
    bugs = []
    skipped = 0
    for cat_dir in sorted(DATASET_DIR.iterdir()):
        if not cat_dir.is_dir(): continue
        cat = cat_dir.name
        if cat_filter and cat_filter not in cat: continue
        for bug_dir in sorted(cat_dir.iterdir()):
            if not bug_dir.is_dir() or bug_dir.name == "test_logs": continue
            if (bug_dir / "adbgpt_log.txt").exists():
                skipped += 1
                continue
            bugs.append((cat, bug_dir))

    print(f"\n{'='*70}")
    print(f"  AdbGPT Bug Tester")
    print(f"  To test: {len(bugs)} | Already tested: {skipped}")
    print(f"{'='*70}\n")

    for idx, (cat, bug_dir) in enumerate(bugs, 1):
        name = bug_dir.name.removesuffix(" Tested")
        br_path = bug_dir / "bug_report.txt"
        info = parse_bug_report(br_path)

        print(f"{'─'*70}")
        print(f"[{idx}/{len(bugs)}] [{cat}] {name}")
        print(f"  App: {info.get('App', '?')} | Gesture: {info.get('Primary Gesture', '?')}")
        info['category'] = cat

        # Check if AdbGPT can attempt this category
        # Run ALL bugs — even ones AdbGPT likely can't do
        # Let AdbGPT try and fail naturally

        if dry_run:
            print(f"  [DRY RUN] Would test with AdbGPT")
            continue

        # Find APK
        apks = list(bug_dir.glob("*.apk"))
        if not apks:
            print(f"  ⚠ No APK — skipping")
            write_adbgpt_skip_log(bug_dir, info, "no_apk")
            continue

        apk_path = apks[0]
        package = get_package_from_apk(apk_path)

        # Install APK
        go_home(serial)
        # Clear logcat before each test to prevent stale crash detection
        run_adb("-s", serial, "logcat", "-c", timeout=10)
        if package:
            uninstall_package(serial, package)
        run_adb("-s", serial, "install", "-t", "-r", "-d", str(apk_path), timeout=120)
        time.sleep(2)

        # Launch app
        if package:
            run_adb("-s", serial, "shell", "monkey", "-p", package,
                    "-c", "android.intent.category.LAUNCHER", "1")
            time.sleep(3)

        # Get bug steps as text
        steps_text = info.get('steps_text', '')
        if not steps_text:
            steps_text = br_path.read_text(errors="replace")[:2000]

        # Run AdbGPT
        save_path = str(bug_dir / "adbgpt_output")
        print(f"  [AdbGPT] Running...")
        result = run_adbgpt_test(steps_text, serial, port, save_path)
        
        # Determine success/fail from output
        stdout = result['stdout']
        stderr = result['stderr']
        success = False
        fail_reason = ""

        # AdbGPT doesn't have a built-in oracle — it just executes steps.
        # We check multiple signals to determine success/fail:
        
        # Signal 1: App crashed (logcat check)
        logcat = ""
        try:
            lc = run_adb("-s", serial, "logcat", "-d", "*:E", timeout=5)
            logcat = lc.stdout
        except: pass
        
        crash_in_logcat = ("FATAL EXCEPTION" in logcat or "ANR in" in logcat) and package and package in logcat
        
        # Signal 2: AdbGPT completed all steps
        completed_all = False
        total_steps = 0
        done = 0
        steps_match = re.search(r'completed: (\d+)/(\d+)', stdout)
        if steps_match:
            done, total_steps = int(steps_match.group(1)), int(steps_match.group(2))
            completed_all = done == total_steps and total_steps > 0
        
        extracted_match = re.search(r'Extracted (\d+) steps', stdout)
        extracted_count = int(extracted_match.group(1)) if extracted_match else 0
        
        # Signal 3: Errors during execution
        had_errors = result['returncode'] != 0 or "Error" in stderr or "Traceback" in stderr
        
        # Signal 4: App is still running (didn't crash away)
        try:
            current_app = run_adb("-s", serial, "shell", "dumpsys", "activity", "activities", timeout=5)
            app_still_running = package in current_app.stdout if package else True
        except:
            app_still_running = True

        # Determine result
        if extracted_count == 0:
            success = False
            fail_reason = "AdbGPT failed to extract any S2R steps from the bug report. The LLM response could not be parsed into actionable steps."
        elif crash_in_logcat:
            success = True
            fail_reason = f"AdbGPT triggered a crash detected in logcat (FATAL EXCEPTION for {package})."
        elif completed_all and not had_errors:
            success = True
            fail_reason = f"AdbGPT completed all {total_steps} extracted S2R steps without errors."
        elif completed_all and had_errors:
            success = False
            fail_reason = f"AdbGPT completed steps but encountered errors: {stderr[:200]}"
        elif not completed_all:
            success = False
            if total_steps > 0:
                fail_reason = f"AdbGPT only completed {done}/{total_steps} steps. Could not match remaining steps to GUI elements."
            else:
                fail_reason = f"AdbGPT did not complete execution. Output: {stdout[-300:]}"
        
        if had_errors and not success:
            fail_reason += f"\nStderr: {stderr[:300]}"

        result['success'] = success
        result['fail_reason'] = fail_reason
        result['logcat_excerpt'] = logcat[-500:] if crash_in_logcat else ""

        status = "SUCCESS" if success else "FAIL"
        print(f"  [AdbGPT] {status} ({result['elapsed']:.1f}s)")

        write_adbgpt_log(bug_dir, info, result)

        # Cleanup
        if package:
            run_adb("-s", serial, "shell", "pm", "clear", package, timeout=15)
            run_adb("-s", serial, "shell", "am", "force-stop", package, timeout=10)
            uninstall_package(serial, package)
        go_home(serial)
        # Clear logcat after test too
        run_adb("-s", serial, "logcat", "-c", timeout=10)
        run_adb("-s", serial, "shell", "cmd", "package", "set-home-activity",
                "com.google.android.apps.nexuslauncher/.NexusLauncherActivity")
        time.sleep(1)

    print(f"\n{'='*70}")
    print(f"  Done!")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
