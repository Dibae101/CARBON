import re
import time
import random
from hierarchy import *


def wait(duration=1):
    # Wait for the specified duration
    time.sleep(duration)


def restart(device, package_name):  
    device.app_stop(package_name) 
    time.sleep(2)
    device.app_start(package_name)
    time.sleep(2)

def scroll(device, index = 0, direction=None):
    if direction == 'up' or direction == 'top' or direction == None:
        device(scrollable=True)[index].fling.vert.toBeginning()
    elif direction == 'down' or direction == 'bottom':
        device(scrollable=True)[index].fling()
    elif direction == 'end':
        device(scrollable=True)[index].fling.toEnd()
    else:
        device.swipe_ext("down", scale=0.9)


def orientation(device, command):
    direction = command.get('to_direction', None)
    if direction == None:
        direction = command.get('direction', None)
    if direction == None:   
        direction = command.get('orientation', None)
        
    if direction  == 'portrait':
        device.set_orientation('natural')
    elif direction == 'landscape':
        device.set_orientation('left')
    elif direction in ['left', 'right', 'natural', 'upsidedown']:
        device.set_orientation(direction)
    else:
        options = ['left', 'right', 'natural', 'upsidedown']
        current_orientation = device.orientation
        random_option = current_orientation
        while random_option == current_orientation:
            random_option = random.choice(options)

        device.set_orientation(random_option)

def swipe(device, direction=None):
    if direction == 'up':
        device.swipe_ext("up", scale=0.9) 
    elif direction == 'down':
        device.swipe_ext("down", scale=0.9) 
    elif direction == 'right':
        device.swipe_ext("right", scale=0.9) 
    else:

        device.swipe_ext("left", scale=0.9) 

def multiple_selection(device, items, attribute_to_element_map):
    
    if len(items) ==  0:
        return ("No items to select.")
    
    element = attribute_to_element_map.get(items[0], None)
    execute(device, element, {'feature':items[0], 'action':'long_click'})
    if len(items) > 1:
        for item in items[1:]:
            element = attribute_to_element_map.get(item, None)
            execute(device, element, {'feature':item, 'action':'click'})
    
def change_status(device, element, command):

    current_status = command.get('current_status', '')
    target_status = command.get('target_status', '')
    if current_status != target_status:
        return execute(device, element, command) 
def back(device):
    device.press('back')

def click(device, coor):
    device.click(coor[0],coor[1])
    return True

def long_click(device, coor):
    device.long_click(coor[0],coor[1], 1.5)
    return True

def set_text(device, rep_attr, input_text, index):
    ui_object = locate_ui_object(device, rep_attr, 'set_text', index)
    if ui_object is None:
        return False
    elif input_text == None:
        return 'Error: You did not provide the input_text for set_text'
    else:
        '''
        ui_object.set_text('1')
        time.sleep(1)
        try:
            ui_object.set_text(input_text)
        except:
            try:
                set_text(device, '1', input_text, index)
            except:
                return "fail locate the target"
        '''
        try:
            ui_object.set_text(input_text)
        except:
            return "fail locate the target"
        return True

def get_center_if_coordinate(s):
    pattern = r'^\[(\d+),(\d+)\]\[(\d+),(\d+)\]$'
    match = re.match(pattern, s)
    if match:
        x1, y1, x2, y2 = map(int, match.groups())
        centerX = (x1 + x2) // 2
        centerY = (y1 + y2) // 2
        return [centerX, centerY]
    else:
        return None

def get_bounds_dict(bounds):
    pattern = r'^\[(\d+),(\d+)\]\[(\d+),(\d+)\]$'
    match = re.match(pattern, bounds)
    if not match:
        return None
    coordinates = [int(coord) for pair in bounds.split('][') for coord in pair.strip('[]').split(',')]

    if len(coordinates) != 4:
        raise ValueError(f"Expected 4 coordinates, but got {len(coordinates)}")

    bounds_dict = {'left': coordinates[0],
                'top': coordinates[1],
                'right': coordinates[2],
                'bottom': coordinates[3]}

    return bounds_dict


def locate_ui_object(device, rep_attr, type=None, index = 0):
    ui_object = device(text = rep_attr)[index]
    if ui_object:
        return ui_object
    
    ui_object = device(description = rep_attr)[index]
    if ui_object:
        return ui_object
    
    ui_object = device(resourceId = rep_attr)[index]
    if ui_object:
        return ui_object

    bounds_dict = get_bounds_dict(rep_attr)
    if bounds_dict is not None:
        for ui_object in device():
            if ui_object.info['bounds']==bounds_dict:
                if type == None:
                    return ui_object
                if type == 'set_text' and 'EditText' in ui_object.info['className']:
                    return ui_object


# ─── UIAutomator Viewer-Enabled Actions ──────────────────────────────────────
# These actions are enabled by UIAutomator Viewer's visual context: the AI can
# see annotated screenshots with bounding boxes and suggest coordinate-based
# interactions or system-level actions not possible with text-only hierarchy.

def home(device):
    """Press HOME button to return to device launcher.
    Enabled by UIAutomator Viewer: AI can see when app needs to be backgrounded."""
    device.press('home')
    time.sleep(0.5)

def open_notifications(device):
    """Pull down the notification shade from the top of the screen.
    Enabled by UIAutomator Viewer: AI can see notification content in screenshots."""
    device.open_notification()
    time.sleep(1)

def tap_screen(device, x, y):
    """Tap specific screen coordinates identified via UIAutomator Viewer.
    The AI references numbered bounding boxes in the annotated screenshot
    to determine precise coordinates for elements not in the text hierarchy."""
    if x is not None and y is not None:
        device.click(int(x), int(y))
        return True
    return 'Error: tap_screen requires x and y coordinates'

def swipe_region(device, start_x, start_y, end_x, end_y, duration=0.5):
    """Swipe between specific coordinates identified via UIAutomator Viewer.
    Used for precise gestures on elements visible in the annotated screenshot."""
    if all(v is not None for v in [start_x, start_y, end_x, end_y]):
        device.swipe(int(start_x), int(start_y), int(end_x), int(end_y), duration=duration)
        return True
    return 'Error: swipe_region requires start_x, start_y, end_x, end_y coordinates'


def picker_scroll(device, x=None, y=None, bounds=None,
                  direction='up', steps=1, width=None, height=None):
    """Scroll an Android NumberPicker (or spinner dial) by exactly `steps` ticks.

    Android NumberPicker widgets (used in DatePickerDialog, TimePickerDialog,
    and custom pickers like Memento Calendar's birthday dialog) consume a
    fling gesture differently from ordinary swipes:

      * A short swipe of about one cell height advances the picker by 1 value
      * The swipe must be slow enough for the animation to "catch" the gesture
      * Each tick must wait for the snap-into-place animation (~200 ms)
      * `set_text` on the inner EditText can jump to a value but bypasses the
        transient invalid-state window that some bugs require (e.g. setting
        day=31 while month=March, then scrolling month to February to hold
        day=31 in an invalid state)

    For those bugs, the scroll-gesture path is the ONLY way to reproduce the
    crash — `set_text` short-circuits the invalid-state window because the
    picker validates on setValue().

    Parameters:
      x, y      : center coordinate of the picker (from the annotated
                  screenshot). If `bounds` is given these are ignored.
      bounds    : [left, top, right, bottom] of the picker widget
                  (from the UIAutomator hierarchy).
      direction : 'up' moves the picker's value up (next); 'down' moves down
                  (previous). Visually: 'up' drags the cell from bottom to top.
      steps     : how many ticks to scroll. 1 = advance by one value.
      width     : picker width in pixels. Inferred from bounds if omitted.
      height    : picker height in pixels. Inferred from bounds if omitted.

    Example usage (JSON command):
      {"action": "picker_scroll", "bounds": [335,825,511,1320],
       "direction": "up", "steps": 2}          # advances picker by 2 values
    """
    import time as _time

    # Resolve center from bounds if provided
    if bounds is not None and len(bounds) == 4:
        left, top, right, bot = map(int, bounds)
        cx = (left + right) // 2
        cy = (top + bot) // 2
        h = bot - top
    elif x is not None and y is not None:
        cx, cy = int(x), int(y)
        h = int(height) if height else 300
    else:
        return ('Error: picker_scroll requires either bounds=[l,t,r,b] '
                'or (x, y)')

    # One tick ≈ one cell height. A NumberPicker typically shows 3 cells
    # in its visible area, so each cell is h // 3 tall. Use 60% of cell
    # height for the swipe magnitude — enough to trigger a tick, short
    # enough to avoid a multi-cell fling.
    cell = max(60, h // 3)
    swipe_dist = int(cell * 0.6)

    # Total ticks to scroll. direction 'up' advances the value (drag content
    # from bottom up → center shows the next value); 'down' reverses.
    steps = max(1, int(steps))

    for i in range(steps):
        if direction == 'up':
            sx, sy = cx, cy + swipe_dist // 2
            ex, ey = cx, cy - swipe_dist // 2
        elif direction == 'down':
            sx, sy = cx, cy - swipe_dist // 2
            ex, ey = cx, cy + swipe_dist // 2
        else:
            return (f"Error: picker_scroll direction must be 'up' or 'down', "
                    f"got '{direction}'")

        # Slow enough (0.35 s) for the picker to register as a drag, not a
        # fling that overshoots. Fast enough to complete before the next tick.
        device.swipe(sx, sy, ex, ey, duration=0.35)
        _time.sleep(0.25)  # let the snap-into-place animation finish

    return True

def media_gesture(device, gesture_type):
    """Perform a region-specific media player gesture.

    Video players map vertical swipes to different controls depending on
    which HALF of the screen is touched:
      - RIGHT half → Volume (up = swipe up, down = swipe down)
      - LEFT  half → Brightness (up = swipe up, down = swipe down)
    Horizontal swipes on the centre of the screen seek forward/backward.

    IMPORTANT: Most video players only register these gestures when the
    controls overlay is HIDDEN (fullscreen mode).  This function therefore
    taps the centre of the video first to dismiss any visible controls,
    waits for the overlay to fade, and then performs the gesture.

    Args:
        gesture_type: One of 'volume_up', 'volume_down',
                      'brightness_up', 'brightness_down',
                      'seek_forward', 'seek_backward'
    """
    try:
        w, h = device.window_size()
    except Exception:
        w, h = 1080, 2340  # Pixel 4 portrait fallback

    # ── Step 1: Dismiss the controls overlay ──────────────────────────────
    # Tap the centre of the screen to toggle controls off.  If they were
    # already hidden this tap will briefly show them; the second tap (or
    # the wait) ensures they fade before the gesture.
    cx, cy = w // 2, h // 2
    device.click(cx, cy)
    time.sleep(2.0)   # wait for controls fade-out animation

    # Check if controls are still showing by looking for common video UI
    try:
        xml = device.dump_hierarchy()
        controls_visible = ('video_toggle_play_pause' in xml or
                            'video_seekbar' in xml or
                            'bottom_actions' in xml or
                            'medium_viewer_toolbar' in xml)
        if controls_visible:
            # Tap again to dismiss
            device.click(cx, cy)
            time.sleep(2.0)
    except Exception:
        pass  # If dump fails, proceed anyway

    # ── Step 2: Perform the gesture ───────────────────────────────────────
    # Vertical region: 30 %–70 % of screen height (avoids nav bars)
    sy_start = int(h * 0.65)
    sy_end   = int(h * 0.35)

    right_x = int(w * 0.75)  # 75 % across = right half
    left_x  = int(w * 0.25)  # 25 % across = left half
    center_y = int(h * 0.5)

    gesture_map = {
        'volume_up':       (right_x, sy_start, right_x, sy_end),
        'volume_down':     (right_x, sy_end,   right_x, sy_start),
        'brightness_up':   (left_x,  sy_start, left_x,  sy_end),
        'brightness_down': (left_x,  sy_end,   left_x,  sy_start),
        'seek_forward':    (int(w * 0.3), center_y, int(w * 0.7), center_y),
        'seek_backward':   (int(w * 0.7), center_y, int(w * 0.3), center_y),
    }

    if gesture_type not in gesture_map:
        return (f"Error: unknown gesture_type '{gesture_type}'. "
                f"Valid values: {', '.join(gesture_map.keys())}")

    sx, sy, ex, ey = gesture_map[gesture_type]
    # Smooth swipe (0.5 s) — needs enough duration for the app's gesture detector
    device.swipe(sx, sy, ex, ey, duration=0.5)
    time.sleep(2.0)  # wait for gesture overlay to appear and be captured
    return True

def quick_tap(device, feature, delay_ms=100):
    """Tap a UI element with minimal delay — used for timing-sensitive bugs.
    Skips the normal inter-step sleep so the tap fires within ~delay_ms of
    the previous action completing. The LLM should use this when the bug
    requires tapping immediately after a UI transition (e.g. tapping 'Show
    Answer' before AnkiDroid's answer-forwarding timer expires).

    Args:
        feature: text / content-desc / resource-id / bounds of the target widget
        delay_ms: how long to wait before tapping (default 100 ms)
    """
    time.sleep(delay_ms / 1000.0)
    coor = get_center_if_coordinate(feature)
    if coor:
        device.click(coor[0], coor[1])
        return True
    # Try text / description / resourceId lookup
    ui_object = locate_ui_object(device, feature)
    if ui_object:
        ui_object.click()
        return True
    return f"quick_tap: could not locate '{feature}'"


def double_tap_screen(device, x, y):
    """Double-tap at specific screen coordinates.
    Many apps use double-tap for special actions:
      - Video players: double-tap left = rewind, double-tap right = fast-forward
      - Gallery apps: double-tap to zoom in/out
      - Map apps: double-tap to zoom in
    """
    if x is not None and y is not None:
        x, y = int(x), int(y)
        device.click(x, y)
        time.sleep(0.1)
        device.click(x, y)
        time.sleep(0.5)
        return True
    return 'Error: double_tap_screen requires x and y coordinates'

def edge_swipe(device, edge, direction):
    """Swipe from a specific screen edge inward.
    Handles gestures that only trigger when starting from the very edge:
      - 'left' edge  + 'right' direction → Android back gesture / drawer open
      - 'right' edge + 'left' direction  → forward navigation / drawer
      - 'top' edge   + 'down' direction  → pull notification shade / pull-to-refresh
      - 'bottom' edge + 'up' direction   → show navigation bar / bottom sheet
    """
    try:
        w, h = device.window_size()
    except Exception:
        w, h = 1080, 2340

    # 5 % margin from edge to start, swipe 40 % into the screen
    edge_map = {
        ('left', 'right'):   (int(w * 0.02), int(h * 0.5), int(w * 0.40), int(h * 0.5)),
        ('right', 'left'):   (int(w * 0.98), int(h * 0.5), int(w * 0.60), int(h * 0.5)),
        ('top', 'down'):     (int(w * 0.5), int(h * 0.02), int(w * 0.5), int(h * 0.40)),
        ('bottom', 'up'):    (int(w * 0.5), int(h * 0.98), int(w * 0.5), int(h * 0.60)),
    }

    key = (edge, direction)
    if key not in edge_map:
        return (f"Error: invalid edge_swipe combo edge='{edge}', direction='{direction}'. "
                f"Valid combos: left+right, right+left, top+down, bottom+up")

    sx, sy, ex, ey = edge_map[key]
    device.swipe(sx, sy, ex, ey, duration=0.3)
    time.sleep(0.5)
    return True

def _adb_shell(device, cmd):
    """Run an adb shell command on the connected device using its serial."""
    import subprocess
    serial = getattr(device, 'serial', None) or getattr(device, '_serial', None)
    if not serial:
        # fallback: try to get from device info
        try:
            serial = device.info.get('serial', 'emulator-5554')
        except Exception:
            serial = 'emulator-5554'
    try:
        result = subprocess.run(
            ['adb', '-s', serial, 'shell', cmd],
            capture_output=True, text=True, timeout=10
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"[adb_shell] Error: {e}")
        return ''


def pinch(device, pinch_type, cx=None, cy=None):
    """Real two-finger pinch zoom using adb shell input motionevent.
    Sends simultaneous multi-touch events through the Android input pipeline.
      - 'in'  = zoom out (fingers move toward center)
      - 'out' = zoom in  (fingers move apart from center)

    Uses `adb shell input swipe` with two pointer IDs via the motionevent
    approach — both fingers move simultaneously, which the app's gesture
    detector correctly recognises as a pinch.
    """
    try:
        w, h = device.window_size()
    except Exception:
        w, h = 1080, 2340

    cx = int(cx) if cx is not None else w // 2
    cy = int(cy) if cy is not None else h // 2

    extent = int(min(w, h) * 0.28)  # distance from center to each finger

    if pinch_type == 'in':   # zoom out — fingers start apart, move together
        f1_sx, f1_sy = cx - extent, cy
        f1_ex, f1_ey = cx - extent // 5, cy
        f2_sx, f2_sy = cx + extent, cy
        f2_ex, f2_ey = cx + extent // 5, cy
    elif pinch_type == 'out':  # zoom in — fingers start close, move apart
        f1_sx, f1_sy = cx - extent // 5, cy
        f1_ex, f1_ey = cx - extent, cy
        f2_sx, f2_sy = cx + extent // 5, cy
        f2_ex, f2_ey = cx + extent, cy
    else:
        return f"Error: pinch_type must be 'in' or 'out', got '{pinch_type}'"

    # Use adb shell input to send a two-pointer swipe simultaneously.
    # Android's `input` tool supports multi-touch via the format:
    #   input swipe x1 y1 x2 y2 [duration]  (single finger)
    # For two simultaneous fingers we use the touchscreen motionevent approach
    # via a Python-generated sequence of sendevent commands.
    _pinch_via_adb(device, f1_sx, f1_sy, f1_ex, f1_ey,
                   f2_sx, f2_sy, f2_ex, f2_ey, duration_ms=400)
    time.sleep(0.5)
    return True


def _pinch_via_adb(device, f1_sx, f1_sy, f1_ex, f1_ey,
                   f2_sx, f2_sy, f2_ex, f2_ey, duration_ms=400):
    """Send a real two-finger gesture using UiObject pinch on the screen area.

    Uses uiautomator2's UiObject.pinch_in/pinch_out which calls the
    UiAutomator2 server's native pinchIn/pinchOut — these send real
    simultaneous multi-touch MotionEvents that apps recognise as pinch.

    Falls back to jsonrpc.pinchIn on the root element if UiObject fails.
    """
    steps = max(10, int(duration_ms / 40))

    # Always use a strong, consistent percent for both directions
    percent = 80

    # Determine pinch direction from finger movement
    center_x = (f1_sx + f2_sx) // 2
    f1_moving_toward = abs(f1_ex - center_x) < abs(f1_sx - center_x)
    is_pinch_in = f1_moving_toward

    try:
        # Use jsonrpc.pinchIn/pinchOut directly — this calls UiAutomator2's
        # native performMultiPointerGesture which sends real simultaneous
        # multi-touch MotionEvents. We target the screen center area.
        import uiautomator2 as u2

        # Build a selector for the main content area (index 0 = root)
        # pinchIn/pinchOut work on any element with valid bounds
        selector = u2.Selector(index=0)

        if is_pinch_in:
            device.jsonrpc.pinchIn(selector, percent, steps)
            print(f"[pinch] pinch_in {percent}% {steps} steps")
        else:
            device.jsonrpc.pinchOut(selector, percent, steps)
            print(f"[pinch] pinch_out {percent}% {steps} steps")

    except Exception as e:
        print(f"[pinch] jsonrpc pinch failed: {e}")
        # Last resort: try UiObject on first clickable element
        try:
            el = device(clickable=True)
            if el.exists:
                if is_pinch_in:
                    el.pinch_in(percent=percent, steps=steps)
                else:
                    el.pinch_out(percent=percent, steps=steps)
        except Exception as e2:
            print(f"[pinch] UiObject pinch also failed: {e2}")


def two_finger_swipe(device, direction, cx=None, cy=None):
    """Two-finger swipe in a direction. Used for:
      - Scrolling in apps that distinguish 1-finger vs 2-finger scroll
      - Pull-to-refresh with two fingers
      - Two-finger pan in map/canvas apps
    Directions: 'up', 'down', 'left', 'right'
    """
    try:
        w, h = device.window_size()
    except Exception:
        w, h = 1080, 2340

    cx = int(cx) if cx is not None else w // 2
    cy = int(cy) if cy is not None else h // 2
    gap = int(w * 0.08)   # finger separation
    distance = int(min(w, h) * 0.35)

    dir_map = {
        'up':    (0, -distance),
        'down':  (0,  distance),
        'left':  (-distance, 0),
        'right': (distance, 0),
    }
    if direction not in dir_map:
        return f"Error: direction must be up/down/left/right, got '{direction}'"

    dx, dy = dir_map[direction]

    # Two fingers side by side (perpendicular to swipe direction)
    if direction in ('up', 'down'):
        f1_sx, f1_sy = cx - gap, cy
        f2_sx, f2_sy = cx + gap, cy
    else:
        f1_sx, f1_sy = cx, cy - gap
        f2_sx, f2_sy = cx, cy + gap

    _pinch_via_adb(device,
                   f1_sx, f1_sy, f1_sx + dx, f1_sy + dy,
                   f2_sx, f2_sy, f2_sx + dx, f2_sy + dy,
                   duration_ms=350)
    time.sleep(0.5)
    return True


def two_finger_tap(device, cx=None, cy=None):
    """Two-finger tap at a location. Used for:
      - Zoom-to-fit / reset zoom in map/canvas apps
      - Custom two-finger tap shortcuts in various apps
    """
    try:
        w, h = device.window_size()
    except Exception:
        w, h = 1080, 2340

    cx = int(cx) if cx is not None else w // 2
    cy = int(cy) if cy is not None else h // 2
    gap = int(w * 0.08)

    # Use UiObject gesture on the element at the tap location
    try:
        el = device.click(cx - gap, cy)
        time.sleep(0.05)
        device.click(cx + gap, cy)
    except Exception as e:
        print(f"[two_finger_tap] Failed: {e}")

    time.sleep(0.5)
    return True


def three_finger_swipe(device, direction):
    """Three-finger swipe. Used for:
      - Screenshot gesture on some launchers
      - App drawer open/close on some launchers
      - Custom three-finger shortcuts in apps
    Directions: 'up', 'down', 'left', 'right'
    """
    try:
        w, h = device.window_size()
    except Exception:
        w, h = 1080, 2340

    cx, cy = w // 2, h // 2
    gap = int(w * 0.1)
    distance = int(min(w, h) * 0.35)

    dir_map = {
        'up':    (0, -distance),
        'down':  (0,  distance),
        'left':  (-distance, 0),
        'right': (distance, 0),
    }
    if direction not in dir_map:
        return f"Error: direction must be up/down/left/right, got '{direction}'"

    dx, dy = dir_map[direction]

    if direction in ('up', 'down'):
        fingers = [(cx - gap, cy), (cx, cy), (cx + gap, cy)]
    else:
        fingers = [(cx, cy - gap), (cx, cy), (cx, cy + gap)]

    # Send three sequential swipes — best available without true multi-touch
    for fx, fy in fingers:
        device.swipe(fx, fy, fx + dx, fy + dy, duration=0.3)
        time.sleep(0.05)

    time.sleep(0.5)
    return True


def drag_and_drop(device, start_x, start_y, end_x, end_y, hold_ms=800):
    """Drag and drop from one coordinate to another.
    Holds at the start position to trigger long-press selection, then
    drags to the destination. Used for:
      - Reordering list items (use hold_ms=200 when starting from a drag handle)
      - Moving widgets on home screen
      - Drag-to-delete / drag-to-folder operations

    For reorder drag handles, use hold_ms=200 to avoid triggering multi-select.
    """
    if any(v is None for v in [start_x, start_y, end_x, end_y]):
        return 'Error: drag_and_drop requires start_x, start_y, end_x, end_y'

    try:
        device.drag(int(start_x), int(start_y), int(end_x), int(end_y),
                    duration=hold_ms / 2000.0)
        time.sleep(0.5)
        return True
    except Exception as e:
        return f"Error in drag_and_drop: {e}"


def rotate_gesture(device, cx=None, cy=None, degrees=90, clockwise=True):
    """Two-finger rotation gesture. Used for:
      - Rotating images in gallery/photo editors
      - Rotating map orientation
      - Custom rotation controls in drawing apps
    Uses UiObject.gesture() which sends real multi-touch events.
    """
    import math

    try:
        w, h = device.window_size()
    except Exception:
        w, h = 1080, 2340

    cx = int(cx) if cx is not None else w // 2
    cy = int(cy) if cy is not None else h // 2
    radius = int(min(w, h) * 0.2)
    steps = 12
    angle_step = math.radians(degrees / steps) * (1 if clockwise else -1)
    start_angle = 0.0

    def finger_pos(angle, offset=0):
        a = angle + offset
        return (int(cx + radius * math.cos(a)), int(cy + radius * math.sin(a)))

    # Build gesture path as list of (x1,y1,x2,y2) tuples for each step
    # UiObject.gesture takes two lists of points (one per finger)
    path1 = [finger_pos(start_angle + angle_step * i, 0) for i in range(steps + 1)]
    path2 = [finger_pos(start_angle + angle_step * i, math.pi) for i in range(steps + 1)]

    try:
        # Use UiObject.gesture on the screen element
        el = device(className='android.view.View', clickable=True)
        if not el.exists:
            el = device(index=0)
        el.gesture(path1, path2, steps=steps)
    except Exception as e:
        print(f"[rotate_gesture] Failed: {e}")

    time.sleep(0.5)
    return True


def get_element(attribute_to_element_map, command):
    if isinstance(command['feature'], dict):
        return None, f"command['feature'] is not the right format, please provide the feature only "

    element_list = attribute_to_element_map.get(command['feature'], [])
    if element_list != []:
        index = command.get('index', 0)
        if index >= len(element_list):
            return None, f"the idex, {index}, is out of range, {len(element_list)}"
        else:
            element = element_list[index]
    else:
        element = None
    return element, None

def execute(device, element, command):
    
    rep_attr = command['feature']
    action = command['action']
    index = command.get('index', 0)
        
    if action == 'set_text':
        
        return set_text(device, rep_attr, command.get('input_text', None), index)
        
    if action in ['click', 'long_click']:
        if element is None:
            if 'click' in action and index ==0:
                coor = get_center_if_coordinate(rep_attr)
                if coor:
                    globals()[action](device, coor)
                    return True
            ui_object = locate_ui_object(device, rep_attr, index)
            if ui_object:
                getattr(ui_object, action)()
                return True
        else:
            coor = get_center_if_coordinate(element.attrib.get('bounds', ''))
            if coor:
                globals()[action](device, coor)
                return True
    return False

def handle_command(command, device, attribute_to_element_map, package_name):
    command_map = {
        'complete': lambda: None,
        'restart': lambda: restart(device, package_name),
        'scroll': lambda: scroll(device, command.get('index', 0), command.get('to_direction', command.get('target_direction', None))),
        'orientation': lambda: orientation(device, command),
        'rotate': lambda: orientation(device, command),
        'back': lambda: back(device),
        'swipe': lambda: swipe(device, command.get('to_direction', None)),
        'multiple_selection': lambda: multiple_selection(device, command['features'], attribute_to_element_map),
        'Navigate up': lambda: back(device),
        'wait':lambda: wait(command.get('duration', None)),
        # UIAutomator Viewer-enabled actions (require visual context)
        'home': lambda: home(device),
        'open_notifications': lambda: open_notifications(device),
        'tap_screen': lambda: tap_screen(device, command.get('x'), command.get('y')),
        'swipe_region': lambda: swipe_region(device, command.get('start_x'), command.get('start_y'), command.get('end_x'), command.get('end_y'), command.get('duration', 0.5)),
        'picker_scroll': lambda: picker_scroll(
            device,
            x=command.get('x'),
            y=command.get('y'),
            bounds=command.get('bounds'),
            direction=command.get('to_direction', command.get('direction', 'up')),
            steps=command.get('steps', 1),
            width=command.get('width'),
            height=command.get('height'),
        ),
        'media_gesture': lambda: media_gesture(device, command.get('gesture_type')),
        'double_tap_screen': lambda: double_tap_screen(device, command.get('x'), command.get('y')),
        'edge_swipe': lambda: edge_swipe(device, command.get('edge'), command.get('to_direction')),
        'pinch': lambda: pinch(device, command.get('pinch_type', 'out'), command.get('x'), command.get('y')),
        'two_finger_swipe': lambda: two_finger_swipe(device, command.get('to_direction', 'up'), command.get('x'), command.get('y')),
        'two_finger_tap': lambda: two_finger_tap(device, command.get('x'), command.get('y')),
        'three_finger_swipe': lambda: three_finger_swipe(device, command.get('to_direction', 'up')),
        'drag_and_drop': lambda: drag_and_drop(device, command.get('start_x'), command.get('start_y'), command.get('end_x'), command.get('end_y'), command.get('hold_ms', 800)),
        'rotate_gesture': lambda: rotate_gesture(device, command.get('x'), command.get('y'), command.get('degrees', 90), command.get('clockwise', True)),
        'quick_tap': lambda: quick_tap(device, command.get('feature', ''), command.get('delay_ms', 100)),
    }
    print(command)
    if command['action'] in command_map:
        command_map[command['action']]()
        return True
    elif command.get('feature', None) == None:
        return f"The program cannot regconized this actions {command}"
    elif command.get('current_status', '') and command.get('target_status', ''):
        element, warning = get_element(attribute_to_element_map, command)
        if warning is None:
            return change_status(device, element, command)
        else:
            return warning
    else:
        element, warning = get_element(attribute_to_element_map, command)
        if warning is None:
            return execute(device, element, command)
        else:
            return warning

   




