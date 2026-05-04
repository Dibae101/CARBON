"""
UIAutomator Viewer Module for ReBL
===================================
Programmatic replication of Android SDK's UIAutomator Viewer tool.

UIAutomator Viewer (uiautomatorviewer) is a GUI tool in the Android SDK that:
  1. Captures a device screenshot
  2. Dumps the UI hierarchy XML via `uiautomator dump`
  3. Overlays element bounding boxes on the screenshot
  4. Displays element properties in a detail panel

This module replicates that entire workflow programmatically:
  - capture_screenshot()        → Device Screenshot (uiautomator2)
  - extract_elements_from_xml() → UI hierarchy parsing + property extraction
  - annotate_screenshot()       → Bounding box overlay with color-coded types
  - build_element_legend()      → Text property panel (element map)
  - capture_viewer_state()      → Full viewer capture (main entry point)

The annotated screenshot + element map are sent to Gemini Vision (multimodal),
giving the AI the exact same view a human tester gets in UIAutomator Viewer.

Why this matters (paper contribution):
  Traditional ReBL sends TEXT-ONLY hierarchy to the LLM. The AI never sees
  the actual screen, causing failures when:
    - Elements are not in the accessibility tree (video overlays, custom views)
    - Visual context matters (colors, status indicators, rendering bugs)
    - System UI interactions are needed (notifications, permission dialogs)
    - Precise coordinate-based taps are required (canvas elements)

  UIAutomator Viewer Enhanced ReBL sends ANNOTATED SCREENSHOTS with
  color-coded bounding boxes + a numbered element map. The AI can now:
    - SEE every element's visual position and appearance
    - Cross-reference numbered bounding boxes with element properties
    - Identify elements missing from the text hierarchy
    - Suggest coordinate-based taps on unlisted elements
    - Understand visual state (colors, overlays, system UI)
"""

import os
import io
import re
import time
import base64
import xml.etree.ElementTree as ET

from collections import Counter

try:
    from PIL import Image, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("[UIAutomator Viewer] WARNING: Pillow not installed. Run: pip install Pillow")


# ─── Configuration 

SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'screenshots')

# Maximum image dimension for Gemini API (keeps detail while controlling tokens)
MAX_IMAGE_SIZE = 1280

# ─── Color Name Mapping
# Human-readable color names so Gemini can reason about colors naturally.

COLOR_NAMES = {
    'black':        (0, 0, 0),
    'white':        (255, 255, 255),
    'red':          (255, 0, 0),
    'green':        (0, 128, 0),
    'blue':         (0, 0, 255),
    'yellow':       (255, 255, 0),
    'cyan':         (0, 255, 255),
    'magenta':      (255, 0, 255),
    'orange':       (255, 165, 0),
    'purple':       (128, 0, 128),
    'pink':         (255, 192, 203),
    'brown':        (139, 69, 19),
    'gray':         (128, 128, 128),
    'light-gray':   (192, 192, 192),
    'dark-gray':    (64, 64, 64),
    'navy':         (0, 0, 128),
    'teal':         (0, 128, 128),
    'olive':        (128, 128, 0),
    'dark-red':     (139, 0, 0),
    'dark-green':   (0, 100, 0),
}

# Color scheme for bounding box overlays (matches UIAutomator Viewer conventions)
# Format: (R, G, B, Alpha)
ELEMENT_COLORS = {
    'clickable':  {'fill': (0, 200, 0, 50),    'border': (0, 200, 0, 255)},      # Green
    'editable':   {'fill': (0, 100, 255, 50),   'border': (0, 100, 255, 255)},    # Blue
    'scrollable': {'fill': (255, 165, 0, 50),   'border': (255, 165, 0, 255)},    # Orange
    'checkable':  {'fill': (200, 0, 200, 50),   'border': (200, 0, 200, 255)},    # Purple
    'focused':    {'fill': (255, 255, 0, 50),   'border': (255, 255, 0, 255)},    # Yellow
    'text_only':  {'fill': (180, 180, 180, 30), 'border': (180, 180, 180, 160)},  # Gray
}

# Maximum elements to include in the text legend (to control prompt size)
MAX_LEGEND_ELEMENTS = 60


# ─── Utility Functions ───

def ensure_screenshot_dir():
    """Create screenshot directory if it doesn't exist."""
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def parse_bounds_string(bounds_str):
    """
    Parse UIAutomator bounds string '[x1,y1][x2,y2]' into (x1, y1, x2, y2).
    This is the same format used in UIAutomator Viewer's detail panel.
    """
    match = re.match(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]', bounds_str)
    if match:
        return tuple(int(v) for v in match.groups())
    return None


def resize_for_api(image, max_size=MAX_IMAGE_SIZE):
    """Resize image for Gemini API while maintaining aspect ratio."""
    if image is None:
        return None
    w, h = image.size
    if max(w, h) > max_size:
        scale = max_size / max(w, h)
        image = image.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
    return image


def image_to_base64(image):
    """Convert PIL Image to base64-encoded PNG string."""
    if image is None:
        return None
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode('utf-8')


# ─── Element Classification (mirrors UIAutomator Viewer property panel) 

def classify_element(attribs):
    """
    Classify a UI element by type for color-coded annotation.
    Priority order matches what UIAutomator Viewer highlights.
    """
    if attribs.get('focused', 'false') == 'true':
        return 'focused'
    if 'EditText' in attribs.get('class', ''):
        return 'editable'
    if attribs.get('scrollable', 'false') == 'true':
        return 'scrollable'
    if attribs.get('checkable', 'false') == 'true':
        return 'checkable'
    if (attribs.get('clickable', 'false') == 'true' or
            attribs.get('long-clickable', 'false') == 'true'):
        return 'clickable'
    # Include text-bearing elements (useful for visual context)
    if attribs.get('text', '') or attribs.get('content-desc', ''):
        return 'text_only'
    return None  # Skip invisible/empty elements


# ─── Hierarchy XML Parsing ───────────────────────────────────────────────────

def extract_elements_from_xml(hierarchy_xml):
    """
    Parse UI hierarchy XML and extract all visible elements with their bounds.
    This replicates UIAutomator Viewer's element tree panel.

    The hierarchy XML is obtained via `uiautomator dump` (or uiautomator2's
    dump_hierarchy()), which is the same XML that UIAutomator Viewer loads.

    Args:
        hierarchy_xml: XML string or ElementTree object

    Returns:
        list of dicts, each containing element properties + classification
    """
    elements = []

    try:
        if isinstance(hierarchy_xml, str):
            root = ET.fromstring(hierarchy_xml)
        elif hasattr(hierarchy_xml, 'getroot'):
            root = hierarchy_xml.getroot()
        else:
            root = hierarchy_xml
    except ET.ParseError as e:
        print(f"[UIAutomator Viewer] XML parse error: {e}")
        return elements

    for node in root.iter('node'):
        attribs = node.attrib
        bounds = parse_bounds_string(attribs.get('bounds', ''))
        if bounds is None:
            continue

        x1, y1, x2, y2 = bounds
        # Skip zero-area or off-screen elements
        if x2 <= x1 or y2 <= y1:
            continue

        elem_type = classify_element(attribs)
        if elem_type is None:
            continue

        element = {
            'bounds': bounds,
            'type': elem_type,
            'text': attribs.get('text', ''),
            'content_desc': attribs.get('content-desc', ''),
            'resource_id': attribs.get('resource-id', ''),
            'class_name': attribs.get('class', ''),
            'package': attribs.get('package', ''),
            'clickable': attribs.get('clickable', 'false') == 'true',
            'long_clickable': attribs.get('long-clickable', 'false') == 'true',
            'scrollable': attribs.get('scrollable', 'false') == 'true',
            'checkable': attribs.get('checkable', 'false') == 'true',
            'checked': attribs.get('checked', 'false') == 'true',
            'enabled': attribs.get('enabled', 'true') == 'true',
            'focused': attribs.get('focused', 'false') == 'true',
        }

        # Build short label for annotation overlay
        label = element['text'] or element['content_desc'] or ''
        if not label and element['resource_id']:
            rid = element['resource_id']
            label = rid[rid.rfind('/') + 1:] if '/' in rid else rid
        if len(label) > 25:
            label = label[:22] + '...'
        element['label'] = label

        elements.append(element)

    return elements


# ─── Screenshot Annotation (core UIAutomator Viewer visual functionality) ────

def _load_font():
    """Load a font for annotation text, with fallbacks."""
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",           # macOS
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",  # Linux
        "/usr/share/fonts/TTF/DejaVuSans.ttf",           # Arch Linux
    ]
    for path in font_paths:
        try:
            return ImageFont.truetype(path, 13)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


def annotate_screenshot(screenshot, elements):
    """
    Draw color-coded bounding boxes on the screenshot for each UI element.
    This is the core UIAutomator Viewer visualization:

    - Each element gets a colored border matching its type
    - Interactive elements (clickable, editable) get semi-transparent fill
    - Each element is numbered with an index badge in the corner
    - The index numbers correspond to the element legend text

    Color coding:
        GREEN  = clickable elements      BLUE   = text input fields
        ORANGE = scrollable containers   PURPLE = checkable widgets
        YELLOW = focused element         GRAY   = static text

    Args:
        screenshot: PIL.Image of the device screen (full resolution)
        elements:   list of element dicts from extract_elements_from_xml()

    Returns:
        PIL.Image with UIAutomator Viewer-style annotations overlaid
    """
    if not PIL_AVAILABLE or screenshot is None:
        return screenshot

    # Work in RGBA for transparency compositing
    if screenshot.mode != 'RGBA':
        base = screenshot.convert('RGBA')
    else:
        base = screenshot.copy()

    # Create transparent overlay for semi-transparent fills
    overlay = Image.new('RGBA', base.size, (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)

    # Main draw context for borders and labels
    draw_main = ImageDraw.Draw(base)

    font = _load_font()

    for idx, elem in enumerate(elements):
        x1, y1, x2, y2 = elem['bounds']
        colors = ELEMENT_COLORS.get(elem['type'], ELEMENT_COLORS['text_only'])

        # Semi-transparent fill (only for interactive elements)
        if elem['type'] != 'text_only':
            draw_overlay.rectangle([x1, y1, x2, y2], fill=colors['fill'])

        # Solid border
        border_width = 2 if elem['type'] != 'text_only' else 1
        draw_main.rectangle([x1, y1, x2, y2],
                            outline=colors['border'], width=border_width)

        # Index badge in top-left corner
        badge_text = str(idx)
        badge_w = len(badge_text) * 9 + 6
        badge_h = 16
        # Position badge above element if possible, inside otherwise
        bx = x1
        by = y1 - badge_h if y1 > badge_h else y1
        draw_main.rectangle([bx, by, bx + badge_w, by + badge_h],
                            fill=colors['border'])
        draw_main.text((bx + 3, by + 1), badge_text,
                       fill=(255, 255, 255, 255), font=font)

    # Composite overlay onto base
    annotated = Image.alpha_composite(base, overlay)

    # Convert to RGB for saving/API
    return annotated.convert('RGB')


# ─── Element Legend (text companion to annotated screenshot) ─────────────────

def build_element_legend(elements):
    """
    Build a text legend mapping element indices to their properties.
    This accompanies the annotated screenshot, allowing the AI to
    cross-reference numbered bounding boxes with element details.

    Equivalent to UIAutomator Viewer's "Node Detail" panel.

    Returns:
        str: formatted legend text
    """
    if not elements:
        return ""

    lines = []
    lines.append("[UIAutomator Viewer - Element Map]")
    lines.append(f"Total visible elements: {len(elements)}")
    lines.append("Box colors: GREEN=clickable, BLUE=text-input, "
                 "ORANGE=scrollable, PURPLE=checkable, YELLOW=focused, GRAY=text")
    lines.append("---")

    # Prioritize interactive elements, then text-only
    interactive = [e for e in elements if e['type'] != 'text_only']
    text_only = [e for e in elements if e['type'] == 'text_only']
    ordered = interactive + text_only

    count = 0
    for elem in ordered:
        if count >= MAX_LEGEND_ELEMENTS:
            remaining = len(elements) - count
            lines.append(f"... and {remaining} more elements (see screenshot)")
            break

        idx = elements.index(elem)
        parts = [f"#{idx}"]
        parts.append(f"[{elem['type'].upper()}]")

        # Short class name
        cls = elem['class_name']
        if '.' in cls:
            cls = cls[cls.rfind('.') + 1:]
        parts.append(cls)

        if elem['text']:
            display_text = elem['text'][:40]
            parts.append(f'text="{display_text}"')
        if elem['content_desc']:
            display_desc = elem['content_desc'][:40]
            parts.append(f'desc="{display_desc}"')
        if elem['resource_id']:
            rid = elem['resource_id']
            short_rid = rid[rid.rfind('/') + 1:] if '/' in rid else rid
            parts.append(f'id={short_rid}')

        x1, y1, x2, y2 = elem['bounds']
        parts.append(f'bounds=[{x1},{y1}][{x2},{y2}]')

        if elem['checked']:
            parts.append('checked')
        if not elem['enabled']:
            parts.append('DISABLED')

        lines.append(' '.join(parts))
        count += 1

    return '\n'.join(lines)


# ─── Screenshot Capture ─────────────────────────────────────────────────────

def capture_screenshot(device):
    """
    Capture raw device screenshot via uiautomator2.
    Equivalent to clicking 'Device Screenshot' in UIAutomator Viewer.

    Returns PIL.Image at original device resolution, or None on failure.
    """
    if not PIL_AVAILABLE:
        return None

    try:
        return device.screenshot()
    except Exception as e:
        print(f"[UIAutomator Viewer] Screenshot capture failed: {e}")
        return None


# ─── Color Sampling (Visual Rendering Bug Support) ──────────────────────────
#
# UI hierarchy XML has NO color data — only text, bounds, and interaction state.
# Screenshots are sent to Gemini, but the model can struggle to precisely compare
# colors between steps or detect subtle shifts (e.g. status bar white→black).
#
# This module extracts pixel colors from key screen regions and encodes them as
# TEXT data appended to each step's prompt.  This gives Gemini concrete RGB values
# and human-readable color names to compare across steps — enabling reliable
# detection of visual rendering bugs (wrong colors, theme glitches, etc.).

def _color_distance(c1, c2):
    """Euclidean distance between two RGB tuples."""
    return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5


def rgb_to_color_name(rgb):
    """Map an RGB tuple to the closest human-readable color name."""
    best_name = 'unknown'
    best_dist = float('inf')
    for name, ref_rgb in COLOR_NAMES.items():
        d = _color_distance(rgb, ref_rgb)
        if d < best_dist:
            best_dist = d
            best_name = name
    return best_name


def rgb_to_hex(rgb):
    """Convert (R, G, B) to '#RRGGBB'."""
    return '#{:02x}{:02x}{:02x}'.format(*rgb[:3])


def _quantize_color(rgb, bucket_size=16):
    """Quantize RGB to reduce noise — groups similar shades together."""
    return tuple((c // bucket_size) * bucket_size for c in rgb[:3])


def sample_region_colors(image, region, num_samples=200, top_n=3):
    """
    Extract dominant colors from a rectangular region of a screenshot.

    Samples pixels uniformly across the region, quantizes them to reduce noise
    from anti-aliasing / gradients, and returns the top-N most frequent colors
    with their percentage, hex code, and human-readable name.

    Args:
        image:       PIL.Image (RGB or RGBA)
        region:      (x1, y1, x2, y2) pixel coordinates of the region
        num_samples: number of pixels to sample (more = slower but more accurate)
        top_n:       number of dominant colors to return

    Returns:
        list of dicts: [{'rgb': (R,G,B), 'hex': '#rrggbb', 'name': 'white',
                         'percentage': 85.5}, ...]
    """
    if not PIL_AVAILABLE or image is None:
        return []

    x1, y1, x2, y2 = region
    w, h = image.size
    # Clamp to image bounds
    x1, y1 = max(0, x1), max(0, y1)
    x2, y2 = min(w, x2), min(h, y2)
    if x2 <= x1 or y2 <= y1:
        return []

    # Crop and sample
    crop = image.crop((x1, y1, x2, y2))
    if crop.mode == 'RGBA':
        crop = crop.convert('RGB')

    cw, ch = crop.size
    pixels = []
    import random as _rng
    for _ in range(num_samples):
        px = _rng.randint(0, cw - 1)
        py = _rng.randint(0, ch - 1)
        pixels.append(crop.getpixel((px, py))[:3])

    # Quantize and count
    quantized = [_quantize_color(p) for p in pixels]
    counter = Counter(quantized)
    total = len(quantized)

    results = []
    for color, count in counter.most_common(top_n):
        pct = round(100.0 * count / total, 1)
        results.append({
            'rgb': color,
            'hex': rgb_to_hex(color),
            'name': rgb_to_color_name(color),
            'percentage': pct,
        })
    return results


def build_color_report(image, hierarchy_xml=None):
    """
    Build a structured color analysis of key screen regions.

    Divides the screen into semantically meaningful zones and extracts
    the dominant color(s) from each.  The report is appended as text
    to the Gemini prompt so the AI has concrete, comparable color data.

    Regions sampled:
      - Status bar       (top ~3 % of screen)
      - Toolbar / header (3 %–10 %)
      - Content area     (10 %–85 % — main body)
      - Navigation bar   (bottom ~10 %)

    If a UI hierarchy XML is provided, also detects and color-samples:
      - Notification media artwork (album art ImageViews)
      - Any large ImageView elements (icons, thumbnails, cover images)

    This is critical for bugs where the *rendered image* is wrong (e.g.,
    wrong album art in notification) — the hierarchy shows "ImageView exists"
    but cannot reveal WHAT image is displayed.  Pixel color sampling bridges
    that gap, giving Gemini a color fingerprint to compare across steps.

    Returns:
        str: formatted color report text, or '' if unavailable
    """
    if not PIL_AVAILABLE or image is None:
        return ''

    w, h = image.size

    regions = {
        'Status Bar':      (0, 0,          w, int(h * 0.03)),
        'Toolbar/Header':  (0, int(h*0.03), w, int(h * 0.10)),
        'Content Area':    (0, int(h*0.10), w, int(h * 0.85)),
        'Navigation Bar':  (0, int(h*0.90), w, h),
    }

    lines = ['[Color Analysis — pixel sampling from screenshot]']
    for region_name, bounds in regions.items():
        colors = sample_region_colors(image, bounds, num_samples=300, top_n=2)
        if not colors:
            continue
        color_strs = []
        for c in colors:
            color_strs.append(f"{c['name']} ({c['hex']}, {c['percentage']}%)")
        lines.append(f"  {region_name}: {', '.join(color_strs)}")

    # ── Dynamic element color sampling from hierarchy ─────────────────────
    # Detect ImageViews and other visual elements from the XML, then sample
    # their actual pixel colors from the screenshot.  This is how ReBL can
    # "see" what image is rendered in an ImageView (album art, thumbnail, etc.)
    if hierarchy_xml:
        element_colors = _sample_elements_from_hierarchy(image, hierarchy_xml)
        if element_colors:
            lines.append('')
            lines.append('[Element Color Sampling — pixel colors of image/visual elements]')
            for entry in element_colors:
                lines.append(f"  {entry}")

    if len(lines) == 1:
        return ''  # no data extracted

    return '\n'.join(lines)


def _sample_elements_from_hierarchy(image, hierarchy_xml):
    """
    Find notable visual elements (ImageViews, notification artwork, etc.)
    in the hierarchy XML, then sample their pixel colors from the screenshot.

    Targets:
      1. Notification media artwork — large ImageViews inside notification rows
         (album art for music players, video thumbnails, etc.)
      2. Any ImageView with resource-id hinting at artwork/thumbnail/icon
      3. Large ImageViews (> 100×100 px) without text — these are purely visual

    Returns:
        list of str: one line per sampled element, e.g.:
          "Notification artwork [120,540][480,900]: orange (#e08030, 72%), brown (#604020, 18%)"
    """
    if not PIL_AVAILABLE or image is None or not hierarchy_xml:
        return []

    try:
        if isinstance(hierarchy_xml, str):
            root = ET.fromstring(hierarchy_xml)
        elif hasattr(hierarchy_xml, 'getroot'):
            root = hierarchy_xml.getroot()
        else:
            root = hierarchy_xml
    except ET.ParseError:
        return []

    results = []
    sampled_bounds = set()  # avoid duplicates

    # Keywords that suggest an element is an image/artwork worth sampling
    artwork_keywords = [
        'artwork', 'album', 'cover', 'thumbnail', 'poster', 'icon_big',
        'big_picture', 'media_image', 'right_icon', 'large_icon',
        'big_icon', 'image', 'photo', 'picture', 'avatar', 'banner',
    ]

    # Walk the hierarchy looking for visual elements to sample
    in_notification = False
    notification_depth = 0

    for node in root.iter('node'):
        pkg = node.attrib.get('package', '')
        rid = node.attrib.get('resource-id', '')
        cls = node.attrib.get('class', '')
        text = node.attrib.get('text', '')
        desc = node.attrib.get('content-desc', '')
        bounds_str = node.attrib.get('bounds', '')

        bounds = parse_bounds_string(bounds_str)
        if bounds is None:
            continue
        x1, y1, x2, y2 = bounds
        bw, bh = x2 - x1, y2 - y1

        # Track if we're inside a notification row
        if 'expandableNotificationRow' in rid or 'notification_panel' in rid:
            in_notification = True

        # Skip tiny elements (< 50×50 px)
        if bw < 50 or bh < 50:
            continue

        # Skip if we already sampled this exact region
        bounds_key = (x1, y1, x2, y2)
        if bounds_key in sampled_bounds:
            continue

        should_sample = False
        label = ''

        # Rule 1: ImageView/Image inside a notification — likely album art/icon
        if ('ImageView' in cls or 'Image' in cls) and (in_notification or pkg == 'com.android.systemui'):
            # Must be reasonably large to be artwork (not a tiny status icon)
            if bw >= 80 and bh >= 80:
                should_sample = True
                label = f"Notification image [{x1},{y1}][{x2},{y2}]"
                # More specific label if resource-id gives hints
                rid_lower = rid.lower()
                if any(kw in rid_lower for kw in ['right_icon', 'big_icon', 'large_icon', 'artwork', 'album', 'cover']):
                    label = f"Notification artwork [{x1},{y1}][{x2},{y2}]"

        # Rule 2: Any ImageView with artwork-related resource-id
        if not should_sample and ('ImageView' in cls or 'Image' in cls):
            rid_lower = rid.lower()
            if any(kw in rid_lower for kw in artwork_keywords):
                if bw >= 80 and bh >= 80:
                    should_sample = True
                    label = f"Image ({rid.split('/')[-1] if '/' in rid else rid}) [{x1},{y1}][{x2},{y2}]"

        # Rule 3: Large ImageView without text (purely visual element)
        if not should_sample and ('ImageView' in cls) and not text and not desc:
            if bw >= 150 and bh >= 150:
                should_sample = True
                short_rid = rid.split('/')[-1] if '/' in rid else 'unnamed'
                label = f"Large image ({short_rid}) [{x1},{y1}][{x2},{y2}]"

        if should_sample:
            sampled_bounds.add(bounds_key)
            colors = sample_region_colors(image, (x1, y1, x2, y2), num_samples=200, top_n=3)
            if colors:
                color_strs = [f"{c['name']} ({c['hex']}, {c['percentage']}%)" for c in colors]
                results.append(f"{label}: {', '.join(color_strs)}")

    return results


def build_color_diff(prev_report, curr_report):
    """
    Compare two color reports and produce an explicit diff highlighting
    any region whose dominant color changed between steps.

    This eliminates the need for Gemini to search through conversation
    history — the diff is included directly in the current prompt.

    Returns:
        str: e.g. '[Color Change Detected]\n  Status Bar: white -> black'
              or '' if nothing changed
    """
    if not prev_report or not curr_report:
        return ''

    def _parse_report(report):
        """Extract {region_name: dominant_color_name} from report text."""
        result = {}
        for line in report.split('\n'):
            line = line.strip()
            if ':' not in line or line.startswith('['):
                continue
            # e.g. "Status Bar: white (#f0f0f0, 88.0%), black (#000000, 2.3%)"
            region, colors_str = line.split(':', 1)
            region = region.strip()
            # First color listed is the dominant one
            first_color = colors_str.strip().split('(')[0].strip()
            # Also grab the hex for precision
            hex_match = colors_str.strip()
            hex_val = ''
            if '(' in hex_match and '#' in hex_match:
                hex_val = hex_match.split('(')[1].split(',')[0].strip()
            result[region] = (first_color, hex_val)
        return result

    prev = _parse_report(prev_report)
    curr = _parse_report(curr_report)

    changes = []
    for region in curr:
        if region in prev:
            prev_name, prev_hex = prev[region]
            curr_name, curr_hex = curr[region]
            if prev_name != curr_name:
                changes.append(
                    f"  {region}: {prev_name} ({prev_hex}) -> {curr_name} ({curr_hex})"
                )

    if not changes:
        return ''

    return '[Color Change Detected]\n' + '\n'.join(changes)


# ─── Main Entry Point ───────────────────────────────────────────────────────

def capture_viewer_state(device, step_number=None):
    """
    Main entry point — captures the full UIAutomator Viewer state.

    This replicates the complete UIAutomator Viewer workflow:
      1. Capture device screenshot (full resolution)
      2. Dump UI hierarchy XML via uiautomator
      3. Parse XML into structured element list
      4. Annotate screenshot with color-coded bounding boxes
      5. Build text element legend (Node Detail panel)
      6. Resize for API transmission

    Args:
        device:      uiautomator2 device object
        step_number: optional step number for file naming/logging

    Returns:
        dict with:
            'screenshot':    resized raw PIL.Image
            'annotated':     resized annotated PIL.Image (for Gemini Vision)
            'elements':      list of element property dicts
            'legend':        text element map (for prompt text)
            'element_count': total elements found
            'timestamp':     capture timestamp
    """
    # Step 1: Capture raw screenshot at full device resolution
    raw_screenshot = capture_screenshot(device)

    # Step 2: Dump and parse UI hierarchy XML
    elements = []
    hierarchy_xml = None
    try:
        hierarchy_xml = device.dump_hierarchy()
        elements = extract_elements_from_xml(hierarchy_xml)
    except Exception as e:
        print(f"[UIAutomator Viewer] Hierarchy dump failed: {e}")

    # Step 3: Annotate screenshot with bounding boxes (at full resolution)
    annotated = annotate_screenshot(raw_screenshot, elements)

    # Step 4: Resize both images for API efficiency
    raw_resized = resize_for_api(raw_screenshot)
    annotated_resized = resize_for_api(annotated)

    # Step 5: Save to disk for debugging/paper figures
    if step_number is not None:
        ensure_screenshot_dir()
        try:
            if raw_resized:
                raw_resized.save(
                    os.path.join(SCREENSHOT_DIR, f'step_{step_number:03d}_raw.png'))
            if annotated_resized:
                annotated_resized.save(
                    os.path.join(SCREENSHOT_DIR, f'step_{step_number:03d}_annotated.png'))
        except Exception as e:
            print(f"[UIAutomator Viewer] Failed to save screenshots: {e}")

    # Step 6: Build text element legend
    legend = build_element_legend(elements)

    # Step 7: Extract color data from raw screenshot (before annotation overlay)
    # Pass hierarchy XML so we can also color-sample specific elements
    # (notification artwork, large images, etc.) by their bounds
    color_report = build_color_report(raw_screenshot, hierarchy_xml=hierarchy_xml)

    # Logging
    clickable_count = sum(1 for e in elements if e['clickable'])
    editable_count = sum(1 for e in elements if e['type'] == 'editable')
    scrollable_count = sum(1 for e in elements if e['scrollable'])
    print(f"[UIAutomator Viewer] Step {step_number}: {len(elements)} elements "
          f"({clickable_count} clickable, {editable_count} editable, "
          f"{scrollable_count} scrollable)")

    return {
        'screenshot': raw_resized,
        'annotated': annotated_resized,
        'elements': elements,
        'legend': legend,
        'color_report': color_report,
        'element_count': len(elements),
        'timestamp': time.time(),
    }


# ─── Utility ─────────────────────────────────────────────────────────────────

def is_vision_available():
    """Check if UIAutomator Viewer visual pipeline is available (requires Pillow)."""
    return PIL_AVAILABLE


def clean_screenshots():
    """Remove all saved screenshots from previous runs."""
    if os.path.exists(SCREENSHOT_DIR):
        for f in os.listdir(SCREENSHOT_DIR):
            if f.endswith('.png'):
                try:
                    os.remove(os.path.join(SCREENSHOT_DIR, f))
                except OSError:
                    pass
