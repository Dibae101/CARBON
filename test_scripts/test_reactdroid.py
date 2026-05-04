#!/usr/bin/env python3
"""
Test all bugs against ReActDroid and write reactdroid_log.txt into each Dataset bug folder.

ReActDroid approach:
  1. Takes a crash description (one sentence)
  2. Uses LLM to predict which page the crash occurs on
  3. Uses LLM + ReAct framework to navigate the app step by step
  4. Checks logcat for FATAL EXCEPTION to confirm crash reproduction

Automatically starts and stops Appium server.

Usage:
    python3 test_reactdroid.py
    python3 test_reactdroid.py --dry-run
    python3 test_reactdroid.py --category swipe
"""

import os, re, sys, shutil, subprocess, time, signal, atexit
from pathlib import Path

WORKSPACE       = Path(__file__).resolve().parent.parent
REACTDROID_DIR  = WORKSPACE / "test_repo" / "ReActDroid"
DATASET_DIR     = WORKSPACE / "Dataset"
ADB             = Path.home() / "Library" / "Android" / "sdk" / "platform-tools" / "adb"
AAPT            = Path.home() / "Library" / "Android" / "sdk" / "build-tools"

MAX_STEPS       = 30
TIMEOUT         = 900  # 15 min per bug
APPIUM_PORT     = 4723

_appium_proc = None


def start_appium():
    """Start Appium server in background."""
    global _appium_proc
    
    # Check if already running
    try:
        import requests
        r = requests.get(f"http://localhost:{APPIUM_PORT}/status", timeout=3)
        if r.status_code == 200:
            print(f"Appium: ✅ Already running on port {APPIUM_PORT}")
            return True
    except:
        pass
    
    print(f"Appium: Starting on port {APPIUM_PORT}...")
    appium_log = open(WORKSPACE / "appium.log", "w")
    appium_env = {**os.environ,
                  'ANDROID_HOME': os.path.expanduser('~/Library/Android/sdk'),
                  'ANDROID_SDK_ROOT': os.path.expanduser('~/Library/Android/sdk')}
    _appium_proc = subprocess.Popen(
        ["appium", "--port", str(APPIUM_PORT), "--relaxed-security"],
        stdout=appium_log, stderr=appium_log, env=appium_env,
    )
    
    # Wait for Appium to be ready
    for i in range(30):
        time.sleep(2)
        try:
            import requests
            r = requests.get(f"http://localhost:{APPIUM_PORT}/status", timeout=3)
            if r.status_code == 200:
                print(f"Appium: ✅ Started (PID {_appium_proc.pid})")
                return True
        except:
            pass
    
    print("Appium: ❌ Failed to start after 60s")
    return False


def stop_appium():
    """Stop Appium server."""
    global _appium_proc
    if _appium_proc and _appium_proc.poll() is None:
        print("Appium: Stopping...")
        _appium_proc.terminate()
        try:
            _appium_proc.wait(timeout=10)
        except:
            _appium_proc.kill()
        print("Appium: Stopped")
        _appium_proc = None


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


def get_activity_from_apk(apk_path):
    """Get launcher activity — try aapt first, then install and query device."""
    aapt_bin = find_aapt()
    try:
        result = subprocess.run([aapt_bin, "dump", "badging", str(apk_path)],
                                capture_output=True, text=True, timeout=30)
        for line in result.stdout.splitlines():
            if "launchable-activity:" in line:
                m = re.search(r"name='([^']+)'", line)
                if m: return m.group(1)
    except: pass
    return None


def get_activity_from_device(serial, package):
    """Get launcher activity by querying the installed app on device."""
    try:
        result = run_adb("-s", serial, "shell", "cmd", "package", "resolve-activity",
                         "--brief", package, timeout=10)
        for line in result.stdout.splitlines():
            if "/" in line and package in line:
                activity = line.strip().split("/")[-1]
                if activity.startswith("."):
                    return activity
                return activity
        # Fallback: dumpsys
        result = run_adb("-s", serial, "shell", "dumpsys", "package", package, timeout=10)
        in_activity = False
        for line in result.stdout.splitlines():
            if "android.intent.action.MAIN" in line:
                in_activity = True
            if in_activity and package in line and "/" in line:
                parts = line.strip().split()
                for p in parts:
                    if "/" in p and package in p:
                        activity = p.split("/")[-1]
                        return activity
    except: pass
    return None


def uninstall_package(serial, package):
    if package:
        run_adb("-s", serial, "shell", "pm", "uninstall", package, timeout=30)
        time.sleep(2)


def parse_bug_report(path):
    fields = {}
    if not path.exists(): return fields
    text = path.read_text(errors="replace")
    for line in text.splitlines():
        for key in ("App", "Version", "Issue", "Primary Gesture"):
            if line.startswith(f"{key}:"):
                fields[key] = line.split(":", 1)[1].strip()
                break
    # Get the title (first line) as crash description
    fields['crash_desc'] = text.splitlines()[0] if text.splitlines() else ""
    # Get steps
    steps = []
    in_steps = False
    for line in text.splitlines():
        if "Steps to Reproduce:" in line:
            in_steps = True; continue
        if in_steps and re.match(r'^\s+\d+\.', line):
            steps.append(line.strip())
        elif in_steps and line.strip() and not re.match(r'^\s+\d+\.', line):
            if any(k in line.lower() for k in ['expected', 'actual', '---']): break
    fields['steps'] = steps
    fields['steps_text'] = ' '.join(s.lstrip('0123456789. ') for s in steps)
    return fields


def run_reactdroid_test(crash_desc, package, activity, serial, port, save_path):
    """Run ReActDroid's pipeline on a bug."""
    os.makedirs(save_path, exist_ok=True)
    
    # Create temp directories ReActDroid expects
    temp_dir = REACTDROID_DIR / "Data" / "Temp"
    for d in ["chat_log", "backup", "logcat"]:
        (temp_dir / d).mkdir(parents=True, exist_ok=True)
    # Create placeholder files
    (temp_dir / "cur_screen.png").touch()
    (temp_dir / "cur_screen.xml").write_text("<hierarchy></hierarchy>")

    script = f'''#!/usr/bin/env python3
import sys, os, time, logging
sys.path.insert(0, "{REACTDROID_DIR}")
os.chdir("{REACTDROID_DIR}")

# Add ADB to PATH and set ANDROID_HOME
os.environ["PATH"] = os.path.expanduser("~/Library/Android/sdk/platform-tools") + ":" + os.path.expanduser("~/Library/Android/sdk/emulator") + ":" + os.environ.get("PATH", "")
os.environ["ANDROID_HOME"] = os.path.expanduser("~/Library/Android/sdk")
os.environ["ANDROID_SDK_ROOT"] = os.path.expanduser("~/Library/Android/sdk")

# Create all temp directories ReActDroid expects (relative to cwd)
for d in ["Data/Temp/chat_log", "Data/Temp/backup", "Data/Temp/logcat", "Data/Temp/input",
          "../Data/Temp/chat_log", "../Data/Temp/backup", "../Data/Temp/logcat", "../Data/Temp/input",
          "Data/AppState/TestApp", "../Data/AppState/TestApp"]:
    os.makedirs(d, exist_ok=True)
# Create placeholder files
open("Data/Temp/cur_screen.png", "a").close()
open("Data/Temp/cur_screen.xml", "a").close()
open("../Data/Temp/cur_screen.png", "a").close()
open("../Data/Temp/cur_screen.xml", "a").close()

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

from tool.environment import EmulatorEnv
from tool.memory import Memory
from tool.observe import Observer
from tool.action import Action
from llm.chat import Chat
from main.utils import check_crash, perform_logcat

app_info = {{
    "app_pkg": "{package}",
    "app_acti": "{activity}",
    "app_name": "TestApp",
    "crash_desc": """{crash_desc}""",
}}

crash_info = {{
    "crash_desc": """{crash_desc}""",
    "crash_page": "",
    "xml_path": "",
    "crash_page_id": "unknown",
}}

print(f"[ReActDroid] Package: {{app_info['app_pkg']}}")
print(f"[ReActDroid] Activity: {{app_info['app_acti']}}")
print(f"[ReActDroid] Crash desc: {{crash_info['crash_desc'][:100]}}")

try:
    # Start logcat monitoring
    perform_logcat()
    
    # Initialize environment (connects via Appium)
    env = EmulatorEnv(app_info)
    memory = Memory(app_info, env)
    observer = Observer(env, memory, app_info)
    action = Action(env, memory, observer)
    chat = Chat(memory, crash_info)
    
    print("[ReActDroid] Initialized. Starting exploration...")
    
    crashed = False
    for step_i in range({MAX_STEPS}):
        logging.info(f"Step {{step_i + 1}}")
        
        try:
            observe_res = observer.observe(add_visit_time=True)
            page_id = observe_res["page_id"]
            
            choose_result = chat.choose_action(observe_res)
            choose_action_key = choose_result["action"]
            
            print(f"  Step {{step_i+1}}: [{{choose_result.get('thought','')[:80]}}] -> {{choose_action_key}}")
            
            action.perform_action(page_id, choose_action_key)
            
            dst_observe = observer.observe(add_visit_time=False)
            dst_page = dst_observe["page_id"]
            memory.update_action(page_id, choose_action_key, dst_page)
            
            if dst_observe["page_id"] == "out of app" or dst_observe["page_id"] == "empty page":
                # Check if crash happened
                if check_crash():
                    print(f"[ReActDroid] CRASH DETECTED at step {{step_i+1}}!")
                    crashed = True
                    break
                env.relaunch_app()
                time.sleep(2)
            elif choose_action_key != "Back to previous page":
                memory.stg.update_previous_page(dst_page, page_id)
            
            # Periodic crash check
            if step_i % 5 == 0 and check_crash():
                print(f"[ReActDroid] CRASH DETECTED at step {{step_i+1}}!")
                crashed = True
                break
                
        except Exception as e:
            print(f"  Step {{step_i+1}} error: {{e}}")
            if check_crash():
                print(f"[ReActDroid] CRASH DETECTED after error!")
                crashed = True
                break
            try:
                env.relaunch_app()
                time.sleep(2)
            except:
                # Session might be broken — try to recreate it
                try:
                    env.driver.quit()
                except:
                    pass
                try:
                    time.sleep(3)
                    env.init_appium(app_info)
                    time.sleep(2)
                except:
                    print(f"  Could not recover session, stopping.")
                    break
    
    if crashed:
        print(f"[ReActDroid] SUCCESS — crash reproduced in {{step_i+1}} steps")
    else:
        print(f"[ReActDroid] FAIL — no crash after {MAX_STEPS} steps")
    
    # Clean up Appium session
    try:
        env.driver.quit()
    except:
        pass
        
except Exception as e:
    print(f"[ReActDroid] ERROR: {{e}}")
    import traceback
    traceback.print_exc()
    # Clean up Appium session on error too
    try:
        env.driver.quit()
    except:
        pass
'''
    
    tmp = Path(save_path) / "_reactdroid_run.py"
    tmp.write_text(script)
    
    start = time.time()
    try:
        proc = subprocess.run(
            [sys.executable, str(tmp)],
            capture_output=True, text=True, timeout=TIMEOUT,
            env={**os.environ, 'PYTHONUNBUFFERED': '1', 'VIRTUAL_ENV': '',
                 'ANDROID_HOME': os.path.expanduser('~/Library/Android/sdk'),
                 'ANDROID_SDK_ROOT': os.path.expanduser('~/Library/Android/sdk')},
        )
        elapsed = time.time() - start
        stdout = proc.stdout
        stderr = proc.stderr
    except subprocess.TimeoutExpired as e:
        elapsed = time.time() - start
        stdout = (e.stdout or b"").decode(errors="replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
        stderr = "TIMEOUT"
    except Exception as e:
        elapsed = time.time() - start
        stdout = ""
        stderr = str(e)
    finally:
        try: tmp.unlink()
        except: pass
    
    # Determine result
    success = "SUCCESS" in stdout and "crash reproduced" in stdout.lower()
    if "CRASH DETECTED" in stdout:
        success = True
    
    fail_reason = ""
    if success:
        m = re.search(r"crash reproduced in (\d+) steps", stdout)
        fail_reason = f"ReActDroid triggered a crash in {m.group(1)} steps." if m else "Crash detected."
    elif "ERROR" in stdout:
        fail_reason = "ReActDroid encountered an error during execution."
        err_lines = [l for l in stdout.splitlines() if "ERROR" in l or "error" in l.lower()]
        if err_lines:
            fail_reason += f" {err_lines[-1][:200]}"
    elif "TIMEOUT" in stderr:
        fail_reason = f"ReActDroid timed out after {TIMEOUT}s without reproducing the crash."
    else:
        fail_reason = f"ReActDroid completed {MAX_STEPS} steps without triggering the expected crash."
    
    return {
        "stdout": stdout, "stderr": stderr,
        "elapsed": elapsed, "success": success,
        "fail_reason": fail_reason,
    }


def write_reactdroid_log(bug_dir, info, result):
    status = "SUCCESS" if result['success'] else "FAIL"
    log = f"""ReActDroid Test Log
{'='*60}
App:              {info.get('App', 'unknown')}
Issue:            {info.get('Issue', 'N/A')}
Version:          {info.get('Version', 'N/A')}
Primary Gesture:  {info.get('Primary Gesture', 'N/A')}
Category:         {info.get('category', 'N/A')}
Test Result:      {status}
Execution Time:   {result['elapsed']:.1f}s
{'='*60}

Result Reason:
  {result['fail_reason']}

{'='*60}
FULL EXECUTION LOG (stdout)
{'='*60}
{result['stdout'] if result['stdout'].strip() else '(empty)'}

{'='*60}
STDERR
{'='*60}
{result['stderr'] if result['stderr'].strip() else '(none)'}
"""
    (bug_dir / "reactdroid_log.txt").write_text(log, encoding="utf-8")


def main():
    dry_run = "--dry-run" in sys.argv
    cat_filter = None
    for i, arg in enumerate(sys.argv):
        if arg == "--category" and i + 1 < len(sys.argv):
            cat_filter = sys.argv[i + 1]

    if not dry_run:
        serial, port = detect_device()
        print(f"Device: {serial} (port {port})")
        
        # Start Appium
        if not start_appium():
            print("Cannot proceed without Appium. Exiting.")
            sys.exit(1)
        atexit.register(stop_appium)
    else:
        serial, port = "emulator-5554", "5554"

    # Collect bugs
    bugs = []
    for cat_dir in sorted(DATASET_DIR.iterdir()):
        if not cat_dir.is_dir(): continue
        cat = cat_dir.name
        if cat_filter and cat_filter not in cat: continue
        for bug_dir in sorted(cat_dir.iterdir()):
            if not bug_dir.is_dir() or bug_dir.name == "test_logs": continue
            # Resume: skip if already tested
            if (bug_dir / "reactdroid_log.txt").exists(): continue
            bugs.append((cat, bug_dir))

    print(f"\n{'='*70}")
    print(f"  ReActDroid Bug Tester")
    print(f"  Bugs to test: {len(bugs)}")
    print(f"{'='*70}\n")

    for idx, (cat, bug_dir) in enumerate(bugs, 1):
        name = bug_dir.name.removesuffix(" Tested")
        br_path = bug_dir / "bug_report.txt"
        info = parse_bug_report(br_path)
        info['category'] = cat

        print(f"{'─'*70}")
        print(f"[{idx}/{len(bugs)}] [{cat}] {name}")
        print(f"  App: {info.get('App', '?')} | Crash: {info.get('crash_desc', '?')[:60]}")

        if dry_run:
            print(f"  [DRY RUN]")
            continue

        # Find APK
        apks = list(bug_dir.glob("*.apk"))
        if not apks:
            print(f"  ⚠ No APK")
            result = {"stdout": "", "stderr": "No APK", "elapsed": 0,
                      "success": False, "fail_reason": "No APK file available."}
            write_reactdroid_log(bug_dir, info, result)
            continue

        apk_path = apks[0]
        package = get_package_from_apk(apk_path)
        activity = get_activity_from_apk(apk_path)

        # Install APK first (needed for activity lookup fallback)
        go_home(serial)
        # Clear logcat before each test to prevent stale crash detection
        run_adb("-s", serial, "logcat", "-c", timeout=10)
        if package:
            uninstall_package(serial, package)
        run_adb("-s", serial, "install", "-t", "-r", "-d", "-g", str(apk_path), timeout=120)
        time.sleep(2)

        # If no activity from aapt, try querying the installed app
        if not activity and package:
            activity = get_activity_from_device(serial, package)

        if not package or not activity:
            print(f"  ⚠ Could not extract package/activity (pkg={package}, act={activity})")
            result = {"stdout": "", "stderr": f"No package/activity. pkg={package} act={activity}", "elapsed": 0,
                      "success": False, "fail_reason": f"Could not determine launcher activity. Package: {package}"}
            write_reactdroid_log(bug_dir, info, result)
            continue

        # Build crash description from bug report
        crash_desc = info.get('crash_desc', '')
        if info.get('steps_text'):
            crash_desc = f"{crash_desc}. Steps: {info['steps_text']}"

        # Run ReActDroid
        save_path = str(bug_dir / "reactdroid_output")
        print(f"  [ReActDroid] Running...")
        result = run_reactdroid_test(crash_desc, package, activity, serial, port, save_path)

        status = "SUCCESS" if result['success'] else "FAIL"
        print(f"  [ReActDroid] {status} ({result['elapsed']:.1f}s)")

        write_reactdroid_log(bug_dir, info, result)

        # Cleanup
        if package:
            run_adb("-s", serial, "shell", "pm", "clear", package, timeout=15)
            run_adb("-s", serial, "shell", "am", "force-stop", package, timeout=10)
            uninstall_package(serial, package)
        go_home(serial)
        run_adb("-s", serial, "logcat", "-c", timeout=10)
        run_adb("-s", serial, "shell", "cmd", "package", "set-home-activity",
                "com.google.android.apps.nexuslauncher/.NexusLauncherActivity")
        time.sleep(1)

    print(f"\n{'='*70}")
    print(f"  Done!")
    print(f"{'='*70}")
    
    stop_appium()


if __name__ == "__main__":
    main()
