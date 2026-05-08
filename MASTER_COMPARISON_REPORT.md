#  Comparison Report: CARBON vs ReBL vs ReActDroid vs AdbGPT

**Total Bugs Evaluated:** 100

## Overall Summary

| Tool | SUCCESS | FAIL | Success Rate |
|------|---------|------|--------------|
| CARBON | 92 | 8 | 92.0% |
| ReBL | 34 | 66 | 34.0% |
| ReActDroid | 5 | 95 | 5.0% |
| AdbGPT | 54 | 46 | 54.0% |

## Per-Category Breakdown

| Category | Bugs | CARBON | ReBL | ReActDroid | AdbGPT |
|----------|------|--------|------|------------|--------|
| Double Tap | 21 | 19/21 | 6/21 | 2/21 | 11/21 |
| Drag & Drop | 9 | 8/9 | 0/9 | 0/9 | 5/9 |
| Long Press | 9 | 9/9 | 6/9 | 0/9 | 3/9 |
| Orientation | 6 | 5/6 | 5/6 | 0/6 | 4/6 |
| Pinch/Zoom | 12 | 12/12 | 2/12 | 0/12 | 7/12 |
| Quick Tap | 6 | 4/6 | 0/6 | 0/6 | 4/6 |
| Scroll | 6 | 6/6 | 4/6 | 2/6 | 3/6 |
| Swipe | 31 | 29/31 | 11/31 | 1/31 | 17/31 |

## Detailed Results

### Double Tap

| Bug ID | App | CARBON | ReBL | ReActDroid | AdbGPT | Screenshot | Remarks |
|--------|-----|--------|------|------------|--------|------------|---------|
| FossifyOrg_Calendar_1035 | FossifyOrg/Calendar | ✅ | ✅ | ✅ | ✅ | ![screenshot](Dataset/double_tap/FossifyOrg_Calendar_1035%20Tested/Annotation/annotated.png) | C: The bug has been successfully reproduced; R: Reproduced with basic actions; RD: ReActDroid triggered a crash in 4 steps.; A: 4/4 steps, 4 MISSING (fake — tapped rand |
| FossifyOrg_Calendar_273 | FossifyOrg/Calendar | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/double_tap/FossifyOrg_Calendar_273%20Tested/Annotation/annotated.png) | C: I have created a new event by double-tap; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 4/4 steps, 6 MISSING (fake — tapped rand |
| FossifyOrg_Gallery_363 | FossifyOrg/Gallery | ✅ | ❌ | ✅ | ✅ | ![screenshot](Dataset/double_tap/FossifyOrg_Gallery_363%20Tested/Annotation/annotated.png) | C: After opening a .webp image, I used a pi; R: No gesture support — lacks required comm; RD: ReActDroid triggered a crash in 1 steps.; A: 4/4 steps, 8 MISSING (fake — tapped rand |
| FossifyOrg_Gallery_678 | FossifyOrg/Gallery | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/double_tap/FossifyOrg_Gallery_678%20Tested/Annotation/annotated.png) | C: After opening a small image, I was able ; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 6/6 steps, 6 MISSING (fake — tapped rand |
| FossifyOrg_Gallery_846 | FossifyOrg/Gallery | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/double_tap/FossifyOrg_Gallery_846%20Tested/Annotation/annotated.png) | C: After disabling the 'Show extended detai; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/8 steps, 20 MISSING |
| FossifyOrg_Gallery_847 | FossifyOrg/Gallery | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/double_tap/FossifyOrg_Gallery_847%20Tested/Annotation/annotated.png) | C: The bug report states that double-tappin; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 4/4 steps, 8 MISSING (fake — tapped rand |
| LawnchairLauncher_lawnchair_2910 | LawnchairLauncher/lawncha | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/double_tap/LawnchairLauncher_lawnchair_2910%20Tested/Annotation/annotated.png) | C: The bug report states that 'Double tap t; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/4 steps, 10 MISSING |
| LawnchairLauncher_lawnchair_4125 | LawnchairLauncher/lawncha | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/double_tap/LawnchairLauncher_lawnchair_4125%20Tested/Annotation/annotated.png) | C: We have navigated to the 'App info' page; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 8/8 steps, 16 MISSING (fake — tapped ran |
| LawnchairLauncher_lawnchair_4786 | LawnchairLauncher/lawncha | ❌ | ❌ | ❌ | ✅ | ![screenshot](Dataset/double_tap/LawnchairLauncher_lawnchair_4786%20Tested%20F/Annotation/annotated.png) | C: The bug is triggered by a specific TalkB; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 12/12 steps, 12 MISSING (fake — tapped r |
| Pool-Of-Tears_GreenStash_170 | Pool-Of-Tears/GreenStash | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/double_tap/Pool-Of-Tears_GreenStash_170%20Tested/Annotation/annotated.png) | C: The current 'Settings' screen confirms t; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 0/0 steps, 0 MISSING |
| TeamNewPipe_NewPipe_10750 | TeamNewPipe/NewPipe | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/double_tap/TeamNewPipe_NewPipe_10750%20Tested/Annotation/annotated.png) | C: We have successfully triggered a crash s; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/6 steps, 20 MISSING |
| TeamNewPipe_NewPipe_8338 | TeamNewPipe/NewPipe | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/double_tap/TeamNewPipe_NewPipe_8338%20Tested/Annotation/annotated.png) | C: The bug was successfully reproduced. Aft; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/4 steps, 20 MISSING |
| abdallahmehiz_mpvKt_184 | abdallahmehiz/mpvKt | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/double_tap/abdallahmehiz_mpvKt_184%20Tested/Annotation/annotated.png) | C: The bug was successfully reproduced. Aft; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 6/6 steps, 6 MISSING (fake — tapped rand |
| ankidroid_Anki-Android_17393 | ankidroid/Anki-Android | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/double_tap/ankidroid_Anki-Android_17393%20Tested/Annotation/annotated.png) | C: I followed the steps to reproduce the bu; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 0/22 steps, 20 MISSING |
| cromaguy_Rhythm_281 | cromaguy/Rhythm | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/double_tap/cromaguy_Rhythm_281%20Tested/Annotation/annotated.png) | C: On the 'Touch Gestures' screen, a single; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 1/4 steps, 11 MISSING |
| fast4x_RiMusic_1152 | fast4x/RiMusic | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/double_tap/fast4x_RiMusic_1152%20Tested/Annotation/annotated.png) | C: The bug was successfully reproduced. A s; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 4/4 steps, 4 MISSING (fake — tapped rand |
| gsantner_markor_2746 | gsantner/markor | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/double_tap/gsantner_markor_2746%20Tested/Annotation/annotated.png) | C: The bug report states that double-tappin; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/4 steps, 20 MISSING |
| openboard-team_openboard_613 | openboard-team/openboard | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/double_tap/openboard-team_openboard_613%20Tested/Annotation/annotated.png) | C: After setting the system spell checker t; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 0/2 steps, 20 MISSING |
| openboard-team_openboard_758 | openboard-team/openboard | ❌ | ❌ | ❌ | ✅ | ![screenshot](Dataset/double_tap/openboard-team_openboard_758%20Tested%20F/Annotation/annotated.png) | C: The bug report describes a failure of th; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 6/6 steps, 10 MISSING (fake — tapped ran |
| syt0r_Kanji-Dojo_291 | syt0r/Kanji-Dojo | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/double_tap/syt0r_Kanji-Dojo_291%20Tested/Annotation/annotated.png) | C: By starting a practice session, navigati; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 8/8 steps, 8 MISSING (fake — tapped rand |
| yairm210_Unciv_13517 | yairm210/Unciv | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/double_tap/yairm210_Unciv_13517%20Tested/Annotation/annotated.png) | C: The bug report states that in the map ed; R: No gesture support — lacks required comm; RD: ReActDroid encountered an error during e; A: 0/6 steps, 10 MISSING |

### Drag & Drop

| Bug ID | App | CARBON | ReBL | ReActDroid | AdbGPT | Screenshot | Remarks |
|--------|-----|--------|------|------------|--------|------------|---------|
| FossifyOrg_Launcher_304 | FossifyOrg/Launcher | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/drag_and_drop/FossifyOrg_Launcher_304%20Tested/Annotation/annotated.png) | C: Followed the steps to create an invisibl; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 8/8 steps, 8 MISSING (fake — tapped rand |
| FossifyOrg_Notes_59 | FossifyOrg/Notes | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/drag_and_drop/FossifyOrg_Notes_59%20Tested/Annotation/annotated.png) | C: Attempting to drag-and-drop an unchecked; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 14/14 steps, 22 MISSING (fake — tapped r |
| LawnchairLauncher_lawnchair_1247 | LawnchairLauncher/lawncha | ❌ | ❌ | ❌ | ❌ | ![screenshot](Dataset/drag_and_drop/LawnchairLauncher_lawnchair_1247%20Tested%20F/Annotation/annotated.png) | C: The bug report specifies a crash when us; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 1/6 steps, 11 MISSING |
| LawnchairLauncher_lawnchair_4320 | LawnchairLauncher/lawncha | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/drag_and_drop/LawnchairLauncher_lawnchair_4320%20Tested/Annotation/annotated.png) | C: Following the steps to add a widget by d; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 4/4 steps, 4 MISSING (fake — tapped rand |
| MetrolistGroup_Metrolist_3227 | MetrolistGroup/Metrolist | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/drag_and_drop/MetrolistGroup_Metrolist_3227%20Tested/Annotation/annotated.png) | C: We have successfully reproduced the bug.; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/8 steps, 20 MISSING |
| MetrolistGroup_Metrolist_3561 | MetrolistGroup/Metrolist | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/drag_and_drop/MetrolistGroup_Metrolist_3561%20Tested/Annotation/annotated.png) | C: We have successfully reproduced the bug.; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/13 steps, 20 MISSING |
| NeoApplications_Neo-Launcher_130 | NeoApplications/Neo-Launc | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/drag_and_drop/NeoApplications_Neo-Launcher_130%20Tested/Annotation/annotated.png) | C: The primary interaction for 'Cover' fold; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/20 steps, 20 MISSING (fake — tapped ra |
| breezy-weather_breezy-weather_2159 | breezy-weather/breezy-wea | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/drag_and_drop/breezy-weather_breezy-weather_2159%20Tested/Annotation/annotated.png) | C: After dragging the Breezy Weather widget; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/8 steps, 10 MISSING |
| fcitx5-android_fcitx5-android_841 | fcitx5-android/fcitx5-and | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/drag_and_drop/fcitx5-android_fcitx5-android_841%20Tested/Annotation/annotated.png) | C: The bug has been successfully reproduced; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 6/6 steps, 6 MISSING (fake — tapped rand |

### Long Press

| Bug ID | App | CARBON | ReBL | ReActDroid | AdbGPT | Screenshot | Remarks |
|--------|-----|--------|------|------------|--------|------------|---------|
| Anthonyy232_Paperize_325 | Anthonyy232/Paperize | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/long_press/Anthonyy232_Paperize_325%20Tested/Annotation/annotated.png) | C: After selecting an image from the file p; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 0/14 steps, 20 MISSING |
| Crustack_NotallyX_570 | Crustack/NotallyX | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/long_press/Crustack_NotallyX_570%20Tested/Annotation/annotated.png) | C: The bug has been successfully reproduced; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 16/16 steps, 24 MISSING (fake — tapped r |
| FossifyOrg_File-Manager_195 | FossifyOrg/File-Manager | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/long_press/FossifyOrg_File-Manager_195%20Tested/Annotation/annotated.png) | C: The steps to reproduce the bug have been; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 10/10 steps, 20 MISSING (fake — tapped r |
| FossifyOrg_Launcher_198 | FossifyOrg/Launcher | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/long_press/FossifyOrg_Launcher_198%20Tested/Annotation/annotated.png) | C: The folder rename dialog has been opened; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 0/2 steps, 10 MISSING |
| FossifyOrg_Messages_359 | FossifyOrg/Messages | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/long_press/FossifyOrg_Messages_359%20Tested/Annotation/annotated.png) | C: After following the steps to navigate to; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 0/8 steps, 20 MISSING |
| FossifyOrg_Messages_416 | FossifyOrg/Messages | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/long_press/FossifyOrg_Messages_416%20Tested/Annotation/annotated.png) | C: The bug is successfully reproduced. Afte; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 1/4 steps, 11 MISSING |
| FossifyOrg_Messages_641 | FossifyOrg/Messages | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/long_press/FossifyOrg_Messages_641%20Tested/Annotation/annotated.png) | C: We scheduled a message for a time in the; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 0/12 steps, 10 MISSING |
| breezy-weather_breezy-weather_1639 | breezy-weather/breezy-wea | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/long_press/breezy-weather_breezy-weather_1639%20Tested/Annotation/annotated.png) | C: After setting the Breezy Weather live wa; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 0/8 steps, 10 MISSING |
| espresso3389_methings_34 | espresso3389/methings | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/long_press/espresso3389_methings_34%20Tested/Annotation/annotated.png) | C: After sending a message with multiple im; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 9/9 steps, 6 MISSING (fake — tapped rand |

### Orientation

| Bug ID | App | CARBON | ReBL | ReActDroid | AdbGPT | Screenshot | Remarks |
|--------|-----|--------|------|------------|--------|------------|---------|
| FossifyOrg_Calendar_1042 | FossifyOrg/Calendar | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/orientation/FossifyOrg_Calendar_1042%20Tested/Annotation/annotated.png) | C: After navigating to the next day (April ; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 4/4 steps, 2 MISSING (fake — tapped rand |
| FossifyOrg_Camera_91 | FossifyOrg/Camera | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/orientation/FossifyOrg_Camera_91%20Tested/Annotation/annotated.png) | C: I have followed all the steps in the bug; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 0/4 steps, 10 MISSING |
| FossifyOrg_Clock_85 | FossifyOrg/Clock | ❌ | ❌ | ❌ | ✅ | ![screenshot](Dataset/orientation/FossifyOrg_Clock_85%20Tested%20F/Annotation/annotated.png) | C: Unable to trigger the full-screen alarm ; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 5/5 steps, 2 MISSING (fake — tapped rand |
| FossifyOrg_Contacts_197 | FossifyOrg/Contacts | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/orientation/FossifyOrg_Contacts_197%20Tested/Annotation/annotated.png) | C: After selecting the 'Favorites' tab and ; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 0/2 steps, 20 MISSING |
| Waboodoo_HTTP-Shortcuts_262 | Waboodoo/HTTP-Shortcuts | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/orientation/Waboodoo_HTTP-Shortcuts_262%20Tested/Annotation/annotated.png) | C: The bug is reproduced. After tapping the; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 4/4 steps, 6 MISSING (fake — tapped rand |
| ankidroid_Anki-Android_16410 | ankidroid/Anki-Android | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/orientation/ankidroid_Anki-Android_16410%20Tested/Annotation/annotated.png) | C: I successfully reproduced the bug. After; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 8/8 steps, 16 MISSING (fake — tapped ran |

### Pinch/Zoom

| Bug ID | App | CARBON | ReBL | ReActDroid | AdbGPT | Screenshot | Remarks |
|--------|-----|--------|------|------------|--------|------------|---------|
| FossifyOrg_Calendar_621 | FossifyOrg/Calendar | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/pinch_zoom/FossifyOrg_Calendar_621%20Tested/Annotation/annotated.png) | C: After following the steps to go to the w; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 6/6 steps, 4 MISSING (fake — tapped rand |
| FossifyOrg_Camera_23 | FossifyOrg/Camera | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/pinch_zoom/FossifyOrg_Camera_23%20Tested/Annotation/annotated.png) | C: The bug report states that the app uses ; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 2/2 steps, 0 MISSING |
| FossifyOrg_Gallery_289 | FossifyOrg/Gallery | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/pinch_zoom/FossifyOrg_Gallery_289%20Tested/Annotation/annotated.png) | C: The bug report states that opening an im; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 8/8 steps, 10 MISSING (fake — tapped ran |
| FossifyOrg_Gallery_642 | FossifyOrg/Gallery | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/pinch_zoom/FossifyOrg_Gallery_642%20Tested/Annotation/annotated.png) | C: After opening a photo and swiping to the; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 6/6 steps, 4 MISSING (fake — tapped rand |
| FossifyOrg_Gallery_728 | FossifyOrg/Gallery | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/pinch_zoom/FossifyOrg_Gallery_728%20Tested/Annotation/annotated.png) | C: After performing a pinch-to-zoom on an i; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 10/10 steps, 2 MISSING (fake — tapped ra |
| FossifyOrg_Paint_125 | FossifyOrg/Paint | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/pinch_zoom/FossifyOrg_Paint_125%20Tested/Annotation/annotated.png) | C: The bug has been successfully reproduced; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 3/3 steps, 1 MISSING (fake — tapped rand |
| FossifyOrg_Paint_25 | FossifyOrg/Paint | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/pinch_zoom/FossifyOrg_Paint_25%20Tested/Annotation/annotated.png) | C: I have successfully followed the steps t; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 6/6 steps, 6 MISSING (fake — tapped rand |
| ankidroid_Anki-Android_16135 | ankidroid/Anki-Android | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/pinch_zoom/ankidroid_Anki-Android_16135%20Tested/Annotation/annotated.png) | C: After opening Statistics, zooming in and; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/8 steps, 20 MISSING |
| ankidroid_Anki-Android_17667 | ankidroid/Anki-Android | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/pinch_zoom/ankidroid_Anki-Android_17667%20Tested/Annotation/annotated.png) | C: We have followed the steps to reproduce:; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: ? steps, 0 MISSING |
| saber-notes_saber_192 | saber-notes/saber | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/pinch_zoom/saber-notes_saber_192%20Tested/Annotation/annotated.png) | C: The bug is successfully reproduced. Afte; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/8 steps, 20 MISSING |
| streetcomplete_StreetComplete_6068 | streetcomplete/StreetComp | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/pinch_zoom/streetcomplete_StreetComplete_6068%20Tested/Annotation/annotated.png) | C: After zooming out on the map to select a; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 2/2 steps, 0 MISSING |
| you-apps_WallYou_216 | you-apps/WallYou | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/pinch_zoom/you-apps_WallYou_216%20Tested/Annotation/annotated.png) | C: After opening a picture and performing a; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/0 steps, 0 MISSING |

### Quick Tap

| Bug ID | App | CARBON | ReBL | ReActDroid | AdbGPT | Screenshot | Remarks |
|--------|-----|--------|------|------------|--------|------------|---------|
| LawnchairLauncher_lawnchair_5540 | LawnchairLauncher/lawncha | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/quick_tap/LawnchairLauncher_lawnchair_5540%20Tested/Annotation/annotated.png) | C: After navigating to a secondary home scr; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 6/6 steps, 4 MISSING (fake — tapped rand |
| anilbeesetti_nextplayer_1389 | anilbeesetti/nextplayer | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/quick_tap/anilbeesetti_nextplayer_1389%20Tested/Annotation/annotated.png) | C: All the steps from the bug report have b; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 8/8 steps, 14 MISSING (fake — tapped ran |
| ankidroid_Anki-Android_18529 | ankidroid/Anki-Android | ❌ | ❌ | ❌ | ❌ | ![screenshot](Dataset/quick_tap/ankidroid_Anki-Android_18529%20Tested%20F/Annotation/annotated.png) | C: The bug is a race condition that require; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/6 steps, 20 MISSING |
| ankidroid_Anki-Android_19641 | ankidroid/Anki-Android | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/quick_tap/ankidroid_Anki-Android_19641%20Tested/Annotation/annotated.png) | C: The screenshot from the last step shows ; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 4/4 steps, 6 MISSING (fake — tapped rand |
| ankidroid_Anki-Android_20789 | ankidroid/Anki-Android | ❌ | ❌ | ❌ | ✅ | ![screenshot](Dataset/quick_tap/ankidroid_Anki-Android_20789%20Tested%20F/Annotation/annotated.png) | C: The bug report requires a successful col; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 3/3 steps, 2 MISSING (fake — tapped rand |
| ankidroid_Anki-Android_7138 | ankidroid/Anki-Android | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/quick_tap/ankidroid_Anki-Android_7138%20Tested/Annotation/annotated.png) | C: After answering a card and immediately t; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/1 steps, 20 MISSING |

### Scroll

| Bug ID | App | CARBON | ReBL | ReActDroid | AdbGPT | Screenshot | Remarks |
|--------|-----|--------|------|------------|--------|------------|---------|
| Anthonyy232_Paperize_426 | Anthonyy232/Paperize | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/scroll/Anthonyy232_Paperize_426%20Tested/Annotation/annotated.png) | C: The bug report states that after rotatin; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 0/0 steps, 0 MISSING |
| Fandroid745_Open-notes_15 | Fandroid745/Open-notes | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/scroll/Fandroid745_Open-notes_15%20Tested/Annotation/annotated.png) | C: I have successfully reproduced the bug. ; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 6/6 steps, 6 MISSING (fake — tapped rand |
| FossifyOrg_File-Manager_136 | FossifyOrg/File-Manager | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/scroll/FossifyOrg_File-Manager_136%20Tested/Annotation/annotated.png) | C: After disabling ; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 0/12 steps, 10 MISSING |
| ankidroid_Anki-Android_5512 | ankidroid/Anki-Android | ✅ | ❌ | ✅ | ❌ | ![screenshot](Dataset/scroll/ankidroid_Anki-Android_5512%20Tested/Annotation/annotated.png) | C: The bug report states that when ; R: No gesture support — lacks required comm; RD: ReActDroid triggered a crash in 1 steps.; A: 0/6 steps, 20 MISSING |
| ankidroid_Anki-Android_5544 | ankidroid/Anki-Android | ✅ | ✅ | ✅ | ✅ | ![screenshot](Dataset/scroll/ankidroid_Anki-Android_5544%20Tested/Annotation/annotated.png) | C: The app crashed after granting the neces; R: Reproduced with basic actions; RD: ReActDroid triggered a crash in 1 steps.; A: 3/3 steps, 0 MISSING |
| netmackan_ATimeTracker_124 | netmackan/ATimeTracker | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/scroll/netmackan_ATimeTracker_124%20Tested/Annotation/annotated.png) | C: The application has successfully navigat; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 3/3 steps, 0 MISSING |

### Swipe

| Bug ID | App | CARBON | ReBL | ReActDroid | AdbGPT | Screenshot | Remarks |
|--------|-----|--------|------|------------|--------|------------|---------|
| A-EDev_Flow_27 | A-EDev/Flow | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/A-EDev_Flow_27%20Tested/Annotation/annotated.png) | C: I have successfully reproduced the bug. ; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/4 steps, 10 MISSING |
| A-EDev_Flow_284 | A-EDev/Flow | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/A-EDev_Flow_284%20Tested/Annotation/annotated.png) | C: After successfully navigating to a video; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 1/10 steps, 11 MISSING |
| CodeWorksCreativeHub_mLauncher_809 | CodeWorksCreativeHub/mLau | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/swipe/CodeWorksCreativeHub_mLauncher_809%20Tested/Annotation/annotated.png) | C: I have successfully reproduced the core ; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 4/4 steps, 2 MISSING (fake — tapped rand |
| Droid-ify_client_238 | Droid-ify/client | ✅ | ✅ | ✅ | ✅ | ![screenshot](Dataset/swipe/Droid-ify_client_238%20Tested/Annotation/annotated.png) | C: The steps outlined in the bug report wer; R: Reproduced with basic actions; RD: ReActDroid triggered a crash in 7 steps.; A: 6/6 steps, 12 MISSING (fake — tapped ran |
| Droid-ify_client_583 | Droid-ify/client | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/Droid-ify_client_583%20Tested/Annotation/annotated.png) | C: After navigating to the image viewer and; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 4/4 steps, 2 MISSING (fake — tapped rand |
| FossifyOrg_Calendar_1103 | FossifyOrg/Calendar | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/swipe/FossifyOrg_Calendar_1103%20Tested/Annotation/annotated.png) | C: Successfully created an event on April 2; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 0/6 steps, 20 MISSING |
| FossifyOrg_Calendar_153 | FossifyOrg/Calendar | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/swipe/FossifyOrg_Calendar_153%20Tested/Annotation/annotated.png) | C: After multiple successful full-screen sw; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 6/6 steps, 2 MISSING (fake — tapped rand |
| FossifyOrg_Clock_156 | FossifyOrg/Clock | ❌ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/FossifyOrg_Clock_156%20Tested%20F/Annotation/annotated.png) | C: Unable to set a short timer to trigger t; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 8/8 steps, 8 MISSING (fake — tapped rand |
| FossifyOrg_Gallery_237 | FossifyOrg/Gallery | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/FossifyOrg_Gallery_237%20Tested/Annotation/annotated.png) | C: The bug report states that a vertical sw; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 6/6 steps, 4 MISSING (fake — tapped rand |
| FossifyOrg_Gallery_584 | FossifyOrg/Gallery | ❌ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/FossifyOrg_Gallery_584%20Tested%20F/Annotation/image.png) | C: I have systematically explored all folde; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 0/4 steps, 20 MISSING |
| FossifyOrg_Gallery_940 | FossifyOrg/Gallery | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/FossifyOrg_Gallery_940%20Tested/Annotation/annotated.png) | C: After configuring the settings as specif; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/8 steps, 20 MISSING |
| FossifyOrg_Launcher_66 | FossifyOrg/Launcher | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/FossifyOrg_Launcher_66%20Tested/Annotation/annotated.png) | C: I have successfully followed all the ste; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 3/8 steps, 11 MISSING |
| FossifyOrg_Messages_80 | FossifyOrg/Messages | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/FossifyOrg_Messages_80%20Tested/Annotation/annotated.png) | C: After creating a new conversation from t; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/17 steps, 10 MISSING |
| FossifyOrg_Notes_190 | FossifyOrg/Notes | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/swipe/FossifyOrg_Notes_190%20Tested/Annotation/annotated.png) | C: I followed all the steps in the bug repo; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 10/10 steps, 8 MISSING (fake — tapped ra |
| Kin69_EasyNotes_356 | Kin69/EasyNotes | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/Kin69_EasyNotes_356%20Tested/Annotation/annotated.png) | C: Following the bug report; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 1/4 steps, 12 MISSING |
| LawnchairLauncher_lawnchair_4642 | LawnchairLauncher/lawncha | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/swipe/LawnchairLauncher_lawnchair_4642%20Tested/Annotation/annotated.png) | C: The bug report states that after changin; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 4/4 steps, 8 MISSING (fake — tapped rand |
| LawnchairLauncher_lawnchair_4708 | LawnchairLauncher/lawncha | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/LawnchairLauncher_lawnchair_4708%20Tested/Annotation/annotated.png) | C: After swiping up from the home screen to; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 8/8 steps, 2 MISSING (fake — tapped rand |
| LawnchairLauncher_lawnchair_5496 | LawnchairLauncher/lawncha | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/swipe/LawnchairLauncher_lawnchair_5496%20Tested/Annotation/annotated.png) | C: The bug, described as Lawnchair crashing; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 5/5 steps, 4 MISSING (fake — tapped rand |
| MetrolistGroup_Metrolist_3391 | MetrolistGroup/Metrolist | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/swipe/MetrolistGroup_Metrolist_3391%20Tested/Annotation/annotated.png) | C: The bug report states that performing a ; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 0/6 steps, 20 MISSING |
| OuterTune_OuterTune_1044 | OuterTune/OuterTune | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/swipe/OuterTune_OuterTune_1044%20Tested/Annotation/annotated.png) | C: The bug report states that when inside a; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 0/4 steps, 20 MISSING |
| anilbeesetti_nextplayer_1127 | anilbeesetti/nextplayer | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/anilbeesetti_nextplayer_1127%20Tested/Annotation/annotated.png) | C: We have confirmed that when a video is p; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 4/4 steps, 2 MISSING (fake — tapped rand |
| ankidroid_Anki-Android_14934 | ankidroid/Anki-Android | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/ankidroid_Anki-Android_14934%20Tested%20F/Annotation/annotated.png) | C: After performing a rapid sequence of 'qu; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 8/8 steps, 6 MISSING (fake — tapped rand |
| bartoostveen_ViTune_710 | 25huizengek1/ViTune | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/bartoostveen_ViTune_710%20Tested/Annotation/annotated.png) | C: After clicking 'Next track' in the notif; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 4/4 steps, 2 MISSING (fake — tapped rand |
| breezy-weather_breezy-weather_205 | breezy-weather/breezy-wea | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/breezy-weather_breezy-weather_205%20Tested/Annotation/annotated.png) | C: After adding a current location, swiping; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 6/6 steps, 4 MISSING (fake — tapped rand |
| breezy-weather_breezy-weather_85 | breezy-weather/breezy-wea | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/swipe/breezy-weather_breezy-weather_85%20Tested/Annotation/annotated.png) | C: I have followed all the steps in the bug; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 6/6 steps, 6 MISSING (fake — tapped rand |
| dessalines_thumb-key_371 | dessalines/thumb-key | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/dessalines_thumb-key_371%20Tested/Annotation/annotated.png) | C: The swipe gesture starting on a letter k; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 0/4 steps, 10 MISSING |
| iamrasel_lunar-launcher_82 | iamrasel/lunar-launcher | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/iamrasel_lunar-launcher_82%20Tested/Annotation/annotated.png) | C: The bug report states that after closing; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 2/2 steps, 0 MISSING |
| libre-tube_LibreTube_8245 | libre-tube/LibreTube | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/libre-tube_LibreTube_8245%20Tested/Annotation/annotated.png) | C: I have successfully followed the steps o; R: No gesture support — lacks required comm; RD: ReActDroid completed 30 steps without tr; A: 1/14 steps, 11 MISSING |
| msasikanth_twine_1566 | msasikanth/twine | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/msasikanth_twine_1566%20Tested/Annotation/annotated.png) | C: The steps to reproduce the bug were foll; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 0/4 steps, 20 MISSING |
| you-apps_ClockYou_85 | you-apps/ClockYou | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/swipe/you-apps_ClockYou_85%20Tested/Annotation/annotated.png) | C: After navigating from the 'Clock' tab to; R: Reproduced with basic actions; RD: ReActDroid completed 30 steps without tr; A: 4/4 steps, 4 MISSING (fake — tapped rand |
| you-apps_ConnectYou_155 | you-apps/ConnectYou | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/you-apps_ConnectYou_155%20Tested/Annotation/annotated.png) | C: After clicking the search bar, pressing ; R: Ran but could not reproduce; RD: ReActDroid completed 30 steps without tr; A: 0/4 steps, 10 MISSING |

## Issue Links

| Bug ID | Issue URL |
|--------|-----------|
| FossifyOrg_Calendar_1035 | https://github.com/FossifyOrg/Calendar/issues/1035 |
| FossifyOrg_Calendar_273 | https://github.com/FossifyOrg/Calendar/issues/273 |
| FossifyOrg_Gallery_363 | https://github.com/FossifyOrg/Gallery/issues/363 |
| FossifyOrg_Gallery_678 | https://github.com/FossifyOrg/Gallery/issues/678 |
| FossifyOrg_Gallery_846 | https://github.com/FossifyOrg/Gallery/issues/846 |
| FossifyOrg_Gallery_847 | https://github.com/FossifyOrg/Gallery/issues/847 |
| LawnchairLauncher_lawnchair_2910 | https://github.com/LawnchairLauncher/lawnchair/issues/2910 |
| LawnchairLauncher_lawnchair_4125 | https://github.com/LawnchairLauncher/lawnchair/issues/4125 |
| LawnchairLauncher_lawnchair_4786 | https://github.com/LawnchairLauncher/lawnchair/issues/4786 |
| Pool-Of-Tears_GreenStash_170 | https://github.com/Pool-Of-Tears/GreenStash/issues/170 |
| TeamNewPipe_NewPipe_10750 | https://github.com/TeamNewPipe/NewPipe/issues/10750 |
| TeamNewPipe_NewPipe_8338 | https://github.com/TeamNewPipe/NewPipe/issues/8338 |
| abdallahmehiz_mpvKt_184 | https://github.com/abdallahmehiz/mpvKt/issues/184 |
| ankidroid_Anki-Android_17393 | https://github.com/ankidroid/Anki-Android/issues/17393 |
| cromaguy_Rhythm_281 | https://github.com/cromaguy/Rhythm/issues/281 |
| fast4x_RiMusic_1152 | https://github.com/fast4x/RiMusic/issues/1152 |
| gsantner_markor_2746 | https://github.com/gsantner/markor/issues/2746 |
| openboard-team_openboard_613 | https://github.com/openboard-team/openboard/issues/613 |
| openboard-team_openboard_758 | https://github.com/openboard-team/openboard/issues/758 |
| syt0r_Kanji-Dojo_291 | https://github.com/syt0r/Kanji-Dojo/issues/291 |
| yairm210_Unciv_13517 | https://github.com/yairm210/Unciv/issues/13517 |
| FossifyOrg_Launcher_304 | https://github.com/FossifyOrg/Launcher/issues/304 |
| FossifyOrg_Notes_59 | https://github.com/FossifyOrg/Notes/issues/59 |
| LawnchairLauncher_lawnchair_1247 | https://github.com/LawnchairLauncher/lawnchair/issues/1247 |
| LawnchairLauncher_lawnchair_4320 | https://github.com/LawnchairLauncher/lawnchair/issues/4320 |
| MetrolistGroup_Metrolist_3227 | https://github.com/MetrolistGroup/Metrolist/issues/3227 |
| MetrolistGroup_Metrolist_3561 | https://github.com/MetrolistGroup/Metrolist/issues/3561 |
| NeoApplications_Neo-Launcher_130 | https://github.com/NeoApplications/Neo-Launcher/issues/130 |
| breezy-weather_breezy-weather_2159 | https://github.com/breezy-weather/breezy-weather/issues/2159 |
| fcitx5-android_fcitx5-android_841 | https://github.com/fcitx5-android/fcitx5-android/issues/841 |
| Anthonyy232_Paperize_325 | https://github.com/Anthonyy232/Paperize/issues/325 |
| Crustack_NotallyX_570 | https://github.com/Crustack/NotallyX/issues/570 |
| FossifyOrg_File-Manager_195 | https://github.com/FossifyOrg/File-Manager/issues/195 |
| FossifyOrg_Launcher_198 | https://github.com/FossifyOrg/Launcher/issues/198 |
| FossifyOrg_Messages_359 | https://github.com/FossifyOrg/Messages/issues/359 |
| FossifyOrg_Messages_416 | https://github.com/FossifyOrg/Messages/issues/416 |
| FossifyOrg_Messages_641 | https://github.com/FossifyOrg/Messages/issues/641 |
| breezy-weather_breezy-weather_1639 | https://github.com/breezy-weather/breezy-weather/issues/1639 |
| espresso3389_methings_34 | https://github.com/espresso3389/methings/issues/34 |
| FossifyOrg_Calendar_1042 | https://github.com/FossifyOrg/Calendar/issues/1042 |
| FossifyOrg_Camera_91 | https://github.com/FossifyOrg/Camera/issues/91 |
| FossifyOrg_Clock_85 | https://github.com/FossifyOrg/Clock/issues/85 |
| FossifyOrg_Contacts_197 | https://github.com/FossifyOrg/Contacts/issues/197 |
| Waboodoo_HTTP-Shortcuts_262 | https://github.com/Waboodoo/HTTP-Shortcuts/issues/262 |
| ankidroid_Anki-Android_16410 | https://github.com/ankidroid/Anki-Android/issues/16410 |
| FossifyOrg_Calendar_621 | https://github.com/FossifyOrg/Calendar/issues/621 |
| FossifyOrg_Camera_23 | https://github.com/FossifyOrg/Camera/issues/23 |
| FossifyOrg_Gallery_289 | https://github.com/FossifyOrg/Gallery/issues/289 |
| FossifyOrg_Gallery_642 | https://github.com/FossifyOrg/Gallery/issues/642 |
| FossifyOrg_Gallery_728 | https://github.com/FossifyOrg/Gallery/issues/728 |
| FossifyOrg_Paint_125 | https://github.com/FossifyOrg/Paint/issues/125 |
| FossifyOrg_Paint_25 | https://github.com/FossifyOrg/Paint/issues/25 |
| ankidroid_Anki-Android_16135 | https://github.com/ankidroid/Anki-Android/issues/16135 |
| ankidroid_Anki-Android_17667 | https://github.com/ankidroid/Anki-Android/issues/17667 |
| saber-notes_saber_192 | https://github.com/saber-notes/saber/issues/192 |
| streetcomplete_StreetComplete_6068 | https://github.com/streetcomplete/StreetComplete/issues/6068 |
| you-apps_WallYou_216 | https://github.com/you-apps/WallYou/issues/216 |
| LawnchairLauncher_lawnchair_5540 | https://github.com/LawnchairLauncher/lawnchair/issues/5540 |
| anilbeesetti_nextplayer_1389 | https://github.com/anilbeesetti/nextplayer/issues/1389 |
| ankidroid_Anki-Android_18529 | https://github.com/ankidroid/Anki-Android/issues/18529 |
| ankidroid_Anki-Android_19641 | https://github.com/ankidroid/Anki-Android/issues/19641 |
| ankidroid_Anki-Android_20789 | https://github.com/ankidroid/Anki-Android/issues/20789 |
| ankidroid_Anki-Android_7138 | https://github.com/ankidroid/Anki-Android/issues/7138 |
| Anthonyy232_Paperize_426 | https://github.com/Anthonyy232/Paperize/issues/426 |
| Fandroid745_Open-notes_15 | https://github.com/Fandroid745/Open-notes/issues/15 |
| FossifyOrg_File-Manager_136 | https://github.com/FossifyOrg/File-Manager/issues/136 |
| ankidroid_Anki-Android_5512 | https://github.com/ankidroid/Anki-Android/issues/5512 |
| ankidroid_Anki-Android_5544 | https://github.com/ankidroid/Anki-Android/issues/5544 |
| netmackan_ATimeTracker_124 | https://github.com/netmackan/ATimeTracker/issues/124 |
| A-EDev_Flow_27 | https://github.com/A-EDev/Flow/issues/27 |
| A-EDev_Flow_284 | https://github.com/A-EDev/Flow/issues/284 |
| CodeWorksCreativeHub_mLauncher_809 | https://github.com/CodeWorksCreativeHub/mLauncher/issues/809 |
| Droid-ify_client_238 | https://github.com/Droid-ify/client/issues/238 |
| Droid-ify_client_583 | https://github.com/Droid-ify/client/issues/583 |
| FossifyOrg_Calendar_1103 | https://github.com/FossifyOrg/Calendar/issues/1103 |
| FossifyOrg_Calendar_153 | https://github.com/FossifyOrg/Calendar/issues/153 |
| FossifyOrg_Clock_156 | https://github.com/FossifyOrg/Clock/issues/156 |
| FossifyOrg_Gallery_237 | https://github.com/FossifyOrg/Gallery/issues/237 |
| FossifyOrg_Gallery_584 | https://github.com/FossifyOrg/Gallery/issues/584 |
| FossifyOrg_Gallery_940 | https://github.com/FossifyOrg/Gallery/issues/940 |
| FossifyOrg_Launcher_66 | https://github.com/FossifyOrg/Launcher/issues/66 |
| FossifyOrg_Messages_80 | https://github.com/FossifyOrg/Messages/issues/80 |
| FossifyOrg_Notes_190 | https://github.com/FossifyOrg/Notes/issues/190 |
| Kin69_EasyNotes_356 | https://github.com/Kin69/EasyNotes/issues/356 |
| LawnchairLauncher_lawnchair_4642 | https://github.com/LawnchairLauncher/lawnchair/issues/4642 |
| LawnchairLauncher_lawnchair_4708 | https://github.com/LawnchairLauncher/lawnchair/issues/4708 |
| LawnchairLauncher_lawnchair_5496 | https://github.com/LawnchairLauncher/lawnchair/issues/5496 |
| MetrolistGroup_Metrolist_3391 | https://github.com/MetrolistGroup/Metrolist/issues/3391 |
| OuterTune_OuterTune_1044 | https://github.com/OuterTune/OuterTune/issues/1044 |
| anilbeesetti_nextplayer_1127 | https://github.com/anilbeesetti/nextplayer/issues/1127 |
| ankidroid_Anki-Android_14934 | https://github.com/ankidroid/Anki-Android/issues/14934 |
| bartoostveen_ViTune_710 | https://github.com/25huizengek1/ViTune/issues/710 |
| breezy-weather_breezy-weather_205 | https://github.com/breezy-weather/breezy-weather/issues/205 |
| breezy-weather_breezy-weather_85 | https://github.com/breezy-weather/breezy-weather/issues/85 |
| dessalines_thumb-key_371 | https://github.com/dessalines/thumb-key/issues/371 |
| iamrasel_lunar-launcher_82 | https://github.com/iamrasel/lunar-launcher/issues/82 |
| libre-tube_LibreTube_8245 | https://github.com/libre-tube/LibreTube/issues/8245 |
| msasikanth_twine_1566 | https://github.com/msasikanth/twine/issues/1566 |
| you-apps_ClockYou_85 | https://github.com/you-apps/ClockYou/issues/85 |
| you-apps_ConnectYou_155 | https://github.com/you-apps/ConnectYou/issues/155 |

## AdbGPT Reliability Analysis

- AdbGPT reported **54% success rate** (54/100 bugs marked as SUCCESS)
- But only **4% (4/100)** completed all steps correctly without MISSING actions
- The remaining 50 "successes" had 2-24 MISSING steps each (average ~7 MISSING per bug)
- AdbGPT has **no oracle** — it cannot verify whether the bug was actually triggered
- When AdbGPT encounters a step it cannot execute, it taps a random UI element and marks the step as `[MISSING]`, then continues to the next step regardless
- The 4 genuinely clean successes are: `FossifyOrg_Camera_23`, `ankidroid_Anki-Android_5544`, `netmackan_ATimeTracker_124`, `iamrasel_lunar-launcher_82`

## Key Observations

### Tools That Only CARBON Solved

- **FossifyOrg_Gallery_846** (Double Tap): After disabling the 'Show extended details over fullscreen media' setting, zooming into an image, and then dragging the image upwards, the image content renders underneath the top toolbar/status bar area instead of being constrained to the safe area below it. This matches the bug report's description of the image filling the whole screen, including the area under the hidden notch.
- **LawnchairLauncher_lawnchair_2910** (Double Tap): The bug report states that 'Double tap to sleep no longer works through root access.' I configured the 'Double Tap' gesture to 'Sleep' in the Lawnchair settings, returned to the homescreen, and performed a double-tap. The screen did not turn off, confirming that the feature is not working as expected. This successfully reproduces the core issue of the bug.
- **Pool-Of-Tears_GreenStash_170** (Double Tap): The current 'Settings' screen confirms the accessibility issues described in the bug report. 1) The UI hierarchy shows that each setting item is composed of multiple, separate elements (e.g., 'Default Theme' and 'System Default' are distinct), which would cause the fragmented navigation reported. 2) The back button (a NAF widget with bounds [11,88][143,220]) lacks a text or content description, confirming the second issue.
- **TeamNewPipe_NewPipe_10750** (Double Tap): We have successfully triggered a crash screen ('Error report') displaying a 'com.google.android.exoplayer2.ExoPlaybackException' caused by a 'java.net.SocketTimeoutException'. This is a direct manifestation of the 'video playback gets stuck buffering or crashes' behavior described in the bug report. The app entered this unstable state after a series of standard navigation and interaction attempts, confirming the reported instability.
- **TeamNewPipe_NewPipe_8338** (Double Tap): The bug was successfully reproduced. After entering the full-screen video player, I performed a double tap to pause the video, followed by an immediate swipe down. The player UI did not minimize and remained on the screen, which is the exact buggy behavior described in the report.
- **gsantner_markor_2746** (Double Tap): The bug report states that double-tapping a URL should select it and provide an option to open it, but this functionality is broken. We have successfully followed the reproduction steps: 1. Created a new file. 2. Pasted a URL (
- **yairm210_Unciv_13517** (Double Tap): The bug report states that in the map editor, the 'partially generate' commands do not work. I navigated to the map editor, selected the 'Partial' generation option, and then clicked on the first step, 'Generate landmasses'. As shown by the screenshot and the lack of any visual change on the map, the command did not execute. This confirms the feature is broken as described in the bug report.
- **MetrolistGroup_Metrolist_3227** (Drag & Drop): We have successfully reproduced the bug. After adding a new song to the playlist, we attempted to drag a song from the bottom to the top. Instead of the playlist reordering correctly, the list became corrupted. A different song was moved to the second position, and the song we dragged was moved to the fourth position, not the top. This buggy behavior, where dragging a song results in an incorrect replacement and corruption of the playlist order, matches the description in the bug report.
- **MetrolistGroup_Metrolist_3561** (Drag & Drop): We have successfully reproduced the bug. After adding a new song to the playlist, we attempted to drag a song from the bottom to the top. Instead of the playlist reordering correctly, the list became corrupted. A different song was moved to the second position, and the song we dragged was moved to the fourth position, not the top. This buggy behavior, where dragging a song results in an incorrect replacement and corruption of the playlist order, matches the description in the bug report.
- **breezy-weather_breezy-weather_2159** (Drag & Drop): After dragging the Breezy Weather widget to the home screen, the launcher crashed and returned to the home screen without adding the widget, which matches the behavior described in the bug report.
- **Anthonyy232_Paperize_325** (Long Press): After selecting an image from the file picker and confirming, the app returned to the album screen, but the album remained empty. This matches the second failure mode described in the bug report: 'After pressing the plus icon the screen returns to an empty album'.
- **FossifyOrg_Launcher_198** (Long Press): The folder rename dialog has been opened, and as described in the bug report, it displays dark text on a dark background, making the text difficult to read. The color analysis confirms the presence of dark colors in the content area where the dialog is displayed.
- **ankidroid_Anki-Android_16135** (Pinch/Zoom): After opening Statistics, zooming in and out, and then scrolling to the bottom of the page, a final scroll attempt resulted in a completely blank screen, confirming the 'infinite scroll' behavior described in the bug report.
- **saber-notes_saber_192** (Pinch/Zoom): The bug is successfully reproduced. After enabling finger drawing mode, zooming in, and then using a two-finger swipe to navigate the canvas, a small dot was created on the note page. This matches the bug report which states that using a two-finger gesture to navigate will leave a dot on the page, which is not the expected behavior.
- **streetcomplete_StreetComplete_6068** (Pinch/Zoom): After zooming out on the map to select a large area and then initiating a manual download by clicking 
- **you-apps_WallYou_216** (Pinch/Zoom): After opening a picture and performing a pinch-zoom action, the image content began to render underneath the system status bar. The color analysis of the status bar region confirmed that its pixels (#302020) were from the underlying image, not a standard system status bar color.
- **ankidroid_Anki-Android_7138** (Quick Tap): After answering a card and immediately tapping 'Show Answer' on the next card with delay_ms=0, the app enters an inconsistent state. The screen displays the question of the new card ('test1'), but instead of showing the 'Show Answer' button, it incorrectly displays the difficulty rating buttons. This prevents the user from viewing the answer, effectively skipping the card.
- **A-EDev_Flow_27** (Swipe): I have successfully reproduced the bug. After navigating to a fullscreen video player (the 
- **A-EDev_Flow_284** (Swipe): After successfully navigating to a video, starting playback, and performing a 
- **FossifyOrg_Gallery_940** (Swipe): After configuring the settings as specified (notch disabled, brightness gesture enabled), opening an image, and rotating to landscape, a vertical swipe on the left side of the screen failed to trigger the brightness control, which is the exact buggy behavior described in the report.
- **FossifyOrg_Launcher_66** (Swipe): I have successfully followed all the steps in the bug report. I created two home screens and a folder. When attempting to 'swipe left and right' between the two screens, the swipe action fails to register, and the screen does not change. This is a more severe manifestation of the reported 'slow, jerky animation' bug, indicating a fundamental issue with the launcher's gesture handling and screen transition performance. I also successfully created and opened a folder as described.
- **FossifyOrg_Messages_80** (Swipe): After creating a new conversation from the home screen shortcut while another conversation was in the background, pressing the back button repeatedly navigated through a bloated stack (New Conversation screen -> previous conversation -> New Conversation screen again) before finally reaching the main conversation list. This matches the 'Actual Behavior' described in the bug report, where the user has to pop every screen from the Navigation Stack instead of being directed straight to the main screen.
- **Kin69_EasyNotes_356** (Swipe): Following the bug report
- **dessalines_thumb-key_371** (Swipe): The swipe gesture starting on a letter key and ending on the capitalize key resulted in the input being ignored, which matches the bug report\
- **libre-tube_LibreTube_8245** (Swipe): I have successfully followed the steps outlined in the bug report to trigger the specified buggy behavior. I initiated playback in both video and audio modes and, in each case, minimized the player using the system\
- **msasikanth_twine_1566** (Swipe): The steps to reproduce the bug were followed: a post was opened, and then a back action was performed to close it. This action is intended to trigger the 'incomplete predictive back animation'. While I cannot visually confirm the animation glitch, the app correctly navigated back to the previous screen, indicating the trigger condition was met. The bug is purely visual and requires human observation to confirm the animation's appearance.
- **you-apps_ConnectYou_155** (Swipe): After clicking the search bar, pressing the back button twice caused the application to close and return to the home screen. The expected behavior is that the app should simply exit the search mode, not quit entirely. The current screen is the device

### Bugs All Tools Failed

- **LawnchairLauncher_lawnchair_1247** (Drag & Drop)
- **ankidroid_Anki-Android_18529** (Quick Tap)
- **FossifyOrg_Gallery_584** (Swipe)

### False Positives (FP_BUGS)

These bugs are known false positives where tools may report SUCCESS incorrectly:

- FossifyOrg_Gallery_584
- LawnchairLauncher_lawnchair_1247
- ankidroid_Anki-Android_20789
- openboard-team_openboard_758

---
*Generated automatically from Dataset/ logs*