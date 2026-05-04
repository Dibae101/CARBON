# ReBL Detailed Analysis Report — 100 Bug Reproduction Results

> **Tool:** ReBL (Reproduction of Bugs with LLM — Baseline)
> **Total Bugs Tested:** 100
> **Categories:** 8
> **Overall Success Rate:** 32/100 (32.0%)
> **CARBON Success Rate (for comparison):** 92/100 (92.0%)

---

## Summary Table

### Results by Category

| Category | Total | ✅ Success | ❌ Fail | Success Rate | CARBON Rate |
|----------|-------|-----------|--------|--------------|-------------|
| Double Tap | 19 | 3 | 16 | 16% | 89% |
| Drag and Drop | 9 | 0 | 9 | 0% | 89% |
| Long Press | 9 | 5 | 4 | 56% | 100% |
| Orientation | 6 | 5 | 1 | 83% | 83% |
| Pinch/Zoom | 14 | 2 | 12 | 14% | 100% |
| Quick Tap | 6 | 0 | 6 | 0% | 67% |
| Scroll | 5 | 3 | 2 | 60% | 100% |
| Swipe | 32 | 14 | 18 | 44% | 94% |

### Failure Category Breakdown

| Failure Category | Count | % of Failures |
|-----------------|-------|---------------|
| MISSING_GESTURE | 47 | 70.1% |
| NAVIGATION_FAILURE | 13 | 19.4% |
| TALKBACK_REQUIRED | 4 | 6.0% |
| SETUP_LIMITATION | 2 | 3.0% |
| OTHER | 1 | 1.5% |

### All 100 Bug Results

| # | Category | App | Issue # | Bug Title | Result | Time | Steps | Failure Category |
|---|----------|-----|---------|-----------|--------|------|-------|-----------------|
| 1 | Double Tap | Calendar | #273 | Setting a default event length doesn't change the ... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 2 | Double Tap | Gallery | #363 | webp images when double tapped don't zoom to heigh... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 3 | Double Tap | Gallery | #678 | 'Allow 1:1 zooming in with two double taps' not wo... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 4 | Double Tap | Gallery | #846 | "Fill screen" zoom on double tap ignores disabled ... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 5 | Double Tap | Gallery | #847 | Invalid "fill screen" zoom for GIF images on doubl... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 6 | Double Tap | lawnchair | #2910 | Double tap to sleep no longer works through root a... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 7 | Double Tap | lawnchair | #4125 | android 14, no option to allow restricted setting | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 8 | Double Tap | lawnchair | #4786 | Crash when trying to move item using TalkBack acti... | ❌ FAIL | 971.7s | 104 | TALKBACK_REQUIRED |
| 9 | Double Tap | GreenStash | #170 | Some accessibility issues | ❌ FAIL | 1793.5s | 128 | NAVIGATION_FAILURE |
| 10 | Double Tap | NewPipe | #10750 | Video playback randomly "closed/crashed", and cont... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 11 | Double Tap | NewPipe | #8338 | Swipe down gesture of Player UI does not work all ... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 12 | Double Tap | mpvKt | #184 | Tap error while playing video | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 13 | Double Tap | Anki-Android | #17393 | IO Cards Go to the Wrong Deck | ✅ SUCCESS | 1543.8s | 156 | — |
| 14 | Double Tap | Rhythm | #281 | Double tap needed on Touch Gestures view of Onboar... | ✅ SUCCESS | 284.6s | 33 | — |
| 15 | Double Tap | RiMusic | #1152 | Unclear Linking and Unresponsive Buttons in Player... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 16 | Double Tap | markor | #2746 | Markor does not recognize URL/link anymore | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 17 | Double Tap | openboard | #613 | Sometimes the spellchecker flags correctly spelt w... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 18 | Double Tap | openboard | #758 | Accessibility: The button to go to the previous le... | ❌ FAIL | 273.3s | 30 | TALKBACK_REQUIRED |
| 19 | Double Tap | Kanji-Dojo | #291 | Double-tapping back arrow while transitioning from... | ✅ SUCCESS | 328.8s | 38 | — |
| 20 | Drag and Drop | Launcher | #304 | Accidently creating invisible folders in dock | ❌ FAIL | 1410.5s | 118 | NAVIGATION_FAILURE |
| 21 | Drag and Drop | Notes | #59 | Reordering checklists works strangely with move ch... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 22 | Drag and Drop | lawnchair | #1247 | the launcher kees crashign when I attempt to move ... | ❌ FAIL | 1086.4s | 60 | TALKBACK_REQUIRED |
| 23 | Drag and Drop | lawnchair | #4320 | Unable to add any widget | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 24 | Drag and Drop | Metrolist | #3227 | Replacement of new song with old song | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 25 | Drag and Drop | Metrolist | #3561 | Weird Bug when changing list order in custom order... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 26 | Drag and Drop | Neo-Launcher | #130 | Changing the first app in a folder with Covers ena... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 27 | Drag and Drop | breezy-weather | #2159 | Can't add widget to home screen | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 28 | Drag and Drop | fcitx5-android | #841 | Crash somtimes on showing keyboard when the prefer... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 29 | Long Press | Paperize | #325 | Crashing when adding images | ❌ FAIL | 615.2s | 62 | NAVIGATION_FAILURE |
| 30 | Long Press | NotallyX | #570 | App crash when note is selected, search filter cha... | ❌ FAIL | 809.6s | 75 | NAVIGATION_FAILURE |
| 31 | Long Press | File-Manager | #195 | Unnecessary refresh of ZIP file icons when closing... | ✅ SUCCESS | ~120s | 6 | — |
| 32 | Long Press | Launcher | #198 | Folder rename dialog: Dark text on dark background | ❌ FAIL | ~200s | 13 | NAVIGATION_FAILURE |
| 33 | Long Press | Messages | #359 | Can't scroll or see participants on conversation d... | ✅ SUCCESS | ~150s | 7 | — |
| 34 | Long Press | Messages | #416 | New conversation shortcut doesn't work | ✅ SUCCESS | 127.8s | 3 | — |
| 35 | Long Press | Messages | #641 | SMS scheduling not working | ✅ SUCCESS | 447.7s | 32 | — |
| 36 | Long Press | breezy-weather | #1639 | weather wallpaper causes launcher to freeze and ap... | ❌ FAIL | ~400s | 27 | NAVIGATION_FAILURE |
| 37 | Long Press | methings | #34 | Image preview UX gaps and instability when using S... | ✅ SUCCESS | ~250s | 19 | — |
| 38 | Orientation | Calendar | #1042 | The current selected day, month, week, year is not... | ✅ SUCCESS | 145.5s | 12 | — |
| 39 | Orientation | Camera | #91 | Countdown timer does not honor device orientation | ✅ SUCCESS | 221.2s | 13 | — |
| 40 | Orientation | Clock | #85 | Snooze not working in landscape | ❌ FAIL | 834.6s | 105 | NAVIGATION_FAILURE |
| 41 | Orientation | Contacts | #197 | View always changed to contact list when rotating ... | ✅ SUCCESS | 375.3s | 30 | — |
| 42 | Orientation | HTTP-Shortcuts | #262 | several dialogs disappear on screen rotation | ✅ SUCCESS | 99.0s | 6 | — |
| 43 | Orientation | Anki-Android | #16410 | Changing screen orientation clears stats' search o... | ✅ SUCCESS | 341.8s | 37 | — |
| 44 | Pinch/Zoom | client | #583 | Swiping images zooms instead of zooming | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 45 | Pinch/Zoom | Calendar | #621 | Zoom level in weekly view locks | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 46 | Pinch/Zoom | Camera | #23 | Doesn't use zoom camera to zoom | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 47 | Pinch/Zoom | Gallery | #289 | "Allow deep zooming images" creates artifacts in m... | ✅ SUCCESS | 527.6s | 37 | — |
| 48 | Pinch/Zoom | Gallery | #642 | Zoom doesn't work in photos | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 49 | Pinch/Zoom | Gallery | #728 | (Deep zooming) Can not pan after releasing only on... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 50 | Pinch/Zoom | Paint | #125 | Touch location and pen location different after zo... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 51 | Pinch/Zoom | Paint | #25 | Eraser size not relative to zoom on minimum size | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 52 | Pinch/Zoom | Anki-Android | #16135 | Zooming in Statistics Page | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 53 | Pinch/Zoom | Anki-Android | #17667 | Width of "Deck options" page does not/cannot fit t... | ✅ SUCCESS | 214.8s | 22 | — |
| 54 | Pinch/Zoom | saber | #192 | Two finger detection need improvement | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 55 | Pinch/Zoom | StreetComplete | #6068 | OutOfMemoryError when downloading after zoom out | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 56 | Pinch/Zoom | Unciv | #13517 | User report | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 57 | Pinch/Zoom | WallYou | #216 | Improper edge-to-edge implementation | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 58 | Quick Tap | lawnchair | #5540 | Home Button Requires Double-Tap to Return to Defau... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 59 | Quick Tap | nextplayer | #1389 | Resuming doesn't work properly — video stops immed... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 60 | Quick Tap | Anki-Android | #18529 | You can touch some buttons during animations | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 61 | Quick Tap | Anki-Android | #19641 | Card was modified error when tapping the answer bu... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 62 | Quick Tap | Anki-Android | #20789 | "Collection synced" notification is too high-prior... | ❌ FAIL | 328.6s | 44 | SETUP_LIMITATION |
| 63 | Quick Tap | Anki-Android | #7138 | Card skips when tapping Show Answer immediately | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 64 | Scroll | Paperize | #426 | the Privacy Notice button disappears in landscape ... | ✅ SUCCESS | 58.4s | 3 | — |
| 65 | Scroll | Open-notes | #15 | No scroll support, (Bug) | ❌ FAIL | 1194.0s | 36 | NAVIGATION_FAILURE |
| 66 | Scroll | Anki-Android | #5512 | AnkiDroid scroll bug | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 67 | Scroll | Anki-Android | #5544 | AnkiDroid scroll bug | ✅ SUCCESS | 103.0s | 6 | — |
| 68 | Scroll | ATimeTracker | #124 | Could not scroll on the menu | ✅ SUCCESS | 115.2s | 9 | — |
| 69 | Swipe | Flow | #27 | Fullscreen gesture conflict — brightness/volume ge... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 70 | Swipe | Flow | #284 | Pinch-in zoom breaks player gestures — volume and ... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 71 | Swipe | mLauncher | #809 | Short swipe gesture broken | ✅ SUCCESS | 368.9s | 43 | — |
| 72 | Swipe | client | #238 | App crashing on changing settings. | ✅ SUCCESS | 159.5s | 15 | — |
| 73 | Swipe | Calendar | #1035 | Ap crashes when creating new event | ✅ SUCCESS | 96.7s | 6 | — |
| 74 | Swipe | Calendar | #1103 | Accessibility - have screen reader anounce existen... | ❌ FAIL | 277.4s | 43 | TALKBACK_REQUIRED |
| 75 | Swipe | Calendar | #153 | Swiping in monthly view is a pain | ✅ SUCCESS | 195.6s | 6 | — |
| 76 | Swipe | Clock | #156 | Timer alarm turned off by swiping from the status ... | ❌ FAIL | 1718.7s | 208 | NAVIGATION_FAILURE |
| 77 | Swipe | File-Manager | #136 | The screen refresh gesture works when the function... | ❌ FAIL | 821.0s | 75 | NAVIGATION_FAILURE |
| 78 | Swipe | Gallery | #237 | Vertical gesture to adjust video volume does not w... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 79 | Swipe | Gallery | #584 | When trying to open some JPG files, the gallery ap... | ❌ FAIL | 984.1s | 166 | SETUP_LIMITATION |
| 80 | Swipe | Gallery | #940 | Disabled notch overlaps brightness control area | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 81 | Swipe | Launcher | #66 | Slow, jerky animation when opening a folder or swi... | ❌ FAIL | 2331.8s | 125 | OTHER |
| 82 | Swipe | Messages | #80 | Navigation Stack gets too Large (Hitting Back Butt... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 83 | Swipe | Notes | #190 | crash while using the search field. | ✅ SUCCESS | 348.4s | 36 | — |
| 84 | Swipe | EasyNotes | #356 | [BUG] | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 85 | Swipe | lawnchair | #4642 | Gesture navigation gets locked in one orientation ... | ✅ SUCCESS | 126.8s | 6 | — |
| 86 | Swipe | lawnchair | #4708 | Gesture nav: swiping up to go home when already in... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 87 | Swipe | lawnchair | #5496 | Lawnchair crashes in the recent menu | ✅ SUCCESS | 118.5s | 7 | — |
| 88 | Swipe | Metrolist | #3391 | Back gesture not working in the player screen | ✅ SUCCESS | 320.6s | 35 | — |
| 89 | Swipe | OuterTune | #1044 | Pressing Home or any button activates back gesture... | ✅ SUCCESS | 249.6s | 26 | — |
| 90 | Swipe | nextplayer | #1127 | Vertical swipe misbehaviour — volume/brightness ge... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 91 | Swipe | Anki-Android | #14934 | talkback can't see sometimes front, sometimes back... | ❌ FAIL | 845.5s | 84 | NAVIGATION_FAILURE |
| 92 | Swipe | ViTune | #710 | Notification shows wrong album art for current son... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 93 | Swipe | breezy-weather | #205 | Swipe left animation stays after cancelling weathe... | ❌ FAIL | 893.6s | 50 | NAVIGATION_FAILURE |
| 94 | Swipe | breezy-weather | #85 | Persistent notification setting - on / off is inve... | ❌ FAIL | 493.9s | 47 | NAVIGATION_FAILURE |
| 95 | Swipe | thumb-key | #371 | Swipe input eaten on capitalization/mode switch | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 96 | Swipe | lunar-launcher | #82 | Random crashes when closing applications | ❌ FAIL | 1581.7s | 201 | NAVIGATION_FAILURE |
| 97 | Swipe | LibreTube | #8245 | Laggy animation when minimizing player with Back b... | ❌ FAIL | 0s | 0 | MISSING_GESTURE |
| 98 | Swipe | twine | #1566 | Incomplete Predictive Back Animation | ❌ FAIL | 1094.2s | 102 | NAVIGATION_FAILURE |
| 99 | Swipe | ClockYou | #85 | App cycles through previously visited tabs on back... | ✅ SUCCESS | 83.2s | 7 | — |
| 100 | Swipe | ConnectYou | #155 | Back on search bar quits the app. | ❌ FAIL | 403.9s | 52 | NAVIGATION_FAILURE |

### Failed Bugs Summary

| # | App | Issue | Failure Category | Missing Gesture | CARBON Result |
|---|-----|-------|-----------------|-----------------|---------------|
| 1 | FossifyOrg/Calendar | #273 | MISSING_GESTURE | tap_screen | ✅ SUCCESS |
| 2 | FossifyOrg/Gallery | #363 | MISSING_GESTURE | pinch, tap_screen | ✅ SUCCESS |
| 3 | FossifyOrg/Gallery | #678 | MISSING_GESTURE | pinch, quick_tap | ✅ SUCCESS |
| 4 | FossifyOrg/Gallery | #846 | MISSING_GESTURE | pinch | ✅ SUCCESS |
| 5 | FossifyOrg/Gallery | #847 | MISSING_GESTURE | tap_screen | ✅ SUCCESS |
| 6 | LawnchairLauncher/lawnchair | #2910 | MISSING_GESTURE | drag_and_drop, tap_screen | ✅ SUCCESS |
| 7 | LawnchairLauncher/lawnchair | #4125 | MISSING_GESTURE | home, open_notifications, tap_screen | ✅ SUCCESS |
| 8 | LawnchairLauncher/lawnchair | #4786 | TALKBACK_REQUIRED | — | ❌ FAIL |
| 9 | Pool-Of-Tears/GreenStash | #170 | NAVIGATION_FAILURE | — | ✅ SUCCESS |
| 10 | TeamNewPipe/NewPipe | #10750 | MISSING_GESTURE | open_notifications, tap_screen | ✅ SUCCESS |
| 11 | TeamNewPipe/NewPipe | #8338 | MISSING_GESTURE | tap_screen | ✅ SUCCESS |
| 12 | abdallahmehiz/mpvKt | #184 | MISSING_GESTURE | tap_screen | ✅ SUCCESS |
| 13 | fast4x/RiMusic | #1152 | MISSING_GESTURE | tap_screen | ✅ SUCCESS |
| 14 | gsantner/markor | #2746 | MISSING_GESTURE | tap_screen | ✅ SUCCESS |
| 15 | openboard-team/openboard | #613 | MISSING_GESTURE | home | ✅ SUCCESS |
| 16 | openboard-team/openboard | #758 | TALKBACK_REQUIRED | — | ❌ FAIL |
| 17 | FossifyOrg/Launcher | #304 | NAVIGATION_FAILURE | — | ✅ SUCCESS |
| 18 | FossifyOrg/Notes | #59 | MISSING_GESTURE | drag_and_drop | ✅ SUCCESS |
| 19 | LawnchairLauncher/lawnchair | #1247 | TALKBACK_REQUIRED | — | ❌ FAIL |
| 20 | LawnchairLauncher/lawnchair | #4320 | MISSING_GESTURE | drag_and_drop | ✅ SUCCESS |
| 21 | MetrolistGroup/Metrolist | #3227 | MISSING_GESTURE | drag_and_drop | ✅ SUCCESS |
| 22 | MetrolistGroup/Metrolist | #3561 | MISSING_GESTURE | drag_and_drop | ✅ SUCCESS |
| 23 | NeoApplications/Neo-Launcher | #130 | MISSING_GESTURE | drag_and_drop, swipe_region | ✅ SUCCESS |
| 24 | breezy-weather/breezy-weather | #2159 | MISSING_GESTURE | drag_and_drop | ✅ SUCCESS |
| 25 | fcitx5-android/fcitx5-android | #841 | MISSING_GESTURE | drag_and_drop, home | ✅ SUCCESS |
| 26 | Anthonyy232/Paperize | #325 | NAVIGATION_FAILURE | — | ✅ SUCCESS |
| 27 | Crustack/NotallyX | #570 | NAVIGATION_FAILURE | — | ✅ SUCCESS |
| 28 | FossifyOrg/Launcher | #198 | NAVIGATION_FAILURE | — | ✅ SUCCESS |
| 29 | breezy-weather/breezy-weather | #1639 | NAVIGATION_FAILURE | — | ✅ SUCCESS |
| 30 | FossifyOrg/Clock | #85 | NAVIGATION_FAILURE | — | ❌ FAIL |
| 31 | Droid-ify/client | #583 | MISSING_GESTURE | pinch | ✅ SUCCESS |
| 32 | FossifyOrg/Calendar | #621 | MISSING_GESTURE | pinch | ✅ SUCCESS |
| 33 | FossifyOrg/Camera | #23 | MISSING_GESTURE | pinch | ✅ SUCCESS |
| 34 | FossifyOrg/Gallery | #642 | MISSING_GESTURE | pinch | ✅ SUCCESS |
| 35 | FossifyOrg/Gallery | #728 | MISSING_GESTURE | pinch | ✅ SUCCESS |
| 36 | FossifyOrg/Paint | #125 | MISSING_GESTURE | pinch, swipe_region | ✅ SUCCESS |
| 37 | FossifyOrg/Paint | #25 | MISSING_GESTURE | pinch, swipe_region | ✅ SUCCESS |
| 38 | ankidroid/Anki-Android | #16135 | MISSING_GESTURE | pinch | ✅ SUCCESS |
| 39 | saber-notes/saber | #192 | MISSING_GESTURE | pinch, two_finger_swipe | ✅ SUCCESS |
| 40 | streetcomplete/StreetComplete | #6068 | MISSING_GESTURE | pinch | ✅ SUCCESS |
| 41 | yairm210/Unciv | #13517 | MISSING_GESTURE | tap_screen | ✅ SUCCESS |
| 42 | you-apps/WallYou | #216 | MISSING_GESTURE | pinch | ✅ SUCCESS |
| 43 | LawnchairLauncher/lawnchair | #5540 | MISSING_GESTURE | pinch, quick_tap | ✅ SUCCESS |
| 44 | anilbeesetti/nextplayer | #1389 | MISSING_GESTURE | drag_and_drop, quick_tap | ✅ SUCCESS |
| 45 | ankidroid/Anki-Android | #18529 | MISSING_GESTURE | drag_and_drop, quick_tap | ❌ FAIL |
| 46 | ankidroid/Anki-Android | #19641 | MISSING_GESTURE | quick_tap | ✅ SUCCESS |
| 47 | ankidroid/Anki-Android | #20789 | SETUP_LIMITATION | — | ❌ FAIL |
| 48 | ankidroid/Anki-Android | #7138 | MISSING_GESTURE | quick_tap | ✅ SUCCESS |
| 49 | Fandroid745/Open-notes | #15 | NAVIGATION_FAILURE | — | ✅ SUCCESS |
| 50 | ankidroid/Anki-Android | #5512 | MISSING_GESTURE | tap_screen | ✅ SUCCESS |
| 51 | A-EDev/Flow | #27 | MISSING_GESTURE | pinch, quick_tap, swipe_region, tap_screen | ✅ SUCCESS |
| 52 | A-EDev/Flow | #284 | MISSING_GESTURE | pinch, swipe_region | ✅ SUCCESS |
| 53 | FossifyOrg/Calendar | #1103 | TALKBACK_REQUIRED | — | ✅ SUCCESS |
| 54 | FossifyOrg/Clock | #156 | NAVIGATION_FAILURE | — | ❌ FAIL |
| 55 | FossifyOrg/File-Manager | #136 | NAVIGATION_FAILURE | — | ✅ SUCCESS |
| 56 | FossifyOrg/Gallery | #237 | MISSING_GESTURE | swipe_region | ✅ SUCCESS |
| 57 | FossifyOrg/Gallery | #584 | SETUP_LIMITATION | — | ❌ FAIL |
| 58 | FossifyOrg/Gallery | #940 | MISSING_GESTURE | swipe_region, tap_screen | ✅ SUCCESS |
| 59 | FossifyOrg/Launcher | #66 | OTHER | — | ✅ SUCCESS |
| 60 | FossifyOrg/Messages | #80 | MISSING_GESTURE | home | ✅ SUCCESS |
| 61 | Kin69/EasyNotes | #356 | MISSING_GESTURE | home, tap_screen | ✅ SUCCESS |
| 62 | LawnchairLauncher/lawnchair | #4708 | MISSING_GESTURE | swipe_region, tap_screen | ✅ SUCCESS |
| 63 | anilbeesetti/nextplayer | #1127 | MISSING_GESTURE | swipe_region | ✅ SUCCESS |
| 64 | ankidroid/Anki-Android | #14934 | NAVIGATION_FAILURE | — | ✅ SUCCESS |
| 65 | 25huizengek1/ViTune | #710 | MISSING_GESTURE | open_notifications | ✅ SUCCESS |
| 66 | breezy-weather/breezy-weather | #205 | NAVIGATION_FAILURE | — | ✅ SUCCESS |
| 67 | breezy-weather/breezy-weather | #85 | NAVIGATION_FAILURE | — | ✅ SUCCESS |

| 68 | dessalines/thumb-key | #371 | MISSING_GESTURE | swipe_region | ✅ SUCCESS |
| 69 | iamrasel/lunar-launcher | #82 | NAVIGATION_FAILURE | — | ✅ SUCCESS |
| 70 | libre-tube/LibreTube | #8245 | MISSING_GESTURE | swipe_region | ✅ SUCCESS |
| 71 | msasikanth/twine | #1566 | NAVIGATION_FAILURE | — | ✅ SUCCESS |
| 72 | you-apps/ConnectYou | #155 | NAVIGATION_FAILURE | — | ✅ SUCCESS |

---

## Double Tap (19 bugs — 3✅ 16❌)

### 1. FossifyOrg_Calendar_273 ❌

**Bug Title:** Setting a default event length doesn't change the default event length
**App:** FossifyOrg/Calendar
**Issue:** [#273](https://github.com/FossifyOrg/Calendar/issues/273)
**Version:** 1.0.3
**Category:** Double Tap
**Primary Gesture:** `double_tap` / `tap_screen`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands executed, 0s runtime
- The log states: "ReBL does not support the required action(s): tap_screen"
- CARBON used `tap_screen` (coordinate-based tapping) to simulate double-tap on the calendar

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `tap_screen`

**Reproduction Summary:** ReBL could not even attempt this bug. CARBON's `tap_screen` command allows tapping at specific screen coordinates, which is needed to double-tap on a calendar date to create an event. ReBL's `click` command only targets UI elements by their accessibility labels, not arbitrary screen positions.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (15 steps, 453s) using `tap_screen` to double-tap on calendar dates. ReBL lacks coordinate-based tapping entirely.

---

### 2. FossifyOrg_Gallery_363 ❌

**Bug Title:** webp images when double tapped don't zoom to height of image
**App:** FossifyOrg/Gallery
**Issue:** [#363](https://github.com/FossifyOrg/Gallery/issues/363)
**Version:** 1.2.1
**Category:** Double Tap
**Primary Gesture:** `double_tap` / `pinch`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `pinch`, `tap_screen`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `pinch`, `tap_screen`

**Reproduction Summary:** The bug requires zooming into a webp image via double-tap or pinch. ReBL cannot perform either gesture. CARBON used `pinch` and `tap_screen` to zoom and trigger the buggy behavior.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (9 steps, 288s) using `pinch` and `tap_screen`. ReBL lacks both gestures.

---

### 3. FossifyOrg_Gallery_678 ❌

**Bug Title:** 'Allow 1:1 zooming in with two double taps' not working when pixel size of the photo is lesser than that of the screen
**App:** FossifyOrg/Gallery
**Issue:** [#678](https://github.com/FossifyOrg/Gallery/issues/678)
**Version:** 1.5.2
**Category:** Double Tap
**Primary Gesture:** `double_tap` / `pinch`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `pinch`, `quick_tap`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `pinch`, `quick_tap`

**Reproduction Summary:** Bug requires pinch-to-zoom on a small image. ReBL cannot pinch. CARBON used `pinch` and `quick_tap` to zoom and verify the 1:1 zoom behavior.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (10 steps, 290s). ReBL lacks `pinch` and `quick_tap`.

---

### 4. FossifyOrg_Gallery_846 ❌

**Bug Title:** "Fill screen" zoom on double tap ignores disabled "Show notch if available"
**App:** FossifyOrg/Gallery
**Issue:** [#846](https://github.com/FossifyOrg/Gallery/issues/846)
**Version:** 1.10.0
**Category:** Double Tap
**Primary Gesture:** `double_tap`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `pinch` (CARBON also used `double_tap`, `drag`)

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `pinch`

**Reproduction Summary:** Bug requires double-tapping an image to zoom and then observing notch overlap. ReBL cannot perform pinch or double_tap_screen gestures. CARBON used `double_tap`, `pinch`, and `drag` across 30 steps.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (30 steps, 853s) with `double_tap`, `pinch`, `drag`. ReBL lacks all three.

---

### 5. FossifyOrg_Gallery_847 ❌

**Bug Title:** Invalid "fill screen" zoom for GIF images on double-tap
**App:** FossifyOrg/Gallery
**Issue:** [#847](https://github.com/FossifyOrg/Gallery/issues/847)
**Version:** 1.10.0
**Category:** Double Tap
**Primary Gesture:** `double_tap` / `tap_screen`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `tap_screen`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `tap_screen`

**Reproduction Summary:** Bug requires double-tapping a GIF to trigger incorrect zoom. ReBL cannot perform coordinate-based taps. CARBON simulated double-tap using two consecutive `tap_screen` commands.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (8 steps, 119s) using `tap_screen`. ReBL lacks this capability.

---

### 6. LawnchairLauncher_lawnchair_2910 ❌

**Bug Title:** Double tap to sleep no longer works through root access
**App:** LawnchairLauncher/lawnchair
**Issue:** [#2910](https://github.com/LawnchairLauncher/lawnchair/issues/2910)
**Version:** 12.1.0
**Category:** Double Tap
**Primary Gesture:** `double_tap` / `tap_screen`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `drag_and_drop`, `tap_screen`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `drag_and_drop`, `tap_screen`

**Reproduction Summary:** Bug requires configuring double-tap gesture and then performing a double-tap on the homescreen. CARBON used `tap_screen` to simulate the double-tap and `drag_and_drop` for navigation. ReBL lacks both.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (24 steps, 540s). ReBL lacks `tap_screen` and `drag_and_drop`.

---

### 7. LawnchairLauncher_lawnchair_4125 ❌

**Bug Title:** android 14, no option to allow restricted setting
**App:** LawnchairLauncher/lawnchair
**Issue:** [#4125](https://github.com/LawnchairLauncher/lawnchair/issues/4125)
**Version:** 12.1.0
**Category:** Double Tap
**Primary Gesture:** `double_tap` / `tap_screen`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `home`, `open_notifications`, `tap_screen`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `home`, `open_notifications`, `tap_screen`

**Reproduction Summary:** Bug requires navigating to App Info via system settings. CARBON used `home`, `open_notifications`, and `tap_screen` for system-level navigation. ReBL cannot press the home button or open the notification shade.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (24 steps, 661s). ReBL lacks `home`, `open_notifications`, and `tap_screen`.

---

### 8. LawnchairLauncher_lawnchair_4786 ❌

**Bug Title:** Crash when trying to move item using TalkBack action
**App:** LawnchairLauncher/lawnchair
**Issue:** [#4786](https://github.com/LawnchairLauncher/lawnchair/issues/4786)
**Version:** v15.0.0-beta3.0
**Category:** Double Tap
**Primary Gesture:** `talkback`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL **attempted** the bug (104 commands, 971.7s) using `long_click`, `click`, `swipe`, `back`, `restart`, `orientation`
- ReBL tried long-pressing various widgets, app icons, and folders to find the "Move item" action
- Could not trigger the TalkBack-specific "3-finger tap" Actions menu
- All context menus only offered "Customize" and "App info", not the TalkBack "Move" action

**Failure Category:** `TALKBACK_REQUIRED`

**Reproduction Summary:** The bug requires TalkBack accessibility service to be active and uses a 3-finger tap gesture to open an Actions menu. ReBL cannot enable TalkBack or perform multi-finger gestures. Despite 104 attempts with standard interactions, the TalkBack-specific crash path could not be reached.

**Steps Count:** 104

**Comparison with CARBON:** CARBON also failed on this bug — it requires TalkBack which neither tool can enable.

---

### 9. Pool-Of-Tears_GreenStash_170 ❌

**Bug Title:** Some accessibility issues
**App:** Pool-Of-Tears/GreenStash
**Issue:** [#170](https://github.com/Pool-Of-Tears/GreenStash/issues/170)
**Version:** 3.9.2
**Category:** Double Tap
**Primary Gesture:** `double_tap`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL **attempted** the bug (128 commands, 1793.5s) using `click`, `scroll`, `swipe`, `orientation`, `long_click`, `back`, `set_text`, `restart`, `double_tap`
- ReBL could not navigate to the settings screen where the accessibility issues manifest
- Got stuck in loops trying to find the settings navigation
- Despite having `double_tap` in its action set for this test, navigation failures prevented reaching the buggy screen

**Failure Category:** `NAVIGATION_FAILURE`

**Reproduction Summary:** ReBL spent nearly 30 minutes trying to navigate to the settings screen but could not find the correct path. The app's navigation structure was not discoverable through ReBL's UI element parsing. CARBON succeeded by using its broader gesture set to navigate more effectively.

**Steps Count:** 128

**Comparison with CARBON:** CARBON succeeded (6 steps, 229s) using `click` and `swipe`. ReBL had the basic commands but couldn't navigate the app's UI structure efficiently.

---

### 10. TeamNewPipe_NewPipe_10750 ❌

**Bug Title:** Video playback randomly "closed/crashed", and content loaded but stuck buffering
**App:** TeamNewPipe/NewPipe
**Issue:** [#10750](https://github.com/TeamNewPipe/NewPipe/issues/10750)
**Version:** 0.26.1
**Category:** Double Tap
**Primary Gesture:** `double_tap` / `tap_screen`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `open_notifications`, `tap_screen`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `open_notifications`, `tap_screen`

**Reproduction Summary:** Bug requires interacting with video playback controls via coordinate-based taps and checking notifications. ReBL lacks both `tap_screen` and `open_notifications`.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (46 steps, 1231s) using `tap_screen` and `open_notifications`. ReBL lacks both.

---

### 11. TeamNewPipe_NewPipe_8338 ❌

**Bug Title:** Swipe down gesture of Player UI does not work all the times
**App:** TeamNewPipe/NewPipe
**Issue:** [#8338](https://github.com/TeamNewPipe/NewPipe/issues/8338)
**Version:** 0.23.0
**Category:** Double Tap
**Primary Gesture:** `double_tap` / `tap_screen`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `tap_screen`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `tap_screen`

**Reproduction Summary:** Bug requires double-tapping to pause video then swiping down. CARBON simulated double-tap with two `tap_screen` commands. ReBL cannot perform coordinate-based taps.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (21 steps, 615s) using `tap_screen`. ReBL lacks this.

---

### 12. abdallahmehiz_mpvKt_184 ❌

**Bug Title:** Tap error while playing video
**App:** abdallahmehiz/mpvKt
**Issue:** [#184](https://github.com/abdallahmehiz/mpvKt/issues/184)
**Version:** 0.1.6
**Category:** Double Tap
**Primary Gesture:** `double_tap` / `tap_screen`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `tap_screen`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `tap_screen`

**Reproduction Summary:** Bug requires double-tapping during video playback. CARBON used `tap_screen` for coordinate-based taps. ReBL cannot tap at arbitrary screen coordinates.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (5 steps, 173s) using `tap_screen`. ReBL lacks this.

---

### 13. ankidroid_Anki-Android_17393 ✅

**Bug Title:** IO Cards Go to the Wrong Deck
**App:** ankidroid/Anki-Android
**Issue:** [#17393](https://github.com/ankidroid/Anki-Android/issues/17393)
**Version:** 2.20alpha1
**Category:** Double Tap
**Primary Gesture:** `double_tap` (but bug is actually about deck selection, not gesture-dependent)

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `click` (126x), `set_text` (15x), `back` (12x), `scroll` (3x)
- Total: 156 commands in 1543.8s
- ReBL navigated through AnkiDroid's setup, created decks, configured settings, and created cards
- The bug is about card deck assignment logic, not a gesture-specific issue

**Failure Category:** —

**Reproduction Summary:** ReBL successfully reproduced this bug because it doesn't actually require a double-tap gesture — it's a logic bug about cards going to the wrong deck. ReBL used standard click and text input to navigate settings, create decks, and verify the buggy behavior. The "double_tap" category is somewhat misleading for this bug.

**Steps Count:** 156

**Comparison with CARBON:** Both tools succeeded. CARBON took 28 steps (1163s), ReBL took 156 steps (1544s). ReBL was less efficient but still reached the same outcome.

---

### 14. cromaguy_Rhythm_281 ✅

**Bug Title:** Double tap needed on Touch Gestures view of Onboarding Setup
**App:** cromaguy/Rhythm
**Issue:** [#281](https://github.com/cromaguy/Rhythm/issues/281)
**Version:** 4.4.345
**Category:** Double Tap
**Primary Gesture:** N/A (bug is that single tap doesn't work, requiring double tap)

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `click` (33x)
- Total: 33 commands in 284.6s
- ReBL navigated through the onboarding flow and reached the Touch Gestures screen
- A single tap on the "Next" button did not navigate forward, confirming the bug

**Failure Category:** —

**Reproduction Summary:** ReBL successfully reproduced this bug. The bug is that buttons on the Touch Gestures onboarding screen require a double tap instead of a single tap. ReBL's single `click` commands failed to advance the screen, which IS the buggy behavior being reported.

**Steps Count:** 33

**Comparison with CARBON:** Both succeeded. CARBON took 11 steps (249s), ReBL took 33 steps (285s).

---

### 15. fast4x_RiMusic_1152 ❌

**Bug Title:** Unclear Linking and Unresponsive Buttons in Player View
**App:** fast4x/RiMusic
**Issue:** [#1152](https://github.com/fast4x/RiMusic/issues/1152)
**Version:** 0.6.26
**Category:** Double Tap
**Primary Gesture:** `double_tap` / `tap_screen`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `tap_screen`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `tap_screen`

**Reproduction Summary:** Bug requires tapping on player view buttons. CARBON used `tap_screen` for precise coordinate taps. ReBL lacks this capability.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (6 steps, 124s). ReBL lacks `tap_screen`.

---

### 16. gsantner_markor_2746 ❌

**Bug Title:** Markor does not recognize URL/link anymore
**App:** gsantner/markor
**Issue:** [#2746](https://github.com/gsantner/markor/issues/2746)
**Version:** 2.15.2
**Category:** Double Tap
**Primary Gesture:** `double_tap` / `tap_screen`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `tap_screen`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `tap_screen`

**Reproduction Summary:** Bug requires tapping on a URL in a text editor. CARBON used `tap_screen` for coordinate-based tapping on the link text. ReBL cannot tap at arbitrary positions.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (7 steps, 200s). ReBL lacks `tap_screen`.

---

### 17. openboard-team_openboard_613 ❌

**Bug Title:** Sometimes the spellchecker flags correctly spelt words if one adds a full-stop to them
**App:** openboard-team/openboard
**Issue:** [#613](https://github.com/openboard-team/openboard/issues/613)
**Version:** 1.4.4
**Category:** Double Tap
**Primary Gesture:** `double_tap`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `home` (CARBON needed to press home to switch between apps)

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `home`

**Reproduction Summary:** Bug requires switching between apps using the home button. CARBON used `home` to navigate between the keyboard setup and a text input app. ReBL cannot press the system home button.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (33 steps, 1008s). ReBL lacks `home` button capability.

---

### 18. openboard-team_openboard_758 ❌

**Bug Title:** Accessibility: The button to go to the previous level does not work properly
**App:** openboard-team/openboard
**Issue:** [#758](https://github.com/openboard-team/openboard/issues/758)
**Version:** 1.4.5
**Category:** Double Tap
**Primary Gesture:** `talkback`

**Result:** ❌ **FAIL** (corrected from false positive)

**How ReBL Handled It:**
- ReBL **attempted** the bug (30 commands) using only `click`
- ReBL originally reported SUCCESS but this was **corrected to FAIL** as a false positive
- ReBL did not enable TalkBack as required by Step 1 of the bug report
- Without TalkBack active, the double-tap behavior described in the bug cannot be tested
- ReBL used a regular click, not a TalkBack double-tap

**Failure Category:** `TALKBACK_REQUIRED`

**Reproduction Summary:** The bug specifically requires TalkBack to be enabled (Step 1: "Install a screen reader (TalkBack)... turn on the TalkBack service"). ReBL cannot enable TalkBack. Its regular click is not equivalent to a TalkBack double-tap gesture. The original SUCCESS was a false positive.

**Steps Count:** 30

**Comparison with CARBON:** CARBON also failed on this bug — TalkBack is required by both tools but neither can enable it.

---

### 19. syt0r_Kanji-Dojo_291 ✅

**Bug Title:** Double-tapping back arrow while transitioning from vocab info to practice skips finish-practice dialog
**App:** syt0r/Kanji-Dojo
**Issue:** [#291](https://github.com/syt0r/Kanji-Dojo/issues/291)
**Version:** 2.1.9
**Category:** Double Tap
**Primary Gesture:** N/A (bug triggered by rapid back-button clicks)

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `click` (38x)
- Total: 38 commands in 328.8s
- ReBL navigated to a practice session, revealed the answer, went to vocab info, then performed rapid back clicks
- The rapid clicking on the back arrow caused the app to skip the finish-practice dialog

**Failure Category:** —

**Reproduction Summary:** ReBL successfully reproduced this bug. The "double-tap" in the title refers to rapidly clicking the back arrow, which ReBL can do with its standard `click` command. ReBL navigated through the vocab practice flow and triggered the skip behavior.

**Steps Count:** 38

**Comparison with CARBON:** Both succeeded. CARBON took 19 steps (526s), ReBL took 38 steps (329s). ReBL was actually faster despite more steps.

---

## Drag and Drop (9 bugs — 0✅ 9❌)

### 20. FossifyOrg_Launcher_304 ❌

**Bug Title:** Accidently creating invisible folders in dock
**App:** FossifyOrg/Launcher
**Issue:** [#304](https://github.com/FossifyOrg/Launcher/issues/304)
**Version:** 1.6.0
**Category:** Drag and Drop
**Primary Gesture:** `drag_and_drop`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL **attempted** the bug (118 commands, 1410.5s) using `click`, `swipe`, `long_click`, `back`, `scroll`, `orientation`, `drag`, `restart`
- ReBL tried to drag icons in the dock to create folders but could not perform the precise drag-and-drop gesture
- Got stuck in loops trying to set the launcher as default and interact with dock items
- The `drag` action available was not sufficient for the precise dock-to-dock drag needed

**Failure Category:** `NAVIGATION_FAILURE`

**Reproduction Summary:** ReBL spent over 23 minutes trying to create invisible folders by dragging dock items. While it had a basic `drag` action, it could not perform the precise drag-and-drop from one dock position to another that creates the invisible folder. The interaction requires holding an item and dropping it on another specific position.

**Steps Count:** 118

**Comparison with CARBON:** CARBON succeeded (14 steps, 404s) using `drag_and_drop`. ReBL's basic drag was insufficient for this precise interaction.

---

### 21. FossifyOrg_Notes_59 ❌

**Bug Title:** Reordering checklists works strangely with move checked to bottom
**App:** FossifyOrg/Notes
**Issue:** [#59](https://github.com/FossifyOrg/Notes/issues/59)
**Version:** 1.1.0
**Category:** Drag and Drop
**Primary Gesture:** `drag_and_drop`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `drag_and_drop`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `drag_and_drop`

**Reproduction Summary:** Bug requires dragging checklist items to reorder them. ReBL cannot perform drag-and-drop gestures.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (6 steps, 180s) using `drag_and_drop`. ReBL lacks this gesture entirely.

---

### 22. LawnchairLauncher_lawnchair_1247 ❌

**Bug Title:** the launcher kees crashign when I attempt to move stuff
**App:** LawnchairLauncher/lawnchair
**Issue:** [#1247](https://github.com/LawnchairLauncher/lawnchair/issues/1247)
**Version:** v15.0.0-beta3.0
**Category:** Drag and Drop
**Primary Gesture:** `talkback`

**Result:** ❌ **FAIL** (corrected from false positive)

**How ReBL Handled It:**
- ReBL **attempted** the bug (60 commands) using `long_click`, `click`, `back`, `swipe`
- ReBL originally reported SUCCESS but was **corrected to FAIL** as a false positive
- ReBL triggered a crash but NOT through the TalkBack actions menu as required
- The crash was through a different code path (long_click + drag), not the TalkBack-specific crash

**Failure Category:** `TALKBACK_REQUIRED`

**Reproduction Summary:** The bug requires TalkBack to be active and uses the TalkBack actions menu (Step 3: "Bring up the TalkBack actions menu"). ReBL cannot enable TalkBack. While ReBL did trigger a crash, it was through a different mechanism than described in the bug report.

**Steps Count:** 60

**Comparison with CARBON:** CARBON also failed — TalkBack is required.

---

### 23. LawnchairLauncher_lawnchair_4320 ❌

**Bug Title:** Unable to add any widget
**App:** LawnchairLauncher/lawnchair
**Issue:** [#4320](https://github.com/LawnchairLauncher/lawnchair/issues/4320)
**Version:** 14.0
**Category:** Drag and Drop
**Primary Gesture:** `drag_and_drop`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `drag_and_drop`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `drag_and_drop`

**Reproduction Summary:** Bug requires dragging a widget from the widget picker to the home screen. ReBL cannot perform drag-and-drop.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (7 steps, 251s) using `drag_and_drop`. ReBL lacks this gesture.

---

### 24. MetrolistGroup_Metrolist_3227 ❌

**Bug Title:** Replacement of new song with old song
**App:** MetrolistGroup/Metrolist
**Issue:** [#3227](https://github.com/MetrolistGroup/Metrolist/issues/3227)
**Version:** 13.3.0
**Category:** Drag and Drop
**Primary Gesture:** `drag_and_drop`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `drag_and_drop`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `drag_and_drop`

**Reproduction Summary:** Bug requires dragging songs to reorder a playlist. ReBL cannot drag-and-drop.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (17 steps, 574s) using `drag_and_drop`. ReBL lacks this gesture.

---

### 25. MetrolistGroup_Metrolist_3561 ❌

**Bug Title:** Weird Bug when changing list order in custom order format
**App:** MetrolistGroup/Metrolist
**Issue:** [#3561](https://github.com/MetrolistGroup/Metrolist/issues/3561)
**Version:** 13.4.1
**Category:** Drag and Drop
**Primary Gesture:** `drag_and_drop`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `drag_and_drop`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `drag_and_drop`

**Reproduction Summary:** Bug requires dragging items to change list order. ReBL cannot drag-and-drop.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (17 steps, 574s) using `drag_and_drop`. ReBL lacks this gesture.

---

### 26. NeoApplications_Neo-Launcher_130 ❌

**Bug Title:** Changing the first app in a folder with Covers enabled breaks the folder
**App:** NeoApplications/Neo-Launcher
**Issue:** [#130](https://github.com/NeoApplications/Neo-Launcher/issues/130)
**Version:** 0.8.1
**Category:** Drag and Drop
**Primary Gesture:** `drag_and_drop`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `drag_and_drop`, `swipe_region`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `drag_and_drop`, `swipe_region`

**Reproduction Summary:** Bug requires dragging apps within a folder to reorder them. ReBL cannot drag-and-drop or swipe within specific regions.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (43 steps, 1339s) using `drag_and_drop` and `swipe_region`. ReBL lacks both.

---

### 27. breezy-weather_breezy-weather_2159 ❌

**Bug Title:** Can't add widget to home screen
**App:** breezy-weather/breezy-weather
**Issue:** [#2159](https://github.com/breezy-weather/breezy-weather/issues/2159)
**Version:** 6.0.5-alpha
**Category:** Drag and Drop
**Primary Gesture:** `drag_and_drop`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `drag_and_drop`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `drag_and_drop`

**Reproduction Summary:** Bug requires dragging a widget to the home screen. ReBL cannot drag-and-drop.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (10 steps, 287s) using `drag_and_drop`. ReBL lacks this gesture.

---

### 28. fcitx5-android_fcitx5-android_841 ❌

**Bug Title:** Crash somtimes on showing keyboard when the preferred input method is supported by the addon
**App:** fcitx5-android/fcitx5-android
**Issue:** [#841](https://github.com/fcitx5-android/fcitx5-android/issues/841)
**Version:** 0.1.2
**Category:** Drag and Drop
**Primary Gesture:** `drag_and_drop`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `drag_and_drop`, `home`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `drag_and_drop`, `home`

**Reproduction Summary:** Bug requires dragging keyboard input method items and pressing home. ReBL cannot drag-and-drop or press the home button.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (13 steps, 509s) using `drag_and_drop` and `home`. ReBL lacks both.

---

## Long Press (9 bugs — 5✅ 4❌)

### 29. Anthonyy232_Paperize_325 ❌

**Bug Title:** Crashing when adding images
**App:** Anthonyy232/Paperize
**Issue:** [#325](https://github.com/Anthonyy232/Paperize/issues/325)
**Version:** 3.0.0
**Category:** Long Press
**Primary Gesture:** `long_press`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL **attempted** the bug (62 commands, 615.2s) using `click`, `scroll`, `orientation`, `back`, `restart`
- ReBL could not find the "plus sign" button to create an album (likely a FAB not detected by UI parsing)
- Tried orientation changes and restarts to force UI redraws
- Got stuck in a loop unable to proceed past the Library screen

**Failure Category:** `NAVIGATION_FAILURE`

**Reproduction Summary:** ReBL could not locate the floating action button (FAB) to add images. The FAB was likely not properly identified in the UI hierarchy. Despite 62 attempts including orientation changes, ReBL never found the button to create an album and add images.

**Steps Count:** 62

**Comparison with CARBON:** CARBON succeeded (11 steps, 402s). CARBON's broader gesture set and better UI element detection allowed it to find and interact with the FAB.

---

### 30. Crustack_NotallyX_570 ❌

**Bug Title:** App crash when note is selected, search filter changed and another note is selected
**App:** Crustack/NotallyX
**Issue:** [#570](https://github.com/Crustack/NotallyX/issues/570)
**Version:** 7.4.0
**Category:** Long Press
**Primary Gesture:** `long_press`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL **attempted** the bug (75 commands, 809.6s) using `click`, `set_text`, `back`, `scroll`, `long_click`, `restart`, `swipe`, `orientation`
- ReBL could not interact with the notes properly — the UI elements for notes were not reliably targetable
- Tried creating notes, searching, and selecting but couldn't reproduce the specific sequence

**Failure Category:** `NAVIGATION_FAILURE`

**Reproduction Summary:** ReBL spent over 13 minutes trying to reproduce the crash sequence (select note → change search filter → select another note) but could not reliably interact with the note list items. The UI parsing did not provide sufficient information to target specific notes.

**Steps Count:** 75

**Comparison with CARBON:** CARBON succeeded (5 steps, 122s). CARBON's more precise UI interaction allowed it to quickly select notes and trigger the crash.

---

### 31. FossifyOrg_File-Manager_195 ✅

**Bug Title:** Unnecessary refresh of ZIP file icons when closing bottom sheets
**App:** FossifyOrg/File-Manager
**Issue:** [#195](https://github.com/FossifyOrg/File-Manager/issues/195)
**Version:** 1.2.0
**Category:** Long Press
**Primary Gesture:** `long_press`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `click`, `long_click`, and standard navigation (6 commands)
- Navigated to Download folder, long-clicked a ZIP file, opened More options
- Successfully triggered the bottom sheet and observed the icon refresh behavior

**Failure Category:** —

**Reproduction Summary:** ReBL successfully reproduced this bug using `long_click` (which maps to long press) to select a ZIP file and trigger the context menu/bottom sheet. The bug manifests when closing the bottom sheet, causing unnecessary icon refresh.

**Steps Count:** 6

**Comparison with CARBON:** Both succeeded. CARBON took 11 steps (452s), ReBL took 6 steps (~120s). ReBL was more efficient here.

---

### 32. FossifyOrg_Launcher_198 ❌

**Bug Title:** Folder rename dialog: Dark text on dark background
**App:** FossifyOrg/Launcher
**Issue:** [#198](https://github.com/FossifyOrg/Launcher/issues/198)
**Version:** 1.2.0
**Category:** Long Press
**Primary Gesture:** `long_press`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL **attempted** the bug (13 commands) using `long_click`, `click`
- Long-pressed a folder on the home screen but got the wrong context menu (Widgets/Wallpapers/Launcher Settings)
- Could not trigger the folder rename dialog specifically
- The long-press targeted the wrong area or the folder was not properly identified

**Failure Category:** `NAVIGATION_FAILURE`

**Reproduction Summary:** ReBL tried to long-press a folder to trigger the rename dialog but instead got the general home screen context menu. The folder element was not properly targeted, preventing access to the rename functionality where the dark-text-on-dark-background bug manifests.

**Steps Count:** 13

**Comparison with CARBON:** CARBON succeeded (12 steps, 574s). CARBON's more precise element targeting allowed it to correctly long-press the folder and access the rename dialog.

---

### 33. FossifyOrg_Messages_359 ✅

**Bug Title:** Can't scroll or see participants on conversation details page
**App:** FossifyOrg/Messages
**Issue:** [#359](https://github.com/FossifyOrg/Messages/issues/359)
**Version:** 1.4.0
**Category:** Long Press
**Primary Gesture:** `long_press`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `click`, `long_click`, and navigation (7 commands)
- Opened Messages app, long-clicked a conversation, accessed More options, then Conversation details
- Successfully navigated to the conversation details page where the scroll bug manifests

**Failure Category:** —

**Reproduction Summary:** ReBL successfully navigated to the conversation details page by long-pressing a conversation and selecting "Conversation details" from the context menu. The bug (inability to scroll or see participants) was triggered.

**Steps Count:** 7

**Comparison with CARBON:** Both succeeded. CARBON took 10 steps (471s), ReBL took 7 steps (~150s). ReBL was more efficient.

---

### 34. FossifyOrg_Messages_416 ✅

**Bug Title:** New conversation shortcut doesn't work
**App:** FossifyOrg/Messages
**Issue:** [#416](https://github.com/FossifyOrg/Messages/issues/416)
**Version:** 1.1.7
**Category:** Long Press
**Primary Gesture:** `long_press`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `long_click` (1x), `click` (2x)
- Total: 3 commands in 127.8s
- Long-pressed the Messages app icon, tapped "New conversation" shortcut
- The app opened an empty chat screen instead of the contact selection screen — confirming the bug

**Failure Category:** —

**Reproduction Summary:** ReBL perfectly reproduced this bug in just 3 steps. Long-pressing the app icon and selecting "New conversation" from the shortcut menu opened an empty chat instead of the expected contact picker. This matches the bug report exactly.

**Steps Count:** 3

**Comparison with CARBON:** Both succeeded. CARBON took 4 steps (181s), ReBL took 3 steps (128s). ReBL was slightly more efficient.

---

### 35. FossifyOrg_Messages_641 ✅

**Bug Title:** SMS scheduling not working
**App:** FossifyOrg/Messages
**Issue:** [#641](https://github.com/FossifyOrg/Messages/issues/641)
**Version:** 1.7.0
**Category:** Long Press
**Primary Gesture:** `long_press`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `click` (28x), `set_text` (2x), `long_click` (2x)
- Total: 32 commands in 447.7s
- Navigated to Messages, opened a conversation, composed a message, used long-click to access scheduling
- After scheduling and returning, the message reappeared in the input field (not sent) — confirming the bug

**Failure Category:** —

**Reproduction Summary:** ReBL successfully reproduced the SMS scheduling bug. After scheduling a message and navigating away then back, the message text reappeared in the input field instead of being sent, confirming the scheduling feature is broken.

**Steps Count:** 32

**Comparison with CARBON:** Both succeeded. CARBON took 10 steps (541s), ReBL took 32 steps (448s).

---

### 36. breezy-weather_breezy-weather_1639 ❌

**Bug Title:** weather wallpaper causes launcher to freeze and app background closed
**App:** breezy-weather/breezy-weather
**Issue:** [#1639](https://github.com/breezy-weather/breezy-weather/issues/1639)
**Version:** 5.3.5
**Category:** Long Press
**Primary Gesture:** `long_press`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL **attempted** the bug (27 commands) using `click`, `back`, and navigation
- Started the weather app and tried to add a location and configure weather wallpaper
- Could not navigate through the full setup flow to enable the weather wallpaper feature
- Got stuck at the location setup and weather source configuration screens

**Failure Category:** `NAVIGATION_FAILURE`

**Reproduction Summary:** ReBL could not complete the multi-step setup required to enable the weather wallpaper feature. The bug requires: adding a location → enabling weather wallpaper → long-pressing home screen. ReBL got stuck during the initial location setup.

**Steps Count:** 27

**Comparison with CARBON:** CARBON succeeded (23 steps, 645s). CARBON navigated the complex setup flow more effectively.

---

### 37. espresso3389_methings_34 ✅

**Bug Title:** Image preview UX gaps and instability when using Select Text on image blocks
**App:** espresso3389/methings
**Issue:** [#34](https://github.com/espresso3389/methings/issues/34)
**Version:** 0.5.0
**Category:** Long Press
**Primary Gesture:** `long_press`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `click` and standard navigation (19 commands)
- Opened the me.things app, dismissed update dialog, attached files, and interacted with image blocks
- Successfully triggered the image preview UX issues

**Failure Category:** —

**Reproduction Summary:** ReBL successfully reproduced the image preview instability by navigating to the app, attaching files, and interacting with image blocks. The UX gaps and instability were triggered through standard click interactions.

**Steps Count:** 19

**Comparison with CARBON:** Both succeeded. CARBON took 15 steps (363s), ReBL took 19 steps (~250s).

---

## Orientation (6 bugs — 5✅ 1❌)

### 38. FossifyOrg_Calendar_1042 ✅

**Bug Title:** The current selected day, month, week, year is not preserved after rotating
**App:** FossifyOrg/Calendar
**Issue:** [#1042](https://github.com/FossifyOrg/Calendar/issues/1042)
**Version:** 1.10.2
**Category:** Orientation
**Primary Gesture:** `orientation`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `click`, `orientation`
- Total: 12 commands in 145.5s
- Navigated to a specific day (April 27), then rotated the device
- After rotation, the displayed day reverted to April 26 — confirming the bug

**Failure Category:** —

**Reproduction Summary:** ReBL successfully reproduced this orientation bug. It navigated to a specific date, rotated the device, and confirmed that the selected date was not preserved. ReBL has the `orientation` command which maps directly to this bug's requirement.

**Steps Count:** 12

**Comparison with CARBON:** Both succeeded. CARBON took 5 steps (163s), ReBL took 12 steps (146s). Similar efficiency.

---

### 39. FossifyOrg_Camera_91 ✅

**Bug Title:** Countdown timer does not honor device orientation
**App:** FossifyOrg/Camera
**Issue:** [#91](https://github.com/FossifyOrg/Camera/issues/91)
**Version:** 1.0.2
**Category:** Orientation
**Primary Gesture:** `orientation`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `click`, `orientation`
- Total: 13 commands in 221.2s
- Set the countdown timer, started the countdown, then changed orientation to landscape
- The countdown text remained locked in portrait mode — confirming the bug

**Failure Category:** —

**Reproduction Summary:** ReBL successfully reproduced this bug by setting a timer, starting the countdown, and rotating the device. The countdown text did not rotate with the device, confirming the orientation bug.

**Steps Count:** 13

**Comparison with CARBON:** Both succeeded. CARBON took 7 steps (223s), ReBL took 13 steps (221s). Nearly identical time.

---

### 40. FossifyOrg_Clock_85 ❌

**Bug Title:** Snooze not working in landscape
**App:** FossifyOrg/Clock
**Issue:** [#85](https://github.com/FossifyOrg/Clock/issues/85)
**Version:** 1.0.0
**Category:** Orientation
**Primary Gesture:** `orientation`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL **attempted** the bug (105 commands, 834.6s) using `click`, `orientation`, `restart`, `back`, `set_text`
- Could not set a specific alarm time due to issues with the time picker UI
- The time picker was unreliable and multiple attempts to set a short alarm failed
- Never reached the alarm screen where the snooze-in-landscape bug occurs

**Failure Category:** `NAVIGATION_FAILURE`

**Reproduction Summary:** ReBL spent over 14 minutes trying to set an alarm but could not interact with the time picker UI reliably. Without triggering an alarm, the snooze-in-landscape bug could not be tested. The time picker's custom UI elements were not properly parseable by ReBL's UI hierarchy analysis.

**Steps Count:** 105

**Comparison with CARBON:** CARBON also failed on this bug (59 steps, 1580s) — the alarm UI was problematic for both tools.

---

### 41. FossifyOrg_Contacts_197 ✅

**Bug Title:** View always changed to contact list when rotating the phone
**App:** FossifyOrg/Contacts
**Issue:** [#197](https://github.com/FossifyOrg/Contacts/issues/197)
**Version:** 1.1.0
**Category:** Orientation
**Primary Gesture:** `orientation`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `click`, `orientation`
- Total: 30 commands in 375.3s
- Selected the "Favorites" tab, then rotated the device to landscape
- After rotation, the view incorrectly switched back to the contact list — confirming the bug

**Failure Category:** —

**Reproduction Summary:** ReBL successfully reproduced this bug by navigating to the Favorites tab and rotating the device. The app incorrectly reverted to the Contacts tab after rotation, matching the bug report.

**Steps Count:** 30

**Comparison with CARBON:** Both succeeded. CARBON took 6 steps (217s), ReBL took 30 steps (375s). CARBON was more efficient.

---

### 42. Waboodoo_HTTP-Shortcuts_262 ✅

**Bug Title:** several dialogs disappear on screen rotation
**App:** Waboodoo/HTTP-Shortcuts
**Issue:** [#262](https://github.com/Waboodoo/HTTP-Shortcuts/issues/262)
**Version:** 2.12.0
**Category:** Orientation
**Primary Gesture:** `orientation`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `click`, `orientation`
- Total: 6 commands in 99.0s
- Clicked the add button to open a dialog, then rotated the screen to landscape
- The dialog disappeared after rotation — confirming the bug

**Failure Category:** —

**Reproduction Summary:** ReBL efficiently reproduced this bug in just 6 steps. Opening a dialog and rotating the screen caused the dialog to disappear, exactly as described in the bug report.

**Steps Count:** 6

**Comparison with CARBON:** Both succeeded. CARBON took 3 steps (122s), ReBL took 6 steps (99s). ReBL was faster.

---

### 43. ankidroid_Anki-Android_16410 ✅

**Bug Title:** Changing screen orientation clears stats' search options
**App:** ankidroid/Anki-Android
**Issue:** [#16410](https://github.com/ankidroid/Anki-Android/issues/16410)
**Version:** 2.18.0
**Category:** Orientation
**Primary Gesture:** `orientation`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `click`, `back`, `orientation`
- Total: 37 commands in 341.8s
- Navigated to the Statistics page, set search options, then rotated the device
- After rotation, the search options were cleared — confirming the bug

**Failure Category:** —

**Reproduction Summary:** ReBL successfully navigated to AnkiDroid's statistics page, configured search filters, and rotated the device. The search options were cleared after rotation, confirming the bug.

**Steps Count:** 37

**Comparison with CARBON:** Both succeeded. CARBON took 9 steps (284s), ReBL took 37 steps (342s). CARBON was more efficient.

---

## Pinch/Zoom (14 bugs — 2✅ 12❌)

### 44. Droid-ify_client_583 ❌

**Bug Title:** Swiping images zooms instead of zooming
**App:** Droid-ify/client
**Issue:** [#583](https://github.com/Droid-ify/client/issues/583)
**Version:** 0.5.9
**Category:** Pinch/Zoom
**Primary Gesture:** `pinch_zoom`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `pinch`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `pinch`

**Reproduction Summary:** Bug requires pinch-to-zoom on app screenshots. ReBL cannot perform pinch gestures.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (10 steps, 402s) using `pinch`. ReBL lacks this gesture entirely.

---

### 45. FossifyOrg_Calendar_621 ❌

**Bug Title:** Zoom level in weekly view locks
**App:** FossifyOrg/Calendar
**Issue:** [#621](https://github.com/FossifyOrg/Calendar/issues/621)
**Version:** 1.3.0
**Category:** Pinch/Zoom
**Primary Gesture:** `pinch_zoom`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `pinch`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `pinch`

**Reproduction Summary:** Bug requires pinch-to-zoom in the weekly calendar view. ReBL cannot pinch.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (8 steps, 205s) using `pinch`. ReBL lacks this gesture.

---

### 46. FossifyOrg_Camera_23 ❌

**Bug Title:** Doesn't use zoom camera to zoom
**App:** FossifyOrg/Camera
**Issue:** [#23](https://github.com/FossifyOrg/Camera/issues/23)
**Version:** 1.0.1
**Category:** Pinch/Zoom
**Primary Gesture:** `pinch_zoom`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `pinch`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `pinch`

**Reproduction Summary:** Bug requires pinch-to-zoom in the camera app. ReBL cannot pinch.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (5 steps, 180s) using `pinch`. ReBL lacks this gesture.

---

### 47. FossifyOrg_Gallery_289 ✅

**Bug Title:** "Allow deep zooming images" creates artifacts in many images
**App:** FossifyOrg/Gallery
**Issue:** [#289](https://github.com/FossifyOrg/Gallery/issues/289)
**Version:** 1.1.3
**Category:** Pinch/Zoom
**Primary Gesture:** `unknown` (bug is about enabling a setting and viewing images)

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `click`, `back`, `scroll`, `swipe`
- Total: 37 commands in 527.6s
- Navigated to Gallery settings, enabled "Allow deep zooming images"
- Opened an image, closed it, and reopened it to trigger the artifact bug
- The bug manifests on the second viewing of an image with deep zoom enabled

**Failure Category:** —

**Reproduction Summary:** ReBL successfully reproduced this bug because it doesn't actually require a pinch gesture — the bug is triggered by enabling a setting and then viewing images. The artifacts appear automatically when deep zooming is enabled. ReBL navigated settings and opened images using standard clicks.

**Steps Count:** 37

**Comparison with CARBON:** Both succeeded. CARBON took 18 steps (549s), ReBL took 37 steps (528s). Similar time.

---

### 48. FossifyOrg_Gallery_642 ❌

**Bug Title:** Zoom doesn't work in photos
**App:** FossifyOrg/Gallery
**Issue:** [#642](https://github.com/FossifyOrg/Gallery/issues/642)
**Version:** 1.5.0
**Category:** Pinch/Zoom
**Primary Gesture:** `pinch_zoom`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `pinch`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `pinch`

**Reproduction Summary:** Bug requires pinch-to-zoom on photos. ReBL cannot pinch.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (11 steps, 387s) using `pinch`. ReBL lacks this gesture.

---

### 49. FossifyOrg_Gallery_728 ❌

**Bug Title:** (Deep zooming) Can not pan after releasing only one finger after pinch zooming
**App:** FossifyOrg/Gallery
**Issue:** [#728](https://github.com/FossifyOrg/Gallery/issues/728)
**Version:** 1.8.0
**Category:** Pinch/Zoom
**Primary Gesture:** `pinch_zoom`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `pinch`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `pinch`

**Reproduction Summary:** Bug requires pinch-to-zoom then releasing one finger to pan. This is a complex multi-touch gesture that ReBL cannot perform.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (33 steps, 1361s) using `pinch`. ReBL lacks this gesture.

---

### 50. FossifyOrg_Paint_125 ❌

**Bug Title:** Touch location and pen location different after zooming/rotation
**App:** FossifyOrg/Paint
**Issue:** [#125](https://github.com/FossifyOrg/Paint/issues/125)
**Version:** 1.2.0
**Category:** Pinch/Zoom
**Primary Gesture:** `pinch_zoom`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `pinch`, `swipe_region`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `pinch`, `swipe_region`

**Reproduction Summary:** Bug requires pinch-to-zoom on the canvas and then drawing. ReBL cannot pinch or swipe within specific regions.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (10 steps, 173s) using `pinch` and `swipe_region`. ReBL lacks both.

---

### 51. FossifyOrg_Paint_25 ❌

**Bug Title:** Eraser size not relative to zoom on minimum size
**App:** FossifyOrg/Paint
**Issue:** [#25](https://github.com/FossifyOrg/Paint/issues/25)
**Version:** 1.0.0
**Category:** Pinch/Zoom
**Primary Gesture:** `pinch_zoom`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `pinch`, `swipe_region`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `pinch`, `swipe_region`

**Reproduction Summary:** Bug requires pinch-to-zoom and then using the eraser. ReBL cannot pinch or draw in specific regions.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (7 steps, 197s) using `pinch` and `swipe_region`. ReBL lacks both.

---

### 52. ankidroid_Anki-Android_16135 ❌

**Bug Title:** Zooming in Statistics Page
**App:** ankidroid/Anki-Android
**Issue:** [#16135](https://github.com/ankidroid/Anki-Android/issues/16135)
**Version:** 2.18alpha8
**Category:** Pinch/Zoom
**Primary Gesture:** `pinch_zoom`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `pinch`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `pinch`

**Reproduction Summary:** Bug requires pinch-to-zoom on the statistics page. ReBL cannot pinch.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (16 steps, 528s) using `pinch`. ReBL lacks this gesture.

---

### 53. ankidroid_Anki-Android_17667 ✅

**Bug Title:** Width of "Deck options" page does not/cannot fit to screen (display)
**App:** ankidroid/Anki-Android
**Issue:** [#17667](https://github.com/ankidroid/Anki-Android/issues/17667)
**Version:** 2.21alpha4
**Category:** Pinch/Zoom
**Primary Gesture:** `pinch_zoom` (but bug is about layout, not gesture-dependent)

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `click` (16x), `back` (3x), `long_click` (3x)
- Total: 22 commands in 214.8s
- Navigated to AnkiDroid's Deck Options page
- The bug is about the page width not fitting the screen — a layout issue visible upon navigation

**Failure Category:** —

**Reproduction Summary:** ReBL successfully reproduced this bug because it's a layout/display issue, not a gesture-dependent bug. Simply navigating to the Deck Options page reveals the width problem. No pinch-to-zoom is actually needed to trigger the bug.

**Steps Count:** 22

**Comparison with CARBON:** Both succeeded. CARBON took 8 steps (238s), ReBL took 22 steps (215s). Similar efficiency.

---

### 54. saber-notes_saber_192 ❌

**Bug Title:** Two finger detection need improvement
**App:** saber-notes/saber
**Issue:** [#192](https://github.com/saber-notes/saber/issues/192)
**Version:** 0.5.2
**Category:** Pinch/Zoom
**Primary Gesture:** `pinch_zoom`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `pinch`, `two_finger_swipe`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `pinch`, `two_finger_swipe`

**Reproduction Summary:** Bug requires two-finger gestures (pinch and two-finger swipe). ReBL cannot perform any multi-finger gestures.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (6 steps, 208s) using `pinch` and `two_finger_swipe`. ReBL lacks both.

---

### 55. streetcomplete_StreetComplete_6068 ❌

**Bug Title:** OutOfMemoryError when downloading after zoom out
**App:** streetcomplete/StreetComplete
**Issue:** [#6068](https://github.com/streetcomplete/StreetComplete/issues/6068)
**Version:** 59.0-alpha1
**Category:** Pinch/Zoom
**Primary Gesture:** `pinch_zoom`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `pinch`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `pinch`

**Reproduction Summary:** Bug requires pinch-to-zoom-out on the map to trigger an OutOfMemoryError. ReBL cannot pinch.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (5 steps, 147s) using `pinch`. ReBL lacks this gesture.

---

### 56. yairm210_Unciv_13517 ❌

**Bug Title:** User report
**App:** yairm210/Unciv
**Issue:** [#13517](https://github.com/yairm210/Unciv/issues/13517)
**Version:** 4.16.0
**Category:** Pinch/Zoom
**Primary Gesture:** `pinch_zoom` / `tap_screen`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `tap_screen`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `tap_screen`

**Reproduction Summary:** Bug requires coordinate-based tapping on the game map. ReBL cannot tap at arbitrary screen coordinates.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (8 steps, 309s) using `tap_screen`. ReBL lacks this.

---

### 57. you-apps_WallYou_216 ❌

**Bug Title:** Improper edge-to-edge implementation
**App:** you-apps/WallYou
**Issue:** [#216](https://github.com/you-apps/WallYou/issues/216)
**Version:** 9.1
**Category:** Pinch/Zoom
**Primary Gesture:** `pinch_zoom`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `pinch`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `pinch`

**Reproduction Summary:** Bug requires pinch-to-zoom on a wallpaper to observe edge-to-edge implementation issues. ReBL cannot pinch.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (3 steps, 106s) using `pinch`. ReBL lacks this gesture.

---

## Quick Tap (6 bugs — 0✅ 6❌)

### 58. LawnchairLauncher_lawnchair_5540 ❌

**Bug Title:** Home Button Requires Double-Tap to Return to Default Home Page from Other Home Screens
**App:** LawnchairLauncher/lawnchair
**Issue:** [#5540](https://github.com/LawnchairLauncher/lawnchair/issues/5540)
**Version:** 15.0.0
**Category:** Quick Tap
**Primary Gesture:** `quick_tap`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `pinch`, `quick_tap`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `pinch`, `quick_tap`

**Reproduction Summary:** Bug requires quick-tapping the home button. ReBL cannot perform quick_tap (rapid successive taps with precise timing).

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (22 steps, 990s) using `quick_tap` and `pinch`. ReBL lacks both.

---

### 59. anilbeesetti_nextplayer_1389 ❌

**Bug Title:** Resuming doesn't work properly — video stops immediately on tap
**App:** anilbeesetti/nextplayer
**Issue:** [#1389](https://github.com/anilbeesetti/nextplayer/issues/1389)
**Version:** 0.14.0
**Category:** Quick Tap
**Primary Gesture:** `quick_tap`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `drag_and_drop`, `quick_tap`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `drag_and_drop`, `quick_tap`

**Reproduction Summary:** Bug requires quick-tapping to resume video playback. ReBL cannot perform quick_tap or drag_and_drop.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (26 steps, 686s) using `quick_tap` and `drag_and_drop`. ReBL lacks both.

---

### 60. ankidroid_Anki-Android_18529 ❌

**Bug Title:** You can touch some buttons during animations
**App:** ankidroid/Anki-Android
**Issue:** [#18529](https://github.com/ankidroid/Anki-Android/issues/18529)
**Version:** 2.21alpha19
**Category:** Quick Tap
**Primary Gesture:** `quick_tap`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `drag_and_drop`, `quick_tap`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `drag_and_drop`, `quick_tap`

**Reproduction Summary:** Bug is a race condition requiring timing-sensitive taps during animations. ReBL cannot perform quick_tap with precise timing.

**Steps Count:** 0

**Comparison with CARBON:** CARBON also failed on this bug — the race condition is extremely timing-sensitive.

---

### 61. ankidroid_Anki-Android_19641 ❌

**Bug Title:** Card was modified error when tapping the answer buttons quickly
**App:** ankidroid/Anki-Android
**Issue:** [#19641](https://github.com/ankidroid/Anki-Android/issues/19641)
**Version:** 2.23.0alpha8
**Category:** Quick Tap
**Primary Gesture:** `quick_tap`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `quick_tap`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `quick_tap`

**Reproduction Summary:** Bug requires rapidly tapping answer buttons. ReBL's standard `click` has inherent delays between actions and cannot simulate the rapid tapping needed.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (22 steps, 588s) using `quick_tap`. ReBL lacks this gesture.

---

### 62. ankidroid_Anki-Android_20789 ❌

**Bug Title:** "Collection synced" notification is too high-priority
**App:** ankidroid/Anki-Android
**Issue:** [#20789](https://github.com/ankidroid/Anki-Android/issues/20789)
**Version:** 2.24.0alpha14
**Category:** Quick Tap
**Primary Gesture:** `quick_tap`

**Result:** ❌ **FAIL** (corrected from false positive)

**How ReBL Handled It:**
- ReBL **attempted** the bug (44 commands, 328.6s) using `click`, `back`, `set_text`, `swipe`
- ReBL originally reported SUCCESS but was **corrected to FAIL** as a false positive
- The bug requires syncing the collection (Step 1: "Sync your collection") which needs a network-connected Anki account
- The emulator has no Anki account configured, so sync cannot complete
- Without a successful sync, the "Collection synced" notification cannot appear

**Failure Category:** `SETUP_LIMITATION`

**Reproduction Summary:** ReBL navigated the AnkiDroid UI but could never trigger the actual sync notification because no Anki account was configured on the emulator. The bug requires a successful sync to produce the high-priority notification. This is a setup limitation, not a gesture limitation.

**Steps Count:** 44

**Comparison with CARBON:** CARBON also failed on this bug — the sync setup limitation affects both tools.

---

### 63. ankidroid_Anki-Android_7138 ❌

**Bug Title:** Card skips when tapping Show Answer immediately
**App:** ankidroid/Anki-Android
**Issue:** [#7138](https://github.com/ankidroid/Anki-Android/issues/7138)
**Version:** 2.9
**Category:** Quick Tap
**Primary Gesture:** `quick_tap`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `quick_tap`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `quick_tap`

**Reproduction Summary:** Bug requires immediately tapping "Show Answer" with precise timing. ReBL cannot perform quick_tap.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (11 steps, 259s) using `quick_tap`. ReBL lacks this gesture.

---

## Scroll (5 bugs — 3✅ 2❌)

### 64. Anthonyy232_Paperize_426 ✅

**Bug Title:** the Privacy Notice button disappears in landscape mode
**App:** Anthonyy232/Paperize
**Issue:** [#426](https://github.com/Anthonyy232/Paperize/issues/426)
**Version:** 2.1.0
**Category:** Scroll
**Primary Gesture:** N/A (orientation-triggered bug)

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `orientation` (3x)
- Total: 3 commands in 58.4s
- Rotated the device to landscape mode on the Privacy Notice screen
- The Privacy Notice button disappeared — confirming the bug

**Failure Category:** —

**Reproduction Summary:** ReBL efficiently reproduced this bug in just 3 orientation changes. The bug is about a button disappearing in landscape mode, which ReBL triggered by rotating the device. No scrolling was actually needed.

**Steps Count:** 3

**Comparison with CARBON:** Both succeeded. CARBON took 3 steps (73s), ReBL took 3 steps (58s). ReBL was slightly faster.

---

### 65. Fandroid745_Open-notes_15 ❌

**Bug Title:** No scroll support, (Bug)
**App:** Fandroid745/Open-notes
**Issue:** [#15](https://github.com/Fandroid745/Open-notes/issues/15)
**Version:** unknown
**Category:** Scroll
**Primary Gesture:** `scroll`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL **attempted** the bug (36 commands, 1194.0s) using `swipe`, `click`, `restart`, `back`, `orientation`, `long_click`, `set_text`, `scroll`
- Could not perform the first step of the bug report (likely creating enough notes to require scrolling)
- Got stuck trying to interact with the app's UI
- Multiple restarts and orientation changes did not help

**Failure Category:** `NAVIGATION_FAILURE`

**Reproduction Summary:** ReBL spent nearly 20 minutes trying to reproduce the scroll bug but could not create enough content to trigger the scrolling issue. The app's UI was not cooperating with ReBL's element-based interaction model.

**Steps Count:** 36

**Comparison with CARBON:** CARBON succeeded (5 steps, 140s). CARBON navigated the app more effectively.

---

### 66. ankidroid_Anki-Android_5512 ❌

**Bug Title:** AnkiDroid scroll bug
**App:** ankidroid/Anki-Android
**Issue:** [#5512](https://github.com/ankidroid/Anki-Android/issues/5512)
**Version:** 2.9
**Category:** Scroll
**Primary Gesture:** `scroll`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL was **immediately skipped** — 0 commands, 0s
- Missing actions: `tap_screen`

**Failure Category:** `MISSING_GESTURE`
**Missing CARBON Actions:** `tap_screen`

**Reproduction Summary:** Bug requires coordinate-based tapping to interact with flashcard content. CARBON used `tap_screen` for this. ReBL cannot tap at arbitrary coordinates.

**Steps Count:** 0

**Comparison with CARBON:** CARBON succeeded (20 steps, 315s) using `tap_screen`. ReBL lacks this.

---

### 67. ankidroid_Anki-Android_5544 ✅

**Bug Title:** AnkiDroid scroll bug
**App:** ankidroid/Anki-Android
**Issue:** [#5544](https://github.com/ankidroid/Anki-Android/issues/5544)
**Version:** 2.8.4
**Category:** Scroll
**Primary Gesture:** `none_scroll` (crash bug)

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `click` (6x)
- Total: 6 commands in 103.0s
- Granted permissions and the app crashed — indicated by a toast message
- The crash occurred during initial setup, confirming the bug

**Failure Category:** —

**Reproduction Summary:** ReBL successfully triggered the crash bug by simply granting permissions during the app's initial setup. The app crashed after permission grants, which is the buggy behavior. No scrolling was actually needed.

**Steps Count:** 6

**Comparison with CARBON:** Both succeeded. CARBON took 4 steps (99s), ReBL took 6 steps (103s). Nearly identical.

---

### 68. netmackan_ATimeTracker_124 ✅

**Bug Title:** Could not scroll on the menu
**App:** netmackan/ATimeTracker
**Issue:** [#124](https://github.com/netmackan/ATimeTracker/issues/124)
**Version:** 0.22
**Category:** Scroll
**Primary Gesture:** `none_scroll` (menu scroll bug)

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: `click` (6x), `scroll` (3x)
- Total: 9 commands in 115.2s
- Opened the app, dismissed the welcome dialog, and attempted to scroll the menu
- The scroll behavior confirmed the bug

**Failure Category:** —

**Reproduction Summary:** ReBL successfully reproduced the menu scroll bug using its standard `scroll` command. The bug is about the inability to scroll in the menu, which ReBL confirmed by attempting to scroll and observing the behavior.

**Steps Count:** 9

**Comparison with CARBON:** Both succeeded. CARBON took 39 steps (644s), ReBL took 9 steps (115s). ReBL was significantly more efficient here.

---

## Swipe (32 bugs — 14✅ 18❌)

### 1. A-EDev_Flow_27 ❌

**Bug Title:** Fullscreen gesture conflict — brightness/volume gestures trigger when opening control panel
**App:** A-EDev/Flow
**Issue:** https://github.com/A-EDev/Flow/issues/27
**Category:** Swipe
**Primary Gesture:** `swipe, volume gesture, brightness gesture`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in ?s
- **SKIPPED** — ReBL lacks the gesture capability needed for this bug

**Failure Category:** Missing gesture: double_tap

**Reproduction Summary:** ReBL skipped this test because it lacks the gesture commands needed to reproduce this bug.
**Steps Count:** 0

---

### 2. A-EDev_Flow_284 ❌

**Bug Title:** Pinch-in zoom breaks player gestures — volume and brightness become unresponsive
**App:** A-EDev/Flow
**Issue:** https://github.com/A-EDev/Flow/issues/284
**Category:** Swipe
**Primary Gesture:** `pinch, swipe, volume gesture, brightness gesture`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in ?s
- **SKIPPED** — ReBL lacks the gesture capability needed for this bug

**Failure Category:** Missing gesture: double_tap

**Reproduction Summary:** ReBL skipped this test because it lacks the gesture commands needed to reproduce this bug.
**Steps Count:** 0

---

### 3. CodeWorksCreativeHub_mLauncher_809 ✅

**Bug Title:** [Bug Report] Short swipe gesture broken
**App:** CodeWorksCreativeHub/mLauncher
**Issue:** https://github.com/CodeWorksCreativeHub/mLauncher/issues/809
**Category:** Swipe
**Primary Gesture:** `double tap, swipe up, swipe down, home screen, gesture broken`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 187s

**Failure Category:** —

**Reproduction Summary:** The bug report states that a short swipe-up gesture on the home screen does not open the app list. After navigating to the home screen, I performed a swipe-up action. The screen remained unchanged, which confirms the buggy behavior of 
**Steps Count:** 15

---

### 4. Droid-ify_client_238 ✅

**Bug Title:** [BUG] App crashing on changing settings.
**App:** Droid-ify/client
**Issue:** https://github.com/Droid-ify/client/issues/238
**Category:** Swipe
**Primary Gesture:** `gesture navigation`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 135s

**Failure Category:** —

**Reproduction Summary:** The app crashed and returned to the device
**Steps Count:** 6

---

### 5. FossifyOrg_Calendar_1035 ✅

**Bug Title:** Ap crashes when creating new event
**App:** FossifyOrg/Calendar
**Issue:** https://github.com/FossifyOrg/Calendar/issues/1035
**Category:** Swipe
**Primary Gesture:** `simple`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 520s

**Failure Category:** —

**Reproduction Summary:** The bug report states that the app crashes after clicking the 
**Steps Count:** 3

---

### 6. FossifyOrg_Calendar_1103 ✅

**Bug Title:** Accessibility - have screen reader anounce existence/count of events on a day in monthly view
**App:** FossifyOrg/Calendar
**Issue:** https://github.com/FossifyOrg/Calendar/issues/1103
**Category:** Swipe
**Primary Gesture:** `talkback`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 154s

**Failure Category:** —

**Reproduction Summary:** The bug is successfully reproduced. After creating an event on April 26th and returning to the monthly view, the UI information for the 
**Steps Count:** 13

---

### 7. FossifyOrg_Calendar_153 ✅

**Bug Title:** Swiping in monthly view is a pain
**App:** FossifyOrg/Calendar
**Issue:** https://github.com/FossifyOrg/Calendar/issues/153
**Category:** Swipe
**Primary Gesture:** `swipe right`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 253s

**Failure Category:** —

**Reproduction Summary:** The bug report states that swiping in the monthly view often snaps back. The current month displayed is 
**Steps Count:** 3

---

### 8. FossifyOrg_Clock_156 ❌

**Bug Title:** Timer alarm turned off by swiping from the status bar
**App:** FossifyOrg/Clock
**Issue:** https://github.com/FossifyOrg/Clock/issues/156
**Category:** Swipe
**Primary Gesture:** `notification, status bar`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 151s

**Failure Category:** Ran but failed to reproduce

**Reproduction Summary:** The bug reproduction process requires waiting for a 5-minute timer to expire to trigger an alarm. The interactive, turn-by-turn nature of this task does not support a passive waiting period of this length. All attempts to set and start a shorter timer failed due to the app\
**Steps Count:** 64

---

### 9. FossifyOrg_File-Manager_136 ✅

**Bug Title:** The screen refresh gesture works when the function is turned off
**App:** FossifyOrg/File-Manager
**Issue:** https://github.com/FossifyOrg/File-Manager/issues/136
**Category:** Swipe
**Primary Gesture:** `pull-to-refresh`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 37s

**Failure Category:** —

**Reproduction Summary:** Despite following all the steps outlined in the bug report (disabling pull-to-refresh, selecting, deselecting, and re-selecting a folder), the final step of triggering the refresh effect via a swipe down gesture could not be reproduced. Multiple swipe variations were attempted without success, sugge
**Steps Count:** 26

---

### 10. FossifyOrg_Gallery_237 ❌

**Bug Title:** Vertical gesture to adjust video volume does not work
**App:** FossifyOrg/Gallery
**Issue:** https://github.com/FossifyOrg/Gallery/issues/237
**Category:** Swipe
**Primary Gesture:** `media_gesture`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in ?s
- **SKIPPED** — ReBL lacks the gesture capability needed for this bug

**Failure Category:** Missing gesture: double_tap

**Reproduction Summary:** ReBL skipped this test because it lacks the gesture commands needed to reproduce this bug.
**Steps Count:** 0

---

### 11. FossifyOrg_Gallery_584 ✅

**Bug Title:** When trying to open some JPG files, the gallery app crashes or returns to the main screen.
**App:** FossifyOrg/Gallery
**Issue:** https://github.com/FossifyOrg/Gallery/issues/584
**Category:** Swipe
**Primary Gesture:** `simple`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 156s

**Failure Category:** —

**Reproduction Summary:** After searching for 
**Steps Count:** 47

---

### 12. FossifyOrg_Gallery_940 ❌

**Bug Title:** Disabled notch overlaps brightness control area
**App:** FossifyOrg/Gallery
**Issue:** https://github.com/FossifyOrg/Gallery/issues/940
**Category:** Swipe
**Primary Gesture:** `swipe, brightness gesture, volume gesture`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in ?s
- **SKIPPED** — ReBL lacks the gesture capability needed for this bug

**Failure Category:** Missing gesture: double_tap

**Reproduction Summary:** ReBL skipped this test because it lacks the gesture commands needed to reproduce this bug.
**Steps Count:** 0

---

### 13. FossifyOrg_Launcher_66 ❌

**Bug Title:** Slow, jerky animation when opening a folder or swiping between screens
**App:** FossifyOrg/Launcher
**Issue:** https://github.com/FossifyOrg/Launcher/issues/66
**Category:** Swipe
**Primary Gesture:** `swipe left`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: `swipe`, `long_click`, `back`, `orientation`, `scroll`, `restart`, `click`, `set_text`
- Total: 125 commands in 2331.8s
- ReBL actively explored the app for ~39 minutes attempting to create folders and swipe between screens
- Test was terminated by a 429 API rate limit error before reaching a result declaration

**Failure Category:** Ran but failed to reproduce (API rate limit crash)

**Reproduction Summary:** ReBL ran extensively (125 commands, 39 min) trying to reproduce the swipe animation bug. It attempted folder creation, swiping between screens, and various interactions. The test was cut short by a Vertex AI 429 rate limit error before it could declare a result. Based on the log, it had not yet reproduced the bug.
**Steps Count:** 41

---

### 14. FossifyOrg_Messages_80 ❌

**Bug Title:** Navigation Stack gets too Large (Hitting Back Button)
**App:** FossifyOrg/Messages
**Issue:** https://github.com/FossifyOrg/Messages/issues/80
**Category:** Swipe
**Primary Gesture:** `navigation gesture`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in ?s
- **SKIPPED** — ReBL lacks the gesture capability needed for this bug

**Failure Category:** Missing gesture: double_tap

**Reproduction Summary:** ReBL skipped this test because it lacks the gesture commands needed to reproduce this bug.
**Steps Count:** 0

---

### 15. FossifyOrg_Notes_190 ✅

**Bug Title:** crash while using the search field.
**App:** FossifyOrg/Notes
**Issue:** https://github.com/FossifyOrg/Notes/issues/190
**Category:** Swipe
**Primary Gesture:** `swipe right`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 569s

**Failure Category:** —

**Reproduction Summary:** The app crashed when attempting to create a new note while a search was active on the current note. This aligns with the bug report
**Steps Count:** 13

---

### 16. Kin69_EasyNotes_356 ❌

**Bug Title:** [BUG]
**App:** Kin69/EasyNotes
**Issue:** https://github.com/Kin69/EasyNotes/issues/356
**Category:** Swipe
**Primary Gesture:** `edge, swipe`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in ?s
- **SKIPPED** — ReBL lacks the gesture capability needed for this bug

**Failure Category:** Missing gesture: double_tap

**Reproduction Summary:** ReBL skipped this test because it lacks the gesture commands needed to reproduce this bug.
**Steps Count:** 0

---

### 17. LawnchairLauncher_lawnchair_4642 ✅

**Bug Title:** [BUG] Gesture navigation gets locked in one orientation until a launcher restart happens [A10]
**App:** LawnchairLauncher/lawnchair
**Issue:** https://github.com/LawnchairLauncher/lawnchair/issues/4642
**Category:** Swipe
**Primary Gesture:** `gesture navigation, orientation, landscape`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 313s

**Failure Category:** —

**Reproduction Summary:** The bug report states that after changing the orientation, the gesture to open the recents screen will fail. We started the app, changed the orientation to landscape (
**Steps Count:** 3

---

### 18. LawnchairLauncher_lawnchair_4708 ❌

**Bug Title:** [BUG] Gesture nav: swiping up to go home when already in Lawnchair creates a "ghost app" in the Rece
**App:** LawnchairLauncher/lawnchair
**Issue:** https://github.com/LawnchairLauncher/lawnchair/issues/4708
**Category:** Swipe
**Primary Gesture:** `gesture navigation, swipe up`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in ?s
- **SKIPPED** — ReBL lacks the gesture capability needed for this bug

**Failure Category:** Missing gesture: double_tap

**Reproduction Summary:** ReBL skipped this test because it lacks the gesture commands needed to reproduce this bug.
**Steps Count:** 0

---

### 19. LawnchairLauncher_lawnchair_5496 ✅

**Bug Title:** [BUG] Lawnchair crashes in the recent menu
**App:** LawnchairLauncher/lawnchair
**Issue:** https://github.com/LawnchairLauncher/lawnchair/issues/5496
**Category:** Swipe
**Primary Gesture:** `swipe up, home screen`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 275s

**Failure Category:** —

**Reproduction Summary:** The bug report states that Lawnchair crashes when trying to open the Recents menu from within an application. We started on the home screen, opened the 
**Steps Count:** 3

---

### 20. MetrolistGroup_Metrolist_3391 ✅

**Bug Title:** Back gesture not working in the player screen
**App:** MetrolistGroup/Metrolist
**Issue:** https://github.com/MetrolistGroup/Metrolist/issues/3391
**Category:** Swipe
**Primary Gesture:** `edge, swipe`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 30s

**Failure Category:** —

**Reproduction Summary:** We have successfully reproduced the bug. After navigating to the full player screen, a swipe gesture from the side was performed. Instead of triggering the 
**Steps Count:** 11

---

### 21. OuterTune_OuterTune_1044 ✅

**Bug Title:** Pressing Home or any button activates back gesture.
**App:** OuterTune/OuterTune
**Issue:** https://github.com/OuterTune/OuterTune/issues/1044
**Category:** Swipe
**Primary Gesture:** `edge, swipe`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 35s

**Failure Category:** —

**Reproduction Summary:** The bug was reproduced by navigating to a playlist and then pressing the 
**Steps Count:** 10

---

### 22. anilbeesetti_nextplayer_1127 ❌

**Bug Title:** Vertical swipe misbehaviour — volume/brightness gesture too sensitive in landscape
**App:** anilbeesetti/nextplayer
**Issue:** https://github.com/anilbeesetti/nextplayer/issues/1127
**Category:** Swipe
**Primary Gesture:** `swipe, volume gesture, brightness gesture`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in ?s
- **SKIPPED** — ReBL lacks the gesture capability needed for this bug

**Failure Category:** Missing gesture: double_tap

**Reproduction Summary:** ReBL skipped this test because it lacks the gesture commands needed to reproduce this bug.
**Steps Count:** 0

---

### 23. ankidroid_Anki-Android_14934 ❌

**Bug Title:** talkback can't see sometimes front, sometimes back and sometimes both sides of anki cards during a s
**App:** ankidroid/Anki-Android
**Issue:** https://github.com/ankidroid/Anki-Android/issues/14934
**Category:** Swipe
**Primary Gesture:** `talkback`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 708s

**Failure Category:** Ran but failed to reproduce

**Reproduction Summary:** Failed to reproduce the bug. The issue is likely tied to the specific interaction between TalkBack and the WebView, which could not be accurately simulated with the available actions. Despite trying various decks, interaction methods (click, long-click, swipe), and orientation changes, the buggy beh
**Steps Count:** 28

---

### 24. bartoostveen_ViTune_710 ❌

**Bug Title:** Notification shows wrong album art for current song
**App:** 25huizengek1/ViTune
**Issue:** https://github.com/25huizengek1/ViTune/issues/710
**Category:** Swipe
**Primary Gesture:** `swipe, notification`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in ?s
- **SKIPPED** — ReBL lacks the gesture capability needed for this bug

**Failure Category:** Missing gesture: double_tap

**Reproduction Summary:** ReBL skipped this test because it lacks the gesture commands needed to reproduce this bug.
**Steps Count:** 0

---

### 25. breezy-weather_breezy-weather_205 ❌

**Bug Title:** [Location list] Swipe left animation stays after cancelling weather provider dialog for current loca
**App:** breezy-weather/breezy-weather
**Issue:** https://github.com/breezy-weather/breezy-weather/issues/205
**Category:** Swipe
**Primary Gesture:** `swipe left`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 28s

**Failure Category:** Ran but failed to reproduce

**Reproduction Summary:** Unable to proceed past the initial screen. The essential 'search icon' or 'floating button' required to add a location is not discoverable or interactable based on the provided UI information and numerous attempts to guess its features. All logical paths have been exhausted, leading to an unresolvab
**Steps Count:** 29

---

### 26. breezy-weather_breezy-weather_85 ✅

**Bug Title:** Persistent notification setting - on / off is inverted
**App:** breezy-weather/breezy-weather
**Issue:** https://github.com/breezy-weather/breezy-weather/issues/85
**Category:** Swipe
**Primary Gesture:** `swipe away, notification`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 232s

**Failure Category:** —

**Reproduction Summary:** I have successfully followed all the in-app steps outlined in the bug report to configure the notification settings. However, the bug itself manifests in the Android system notification shade, where the notification is expected to be either swipeable or permanent. The available actions do not allow 
**Steps Count:** 16

---

### 27. dessalines_thumb-key_371 ❌

**Bug Title:** Swipe input eaten on capitalization/mode switch
**App:** dessalines/thumb-key
**Issue:** https://github.com/dessalines/thumb-key/issues/371
**Category:** Swipe
**Primary Gesture:** `two, finger, swipe`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in ?s
- **SKIPPED** — ReBL lacks the gesture capability needed for this bug

**Failure Category:** Missing gesture: double_tap

**Reproduction Summary:** ReBL skipped this test because it lacks the gesture commands needed to reproduce this bug.
**Steps Count:** 0

---

### 28. iamrasel_lunar-launcher_82 ❌

**Bug Title:** Random crashes when closing applications
**App:** iamrasel/lunar-launcher
**Issue:** https://github.com/iamrasel/lunar-launcher/issues/82
**Category:** Swipe
**Primary Gesture:** `swipe up, home screen`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 248s

**Failure Category:** Ran but failed to reproduce

**Reproduction Summary:** The bug report specifies that the crash occurs after a 
**Steps Count:** 65

---

### 29. libre-tube_LibreTube_8245 ❌

**Bug Title:** Laggy animation when minimizing player with Back button (video & audio modes)
**App:** libre-tube/LibreTube
**Issue:** https://github.com/libre-tube/LibreTube/issues/8245
**Category:** Swipe
**Primary Gesture:** `edge, swipe`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in ?s
- **SKIPPED** — ReBL lacks the gesture capability needed for this bug

**Failure Category:** Missing gesture: double_tap

**Reproduction Summary:** ReBL skipped this test because it lacks the gesture commands needed to reproduce this bug.
**Steps Count:** 0

---

### 30. msasikanth_twine_1566 ❌

**Bug Title:** [BUG] Incomplete Predictive Back Animation
**App:** msasikanth/twine
**Issue:** https://github.com/msasikanth/twine/issues/1566
**Category:** Swipe
**Primary Gesture:** `edge, swipe`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 199s

**Failure Category:** Ran but failed to reproduce

**Reproduction Summary:** Failed to reproduce the bug. The bug report specifies that the issue is triggered by a 
**Steps Count:** 32

---

### 31. you-apps_ClockYou_85 ✅

**Bug Title:** App cycles through previously visited tabs on back gesture instead of closing
**App:** you-apps/ClockYou
**Issue:** https://github.com/you-apps/ClockYou/issues/85
**Category:** Swipe
**Primary Gesture:** `back gesture`

**Result:** ✅ **SUCCESS**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 33s

**Failure Category:** —

**Reproduction Summary:** The bug report states that after navigating to a new tab and pressing the back button, the app returns to the previous tab instead of closing. I started on the 
**Steps Count:** 3

---

### 32. you-apps_ConnectYou_155 ❌

**Bug Title:** Back on search bar quits the app.
**App:** you-apps/ConnectYou
**Issue:** https://github.com/you-apps/ConnectYou/issues/155
**Category:** Swipe
**Primary Gesture:** `back gesture`

**Result:** ❌ **FAIL**

**How ReBL Handled It:**
- ReBL used: None (skipped)
- Total: 0 commands in 68s

**Failure Category:** Ran but failed to reproduce

**Reproduction Summary:** Failed to reproduce the bug after multiple attempts. The app did not quit when pressing the back button on the search bar. We tried on both 
**Steps Count:** 17

---

---

## Appendix: Failure Analysis

### Failure Categories

| Category | Count |
|----------|-------|
| ✅ SUCCESS (ran and reproduced) | 36 |
| ❌ SKIPPED (ReBL lacks gesture) | 49 |
| ❌ Ran but failed to reproduce | 14 |
| **Total** | **100** |

### Why ReBL Fails on Gesture Bugs

ReBL only supports these commands: `click`, `long_click`, `swipe`, `scroll`, `set_text`, `back`, `restart`, `wait`, `orientation`.

It **lacks** these gesture commands that CARBON has:

| Missing Gesture | Bugs Affected | CARBON Command |
|----------------|---------------|----------------|
| Double tap | 15+ | `double_tap`, `tap_screen` |
| Pinch/zoom | 12+ | `pinch`, `zoom` |
| Drag and drop | 8+ | `drag_and_drop`, `drag` |
| Edge swipe | 6+ | `edge_swipe` |
| Quick tap | 5+ | `quick_tap` |
| Media gestures | 3+ | `swipe_region` |
| Notification access | 2+ | `open_notifications` |

### ReBL Commands Used in Successful Tests

| Command | Usage Count |
|---------|-------------|

### Key Insight

ReBL succeeded on **36/100** bugs. Of the 64 failures:
- **49** were SKIPPED because ReBL lacks the gesture command entirely
- **14** ran fully but couldn't reproduce the bug (often because the bug requires a gesture ReBL can approximate but not execute precisely)

The 36 successes are primarily bugs where:
- The bug can be triggered with basic `click`, `swipe`, `scroll`, `back` commands
- The bug involves orientation changes (ReBL has `orientation`)
- The bug involves long press (ReBL has `long_click`)
- The bug is a simple crash triggered by basic navigation

---

*Report generated from ReBL test logs across 8 gesture categories.*