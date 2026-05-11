# Android Bug Crawler

A comprehensive tool to crawl GitHub issues for Android bug reports, categorize them by ReBL failure categories, and add APK download links.

## Features

- **Crawls GitHub Issues**: Searches for Android bug reports across GitHub
- **Categorizes by ReBL Categories**: 14 failure categories (gesture, webview, media, etc.)
- **APK Link Enrichment**: Automatically finds and adds direct APK download URLs from GitHub releases
- **Filters Quality**: Only keeps bugs with direct APK download links
- **Generates Reports**: Creates structured bug report TXT files and CSV summary

## Installation

```bash
# Create virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Basic Crawling

```bash
# Crawl 5000 bugs (default)
python bug_crawler.py --token YOUR_GITHUB_TOKEN

# Crawl specific number of bugs
python bug_crawler.py --token YOUR_GITHUB_TOKEN --target 3000

# Include bugs without APK links
python bug_crawler.py --token YOUR_GITHUB_TOKEN --all-bugs

# Custom output directory
python bug_crawler.py --token YOUR_GITHUB_TOKEN --output my_output
```

### Validation

```bash
# Validate existing dataset
python bug_crawler.py --token YOUR_GITHUB_TOKEN --validate
```

## Output Structure

```
output/
├── bug_reports/
│   ├── authentication/
│   │   ├── owner_repo_123.txt
│   │   └── ...
│   ├── camera_file/
│   ├── data_state/
│   ├── external_app/
│   ├── gesture_complex/
│   ├── keyboard_input/
│   ├── map_location/
│   ├── media_playback/
│   ├── network_sync/
│   ├── notification_background/
│   ├── permission_system/
│   ├── state_timing/
│   ├── visual_rendering/
│   └── webview_hybrid/
├── authentication.json
├── camera_file.json
├── ... (one JSON per category)
└── bug_dataset.csv
```

## Bug Report Format

Each bug report TXT file contains:

```
BUG REPORT
==========

TITLE: [Bug Title]

CATEGORY: [ReBL Category]
KEYWORDS: [matched keywords]

SOURCE:
- Issue URL: https://github.com/...
- Repository: owner/repo
- Issue #: 123
- State: open/closed
- Created: 2026-01-01T00:00:00Z

APK DOWNLOAD:
- Available: Yes
- URL: https://github.com/.../releases/download/.../app.apk
- Source: github_releases
- Version: v1.0.0
- File: app-release.apk

VERSION: 1.0.0

STEPS TO REPRODUCE:
1. Step one
2. Step two
...

DESCRIPTION:
[Full issue description]

LABELS: bug, confirmed, ...
```

## ReBL Categories

| Category | Description |
|----------|-------------|
| gesture_complex | Complex gesture interactions |
| webview_hybrid | WebView and hybrid app issues |
| media_playback | Media playback issues |
| camera_file | Camera and file handling |
| notification_background | Notifications and background processing |
| network_sync | Network and synchronization |
| permission_system | Permission and system interactions |
| state_timing | State management and timing |
| authentication | Authentication flows |
| map_location | Maps and location services |
| visual_rendering | Visual rendering issues |
| data_state | Data persistence issues |
| external_app | External app interactions |
| keyboard_input | Keyboard and input issues |

## Getting a GitHub Token

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Select scopes: `public_repo`, `read:org`
4. Copy the token and use with `--token` flag

## Files

- `bug_crawler.py` - Main crawler script (all-in-one)
- `config.py` - Configuration and constants
- `automated_tester.py` - For automated testing (separate tool)
- `requirements.txt` - Python dependencies
