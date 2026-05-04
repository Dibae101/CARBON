#!/usr/bin/env python3
"""
Incremental Batch Testing Script for Bug Reproduction
Tests APKs one by one with their corresponding BRs and logs results to CSV incrementally
"""

import os
import sys
import csv
import json
import time
import subprocess
from datetime import datetime
from collections import defaultdict


class IncrementalTester:
    def __init__(self, device_port):
        self.device_port = device_port
        self.apk_dir = "APKs"
        self.br_dir = "BRs"
        self.results_file = f"test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        self.test_cases = []
        
        # Initialize CSV file
        self.init_csv()
    
    def init_csv(self):
        """Initialize CSV file with headers"""
        headers = [
            'Test_ID',
            'Timestamp',
            'APK_Name',
            'BR_File',
            'App_Name',
            'Package_Name',
            'Issue_Number',
            'Status',
            'Duration_Seconds',
            'Total_Commands',
            'GPT_Responses',
            'Bug_Reproduced',
            'Failure_Reason',
            'Log_File',
            'Remarks'
        ]
        
        with open(self.results_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
        
        print(f"Created results file: {self.results_file}\n")
    
    def get_apk_to_br_mapping(self):
        """
        Hardcoded mapping of APK files to their corresponding BR files.
        Returns list of (apk_file, br_file) tuples.
        
        Format: Each APK can have multiple BR files (one test case per BR)
        """
        # HARDCODED APK-to-BR MAPPING
        # Format: 'APK_filename': ['BR_file1.txt', 'BR_file2.txt', ...]
        hardcoded_mapping = {
            'AIMSICD_debug.apk': [
                'aimsicd_816.txt'
            ],
            'AnkiDroid-2.9alpha4.apk': [
                'ankidroid_4586.txt'
            ],
            'AnyMemo-v8.999.4_debug.apk': [
                'anymemo_18.txt'
            ],
            'Birthdroid_debug.apk': [
                'birthdroid_13.txt'
            ],
            'Bites-v1.0.apk': [
                'bites_20.txt',
                'bites_44.txt'
            ],
            'FastAdapter_debug.apk': [
                'fastadapter_394.txt'
            ],
            'FlashCards.apk': [
                'flashcards_13.txt'
            ],
            'k9_3255.apk': [
                'k9_3255.txt'
            ],
            'LibreNews-v1.4_debug.apk': [
                'librenews_22.txt',
                'librenews_23.txt',
                'librenews_27.txt'
            ],
            'markor-v0.3.2_debug.apk': [
                'markor_194.txt'
            ],
            'materialistic-76.apk': [
                'materialistic_1067.txt'
            ],
            'Memento-Calender-v3.6.apk': [
                'memento_169.txt'
            ],
            'microMathematics-v2.15.4.apk': [
                'micromathematics_39.txt'
            ],
            'newsblur-v6.10_debug.apk': [
                'newsblur_1053.txt'
            ],
            'notepad_debug.apk': [
                'notepad_23.txt'
            ],
            'obd-reader_debug.apk': [
                'obd_reader_22.txt'
            ],
            'ODK-Collect-debug.apk': [
                'odk_collect_2086.txt'
            ],
            'olam_debug.apk': [
                'olam_2.txt'
            ],
            'OpenSudoku.apk': [
                'opensudoku_148.txt',
                'opensudoku_173.txt'
            ],
            'QKSMS-v2.6.0.apk': [
                'qksms_482.txt'
            ],
            'fdroid-1821.apk': [
                'fdroid_1821.txt'
            ],
            'time_tracker-0.20-works_debug.apk': [
                'atimetracker_35.txt',
                'atimetracker_138.txt'
            ]
        }
        
        # Build test cases list
        test_cases = []
        
        for apk_file, br_files in hardcoded_mapping.items():
            apk_path = os.path.join(self.apk_dir, apk_file)
            
            # Check if APK exists
            if not os.path.exists(apk_path):
                print(f"Warning: APK not found - {apk_file}")
                continue
            
            # Add each BR file as a test case
            for br_file in br_files:
                br_path = os.path.join(self.br_dir, br_file)
                
                # Check if BR file exists
                if not os.path.exists(br_path):
                    print(f"Warning: BR file not found - {br_file}")
                    continue
                
                test_cases.append((apk_file, br_file))
        
        return test_cases
    
    def extract_br_info(self, br_file):
        """Extract app name, package name, and issue number from BR file"""
        br_path = os.path.join(self.br_dir, br_file)
        app_name = ""
        package_name = ""
        issue_number = ""
        
        try:
            with open(br_path, 'r') as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if 'App:' in line or 'App Name:' in line:
                        app_name = line.split(':', 1)[1].strip()
                    elif 'Package Name:' in line or 'Package:' in line:
                        package_name = line.split(':', 1)[1].strip()
                    elif 'Issue:' in line and 'http' in line:
                        # Extract issue number from URL
                        import re
                        match = re.search(r'/issues?/(\d+)', line)
                        if match:
                            issue_number = match.group(1)
                    
                    # Stop after first 15 lines
                    if i > 15:
                        break
        except Exception as e:
            print(f"  Warning: Could not parse {br_file}: {e}")
        
        return app_name, package_name, issue_number
    
    def parse_test_output(self, output):
        """Parse reproduction script output to extract metrics"""
        metrics = {
            'total_commands': 0,
            'gpt_responses': 0,
            'bug_reproduced': False,
            'failure_reason': '',
            'log_file': ''
        }
        
        # Count GPT messages
        metrics['gpt_responses'] = output.count('*GPT message:')
        
        # Check for bug reproduction
        if 'result: True' in output or "'result': True" in output:
            metrics['bug_reproduced'] = True
        elif 'result: False' in output or "'result': False" in output:
            metrics['bug_reproduced'] = False
            metrics['failure_reason'] = 'Bug not reproduced by GPT'
        
        # Look for command execution
        import re
        command_matches = re.findall(r'\*Command \d+:', output)
        metrics['total_commands'] = len(command_matches)
        
        # Look for log file
        log_match = re.search(r'Saved to: (.+\.json)', output)
        if log_match:
            metrics['log_file'] = log_match.group(1)
        
        # Look for errors
        if 'Error:' in output or 'Exception' in output:
            error_lines = [line for line in output.split('\n') if 'Error' in line or 'Exception' in line]
            if error_lines:
                metrics['failure_reason'] = error_lines[0][:100]
        
        return metrics
    
    def install_apk(self, apk_file, package_name):
        """Install APK on the device"""
        apk_path = os.path.join(self.apk_dir, apk_file)
        device_serial = f"emulator-{self.device_port}"
        adb_path = os.path.expanduser("~/Library/Android/sdk/platform-tools/adb")
        
        print(f"Installing {apk_file}...")
        try:
            # Uninstall existing version if present
            if package_name:
                subprocess.run(
                    [adb_path, '-s', device_serial, 'uninstall', package_name],
                    capture_output=True,
                    timeout=30
                )
            
            # Install APK
            result = subprocess.run(
                [adb_path, '-s', device_serial, 'install', '-r', apk_path],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                print("✓ APK installed successfully")
                return True
            else:
                print(f"✗ Installation failed: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"✗ Installation error: {e}")
            return False
    
    def run_test(self, test_id, apk_file, br_file):
        """Run a single test and log results to CSV"""
        print(f"\n{'=' * 80}")
        print(f"Test #{test_id}: {br_file}")
        print(f"APK: {apk_file}")
        print(f"{'=' * 80}")
        
        # Extract BR info
        app_name, package_name, issue_number = self.extract_br_info(br_file)
        print(f"App: {app_name}")
        print(f"Package: {package_name}")
        print(f"Issue: #{issue_number}")
        print()
        
        # Wait for user confirmation before starting this test
        input(f"Press Enter to start test #{test_id} (or Ctrl+C to cancel)...")
        print()
        
        # Note: Assuming APK is already installed on emulator
        # Uncomment below if you need to install APKs before testing:
        # if not self.install_apk(apk_file, package_name):
        #     timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #     row = [test_id, timestamp, apk_file, br_file, app_name, package_name, 
        #            issue_number, 'INSTALL_FAILED', '0', 0, 0, 'No', 
        #            'APK installation failed', '', 'Skipped due to installation failure']
        #     with open(self.results_file, 'a', newline='') as f:
        #         writer = csv.writer(f)
        #         writer.writerow(row)
        #     return 'INSTALL_FAILED', 0
        
        # Start test
        start_time = time.time()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        status = 'UNKNOWN'
        duration = 0
        metrics = {
            'total_commands': 0,
            'gpt_responses': 0,
            'bug_reproduced': False,
            'failure_reason': '',
            'log_file': ''
        }
        remarks = ''
        
        try:
            print("Running reproduction script...")
            print(f"{'=' * 80}\n")
            
            # Prepare command and environment
            script_dir = os.path.dirname(os.path.abspath(__file__))
            br_path = f'BRs/{br_file}'
            
            # Set up environment with Android SDK paths
            env = os.environ.copy()
            android_sdk = os.path.expanduser("~/Library/Android/sdk")
            path_additions = f"{android_sdk}/platform-tools:{android_sdk}/emulator"
            env['PATH'] = f"{path_additions}:{env.get('PATH', '')}"
            env['ANDROID_SDK_ROOT'] = android_sdk
            
            # Run the reproduction script with real-time output (like run.sh)
            # We'll capture output in a variable while still showing it
            output_lines = []
            process = subprocess.Popen(
                ['python3', 'reproduction.py', self.device_port, br_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                cwd=script_dir,
                env=env
            )
            
            # Read and display output in real-time
            for line in iter(process.stdout.readline, ''):
                if line:
                    print(line, end='')
                    output_lines.append(line)
            
            # Wait for process to complete (with timeout)
            try:
                return_code = process.wait(timeout=300)
            except subprocess.TimeoutExpired:
                process.kill()
                raise
            
            duration = time.time() - start_time
            output = ''.join(output_lines)
            
            print(f"\n{'=' * 80}")
            print(f"Exit code: {return_code}")
            
            # Parse output
            metrics = self.parse_test_output(output)
            
            # Determine status
            if metrics['bug_reproduced']:
                status = 'SUCCESS'
                remarks = 'Bug successfully reproduced'
            elif return_code == 0:
                status = 'COMPLETED'
                remarks = 'Test completed without bug reproduction'
            else:
                status = 'ERROR'
                remarks = f'Exit code: {return_code}'
                if not metrics['failure_reason']:
                    metrics['failure_reason'] = f'Process exited with code {return_code}'
            
            print(f"\nTest completed in {duration:.1f}s")
            print(f"Status: {status}")
            print(f"Bug Reproduced: {metrics['bug_reproduced']}")
            print(f"GPT Responses: {metrics['gpt_responses']}")
            print(f"Commands Executed: {metrics['total_commands']}")
            
        except subprocess.TimeoutExpired:
            duration = time.time() - start_time
            status = 'TIMEOUT'
            metrics['failure_reason'] = 'Test exceeded 5 minute timeout'
            remarks = 'Timeout after 300 seconds'
            print(f"\n⏱ Test timed out after {duration:.1f}s")
            
        except Exception as e:
            duration = time.time() - start_time
            status = 'ERROR'
            metrics['failure_reason'] = str(e)
            remarks = f'Unexpected error: {str(e)[:50]}'
            print(f"\n✗ Error: {e}")
        
        # Write result to CSV immediately
        row = [
            test_id,
            timestamp,
            apk_file,
            br_file,
            app_name,
            package_name,
            issue_number,
            status,
            f'{duration:.2f}',
            metrics['total_commands'],
            metrics['gpt_responses'],
            'Yes' if metrics['bug_reproduced'] else 'No',
            metrics['failure_reason'],
            metrics['log_file'],
            remarks
        ]
        
        with open(self.results_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(row)
        
        print(f"✓ Result logged to {self.results_file}")
        
        return status, duration
    
    def run_all_tests(self):
        """Run all tests and display summary"""
        print("=" * 80)
        print("INCREMENTAL BUG REPRODUCTION TESTING")
        print("=" * 80)
        print(f"Device: emulator-{self.device_port}")
        print(f"Results file: {self.results_file}\n")
        
        # Get test cases
        print("Mapping APKs to Bug Reports...")
        self.test_cases = self.get_apk_to_br_mapping()
        
        if not self.test_cases:
            print("Error: No test cases found!")
            return
        
        print(f"\nFound {len(self.test_cases)} test case(s):\n")
        
        # Group by APK for display
        by_apk = defaultdict(list)
        for apk, br in self.test_cases:
            by_apk[apk].append(br)
        
        for apk, brs in sorted(by_apk.items()):
            print(f"  {apk}")
            for br in brs:
                print(f"    └─ {br}")
        
        print(f"\n{'=' * 80}")
        input("Press Enter to start testing (or Ctrl+C to cancel)...")
        print()
        
        # Run tests
        results = []
        for i, (apk_file, br_file) in enumerate(self.test_cases, 1):
            status, duration = self.run_test(i, apk_file, br_file)
            results.append({'status': status, 'duration': duration})
        
        # Display summary
        self.display_summary(results)
    
    def display_summary(self, results):
        """Display test summary"""
        print("\n" + "=" * 80)
        print("TEST SUMMARY")
        print("=" * 80)
        
        total = len(results)
        success = sum(1 for r in results if r['status'] == 'SUCCESS')
        completed = sum(1 for r in results if r['status'] == 'COMPLETED')
        timeout = sum(1 for r in results if r['status'] == 'TIMEOUT')
        error = sum(1 for r in results if r['status'] == 'ERROR')
        unknown = sum(1 for r in results if r['status'] == 'UNKNOWN')
        
        total_duration = sum(r['duration'] for r in results)
        avg_duration = total_duration / total if total > 0 else 0
        
        print(f"\nTotal Tests:        {total}")
        print(f"Success:            {success} ({success/total*100:.1f}%)")
        print(f"Completed:          {completed} ({completed/total*100:.1f}%)")
        print(f"Timeout:            {timeout} ({timeout/total*100:.1f}%)")
        print(f"Error:              {error} ({error/total*100:.1f}%)")
        print(f"Unknown:            {unknown} ({unknown/total*100:.1f}%)")
        print(f"\nTotal Duration:     {total_duration:.1f}s ({total_duration/60:.1f} min)")
        print(f"Average per Test:   {avg_duration:.1f}s")
        print(f"\nSUCCESS RATE:       {success/total*100:.1f}%")
        print(f"\n{'=' * 80}")
        print(f"All results saved to: {self.results_file}")
        print(f"{'=' * 80}\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 incremental_test.py <device_port>")
        print("Example: python3 incremental_test.py 5554")
        sys.exit(1)
    
    device_port = sys.argv[1]
    
    try:
        tester = IncrementalTester(device_port)
        tester.run_all_tests()
    except KeyboardInterrupt:
        print("\n\nTesting interrupted by user")
        print(f"Partial results saved to: {tester.results_file}")
    except Exception as e:
        print(f"\n✗ Fatal error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
