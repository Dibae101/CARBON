"""
CARBON-Exclusive Gesture Bug Crawl Config
==========================================
Targets 120+ NEW bugs across gesture categories that ONLY CARBON can handle.
ReBL can already do: click, long_click, set_text, swipe (directional), scroll,
                     back, orientation, restart, wait.
CARBON adds: pinch, double_tap_screen, drag_and_drop, edge_swipe, media_gesture,
             quick_tap, two_finger_swipe, two_finger_tap, three_finger_swipe,
             rotate_gesture, tap_screen (coordinate), swipe_region, home,
             open_notifications.

Strategy:
  - Focus on gestures ReBL CANNOT do (skip pure long_press bugs)
  - Include pre-release/alpha/beta/rc APKs (more bugs)
  - Broader repo coverage for diversity
  - Strict quality: must have validation in comments, no "cannot reproduce"
"""

# ── CARBON-exclusive gesture keywords ──
# These are gestures that REQUIRE CARBON's extended action set.
# We intentionally EXCLUDE pure "long press" since ReBL handles those.
GESTURE_KEYWORDS = [
    # ═══ PINCH / ZOOM (requires CARBON's pinch action) ═══
    "pinch", "pinch to zoom", "pinch-to-zoom", "pinch zoom", "pinch in", "pinch out",
    "zoom in", "zoom out", "zoom", "image zoom", "map zoom", "canvas zoom",
    "two finger", "two-finger", "multi-touch", "multitouch",
    "scale", "magnify",

    # ═══ DOUBLE TAP (requires CARBON's double_tap_screen) ═══
    "double tap", "double-tap", "double click", "double-click",
    "doubletap", "double touch", "tap twice", "two taps",

    # ═══ DRAG AND DROP (requires CARBON's drag_and_drop) ═══
    "drag and drop", "drag-and-drop", "drag to reorder", "drag handle",
    "drag", "reorder", "rearrange", "drag to move",
    "sortable", "draggable", "drag to delete", "drag item",

    # ═══ EDGE / NAVIGATION GESTURES (requires CARBON's edge_swipe) ═══
    "edge swipe", "back gesture", "gesture navigation", "edge gesture",
    "navigation gesture", "predictive back", "swipe from edge",
    "drawer swipe", "navigation drawer",

    # ═══ MEDIA GESTURES (requires CARBON's media_gesture) ═══
    "volume gesture", "brightness gesture", "seek gesture",
    "player gesture", "video controls", "player controls",
    "swipe to seek", "swipe volume", "swipe brightness",

    # ═══ COORDINATE-BASED TAPS (requires CARBON's tap_screen) ═══
    "tap on video", "tap on map", "tap on canvas", "tap on image",
    "tap on overlay", "tap on player",

    # ═══ SWIPE REGION / PRECISE SWIPE (requires CARBON's swipe_region) ═══
    "swipe to dismiss", "swipe to delete", "swipe notification",
    "dismiss notification", "swipe away",
    "swipe left", "swipe right", "swipe up", "swipe down",
    "fling", "pull to refresh", "pull-to-refresh",

    # ═══ ROTATION (requires CARBON's rotate_gesture) ═══
    "rotate", "rotation", "rotate gesture",

    # ═══ ORIENTATION CHANGE (CARBON handles better with visual context) ═══
    "orientation", "landscape", "portrait", "screen rotation", "auto-rotate",

    # ═══ QUICK TAP / TIMING (requires CARBON's quick_tap) ═══
    "quick tap", "fast tap", "rapid tap", "immediately tap",
    "race condition", "timing", "before animation",

    # ═══ HOME / NOTIFICATIONS (requires CARBON's home/open_notifications) ═══
    "home screen", "notification", "status bar", "quick settings",

    # ═══ GENERAL GESTURE ISSUES ═══
    "gesture not working", "gesture broken", "gesture conflict",
    "touch not registered", "unresponsive touch",
]

# ── Search queries — BROAD + TARGETED ──
# Focus on repos known to have gesture-heavy UIs and pre-release APKs.
SEARCH_QUERIES = [
    # ═══════════════════════════════════════════════════════════════════
    # BROAD QUERIES — cast a wide net across all of GitHub
    # ═══════════════════════════════════════════════════════════════════

    # Pinch / Zoom
    '"steps to reproduce" "pinch" label:bug language:Kotlin',
    '"steps to reproduce" "pinch" label:bug language:Java',
    '"steps to reproduce" "pinch to zoom" label:bug',
    '"steps to reproduce" "zoom in" label:bug language:Kotlin',
    '"steps to reproduce" "zoom in" label:bug language:Java',
    '"steps to reproduce" "zoom out" label:bug language:Kotlin',
    '"steps to reproduce" "zoom" "image" label:bug language:Kotlin',
    '"steps to reproduce" "zoom" "map" label:bug',
    '"steps to reproduce" "zoom" "pdf" label:bug',
    '"steps to reproduce" "zoom" "photo" label:bug',
    '"steps to reproduce" "zoom" "canvas" label:bug',
    '"steps to reproduce" "zoom" "gallery" label:bug',
    '"steps to reproduce" "zoom" "viewer" label:bug',
    '"steps to reproduce" "zoom" "camera" label:bug',
    '"steps to reproduce" "zoom" "crash" label:bug language:Kotlin',
    '"steps to reproduce" "zoom" "crash" label:bug language:Java',
    '"steps to reproduce" "zoom" "not working" label:bug',
    '"steps to reproduce" "two finger" "zoom" label:bug',
    '"steps to reproduce" "multi-touch" label:bug',
    '"steps to reproduce" "pinch to zoom" language:Kotlin',
    '"steps to reproduce" "pinch to zoom" language:Java',

    # Double Tap
    '"steps to reproduce" "double tap" label:bug language:Kotlin',
    '"steps to reproduce" "double tap" label:bug language:Java',
    '"steps to reproduce" "double-tap" label:bug language:Kotlin',
    '"steps to reproduce" "double-tap" label:bug language:Java',
    '"steps to reproduce" "double tap" "zoom" label:bug',
    '"steps to reproduce" "double tap" "fullscreen" label:bug',
    '"steps to reproduce" "double tap" "crash" label:bug',
    '"steps to reproduce" "double click" label:bug language:Kotlin',
    '"steps to reproduce" "double tap" language:Kotlin',
    '"steps to reproduce" "double tap" language:Java',

    # Drag and Drop
    '"steps to reproduce" "drag and drop" label:bug language:Kotlin',
    '"steps to reproduce" "drag and drop" label:bug language:Java',
    '"steps to reproduce" "drag-and-drop" label:bug',
    '"steps to reproduce" "drag" "reorder" label:bug language:Kotlin',
    '"steps to reproduce" "drag" "reorder" label:bug language:Java',
    '"steps to reproduce" "rearrange" label:bug language:Kotlin',
    '"steps to reproduce" "drag" "widget" label:bug',
    '"steps to reproduce" "drag" "slider" label:bug',
    '"steps to reproduce" "drag" "seekbar" label:bug',
    '"steps to reproduce" "drag to" label:bug language:Kotlin',
    '"steps to reproduce" "drag" "crash" label:bug',
    '"steps to reproduce" "drag" language:Kotlin is:open',

    # Swipe gestures (precise / region-based)
    '"steps to reproduce" "swipe" "dismiss" label:bug language:Kotlin',
    '"steps to reproduce" "swipe" "delete" label:bug language:Kotlin',
    '"steps to reproduce" "swipe" "gesture" label:bug language:Kotlin',
    '"steps to reproduce" "swipe" "gesture" label:bug language:Java',
    '"steps to reproduce" "swipe left" label:bug language:Kotlin',
    '"steps to reproduce" "swipe right" label:bug language:Kotlin',
    '"steps to reproduce" "swipe" "back" label:bug language:Kotlin',
    '"steps to reproduce" "fling" label:bug language:Kotlin',
    '"steps to reproduce" "pull to refresh" label:bug language:Kotlin',

    # Edge / Navigation gestures
    '"steps to reproduce" "edge swipe" label:bug',
    '"steps to reproduce" "back gesture" label:bug language:Kotlin',
    '"steps to reproduce" "gesture navigation" label:bug language:Kotlin',
    '"steps to reproduce" "gesture navigation" label:bug language:Java',
    '"steps to reproduce" "predictive back" label:bug',
    '"steps to reproduce" "swipe from edge" label:bug',
    '"steps to reproduce" "navigation drawer" "swipe" label:bug',

    # Rotation / Orientation
    '"steps to reproduce" "rotate" "screen" label:bug language:Kotlin',
    '"steps to reproduce" "orientation" "change" label:bug language:Kotlin',
    '"steps to reproduce" "landscape" "portrait" label:bug language:Kotlin',
    '"steps to reproduce" "screen rotation" label:bug language:Kotlin',
    '"steps to reproduce" "auto-rotate" label:bug',

    # Scroll (complex — nested, overscroll, fling)
    '"steps to reproduce" "scroll" "crash" label:bug language:Kotlin',
    '"steps to reproduce" "overscroll" label:bug language:Kotlin',
    '"steps to reproduce" "nested scroll" label:bug language:Kotlin',
    '"steps to reproduce" "scroll" "not working" label:bug language:Kotlin',

    # Media player gestures
    '"steps to reproduce" "volume" "swipe" label:bug',
    '"steps to reproduce" "brightness" "swipe" label:bug',
    '"steps to reproduce" "seek" "gesture" label:bug',
    '"steps to reproduce" "player" "gesture" label:bug',
    '"steps to reproduce" "video" "controls" "gesture" label:bug',

    # Notification / Home interactions
    '"steps to reproduce" "notification" "swipe" label:bug language:Kotlin',
    '"steps to reproduce" "notification" "dismiss" label:bug language:Kotlin',

    # ═══════════════════════════════════════════════════════════════════
    # TARGETED REPOS — known gesture-heavy apps with APK releases
    # ═══════════════════════════════════════════════════════════════════

    # Gallery / Image viewers
    'repo:FossifyOrg/Gallery label:bug "swipe"',
    'repo:FossifyOrg/Gallery label:bug "zoom"',
    'repo:FossifyOrg/Gallery label:bug "double tap"',
    'repo:FossifyOrg/Gallery label:bug "rotate"',
    'repo:FossifyOrg/Gallery label:bug "pinch"',
    'repo:SimpleMobileTools/Simple-Gallery label:bug "zoom"',
    'repo:SimpleMobileTools/Simple-Gallery label:bug "swipe"',
    'repo:SimpleMobileTools/Simple-Gallery label:bug "double tap"',
    'repo:T8RIN/ImageToolbox label:bug "zoom"',
    'repo:T8RIN/ImageToolbox label:bug "pinch"',
    'repo:T8RIN/ImageToolbox label:bug "double tap"',
    'repo:T8RIN/ImageToolbox label:bug "drag"',
    'repo:T8RIN/ImageToolbox label:bug "swipe"',

    # Paint / Drawing
    'repo:FossifyOrg/Paint label:bug "zoom"',
    'repo:FossifyOrg/Paint label:bug "pinch"',
    'repo:FossifyOrg/Paint label:bug "drag"',
    'repo:FossifyOrg/Paint label:bug "draw"',
    'repo:FossifyOrg/Paint label:bug "touch"',

    # Calendar
    'repo:FossifyOrg/Calendar label:bug "double tap"',
    'repo:FossifyOrg/Calendar label:bug "drag"',
    'repo:FossifyOrg/Calendar label:bug "swipe"',
    'repo:FossifyOrg/Calendar label:bug "pinch"',
    'repo:Etar-Group/Etar-Calendar label:bug "drag"',
    'repo:Etar-Group/Etar-Calendar label:bug "zoom"',
    'repo:Etar-Group/Etar-Calendar label:bug "swipe"',

    # Notes / Text editors
    'repo:FossifyOrg/Notes label:bug "drag"',
    'repo:FossifyOrg/Notes label:bug "swipe"',
    'repo:Crustack/NotallyX label:bug "drag"',
    'repo:Crustack/NotallyX label:bug "swipe"',
    'repo:gsantner/markor label:bug "zoom"',
    'repo:gsantner/markor label:bug "swipe"',
    'repo:gsantner/markor label:bug "double tap"',

    # File Manager
    'repo:FossifyOrg/File-Manager label:bug "drag"',
    'repo:FossifyOrg/File-Manager label:bug "swipe"',
    'repo:TeamAmaze/AmazeFileManager label:bug "drag"',
    'repo:TeamAmaze/AmazeFileManager label:bug "swipe"',
    'repo:zhanghai/MaterialFiles label:bug "swipe"',
    'repo:zhanghai/MaterialFiles label:bug "drag"',

    # Maps
    'repo:organicmaps/organicmaps label:bug "pinch"',
    'repo:organicmaps/organicmaps label:bug "zoom"',
    'repo:organicmaps/organicmaps label:bug "double tap"',
    'repo:organicmaps/organicmaps label:bug "swipe"',
    'repo:organicmaps/organicmaps label:bug "rotate"',
    'repo:streetcomplete/StreetComplete label:bug "zoom"',
    'repo:streetcomplete/StreetComplete label:bug "pinch"',
    'repo:streetcomplete/StreetComplete label:bug "swipe"',
    'repo:osmandapp/OsmAnd label:bug "pinch"',
    'repo:osmandapp/OsmAnd label:bug "zoom"',
    'repo:osmandapp/OsmAnd label:bug "double tap"',
    'repo:osmandapp/OsmAnd label:bug "rotate"',

    # Launcher
    'repo:FossifyOrg/Launcher label:bug "drag"',
    'repo:FossifyOrg/Launcher label:bug "swipe"',
    'repo:FossifyOrg/Launcher label:bug "pinch"',
    'repo:LawnchairLauncher/lawnchair label:bug "pinch"',
    'repo:LawnchairLauncher/lawnchair label:bug "double tap"',
    'repo:LawnchairLauncher/lawnchair label:bug "drag"',
    'repo:LawnchairLauncher/lawnchair label:bug "swipe"',
    'repo:LawnchairLauncher/lawnchair label:bug "gesture"',

    # Music players (offline capable, no login)
    'repo:fast4x/RiMusic label:bug "swipe"',
    'repo:fast4x/RiMusic label:bug "gesture"',
    'repo:fast4x/RiMusic label:bug "double tap"',
    'repo:FossifyOrg/Music-Player label:bug "swipe"',
    'repo:FossifyOrg/Music-Player label:bug "drag"',
    'repo:OuterTune/OuterTune label:bug "swipe"',
    'repo:OuterTune/OuterTune label:bug "drag"',
    'repo:OuterTune/OuterTune label:bug "gesture"',

    # Video players (gesture-heavy)
    'repo:anilbeesetti/nextplayer label:bug "gesture"',
    'repo:anilbeesetti/nextplayer label:bug "swipe"',
    'repo:anilbeesetti/nextplayer label:bug "double tap"',
    'repo:anilbeesetti/nextplayer label:bug "zoom"',
    'repo:abdallahmehiz/mpvKt label:bug "gesture"',
    'repo:abdallahmehiz/mpvKt label:bug "swipe"',
    'repo:abdallahmehiz/mpvKt label:bug "double tap"',

    # Keyboard
    'repo:florisboard/florisboard label:bug "drag"',
    'repo:florisboard/florisboard label:bug "swipe"',
    'repo:florisboard/florisboard label:bug "double tap"',
    'repo:dessalines/thumb-key label:bug "swipe"',
    'repo:dessalines/thumb-key label:bug "drag"',

    # PDF viewers
    'repo:grapheneos/PdfViewer label:bug "zoom"',
    'repo:grapheneos/PdfViewer label:bug "pinch"',
    'repo:grapheneos/PdfViewer label:bug "double tap"',

    # Camera
    'repo:FossifyOrg/Camera label:bug "zoom"',
    'repo:FossifyOrg/Camera label:bug "pinch"',
    'repo:FossifyOrg/Camera label:bug "tap"',

    # Tasks / TODO
    'repo:tasks/tasks label:bug "drag"',
    'repo:tasks/tasks label:bug "swipe"',

    # Weather
    'repo:breezy-weather/breezy-weather label:bug "swipe"',
    'repo:breezy-weather/breezy-weather label:bug "drag"',

    # RSS / Feed readers (offline capable, no login needed)
    'repo:AntennaPod/AntennaPod label:bug "swipe"',
    'repo:AntennaPod/AntennaPod label:bug "gesture"',

    # Games (gesture-heavy)
    'repo:yairm210/Unciv label:bug "zoom"',
    'repo:yairm210/Unciv label:bug "pinch"',
    'repo:yairm210/Unciv label:bug "drag"',

    # Contacts / Dialer / SMS
    'repo:FossifyOrg/Contacts label:bug "drag"',
    'repo:FossifyOrg/Contacts label:bug "swipe"',
    'repo:FossifyOrg/Dialer label:bug "swipe"',
    'repo:FossifyOrg/SMS-Messenger label:bug "swipe"',

    # Clock / Timer
    'repo:FossifyOrg/Clock label:bug "swipe"',

    # Calculator
    'repo:FossifyOrg/Calculator label:bug "swipe"',
    'repo:Darkempire78/OpenCalc label:bug "swipe"',

    # Voice Recorder
    'repo:FossifyOrg/Voice-Recorder label:bug "swipe"',

    # Browser (gesture-heavy, offline testable)
    'repo:niccokunzmann/mundraub-android label:bug "zoom"',

    # Misc gesture-heavy apps
    'repo:K1rakishou/Kuroba-Experimental label:bug "zoom"',
    'repo:K1rakishou/Kuroba-Experimental label:bug "double tap"',
    'repo:K1rakishou/Kuroba-Experimental label:bug "swipe"',

    # ═══ NEW REPOS not in previous crawl ═══
    # Document viewers
    'repo:AdrienPoupa/VinylMusicPlayer label:bug "swipe"',
    'repo:AdrienPoupa/VinylMusicPlayer label:bug "gesture"',
    'repo:AdrienPoupa/VinylMusicPlayer label:bug "drag"',

    # More gallery/image apps
    'repo:deckerst/MaterialGallery label:bug "zoom"',
    'repo:deckerst/MaterialGallery label:bug "swipe"',
    'repo:deckerst/MaterialGallery label:bug "pinch"',

    # Habit trackers / productivity (simple, offline)
    'repo:iSoron/uhabits label:bug "drag"',
    'repo:iSoron/uhabits label:bug "swipe"',

    # Drawing / Whiteboard
    'repo:niccokunzmann/mundraub-android label:bug "pinch"',

    # More music players
    'repo:AntonyJR/AppImageUpdater label:bug "swipe"',

    # Additional broad queries for new repos
    '"steps to reproduce" "pinch" "crash" label:bug language:Kotlin is:open',
    '"steps to reproduce" "double tap" "crash" label:bug language:Kotlin is:open',
    '"steps to reproduce" "drag" "reorder" "crash" label:bug language:Kotlin is:open',
    '"steps to reproduce" "swipe" "dismiss" "crash" label:bug language:Kotlin is:open',
    '"steps to reproduce" "zoom" "freeze" label:bug language:Kotlin',
    '"steps to reproduce" "zoom" "glitch" label:bug language:Kotlin',
    '"steps to reproduce" "gesture" "not working" label:bug language:Kotlin',
    '"steps to reproduce" "gesture" "broken" label:bug language:Kotlin',
    '"steps to reproduce" "swipe" "not working" label:bug language:Kotlin',
    '"steps to reproduce" "double tap" "not working" label:bug language:Kotlin',
    '"steps to reproduce" "pinch" "not working" label:bug language:Kotlin',
    '"steps to reproduce" "drag" "not working" label:bug language:Kotlin',

    # Pre-release focused queries
    '"steps to reproduce" "alpha" "pinch" label:bug language:Kotlin',
    '"steps to reproduce" "beta" "zoom" label:bug language:Kotlin',
    '"steps to reproduce" "alpha" "double tap" label:bug language:Kotlin',
    '"steps to reproduce" "beta" "swipe" label:bug language:Kotlin',
    '"steps to reproduce" "rc" "gesture" label:bug language:Kotlin',
]

# Deduplicate
SEARCH_QUERIES = list(dict.fromkeys(SEARCH_QUERIES))

# Allow more per repo for comprehensive coverage
MAX_BUGS_PER_REPO = 5

# Quality thresholds
MIN_STEPS = 2
MIN_BODY_LENGTH = 80
MAX_BODY_LENGTH = 12000
MIN_GESTURE_KEYWORDS = 1

# ── STRICT SKIP LIST ──
# Apps that need login, network content, manga libraries, RSS feeds, etc.
SKIP_APP_KEYWORDS = [
    # Authentication / Login required
    "chat", "messenger", "email", "mail",
    "login", "auth", "oauth", "sign in", "signup",
    # Cloud / Network dependent
    "cloud", "sync", "server", "telegram", "signal",
    "whatsapp", "slack", "discord", "nextcloud", "mastodon",
    "matrix", "banking", "payment", "wallet",
    # VPN / Network tools
    "vpn", "proxy", "wireguard",
    # Manga / Comic (needs library content)
    "manga", "comic", "tachiyomi", "mihon", "kotatsu",
    # School / University
    "untis", "school", "university", "artemis",
    # Social media
    "social", "twitter", "reddit", "lemmy", "fediverse",
    "pixelfed", "tusky", "megalodon",
    # Streaming (needs account/content)
    "spotify", "youtube", "twitch", "podcast",
    # Music streaming (needs content)
    "newpipe", "libretube", "piped",
    # E-book / Reader (needs content)
    "ebook", "epub", "reader",
    # Browser (needs network)
    "browser", "firefox", "chromium", "webview",
    # VR / AR
    "wolvic", "vr", "xr",
]

# Repos to skip entirely
SKIP_REPOS = [
    "ArcaneChat/android",
    "meshtastic/Meshtastic-Android",
    "mihonapp/mihon",
    "ls1intum/artemis-android",
    "AntennaPod/AntennaPod",       # needs RSS feeds
    "jocmp/capyreader",            # RSS reader needs feeds
    "libre-tube/LibreTube",        # needs YouTube content
    "TeamNewPipe/NewPipe",         # needs YouTube content
    "videolan/vlc-android",        # needs media files loaded
    "niccokunzmann/mundraub-android",  # needs network/map data
    "osmandapp/OsmAnd",            # huge APK, needs map downloads
    "K1rakishou/Kuroba-Experimental",  # imageboard browser, needs network
    "AdrienPoupa/VinylMusicPlayer",    # needs music files
    "AntonyJR/AppImageUpdater",        # not Android
    "Igalia/wolvic",                   # VR browser
    "niccokunzmann/mundraub-android",  # needs network
    "AntennaPod/AntennaPod",          # podcast, needs feeds
    "mozilla-mobile/firefox-echo-show", # browser
    "niccokunzmann/mundraub-android",  # map app, needs network
    "niccokunzmann/mundraub-android",  # duplicate
]

# ── EXISTING BUGS TO SKIP (already tested) ──
EXISTING_BUGS = {
    ("A-EDev/Flow", 27), ("A-EDev/Flow", 284),
    ("Anthonyy232/Paperize", 325), ("Anthonyy232/Paperize", 426),
    ("Crustack/NotallyX", 570),
    ("Fandroid745/Open-notes", 15),
    ("FossifyOrg/Calendar", 273), ("FossifyOrg/Calendar", 621),
    ("FossifyOrg/Camera", 23),
    ("FossifyOrg/File-Manager", 195),
    ("FossifyOrg/Gallery", 237), ("FossifyOrg/Gallery", 363),
    ("FossifyOrg/Gallery", 642), ("FossifyOrg/Gallery", 678),
    ("FossifyOrg/Gallery", 728), ("FossifyOrg/Gallery", 847),
    ("FossifyOrg/Gallery", 940),
    ("FossifyOrg/Launcher", 198), ("FossifyOrg/Launcher", 304),
    ("FossifyOrg/Messages", 359), ("FossifyOrg/Messages", 416),
    ("FossifyOrg/Messages", 641),
    ("FossifyOrg/Notes", 59),
    ("FossifyOrg/Paint", 125), ("FossifyOrg/Paint", 25),
    ("Jays2Kings/tachiyomiJ2K", 273),
    ("Kin69/EasyNotes", 356),
    ("LawnchairLauncher/lawnchair", 2910),
    ("LawnchairLauncher/lawnchair", 4125),
    ("LawnchairLauncher/lawnchair", 5540),
    ("MetrolistGroup/Metrolist", 3227),
    ("MetrolistGroup/Metrolist", 3391),
    ("MetrolistGroup/Metrolist", 3561),
    ("OuterTune/OuterTune", 1044),
    ("TeamNewPipe/NewPipe", 10750), ("TeamNewPipe/NewPipe", 8338),
    ("abdallahmehiz/mpvKt", 184),
    ("anilbeesetti/nextplayer", 1127), ("anilbeesetti/nextplayer", 1389),
    ("ankidroid/Anki-Android", 5512), ("ankidroid/Anki-Android", 5544),
    ("ankidroid/Anki-Android", 7138), ("ankidroid/Anki-Android", 7730),
    ("25huizengek1/ViTune", 710),
    ("breezy-weather/breezy-weather", 1639),
    ("breezy-weather/breezy-weather", 2159),
    ("cromaguy/Rhythm", 237), ("cromaguy/Rhythm", 281),
    ("dessalines/thumb-key", 371),
    ("espresso3389/methings", 34),
    ("fast4x/RiMusic", 1152),
    ("fcitx5-android/fcitx5-android", 841),
    ("gsantner/markor", 2746),
    ("jocmp/capyreader", 1149),
    ("libre-tube/LibreTube", 8245),
    ("marlboro-advance/mpvEx", 53),
    ("msasikanth/twine", 1566),
    ("netmackan/ATimeTracker", 124),
    ("streetcomplete/StreetComplete", 6068),
    ("syt0r/Kanji-Dojo", 291),
    ("yairm210/Unciv", 13517),
    ("you-apps/WallYou", 216),
}

MAX_APK_SIZE_MB = 150
DOWNLOAD_TIMEOUT = 300
REQUEST_DELAY = 1.2
MAX_RETRIES = 3
