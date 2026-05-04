#!/usr/bin/env python3
"""
CARBON-Exclusive Gesture Bug Crawler
=====================================
Enhanced crawler that finds gesture bugs ONLY CARBON can handle (not ReBL).

Key enhancements over the original gesture_bug_crawler.py:
  1. Includes pre-release APKs (alpha, beta, rc, dev, snapshot)
  2. Skips bugs already in the existing dataset (62 bugs)
  3. Filters out bugs needing login, media libraries, RSS, manga, etc.
  4. Checks comments for "cannot reproduce" signals and skips those
  5. Classifies each bug by primary CARBON gesture type
  6. Assigns ReBL capability (yes/no) based on gesture requirements
  7. Targets 120+ bugs for buffer (need 100 final)

Usage:
    python3 carbon_exclusive_crawler.py --token YOUR_GITHUB_TOKEN
    python3 carbon_exclusive_crawler.py --token YOUR_GITHUB_TOKEN --target 130
    python3 carbon_exclusive_crawler.py --token YOUR_GITHUB_TOKEN --download
"""

import os, re, sys, csv, json, time, argparse, logging, requests
from typing import Optional, List, Tuple, Dict
from dotenv import load_dotenv

load_dotenv()

# Use our CARBON-exclusive config
import carbon_exclusive_config as config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
log = logging.getLogger(__name__)

OUTPUT_DIR = "output/carbon_new_bugs"

# ── CARBON gesture classification ──
# Maps gesture keywords to CARBON action categories.
# Priority order: more specific gestures first.
GESTURE_CATEGORIES = {
    'pinch_zoom': [
        'pinch', 'pinch to zoom', 'pinch-to-zoom', 'pinch zoom',
        'pinch in', 'pinch out', 'two finger', 'two-finger',
        'multi-touch', 'multitouch', 'zoom in', 'zoom out',
        'image zoom', 'map zoom', 'canvas zoom', 'magnify',
    ],
    'double_tap': [
        'double tap', 'double-tap', 'double click', 'double-click',
        'doubletap', 'double touch', 'tap twice', 'two taps',
    ],
    'drag_and_drop': [
        'drag and drop', 'drag-and-drop', 'drag to reorder',
        'drag handle', 'reorder', 'rearrange', 'drag to move',
        'sortable', 'draggable', 'drag to delete', 'drag item',
    ],
    'edge_swipe': [
        'edge swipe', 'back gesture', 'gesture navigation',
        'edge gesture', 'navigation gesture', 'predictive back',
        'swipe from edge', 'drawer swipe', 'navigation drawer',
    ],
    'media_gesture': [
        'volume gesture', 'brightness gesture', 'seek gesture',
        'player gesture', 'video controls', 'player controls',
        'swipe to seek', 'swipe volume', 'swipe brightness',
    ],
    'quick_tap': [
        'quick tap', 'fast tap', 'rapid tap', 'immediately tap',
        'race condition', 'timing', 'before animation',
    ],
    'rotate': [
        'rotate gesture', 'rotation gesture',
    ],
    'swipe': [
        'swipe to dismiss', 'swipe to delete', 'swipe notification',
        'dismiss notification', 'swipe away', 'swipe left',
        'swipe right', 'swipe up', 'swipe down', 'fling',
        'pull to refresh', 'pull-to-refresh', 'swipe',
    ],
    'scroll': [
        'overscroll', 'nested scroll', 'fling scroll',
    ],
    'orientation': [
        'orientation', 'landscape', 'portrait',
        'screen rotation', 'auto-rotate', 'rotate',
    ],
}

# Gestures that ReBL CANNOT do — these are CARBON-exclusive
REBL_CANNOT_DO = {
    'pinch_zoom', 'double_tap', 'drag_and_drop', 'edge_swipe',
    'media_gesture', 'quick_tap', 'rotate',
}

# ── Content that indicates bug needs external resources ──
NEEDS_EXTERNAL_CONTENT = [
    # Login / Account
    'log in', 'sign in', 'sign up', 'create account', 'register',
    'username', 'password', 'credentials', 'authenticate',
    'api key', 'token',
    # Media library content
    'add songs', 'import music', 'music library', 'playlist',
    'add to library', 'download song', 'stream',
    'manga', 'comic', 'chapter',
    # RSS / Feed
    'rss', 'feed', 'subscribe', 'podcast',
    # Network dependent
    'connect to server', 'sync with', 'cloud',
    # Specific app content
    'add account', 'link account',
    # Video content
    'play a video', 'open a video', 'load a video',
    'play video', 'open video', 'load video',
    'watch a video', 'search for a video',
]


def classify_gesture(keywords: List[str]) -> Tuple[str, bool]:
    """Classify bug by primary CARBON gesture and whether ReBL can handle it.

    Returns:
        (primary_gesture, rebl_can_do)
    """
    kw_lower = [k.lower() for k in keywords]
    kw_text = ' '.join(kw_lower)

    # Check each category in priority order
    for category, category_keywords in GESTURE_CATEGORIES.items():
        for ck in category_keywords:
            if ck in kw_text:
                rebl_can = category not in REBL_CANNOT_DO
                return category, rebl_can

    return 'unknown', True


def needs_external_resources(body: str, steps: List[str]) -> Optional[str]:
    """Check if bug reproduction needs external resources (login, media, etc.).

    Returns reason string if it needs external resources, None if OK.
    """
    text = f"{body} {' '.join(steps)}".lower()

    for indicator in NEEDS_EXTERNAL_CONTENT:
        if indicator in text:
            return f"needs: {indicator}"

    return None


# ── Parsing helpers (enhanced from gesture_bug_crawler.py) ──

def extract_version(text: str) -> Optional[str]:
    """Extract app version from issue body. Enhanced to find pre-release versions."""
    text_no_code = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    _ver = r'(\d+\.\d+(?:\.\d+)?(?:[-.]?(?:alpha|beta|rc|dev|pre|snapshot|nightly)\d*(?:\.\d+)*)?)'

    priority1_patterns = [
        r'(?:app\s+)?version\s*[:=]\s*[vV]?' + _ver,
        r'\*\*(?:app\s+)?version\*\*\s*[:=]\s*[vV]?' + _ver,
    ]
    for p in priority1_patterns:
        m = re.search(p, text_no_code, re.IGNORECASE)
        if m:
            return m.group(1)

    code_blocks = re.findall(r'```(?:\w+)?\s*\n(.*?)```', text, re.DOTALL)
    for block in code_blocks:
        m = re.search(
            r'(?:\w+\s+)?version\s*=\s*[vV]?(\d+\.\d+(?:\.\d+)?(?:[-.]?(?:alpha|beta|rc|dev|pre|snapshot|nightly)\d*(?:\.\d+)*)?)',
            block, re.IGNORECASE
        )
        if m:
            return m.group(1)

    m = re.search(
        r'(?:using|running|installed|on)\s+(?:version\s+)?[vV]?(\d+\.\d+(?:\.\d+)?(?:[-.]?(?:alpha|beta|rc|dev|pre|snapshot|nightly)\d*)?)',
        text_no_code, re.IGNORECASE
    )
    if m:
        return m.group(1)

    return None


def extract_numbered_steps(body: str) -> List[str]:
    """Extract numbered steps to reproduce."""
    steps = []
    pattern = r'(?:^|\n)\s*(\d+)[.)]\s*(.+?)(?=\n\s*\d+[.)]|\n\n|\Z)'
    matches = re.findall(pattern, body, re.DOTALL)
    for num, step in matches:
        step = step.strip().replace('\n', ' ')
        step = re.sub(r'\s+', ' ', step)
        if len(step) > 5:
            steps.append(step)
    return steps


def has_expected_and_actual(body: str) -> bool:
    """Check for expected and actual behavior sections."""
    body_lower = body.lower()
    has_expected = any(marker in body_lower for marker in [
        'expected behavior', 'expected behaviour', 'expected result',
        'what should happen', 'expected:', 'expected outcome',
        '### expected', 'should be', 'should show', 'should work',
        'supposed to', 'it should', 'normally',
    ])
    has_actual = any(marker in body_lower for marker in [
        'actual behavior', 'actual behaviour', 'actual result',
        'what happened', 'what actually', 'actual:', 'actual outcome',
        '### actual', 'bug behavior', 'buggy behavior',
        'instead', 'but it', 'however', 'crash', 'doesn\'t work',
        'not working', 'broken', 'fails', 'wrong',
    ])
    return has_expected and has_actual


def has_steps_section(body: str) -> bool:
    """Check for steps to reproduce section."""
    body_lower = body.lower()
    return any(marker in body_lower for marker in [
        'steps to reproduce', 'to reproduce', 'how to reproduce',
        'reproduction steps', 'steps:', 'reproduce:',
        '### steps', '### how to',
    ])


def count_gesture_keywords(text: str) -> Tuple[int, List[str]]:
    """Count gesture keywords in text."""
    text_lower = text.lower()
    matched = []
    seen = set()
    for kw in config.GESTURE_KEYWORDS:
        kw_lower = kw.lower()
        if kw_lower in text_lower and kw_lower not in seen:
            matched.append(kw)
            seen.add(kw_lower)
    return len(matched), matched


def normalize_version(v: str) -> str:
    """Normalize version string for comparison."""
    v = re.sub(r'^[vV]', '', v.strip())
    v = re.sub(r'[^0-9a-zA-Z.]', '.', v)
    v = re.sub(r'\.+', '.', v).strip('.')
    return v


def versions_match(target: str, tag: str) -> bool:
    """Check if a release tag matches the target version.
    Enhanced to handle pre-release versions better."""
    t = normalize_version(target)
    g = normalize_version(tag)

    if t == g:
        return True
    if t + '.0' == g or g + '.0' == t:
        return True
    # Check if tag contains the version
    if t in g and len(t) >= 3:
        idx = g.index(t)
        before_ok = idx == 0 or not g[idx - 1].isdigit()
        after_idx = idx + len(t)
        after_ok = after_idx >= len(g) or not g[after_idx].isdigit()
        if before_ok and after_ok:
            return True
    return False


# ── Crawler class ────────────────────────────────────────────────────────────

class CarbonExclusiveCrawler:
    def __init__(self, token: str):
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'CarbonExclusiveCrawler/1.0',
        })
        self.bugs = []
        self.seen_urls = set()
        self.release_cache = {}
        self.skip_reasons = {}
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    def _api(self, url: str, params: dict = None) -> Optional[dict]:
        """Make a GitHub API request with retry and rate limit handling."""
        for attempt in range(config.MAX_RETRIES):
            try:
                r = self.session.get(url, params=params, timeout=30)
                if r.status_code == 200:
                    return r.json()
                if r.status_code == 403:
                    reset = int(r.headers.get('X-RateLimit-Reset', 0))
                    wait = max(reset - time.time(), 60)
                    log.warning(f"Rate limited. Waiting {wait:.0f}s...")
                    time.sleep(wait)
                    continue
                if r.status_code == 422:
                    return None
                log.warning(f"API {r.status_code}: {url}")
                return None
            except Exception as e:
                log.error(f"Request error: {e}")
                time.sleep(5)
        return None

    def search_issues(self, query: str, max_pages: int = 5) -> List[dict]:
        """Search GitHub issues."""
        issues = []
        for page in range(1, max_pages + 1):
            data = self._api(
                "https://api.github.com/search/issues",
                params={'q': query, 'per_page': 30, 'page': page,
                        'sort': 'created', 'order': 'desc'}
            )
            if not data or 'items' not in data:
                break
            items = data['items']
            if not items:
                break
            issues.extend(items)
            log.info(f"  Page {page}: {len(items)} issues "
                     f"(total: {data.get('total_count', '?')})")
            time.sleep(config.REQUEST_DELAY)
        return issues

    def get_releases(self, repo: str) -> List[dict]:
        """Get ALL releases for a repo (cached), including pre-releases."""
        if repo in self.release_cache:
            return self.release_cache[repo]
        releases = []
        # Fetch up to 200 releases (2 pages) to find pre-release versions
        for page in range(1, 3):
            data = self._api(
                f"https://api.github.com/repos/{repo}/releases",
                params={'per_page': 100, 'page': page}
            )
            if data:
                releases.extend(data)
            else:
                break
            time.sleep(config.REQUEST_DELAY)
        self.release_cache[repo] = releases
        return releases

    def find_apk(self, repo: str, target_version: str) -> Optional[dict]:
        """Find APK download URL for a version match.
        Enhanced: includes pre-release/alpha/beta/rc APKs.
        Prefers universal/arm64 APKs."""
        if not target_version:
            return None

        releases = self.get_releases(repo)
        if not releases:
            return None

        for rel in releases:
            tag = rel.get('tag_name', '')
            if not versions_match(target_version, tag):
                continue

            apks = []
            for asset in rel.get('assets', []):
                name = asset['name'].lower()
                if not name.endswith('.apk'):
                    continue
                size_mb = asset['size'] / (1024 * 1024)
                if size_mb > config.MAX_APK_SIZE_MB:
                    continue
                score = 0
                if 'universal' in name:
                    score = 30
                elif 'foss' in name and 'release' in name:
                    score = 25
                elif 'release' in name:
                    score = 20
                elif 'arm64' in name:
                    score = 15
                elif 'armeabi' in name or 'arm-v7' in name:
                    score = 10
                else:
                    score = 5
                if 'debug' in name:
                    score -= 10
                apks.append({
                    'url': asset['browser_download_url'],
                    'name': asset['name'],
                    'size': asset['size'],
                    'tag': rel['tag_name'],
                    'prerelease': rel.get('prerelease', False),
                    'match': 'exact',
                    '_score': score,
                })

            if apks:
                apks.sort(key=lambda x: x['_score'], reverse=True)
                best = apks[0]
                del best['_score']
                return best

        return None

    def fetch_comments(self, comments_url: str) -> List[dict]:
        """Fetch issue comments."""
        data = self._api(comments_url, params={'per_page': 50})
        time.sleep(config.REQUEST_DELAY)
        return data if isinstance(data, list) else []

    def check_cannot_reproduce(self, issue: dict) -> bool:
        """Check if comments indicate the bug CANNOT be reproduced.
        Returns True if we should SKIP this bug."""
        comments_url = issue.get('comments_url', '')
        comment_count = issue.get('comments', 0)
        if not comments_url or comment_count == 0:
            return False

        comments = self.fetch_comments(comments_url)
        cannot_reproduce_signals = 0
        can_reproduce_signals = 0

        for c in comments:
            c_body = (c.get('body') or '').lower()
            author = c.get('author_association', '')
            is_maintainer = author in ('OWNER', 'MEMBER', 'COLLABORATOR')

            # Cannot reproduce signals
            if any(phrase in c_body for phrase in [
                'cannot reproduce', 'can\'t reproduce', 'unable to reproduce',
                'could not reproduce', 'not reproducible', 'works for me',
                'works fine', 'cannot replicate', 'can\'t replicate',
                'not a bug', 'by design', 'intended behavior',
                'closing as', 'wontfix', 'won\'t fix',
            ]):
                if is_maintainer:
                    return True  # Maintainer says can't reproduce — skip
                cannot_reproduce_signals += 1

            # Can reproduce signals
            if any(phrase in c_body for phrase in [
                'confirmed', 'reproduced', 'can reproduce', 'can confirm',
                'i can confirm', 'verified', 'same issue', 'same here',
                'same bug', 'i also experience', 'happens to me',
                'still happening', 'still broken', 'still present',
            ]):
                can_reproduce_signals += 1

        # Skip if more "cannot reproduce" than "can reproduce"
        if cannot_reproduce_signals > can_reproduce_signals and cannot_reproduce_signals >= 2:
            return True

        return False

    def check_verification(self, issue: dict) -> Tuple[bool, int, List[str]]:
        """Check if bug is verified/confirmed."""
        signals = []
        score = 0
        labels = [l['name'].lower() for l in issue.get('labels', [])]

        confirmed_labels = ['confirmed', 'verified', 'reproducible', 'reproduced',
                            'accepted', 'triaged', 'acknowledged', 'valid']
        for cl in confirmed_labels:
            if any(cl in l for l in labels):
                signals.append(f"label:{cl}")
                score += 20

        if any('bug' in l for l in labels):
            score += 5

        reactions = issue.get('reactions', {})
        thumbs_up = reactions.get('+1', 0)
        if thumbs_up >= 3:
            signals.append(f"+1 reactions: {thumbs_up}")
            score += 15
        elif thumbs_up >= 1:
            signals.append(f"+1 reactions: {thumbs_up}")
            score += 5

        comment_count = issue.get('comments', 0)
        if comment_count >= 3:
            score += 10
            signals.append(f"{comment_count} comments")

        is_verified = score >= 10
        return is_verified, score, signals

    def process_issue(self, issue: dict) -> Optional[dict]:
        """Process a single GitHub issue with STRICT filtering."""
        url = issue.get('html_url', '')
        if url in self.seen_urls:
            return None
        self.seen_urls.add(url)

        title = issue.get('title', '')
        body = issue.get('body') or ''
        labels = [l['name'] for l in issue.get('labels', [])]
        repo_url = issue.get('repository_url', '')
        repo = '/'.join(repo_url.split('/')[-2:]) if repo_url else ''
        issue_num = issue.get('number', 0)
        issue_id = f"{repo}#{issue_num}"

        # ── Skip existing bugs ──
        if (repo, issue_num) in config.EXISTING_BUGS:
            return None

        # ── Skip repos ──
        if repo in config.SKIP_REPOS:
            return None
        repo_lower = repo.lower()
        title_lower = title.lower()
        body_lower = body.lower()
        combined_lower = f"{repo_lower} {title_lower} {body_lower[:500]}"
        if any(kw in repo_lower or kw in title_lower for kw in config.SKIP_APP_KEYWORDS):
            return None

        # ── Body length ──
        if len(body) < config.MIN_BODY_LENGTH or len(body) > config.MAX_BODY_LENGTH:
            self.skip_reasons[issue_id] = "body too short/long"
            return None

        # ── Must have steps section ──
        if not has_steps_section(body):
            self.skip_reasons[issue_id] = "no steps section"
            return None

        # ── Must have numbered steps ──
        steps = extract_numbered_steps(body)
        if len(steps) < config.MIN_STEPS:
            self.skip_reasons[issue_id] = f"only {len(steps)} steps"
            return None

        # ── Must have expected + actual ──
        if not has_expected_and_actual(body):
            self.skip_reasons[issue_id] = "missing expected/actual"
            return None

        # ── Must have gesture keywords ──
        full_text = f"{title} {body}"
        kw_count, kw_matched = count_gesture_keywords(full_text)
        if kw_count < config.MIN_GESTURE_KEYWORDS:
            self.skip_reasons[issue_id] = "no gesture keywords"
            return None

        # ── Gesture keyword must appear in steps or title ──
        steps_text = ' '.join(steps)
        title_and_steps = f"{title} {steps_text}"
        title_step_count, _ = count_gesture_keywords(title_and_steps)
        if title_step_count == 0:
            self.skip_reasons[issue_id] = "gesture not in steps/title"
            return None

        # ── Check if bug needs external resources ──
        ext_reason = needs_external_resources(body, steps)
        if ext_reason:
            self.skip_reasons[issue_id] = ext_reason
            return None

        # ── Must have extractable version ──
        version = extract_version(body)
        if not version:
            self.skip_reasons[issue_id] = "no version found"
            return None

        # ── Must have APK match ──
        apk_info = self.find_apk(repo, version)
        if apk_info is None:
            self.skip_reasons[issue_id] = f"no APK for v{version}"
            return None

        # ── Check comments for "cannot reproduce" ──
        if self.check_cannot_reproduce(issue):
            self.skip_reasons[issue_id] = "cannot reproduce (comments)"
            return None

        # ── Classify gesture and check ReBL capability ──
        primary_gesture, rebl_can_do = classify_gesture(kw_matched)

        # ── Verification ──
        is_verified, verify_score, verify_signals = self.check_verification(issue)

        # ── Build bug dict ──
        bug = {
            'title': title,
            'repo': repo,
            'issue_number': issue_num,
            'issue_url': url,
            'state': issue.get('state', ''),
            'created_at': issue.get('created_at', ''),
            'labels': labels,
            'version': version,
            'gesture_keywords': kw_matched,
            'gesture_keyword_count': kw_count,
            'steps': steps,
            'step_count': len(steps),
            'body': body,
            'has_apk': True,
            'apk_url': apk_info['url'],
            'apk_name': apk_info['name'],
            'apk_tag': apk_info['tag'],
            'apk_match': apk_info['match'],
            'prerelease': apk_info.get('prerelease', False),
            'verified': is_verified,
            'verify_score': verify_score,
            'verify_signals': verify_signals,
            'primary_gesture': primary_gesture,
            'rebl_can_do': 'yes' if rebl_can_do else 'no',
            'carbon_can_do': 'yes',
        }
        return bug

    def crawl(self, target: int = 130):
        """Run the crawl across all search queries."""
        log.info(f"Crawling for {target} CARBON-exclusive gesture bugs...")
        log.info(f"Skipping {len(config.EXISTING_BUGS)} existing bugs")
        log.info(f"Max {config.MAX_BUGS_PER_REPO} bugs per repo")
        repo_counts = {}

        for i, query in enumerate(config.SEARCH_QUERIES):
            if len(self.bugs) >= target:
                break
            log.info(f"\nQuery [{i+1}/{len(config.SEARCH_QUERIES)}]: {query[:80]}...")
            issues = self.search_issues(query, max_pages=5)
            log.info(f"  Found {len(issues)} issues")

            for issue in issues:
                if len(self.bugs) >= target:
                    break

                repo_url = issue.get('repository_url', '')
                repo = '/'.join(repo_url.split('/')[-2:]) if repo_url else ''
                if repo_counts.get(repo, 0) >= config.MAX_BUGS_PER_REPO:
                    continue

                bug = self.process_issue(issue)
                if bug:
                    repo_counts[bug['repo']] = repo_counts.get(bug['repo'], 0) + 1
                    self.bugs.append(bug)
                    pre_tag = " [PRE-RELEASE]" if bug['prerelease'] else ""
                    rebl_tag = " [ReBL:YES]" if bug['rebl_can_do'] == 'yes' else ""
                    log.info(
                        f"  >>> [{len(self.bugs)}/{target}] {bug['repo']}#{bug['issue_number']}: "
                        f"{bug['title'][:50]}... "
                        f"[v{bug['version']} -> APK:{bug['apk_tag']}] "
                        f"[{bug['primary_gesture']}] "
                        f"[{bug['gesture_keyword_count']} kw]{pre_tag}{rebl_tag}"
                        f"{' VERIFIED' if bug['verified'] else ''}"
                    )

        log.info(f"\n{'='*60}")
        log.info(f"Crawl complete: {len(self.bugs)} bugs found")
        unique_repos = len(set(b['repo'] for b in self.bugs))
        log.info(f"Unique repos: {unique_repos}")
        prerelease_count = sum(1 for b in self.bugs if b['prerelease'])
        log.info(f"Pre-release APKs: {prerelease_count}")
        rebl_no = sum(1 for b in self.bugs if b['rebl_can_do'] == 'no')
        log.info(f"CARBON-exclusive (ReBL cannot): {rebl_no}")
        log.info(f"ReBL can also do: {len(self.bugs) - rebl_no}")

        # Gesture distribution
        gesture_dist = {}
        for b in self.bugs:
            g = b['primary_gesture']
            gesture_dist[g] = gesture_dist.get(g, 0) + 1
        log.info(f"\nGesture distribution:")
        for g, c in sorted(gesture_dist.items(), key=lambda x: -x[1]):
            log.info(f"  {g}: {c}")

        # Skip reasons
        reason_counts = {}
        for reason in self.skip_reasons.values():
            reason_counts[reason] = reason_counts.get(reason, 0) + 1
        if reason_counts:
            log.info(f"\nSkip reasons (top 10):")
            for reason, count in sorted(reason_counts.items(), key=lambda x: -x[1])[:10]:
                log.info(f"  {reason}: {count}")

    def generate_br(self, bug: dict, output_path: str):
        """Generate a clean bug report file."""
        body = bug['body']

        # Extract expected behavior
        expected = ""
        for pattern in [
            r'(?:###?\s*)?(?:expected\s+(?:behavior|behaviour|result|outcome))[:\s]*\n+(.*?)(?=\n###?\s|\n\*\*|\Z)',
            r'(?:what\s+should\s+happen)[:\s]*\n+(.*?)(?=\n###?\s|\n\*\*|\Z)',
        ]:
            m = re.search(pattern, body, re.IGNORECASE | re.DOTALL)
            if m:
                expected = m.group(1).strip()
                break

        # Extract actual behavior
        actual = ""
        for pattern in [
            r'(?:###?\s*)?(?:actual\s+(?:behavior|behaviour|result|outcome))[:\s]*\n+(.*?)(?=\n###?\s|\n\*\*|\Z)',
            r'(?:what\s+(?:happened|actually))[:\s]*\n+(.*?)(?=\n###?\s|\n\*\*|\Z)',
        ]:
            m = re.search(pattern, body, re.IGNORECASE | re.DOTALL)
            if m:
                actual = m.group(1).strip()
                break

        def clean_text(t):
            t = re.sub(r'<!--.*?-->', '', t, flags=re.DOTALL)
            t = re.sub(r'!\[.*?\]\(.*?\)', '[screenshot]', t)
            t = re.sub(r'\n{3,}', '\n\n', t)
            return t.strip()

        expected = clean_text(expected) or "(see full report below)"
        actual = clean_text(actual) or "(see full report below)"

        steps_formatted = ""
        for i, step in enumerate(bug['steps'], 1):
            steps_formatted += f"  {i}. {step}\n"

        gestures = ', '.join(bug['gesture_keywords'])
        content = f"""{bug['title']}

App: {bug['repo']}
Version: {bug['version']}
Issue: {bug['issue_url']}
APK: {bug['apk_url']}
APK Tag: {bug['apk_tag']}
Gestures: {gestures}
Primary Gesture: {bug['primary_gesture']}
ReBL can do: {bug['rebl_can_do']}
CARBON can do: {bug['carbon_can_do']}

Steps to Reproduce:
{steps_formatted}
Expected Behavior:
  {expected}

Actual Behavior:
  {actual}

--- Full Issue Body ---
{clean_text(body)}
"""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

    def download_apk(self, url: str, save_path: str) -> bool:
        """Download an APK file."""
        try:
            r = self.session.get(url, stream=True, timeout=config.DOWNLOAD_TIMEOUT)
            r.raise_for_status()
            with open(save_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            return os.path.exists(save_path) and os.path.getsize(save_path) > 0
        except Exception as e:
            log.error(f"Download failed: {e}")
            return False

    def save_all(self, download_apks: bool = False):
        """Save CSV, bug reports, and optionally download APKs."""
        if not self.bugs:
            log.warning("No bugs to save")
            return

        os.makedirs(OUTPUT_DIR, exist_ok=True)

        # Save CSV
        csv_path = os.path.join(OUTPUT_DIR, "carbon_new_bugs.csv")
        fields = [
            'repo', 'issue_number', 'title', 'version',
            'gesture_keyword_count', 'gesture_keywords', 'step_count',
            'primary_gesture', 'rebl_can_do', 'carbon_can_do',
            'prerelease', 'verified', 'verify_score', 'verify_signals',
            'state', 'apk_url', 'apk_tag', 'apk_match',
            'issue_url', 'created_at',
        ]
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
            writer.writeheader()
            for bug in sorted(self.bugs, key=lambda b: b['primary_gesture']):
                row = dict(bug)
                row['gesture_keywords'] = '; '.join(bug['gesture_keywords'])
                row['verify_signals'] = '; '.join(bug['verify_signals'])
                writer.writerow(row)
        log.info(f"Saved CSV: {csv_path}")

        # Save individual bug reports + APKs
        for bug in self.bugs:
            folder_name = f"{bug['repo'].replace('/', '_')}_{bug['issue_number']}"
            folder_path = os.path.join(OUTPUT_DIR, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            br_path = os.path.join(folder_path, "bug_report.txt")
            self.generate_br(bug, br_path)

            if download_apks:
                apk_path = os.path.join(folder_path, bug['apk_name'])
                if not os.path.exists(apk_path):
                    log.info(f"  Downloading APK: {bug['apk_name']} "
                             f"(v{bug['version']} -> {bug['apk_tag']})...")
                    if self.download_apk(bug['apk_url'], apk_path):
                        size_mb = os.path.getsize(apk_path) / (1024 * 1024)
                        log.info(f"    OK: {size_mb:.1f} MB")
                    else:
                        log.warning(f"    FAILED: {bug['apk_url']}")
                    time.sleep(1)

        # Save JSON
        json_path = os.path.join(OUTPUT_DIR, "carbon_new_bugs.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(self.bugs, f, indent=2, default=str)
        log.info(f"Saved JSON: {json_path}")

        self._print_summary()

    def _print_summary(self):
        """Print summary."""
        print(f"\n{'='*70}")
        print(f"  CARBON-EXCLUSIVE GESTURE BUG CRAWLER — SUMMARY")
        print(f"{'='*70}")
        print(f"  Total bugs found:       {len(self.bugs)}")
        print(f"  Unique repos:           {len(set(b['repo'] for b in self.bugs))}")
        print(f"  Pre-release APKs:       {sum(1 for b in self.bugs if b['prerelease'])}")
        print(f"  Verified bugs:          {sum(1 for b in self.bugs if b['verified'])}")
        print(f"  CARBON-exclusive:       {sum(1 for b in self.bugs if b['rebl_can_do'] == 'no')}")
        print(f"  ReBL can also do:       {sum(1 for b in self.bugs if b['rebl_can_do'] == 'yes')}")
        if self.bugs:
            print(f"  Avg steps:              {sum(b['step_count'] for b in self.bugs) / len(self.bugs):.1f}")

        # Gesture distribution
        gesture_dist = {}
        for b in self.bugs:
            g = b['primary_gesture']
            gesture_dist[g] = gesture_dist.get(g, 0) + 1
        print(f"\n  Gesture Distribution:")
        for g, c in sorted(gesture_dist.items(), key=lambda x: -x[1]):
            rebl_no = sum(1 for b in self.bugs if b['primary_gesture'] == g and b['rebl_can_do'] == 'no')
            print(f"    {g:20s}: {c:3d} bugs ({rebl_no} CARBON-exclusive)")

        # Top repos
        repos = {}
        for b in self.bugs:
            repos[b['repo']] = repos.get(b['repo'], 0) + 1
        print(f"\n  Top Repos:")
        for repo, count in sorted(repos.items(), key=lambda x: -x[1])[:15]:
            print(f"    {repo}: {count}")

        print(f"\n  Output: {OUTPUT_DIR}/")
        print(f"{'='*70}")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    global OUTPUT_DIR
    parser = argparse.ArgumentParser(
        description="Crawl GitHub for CARBON-exclusive gesture bugs"
    )
    parser.add_argument('--token', help='GitHub API token (or set GITHUB_TOKEN env var)')
    parser.add_argument('--target', type=int, default=130,
                        help='Target number of bugs (default: 130)')
    parser.add_argument('--download', action='store_true',
                        help='Download APKs after crawling')
    parser.add_argument('--output', default=OUTPUT_DIR,
                        help='Output directory')
    args = parser.parse_args()

    OUTPUT_DIR = args.output

    token = args.token or os.getenv('GITHUB_TOKEN')
    if not token:
        print("ERROR: Provide --token or set GITHUB_TOKEN in .env")
        sys.exit(1)

    crawler = CarbonExclusiveCrawler(token)
    crawler.crawl(target=args.target)
    crawler.save_all(download_apks=args.download)


if __name__ == "__main__":
    main()
