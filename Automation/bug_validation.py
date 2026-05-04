

from utils import  get_logcat, clear_logcat
from datetime import datetime



def log_and_save_history(reprot_file_name, start_time, response_time, total_commands, history, package_name, error_type):
    execution_time = (datetime.now() - start_time).total_seconds()
    print(f"!!!{error_type}!!!. Execution time: {execution_time} seconds")
    print(f"!!!Response Times: {response_time}. Total Commands: {total_commands}")
    

def check_crash(device_port):
    logcat = get_logcat(device_port)
    if 'FATAL' in logcat:
        print('Found fatal')
        return True
    return False


def check_logcat_exceptions(device_port, package_name=None):
    """
    Scan error-level logcat for exception keywords that indicate silent
    app failures — operations that appear successful on-screen but actually
    fail (corrupted files, 0-byte exports, failed saves, camera errors, etc.).

    Uses get_logcat() which runs:  adb logcat -d *:E

    Two-tier keyword matching to reduce Android system noise:
      - CRITICAL keywords (FATAL EXCEPTION, ANR) → always matched
      - APP keywords (IOException, etc.) → only matched when the log line
        contains the app's package_name

    Args:
        device_port:  emulator port (e.g. '5554')
        package_name: app package to filter by (e.g. 'com.example.app').
                      If None, APP keywords match all lines (noisier).

    Returns:
        (bool, list[str]): (exception_found, up-to-10 deduplicated log lines)
    """
    # Tier 1 — always catch regardless of package
    CRITICAL_KEYWORDS = [
        'FATAL EXCEPTION',
        'ANR in',
    ]

    # Tier 2 — only catch in the app's own process
    APP_KEYWORDS = [
        # File & I/O
        'IOException', 'FileNotFoundException', 'ZipException',
        'FileNotFound', 'No such file', 'Permission denied',
        'Read-only file system', 'No space left', 'corrupt',
        # Null / State / Argument
        'NullPointerException', 'IllegalStateException',
        'IllegalArgumentException',
        # Runtime
        'RuntimeException', 'OutOfMemoryError', 'StackOverflowError',
        # Security
        'SecurityException',
        # Camera & Media
        'CameraAccessException', 'MediaCodec error',
        'MediaRecorder error',
    ]

    logcat_output = get_logcat(device_port)
    if not logcat_output:
        return False, []

    matches = []
    for line in logcat_output.splitlines():
        line_stripped = line.strip()
        if not line_stripped:
            continue

        # Tier 1: Always catch critical / fatal exceptions
        if any(kw in line for kw in CRITICAL_KEYWORDS):
            matches.append(line_stripped)
            continue

        # Tier 2: App-specific exceptions (filter by package to reduce noise)
        if package_name and package_name in line:
            if any(kw in line for kw in APP_KEYWORDS):
                matches.append(line_stripped)
        elif not package_name:
            # No package filter — match all (noisier but useful as fallback)
            if any(kw in line for kw in APP_KEYWORDS):
                matches.append(line_stripped)

    # Deduplicate similar lines (first 120 chars as key)
    seen = set()
    unique = []
    for m in matches:
        key = m[:120]
        if key not in seen:
            seen.add(key)
            unique.append(m)

    if unique:
        print(f"[Logcat Monitor] Found {len(unique)} exception(s) in logcat")

    # Cap at 10 lines to avoid prompt bloat
    return len(unique) > 0, unique[:10]















