"""Quick keyword-based gesture scan on raw_bugs.jsonl.

This is a LOWER BOUND — keyword matching misses paraphrased gestures
("hold your finger on" = long_press) and has false positives ("swipe"
in a UI description that isn't a reproduction step). But it gives us
a fast directional answer before spending on Gemini.

Gesture categories (matching CARBON's 8):
  - double_tap: double tap, double click, double-tap, tap twice
  - long_press: long press, long-press, long click, press and hold, hold down, tap and hold
  - drag_and_drop: drag, drop, drag and drop, drag-and-drop, reorder by dragging
  - pinch_zoom: pinch, zoom in, zoom out, pinch to zoom, two finger zoom
  - swipe: swipe, fling, slide (directional)
  - scroll: scroll, pull to refresh, pull-to-refresh
  - rotation/orientation: rotate, orientation, landscape, portrait, screen rotation
  - quick_tap: quick tap, rapid tap, tap quickly, spam tap, tap repeatedly

We do NOT count plain "tap" or "click" — those are basic actions every tool supports.
"""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

RAW = Path(__file__).parent / "raw_bugs.jsonl"

# Patterns — each is (category, compiled_regex)
# We search title + body combined, case-insensitive
GESTURE_PATTERNS = [
    ("double_tap", re.compile(r"\b(double[- ]?tap|double[- ]?click|tap(ped|ping)?\s+twice)\b", re.I)),
    ("long_press", re.compile(r"\b(long[- ]?(press|click|tap)|press\s+and\s+hold|hold\s+(down|your\s+finger)|tap\s+and\s+hold)\b", re.I)),
    ("drag_and_drop", re.compile(r"\b(drag\s*(and|&)?\s*drop|drag(ged|ging)?\s+(it|the|a|an|to|from|into)|reorder\s*(by)?\s*drag|drop(ped|ping)?\s+(it|the|onto|into))\b", re.I)),
    ("pinch_zoom", re.compile(r"\b(pinch|zoom\s*(in|out)|pinch[- ]?to[- ]?zoom|two[- ]?finger\s*zoom)\b", re.I)),
    ("swipe", re.compile(r"\b(swipe|fling|swip(ed|ing))\b", re.I)),
    ("scroll", re.compile(r"\b(scroll(ed|ing)?|pull[- ]?to[- ]?refresh)\b", re.I)),
    ("orientation", re.compile(r"\b(rotat(e|ion|ing)|landscape|portrait|screen\s*rotation|orientation\s*(change|lock))\b", re.I)),
    ("quick_tap", re.compile(r"\b(quick(ly)?\s*tap|rapid(ly)?\s*tap|tap\s*quick(ly)?|spam\s*tap|tap(ped|ping)?\s*repeat(edly)?|tap(ped|ping)?\s*fast)\b", re.I)),
]

bugs = [json.loads(l) for l in RAW.open()]
print(f"Total bugs scanned: {len(bugs)}\n")

# Classify each bug
gesture_bugs = []  # bugs with at least one gesture match
category_counts = Counter()
per_bug_categories = defaultdict(list)  # url -> [categories]

for b in bugs:
    text = (b.get("title", "") + "\n" + b.get("body", "")).lower()
    matched_cats = set()
    for cat, pat in GESTURE_PATTERNS:
        if pat.search(text):
            matched_cats.add(cat)
    if matched_cats:
        gesture_bugs.append(b)
        for c in matched_cats:
            category_counts[c] += 1
        per_bug_categories[b["url"]] = sorted(matched_cats)

pct = len(gesture_bugs) / len(bugs) * 100
print(f"Bugs mentioning at least one non-tap gesture: {len(gesture_bugs)}/{len(bugs)} ({pct:.1f}%)\n")

print("Per-gesture-category breakdown:")
for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
    print(f"  {cat:15s}: {count:4d} ({count/len(bugs)*100:.1f}%)")

print(f"\nBugs with multiple gesture types: {sum(1 for v in per_bug_categories.values() if len(v) > 1)}")

# Show 10 sample gesture bugs with their matched categories
print("\n--- Sample gesture bugs (first 15) ---")
for b in gesture_bugs[:15]:
    cats = per_bug_categories[b["url"]]
    title = b["title"][:80]
    print(f"  [{','.join(cats):20s}] {b['owner']}/{b['repo']}#{b['issue_number']}: {title}")

# Show 5 non-gesture bugs for contrast
print("\n--- Sample NON-gesture bugs (first 5) ---")
non_gesture = [b for b in bugs if b["url"] not in per_bug_categories]
for b in non_gesture[:5]:
    title = b["title"][:80]
    print(f"  {b['owner']}/{b['repo']}#{b['issue_number']}: {title}")
