#!/usr/bin/env python3
"""
Test all bugs against ReBL and write rebl_log.txt into each Dataset bug folder.

ReBL (Reproduction of Bugs with LLM):
  - Uses LLM (Gemini 2.5 Pro) with text-only UI hierarchy
  - Feedback-driven approach using entire bug report
  - Basic actions: click, long_click, swipe, scroll, set_text, back, orientation
  - Dual oracle: crash detection (logcat) + LLM verification

Usage:
    python3 test_rebl.py
    python3 test_rebl.py --dry-run
    python3 test_rebl.py --category swipe
"""

import os, re, sys, subprocess, time, shutil
from pathlib import Path

WORKSPACE    = Path(__file__).resolve().parent.parent
REBL_DIR     = WORKSPACE / "test_repo" / "REBL" / "Automation"
DATASET_DIR  = WORKSPACE / "Dataset"
ADB          = Path.home() / "Library" / "Android" / "sdk" / "platform-tools" / "adb"
AAPT         = Path.home() / "Library" / "Android" / "sdk" / "build-tools"
ANDROID_HOME = str(Path.home() / "Library" / "Android" / "sdk")

TIMEOUT      = 1800  # 30 min per bug


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
    text = path.read_text(errors="replace")
    for line in text.splitlines():
        for key in ("App", "Version", "Issue", "Primary Gesture"):
            if line.startswith(f"{key}:"):
                fields[key] = line.split(":", 1)[1].strip()
                break
    fields['title'] = text.splitlines()[0] if text.splitlines() else ""
    return fields


def run_rebl_test(bug_report_path, port, serial):
    """Run ReBL's reproduction.py on a bug."""
    env = {
        **os.environ,
        'PYTHONUNBUFFERED': '1',
        'ANDROID_HOME': ANDROID_HOME,
        'ANDROID_SDK_ROOT': ANDROID_HOME,
        'PATH': f"{ANDROID_HOME}/platform-tools:{ANDROID_HOME}/emulator:{os.environ.get('PATH', '')}",
    }

    start = time.time()
    try:
        proc = subprocess.run(
            [sys.executable, str(REBL_DIR / "reproduction.py"), port, str(bug_report_path)],
            capture_output=True, text=True, timeout=TIMEOUT,
            cwd=str(REBL_DIR), env=env,
        )
        elapsed = time.time() - start
        return {
            "stdout": proc.stdout, "stderr": proc.stderr,
            "elapsed": elapsed, "returncode": proc.returncode,
        }
    except subprocess.TimeoutExpired as e:
        stdout = (e.stdout or b"").decode(errors="replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
        return {
            "stdout": stdout, "stderr": "TIMEOUT",
            "elapsed": time.time() - start, "returncode": -1,
        }
    except Exception as e:
        return {
            "stdout": "", "stderr": str(e),
            "elapsed": time.time() - start, "returncode": -1,
        }


def determine_result(result):
    """Determine SUCCESS/FAIL from ReBL's output."""
    stdout = result['stdout']
    
    last_result = None
    last_reason = ""
    for line in stdout.split("\n"):
        if "'result':" in line or '"result":' in line:
            if "success" in line.lower():
                last_result = "SUCCESS"
            elif "fail" in line.lower():
                last_result = "FAIL"
            rm = re.search(r"'reason':\s*['\"](.+?)['\"]", line)
            if not rm: rm = re.search(r'"reason":\s*"(.+?)"', line)
            if rm: last_reason = rm.group(1)
        if last_result and not last_reason:
            rm2 = re.search(r'"reason":\s*"(.+)', line)
            if not rm2: rm2 = re.search(r"'reason':\s*['\"](.+)", line)
            if rm2: last_reason = rm2.group(1).rstrip('",').rstrip("',")
    
    if last_result is None:
        if "TIMEOUT" in result.get('stderr', ''):
            last_result = "FAIL"
            last_reason = f"ReBL timed out after {TIMEOUT}s."
        else:
            last_result = "FAIL"
            last_reason = "No result declaration found in output."
    
    return last_result, last_reason


def write_rebl_log(bug_dir, info, result, final_result, reason):
    log = f"""ReBL Test Log
{'='*60}
App:              {info.get('App', 'unknown')}
Issue:            {info.get('Issue', 'N/A')}
Version:          {info.get('Version', 'N/A')}
Primary Gesture:  {info.get('Primary Gesture', 'N/A')}
Category:         {info.get('category', 'N/A')}
Test Result:      {final_result}
Execution Time:   {result['elapsed']:.1f}s
{'='*60}

Result Reason:
  {reason}

{'='*60}
FULL EXECUTION LOG (stdout)
{'='*60}
{result['stdout'] if result['stdout'].strip() else '(empty)'}

{'='*60}
STDERR
{'='*60}
{result['stderr'] if result['stderr'].strip() else '(none)'}
"""
    (bug_dir / "rebl_log.txt").write_text(log, encoding="utf-8")


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
            if (bug_dir / "rebl_log.txt").exists():
                skipped += 1
                continue
            bugs.append((cat, bug_dir))

    print(f"\n{'='*70}")
    print(f"  ReBL Bug Tester")
    print(f"  To test: {len(bugs)} | Already tested: {skipped}")
    print(f"{'='*70}\n")

    for idx, (cat, bug_dir) in enumerate(bugs, 1):
        name = bug_dir.name.removesuffix(" Tested")
        br_path = bug_dir / "bug_report.txt"
        info = parse_bug_report(br_path)
        info['category'] = cat

        print(f"{'─'*70}")
        print(f"[{idx}/{len(bugs)}] [{cat}] {name}")
        print(f"  App: {info.get('App', '?')} | Gesture: {info.get('Primary Gesture', '?')}")

        if dry_run:
            print(f"  [DRY RUN]")
            continue

        # Find APK
        apks = list(bug_dir.glob("*.apk"))
        if not apks:
            print(f"  ⚠ No APK")
            result = {"stdout": "", "stderr": "No APK", "elapsed": 0, "returncode": -1}
            write_rebl_log(bug_dir, info, result, "FAIL", "No APK file available.")
            continue

        apk_path = apks[0]
        package = get_package_from_apk(apk_path)

        # Install APK
        go_home(serial)
        run_adb("-s", serial, "logcat", "-c", timeout=10)
        if package: uninstall_package(serial, package)
        run_adb("-s", serial, "install", "-t", "-r", "-d", "-g", str(apk_path), timeout=120)
        time.sleep(2)

        # Launch app
        if package:
            run_adb("-s", serial, "shell", "monkey", "-p", package,
                    "-c", "android.intent.category.LAUNCHER", "1")
            time.sleep(3)

        # Run ReBL
        print(f"  [ReBL] Running...")
        result = run_rebl_test(br_path, port, serial)
        final_result, reason = determine_result(result)

        print(f"  [ReBL] {final_result} ({result['elapsed']:.1f}s)")
        write_rebl_log(bug_dir, info, result, final_result, reason)

        # Cleanup
        if package:
            run_adb("-s", serial, "shell", "pm", "clear", package, timeout=15)
            run_adb("-s", serial, "shell", "am", "force-stop", package, timeout=10)
            uninstall_package(serial, package)
        go_home(serial)
        run_adb("-s", serial, "logcat", "-c", timeout=10)
        time.sleep(2)

    print(f"\n{'='*70}")
    print(f"  Done!")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
