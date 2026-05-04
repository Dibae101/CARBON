#!/usr/bin/env python3
"""
Targeted crawl for 20+ CARBON-exclusive gesture bugs.
Only pinch_zoom, double_tap, drag_and_drop, edge_swipe.
No orientation, no swipe, no long_press — ReBL can do those.
Strict: no login, no media library, no network content, no iOS.
"""

import os, re, sys, csv, json, time, requests
from typing import Optional, List, Tuple
from dotenv import load_dotenv

load_dotenv()

OUTPUT_DIR = "output/carbon_only_round2"

# All bugs we already have (repo, issue_number)
EXISTING = {
    ("A-EDev/Flow",27),("A-EDev/Flow",284),("Anthonyy232/Paperize",325),
    ("Anthonyy232/Paperize",426),("CodeWorksCreativeHub/mLauncher",809),
    ("Crustack/NotallyX",570),("Droid-ify/client",238),("Droid-ify/client",583),
    ("Fandroid745/Open-notes",15),("FoedusProgramme/Gramophone",174),
    ("FossifyOrg/Calendar",153),("FossifyOrg/Calendar",273),("FossifyOrg/Calendar",621),
    ("FossifyOrg/Camera",23),("FossifyOrg/Clock",156),("FossifyOrg/File-Manager",136),
    ("FossifyOrg/File-Manager",195),("FossifyOrg/Gallery",237),("FossifyOrg/Gallery",289),
    ("FossifyOrg/Gallery",363),("FossifyOrg/Gallery",642),("FossifyOrg/Gallery",678),
    ("FossifyOrg/Gallery",728),("FossifyOrg/Gallery",846),("FossifyOrg/Gallery",847),
    ("FossifyOrg/Gallery",940),("FossifyOrg/Launcher",198),("FossifyOrg/Launcher",304),
    ("FossifyOrg/Launcher",66),("FossifyOrg/Messages",359),("FossifyOrg/Messages",416),
    ("FossifyOrg/Messages",641),("FossifyOrg/Messages",80),("FossifyOrg/Notes",190),
    ("FossifyOrg/Notes",59),("FossifyOrg/Paint",125),("FossifyOrg/Paint",25),
    ("IacobIonut01/ReFra",526),("IacobIonut01/ReFra",768),
    ("Jays2Kings/tachiyomiJ2K",273),("Kin69/EasyNotes",356),
    ("LawnchairLauncher/lawnchair",2910),("LawnchairLauncher/lawnchair",4125),
    ("LawnchairLauncher/lawnchair",4642),("LawnchairLauncher/lawnchair",4708),
    ("LawnchairLauncher/lawnchair",5496),("LawnchairLauncher/lawnchair",5540),
    ("MetrolistGroup/Metrolist",3227),("MetrolistGroup/Metrolist",3391),
    ("MetrolistGroup/Metrolist",3561),("NeoApplications/Neo-Launcher",130),
    ("OuterTune/OuterTune",1044),("TeamNewPipe/NewPipe",10750),
    ("TeamNewPipe/NewPipe",8338),("abdallahmehiz/mpvKt",184),
    ("anilbeesetti/nextplayer",1127),("anilbeesetti/nextplayer",1389),
    ("ankidroid/Anki-Android",16135),("ankidroid/Anki-Android",5512),
    ("ankidroid/Anki-Android",5544),("ankidroid/Anki-Android",7138),
    ("ankidroid/Anki-Android",7730),("25huizengek1/ViTune",710),
    ("breezy-weather/breezy-weather",1639),("breezy-weather/breezy-weather",205),
    ("breezy-weather/breezy-weather",2159),("breezy-weather/breezy-weather",85),
    ("cromaguy/Rhythm",237),("cromaguy/Rhythm",281),("dessalines/thumb-key",371),
    ("espresso3389/methings",34),("fast4x/RiMusic",1152),
    ("fcitx5-android/fcitx5-android",841),("gsantner/markor",2746),
    ("iamrasel/lunar-launcher",82),("jocmp/capyreader",1149),
    ("libre-tube/LibreTube",8245),("marlboro-advance/mpvEx",53),
    ("msasikanth/twine",1566),("netmackan/ATimeTracker",124),
    ("streetcomplete/StreetComplete",6068),("syt0r/Kanji-Dojo",291),
    ("yairm210/Unciv",13517),("you-apps/ClockYou",85),
    ("you-apps/ConnectYou",155),("you-apps/VibeYou",89),
    ("you-apps/WallYou",216),
    # From round 1 crawl
    ("FossifyOrg/Gallery",295),("FossifyOrg/Calendar",76),
    ("FossifyOrg/Paint",20),("FossifyOrg/Launcher",44),
    ("FossifyOrg/Launcher",103),("FossifyOrg/Launcher",156),
    ("FossifyOrg/Notes",201),("FossifyOrg/Gallery",198),
}

SKIP_REPOS = {
    "ArcaneChat/android","meshtastic/Meshtastic-Android","mihonapp/mihon",
    "ls1intum/artemis-android","AntennaPod/AntennaPod","jocmp/capyreader",
    "libre-tube/LibreTube","TeamNewPipe/NewPipe","videolan/vlc-android",
    "niccokunzmann/mundraub-android","osmandapp/OsmAnd",
    "K1rakishou/Kuroba-Experimental","AdrienPoupa/VinylMusicPlayer",
    "Igalia/wolvic","mozilla-mobile/firefox-echo-show",
    "advplyr/audiobookshelf-app","bitwarden/android","bitwarden/mobile",
    "safe-global/safe-android","aniyomiorg/aniyomi","komikku-app/komikku",
    "null2264/yokai","vfsfitvnm/ViMusic","z-huang/InnerTune",
    "fast4x/RiMusic","fast4x/RiPlay","MetrolistGroup/Metrolist",
    "OuterTune/OuterTune","vivizzz007/vivi-music","sayaka-sh/spmp",
    "zyrouge/symphony","FrancescoGrazioso/Meld",
    "RetroMusicPlayer/RetroMusicPlayer","FoedusProgramme/Gramophone",
    "cromaguy/Rhythm","thunder-app/thunder","mudkipme/MoeMemosAndroid",
    "openhab/openhab-android","remotv/controller-for-android",
    "Mahmud0808/Iconify","saber-notes/saber","SimpleMobileTools/Simple-Gallery",
    "RyanYuuki/AnymeX","jrpie/launcher","mozilla-mobile/fenix",
    "mozilla-mobile/focus-android","bromite/bromite","microg/GmsCore",
}

SKIP_TITLE_WORDS = [
    "ios","iphone","ipad","apple","garmin","watch","wear os",
    "talkback","accessibility","screen reader",
]

SKIP_BODY_WORDS = [
    "log in","sign in","sign up","create account","register",
    "username","password","credentials","api key","add account",
    "add songs","import music","music library","playlist","add to library",
    "play a song","play song","audiobook","podcast","episode",
    "play a video","play video","open a video","stream video",
    "manga","comic","chapter","rss","feed url","subscribe to",
    "connect to server","sync with","bluetooth","garmin","smartwatch",
    "incoming call","receive a call","phone call","sim card",
    "banking app","open bank",
]

# ONLY these gestures — the ones ReBL CANNOT do
CARBON_GESTURES = {
    "pinch_zoom": ["pinch","pinch to zoom","pinch-to-zoom","zoom in","zoom out",
                   "two finger","two-finger","multi-touch","image zoom","map zoom",
                   "canvas zoom","magnify","pinch zoom"],
    "double_tap": ["double tap","double-tap","double click","double-click",
                   "doubletap","double touch","tap twice"],
    "drag_and_drop": ["drag and drop","drag-and-drop","drag to reorder",
                      "drag handle","reorder","rearrange","drag to move",
                      "draggable","drag to delete","drag item"],
    "edge_swipe": ["edge swipe","back gesture","gesture navigation",
                   "predictive back","swipe from edge","navigation drawer",
                   "drawer swipe"],
}

# Targeted queries — ONLY for CARBON-exclusive gestures, fresh repos
QUERIES = [
    # ═══ PINCH / ZOOM — new repos ═══
    '"steps to reproduce" "pinch" label:bug language:Kotlin is:closed',
    '"steps to reproduce" "pinch to zoom" label:bug is:closed',
    '"steps to reproduce" "zoom in" "zoom out" label:bug language:Kotlin',
    '"steps to reproduce" "zoom" "image" label:bug language:Java is:closed',
    '"steps to reproduce" "zoom" "crash" label:bug language:Java is:closed',
    '"steps to reproduce" "pinch" "crash" label:bug language:Java',
    '"steps to reproduce" "zoom" "broken" label:bug language:Kotlin',
    '"steps to reproduce" "zoom" "freeze" label:bug',
    'repo:AChep/keyguard-app label:bug "zoom"',
    'repo:AChep/keyguard-app label:bug "pinch"',
    'repo:dessalines/jerboa label:bug "zoom"',
    'repo:dessalines/jerboa label:bug "pinch"',
    'repo:Docile-Alligator/Infinity-For-Reddit label:bug "zoom"',
    'repo:Docile-Alligator/Infinity-For-Reddit label:bug "pinch"',
    'repo:tuskyapp/Tusky label:bug "zoom"',
    'repo:tuskyapp/Tusky label:bug "pinch"',

    # ═══ DOUBLE TAP — new repos ═══
    '"steps to reproduce" "double tap" label:bug language:Kotlin is:closed',
    '"steps to reproduce" "double-tap" label:bug is:closed',
    '"steps to reproduce" "double tap" "crash" label:bug language:Kotlin',
    '"steps to reproduce" "double tap" "not working" label:bug',
    'repo:AChep/keyguard-app label:bug "double tap"',
    'repo:dessalines/jerboa label:bug "double tap"',
    'repo:FossifyOrg/Gallery label:bug "double"',
    'repo:FossifyOrg/Calendar label:bug "double"',
    'repo:tasks/tasks label:bug "double tap"',
    'repo:tasks/tasks label:bug "double"',

    # ═══ DRAG AND DROP — new repos ═══
    '"steps to reproduce" "drag and drop" label:bug language:Kotlin is:closed',
    '"steps to reproduce" "drag" "reorder" label:bug language:Kotlin is:closed',
    '"steps to reproduce" "drag" "reorder" label:bug language:Java',
    '"steps to reproduce" "rearrange" label:bug language:Kotlin',
    '"steps to reproduce" "drag" "crash" label:bug language:Kotlin',
    'repo:tasks/tasks label:bug "drag"',
    'repo:tasks/tasks label:bug "reorder"',
    'repo:FossifyOrg/Contacts label:bug "drag"',
    'repo:FossifyOrg/Calendar label:bug "drag"',
    'repo:FossifyOrg/Notes label:bug "drag"',
    'repo:FossifyOrg/File-Manager label:bug "drag"',
    'repo:Etar-Group/Etar-Calendar label:bug "drag"',
    'repo:iSoron/uhabits label:bug "drag"',
    'repo:iSoron/uhabits label:bug "reorder"',

    # ═══ EDGE SWIPE / BACK GESTURE — new repos ═══
    '"steps to reproduce" "back gesture" label:bug language:Kotlin is:closed',
    '"steps to reproduce" "predictive back" label:bug is:closed',
    '"steps to reproduce" "gesture navigation" label:bug language:Kotlin is:closed',
    '"steps to reproduce" "edge swipe" label:bug is:closed',
    '"steps to reproduce" "back gesture" "crash" label:bug',
    '"steps to reproduce" "predictive back" "crash" label:bug',
    'repo:FossifyOrg/Gallery label:bug "back gesture"',
    'repo:FossifyOrg/Gallery label:bug "predictive back"',
    'repo:FossifyOrg/Calendar label:bug "back"',
    'repo:FossifyOrg/Notes label:bug "back gesture"',
    'repo:tasks/tasks label:bug "back gesture"',
    'repo:tasks/tasks label:bug "predictive back"',
    'repo:breezy-weather/breezy-weather label:bug "back gesture"',
    'repo:breezy-weather/breezy-weather label:bug "predictive back"',
    'repo:Etar-Group/Etar-Calendar label:bug "back gesture"',
    'repo:dessalines/thumb-key label:bug "back gesture"',
]

QUERIES = list(dict.fromkeys(QUERIES))
REQUEST_DELAY = 1.3
MAX_RETRIES = 3
MAX_BUGS_PER_REPO = 3
MAX_APK_SIZE_MB = 150


def classify(text):
    text_l = text.lower()
    for cat, kws in CARBON_GESTURES.items():
        for kw in kws:
            if kw in text_l:
                return cat
    return None


def extract_version(text):
    text_nc = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    _v = r'(\d+\.\d+(?:\.\d+)?(?:[-.]?(?:alpha|beta|rc|dev|pre|snapshot|nightly)\d*(?:\.\d+)*)?)'
    for p in [r'(?:app\s+)?version\s*[:=]\s*[vV]?' + _v,
              r'\*\*(?:app\s+)?version\*\*\s*[:=]\s*[vV]?' + _v]:
        m = re.search(p, text_nc, re.IGNORECASE)
        if m: return m.group(1)
    for block in re.findall(r'```(?:\w+)?\s*\n(.*?)```', text, re.DOTALL):
        m = re.search(r'version\s*=\s*[vV]?' + _v, block, re.IGNORECASE)
        if m: return m.group(1)
    m = re.search(r'(?:using|running|installed|on)\s+(?:version\s+)?[vV]?' + _v, text_nc, re.IGNORECASE)
    if m: return m.group(1)
    return None


def extract_steps(body):
    steps = []
    for _, step in re.findall(r'(?:^|\n)\s*(\d+)[.)]\s*(.+?)(?=\n\s*\d+[.)]|\n\n|\Z)', body, re.DOTALL):
        s = re.sub(r'\s+', ' ', step.strip())
        if len(s) > 5: steps.append(s)
    return steps


def norm_ver(v):
    v = re.sub(r'^[vV]', '', v.strip())
    v = re.sub(r'[^0-9a-zA-Z.]', '.', v)
    return re.sub(r'\.+', '.', v).strip('.')


def ver_match(target, tag):
    t, g = norm_ver(target), norm_ver(tag)
    if t == g: return True
    if t+'.0' == g or g+'.0' == t: return True
    if t in g and len(t) >= 3:
        i = g.index(t)
        if (i == 0 or not g[i-1].isdigit()) and (i+len(t) >= len(g) or not g[i+len(t)].isdigit()):
            return True
    return False


class Crawler:
    def __init__(self, token):
        self.s = requests.Session()
        self.s.headers.update({'Authorization': f'token {token}',
                               'Accept': 'application/vnd.github.v3+json',
                               'User-Agent': 'CarbonOnly/2.0'})
        self.bugs = []
        self.seen = set()
        self.rel_cache = {}
        self.skip_log = {}
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    def api(self, url, params=None):
        for _ in range(MAX_RETRIES):
            try:
                r = self.s.get(url, params=params, timeout=30)
                if r.status_code == 200: return r.json()
                if r.status_code == 403:
                    w = max(int(r.headers.get('X-RateLimit-Reset', 0)) - time.time(), 60)
                    print(f"  Rate limited, waiting {w:.0f}s...")
                    time.sleep(w); continue
                if r.status_code == 422: return None
                return None
            except: time.sleep(5)
        return None

    def search(self, q, pages=3):
        items = []
        for p in range(1, pages+1):
            d = self.api("https://api.github.com/search/issues",
                         {'q': q, 'per_page': 30, 'page': p, 'sort': 'created', 'order': 'desc'})
            if not d or 'items' not in d: break
            if not d['items']: break
            items.extend(d['items'])
            time.sleep(REQUEST_DELAY)
        return items

    def get_releases(self, repo):
        if repo in self.rel_cache: return self.rel_cache[repo]
        rels = self.api(f"https://api.github.com/repos/{repo}/releases", {'per_page': 100}) or []
        self.rel_cache[repo] = rels
        time.sleep(REQUEST_DELAY)
        return rels

    def find_apk(self, repo, ver):
        if not ver: return None
        for rel in self.get_releases(repo):
            if not ver_match(ver, rel.get('tag_name', '')): continue
            best, best_score = None, -1
            for a in rel.get('assets', []):
                n = a['name'].lower()
                if not n.endswith('.apk'): continue
                if a['size'] / 1048576 > MAX_APK_SIZE_MB: continue
                sc = 5
                if 'universal' in n: sc = 30
                elif 'foss' in n and 'release' in n: sc = 25
                elif 'release' in n: sc = 20
                elif 'arm64' in n: sc = 15
                if 'debug' in n: sc -= 10
                if sc > best_score: best, best_score = a, sc
            if best:
                return {'url': best['browser_download_url'], 'name': best['name'],
                        'tag': rel['tag_name'], 'pre': rel.get('prerelease', False)}
        return None

    def check_comments(self, issue):
        """Return True if we should SKIP (cannot reproduce)."""
        cu = issue.get('comments_url', '')
        if not cu or issue.get('comments', 0) == 0: return False
        comments = self.api(cu, {'per_page': 30})
        if not isinstance(comments, list): return False
        time.sleep(REQUEST_DELAY)
        for c in comments:
            b = (c.get('body') or '').lower()
            auth = c.get('author_association', '')
            if auth in ('OWNER', 'MEMBER', 'COLLABORATOR'):
                if any(x in b for x in ['cannot reproduce', "can't reproduce",
                    'unable to reproduce', 'works for me', 'not a bug',
                    'by design', 'wontfix']): return True
        return False

    def process(self, issue):
        url = issue.get('html_url', '')
        if url in self.seen: return None
        self.seen.add(url)

        title = issue.get('title', '')
        body = issue.get('body') or ''
        repo_url = issue.get('repository_url', '')
        repo = '/'.join(repo_url.split('/')[-2:]) if repo_url else ''
        num = issue.get('number', 0)
        iid = f"{repo}#{num}"

        if (repo, num) in EXISTING: return None
        if repo in SKIP_REPOS: return None
        tl = title.lower()
        if any(w in tl for w in SKIP_TITLE_WORDS): return None
        if len(body) < 80 or len(body) > 12000: return None

        # Must have steps section
        bl = body.lower()
        if not any(m in bl for m in ['steps to reproduce','to reproduce','how to reproduce',
                                      'reproduction steps','### steps']): return None

        steps = extract_steps(body)
        if len(steps) < 2 or len(steps) > 7:
            self.skip_log[iid] = f"steps={len(steps)}"
            return None

        # Must have expected/actual
        has_exp = any(m in bl for m in ['expected behavior','expected behaviour','expected result',
                                         'should be','should show','it should','supposed to'])
        has_act = any(m in bl for m in ['actual behavior','actual behaviour','actual result',
                                         'instead','but it','however','crash','doesn\'t work',
                                         'not working','broken','fails','wrong'])
        if not (has_exp and has_act):
            self.skip_log[iid] = "no expected/actual"
            return None

        # Classify gesture — MUST be CARBON-exclusive
        full = f"{title} {' '.join(steps)}"
        gesture = classify(full)
        if gesture is None:
            gesture = classify(f"{title} {body}")
        if gesture is None:
            self.skip_log[iid] = "not carbon gesture"
            return None

        # Check body for skip words
        check = f"{tl} {bl[:1500]} {' '.join(steps)}".lower()
        for w in SKIP_BODY_WORDS:
            if w in check:
                self.skip_log[iid] = f"needs: {w}"
                return None

        # Version + APK
        ver = extract_version(body)
        if not ver:
            self.skip_log[iid] = "no version"
            return None
        apk = self.find_apk(repo, ver)
        if not apk:
            self.skip_log[iid] = f"no APK for v{ver}"
            return None

        # Comment check
        if self.check_comments(issue):
            self.skip_log[iid] = "cannot reproduce"
            return None

        return {
            'title': title, 'repo': repo, 'issue_number': num,
            'issue_url': url, 'version': ver, 'gesture': gesture,
            'steps': steps, 'step_count': len(steps), 'body': body,
            'apk_url': apk['url'], 'apk_name': apk['name'],
            'apk_tag': apk['tag'], 'pre': apk['pre'],
            'state': issue.get('state', ''),
            'labels': [l['name'] for l in issue.get('labels', [])],
        }

    def crawl(self, target=25):
        print(f"Crawling for {target} CARBON-exclusive bugs...")
        repo_counts = {}
        for i, q in enumerate(QUERIES):
            if len(self.bugs) >= target: break
            print(f"\n[{i+1}/{len(QUERIES)}] {q[:70]}...")
            issues = self.search(q, pages=3)
            print(f"  {len(issues)} issues")
            for iss in issues:
                if len(self.bugs) >= target: break
                ru = iss.get('repository_url', '')
                repo = '/'.join(ru.split('/')[-2:]) if ru else ''
                if repo_counts.get(repo, 0) >= MAX_BUGS_PER_REPO: continue
                bug = self.process(iss)
                if bug:
                    repo_counts[bug['repo']] = repo_counts.get(bug['repo'], 0) + 1
                    self.bugs.append(bug)
                    pre = " [PRE]" if bug['pre'] else ""
                    print(f"  >>> [{len(self.bugs)}/{target}] {bug['repo']}#{bug['issue_number']}: "
                          f"{bug['title'][:50]}... [{bug['gesture']}] "
                          f"v{bug['version']}->{bug['apk_tag']} {bug['step_count']}steps{pre}")

        print(f"\nDone: {len(self.bugs)} bugs")
        gd = {}
        for b in self.bugs: gd[b['gesture']] = gd.get(b['gesture'], 0) + 1
        for g, c in sorted(gd.items(), key=lambda x: -x[1]):
            print(f"  {g}: {c}")

    def save(self, download=False):
        if not self.bugs: return
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        for bug in self.bugs:
            fn = f"{bug['repo'].replace('/', '_')}_{bug['issue_number']}"
            fp = os.path.join(OUTPUT_DIR, fn)
            os.makedirs(fp, exist_ok=True)

            # Bug report
            steps_fmt = "\n".join(f"  {i+1}. {s}" for i, s in enumerate(bug['steps']))
            # Extract expected/actual
            exp, act = "", ""
            for pat in [r'(?:###?\s*)?(?:expected\s+(?:behavior|behaviour|result))[:\s]*\n+(.*?)(?=\n###?\s|\n\*\*|\Z)']:
                m = re.search(pat, bug['body'], re.I | re.DOTALL)
                if m: exp = m.group(1).strip()[:300]; break
            for pat in [r'(?:###?\s*)?(?:actual\s+(?:behavior|behaviour|result))[:\s]*\n+(.*?)(?=\n###?\s|\n\*\*|\Z)']:
                m = re.search(pat, bug['body'], re.I | re.DOTALL)
                if m: act = m.group(1).strip()[:300]; break
            body_clean = re.sub(r'<!--.*?-->', '', bug['body'], flags=re.DOTALL)
            body_clean = re.sub(r'!\[.*?\]\(.*?\)', '[screenshot]', body_clean)

            br = f"""{bug['title']}

App: {bug['repo']}
Version: {bug['version']}
Issue: {bug['issue_url']}
APK: {bug['apk_url']}
APK Tag: {bug['apk_tag']}
Primary Gesture: {bug['gesture']}
ReBL can do: no
CARBON can do: yes

Steps to Reproduce:
{steps_fmt}

Expected Behavior:
  {exp or '(see full report below)'}

Actual Behavior:
  {act or '(see full report below)'}

--- Full Issue Body ---
{body_clean}
"""
            with open(os.path.join(fp, "bug_report.txt"), 'w') as f: f.write(br)

            if download:
                apk_path = os.path.join(fp, bug['apk_name'])
                if not os.path.exists(apk_path):
                    print(f"  DL: {bug['apk_name']}...")
                    try:
                        r = self.s.get(bug['apk_url'], stream=True, timeout=300)
                        r.raise_for_status()
                        with open(apk_path, 'wb') as f:
                            for chunk in r.iter_content(8192): f.write(chunk)
                        mb = os.path.getsize(apk_path) / 1048576
                        print(f"    OK: {mb:.1f}MB")
                    except Exception as e:
                        print(f"    FAIL: {e}")
                    time.sleep(1)

        # CSV
        with open(os.path.join(OUTPUT_DIR, "bugs.csv"), 'w', newline='') as f:
            w = csv.DictWriter(f, ['repo','issue_number','title','version','gesture',
                                   'step_count','apk_tag','pre','state','issue_url'],
                               extrasaction='ignore')
            w.writeheader()
            for b in self.bugs: w.writerow(b)
        print(f"Saved to {OUTPUT_DIR}/")


if __name__ == "__main__":
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("Set GITHUB_TOKEN in .env")
        sys.exit(1)
    c = Crawler(token)
    c.crawl(target=25)
    c.save(download=True)
