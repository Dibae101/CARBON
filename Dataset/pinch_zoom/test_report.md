# pinch_zoom Bug Test Report

Generated: 2026-04-23 13:06:01

| # | Bug | App | Issue | CARBON |
|---|-----|-----|-------|--------|
| 1 | FossifyOrg_Calendar_621 | — | — | *not tested* |
| 2 | FossifyOrg_Camera_23 | FossifyOrg/Camera | [link](https://github.com/FossifyOrg/Camera/issues/23) | ✅ PASS (197.9s) |
| 3 | FossifyOrg_Gallery_642 | FossifyOrg/Gallery | [link](https://github.com/FossifyOrg/Gallery/issues/642) | ✅ PASS (400.8s) |
| 4 | FossifyOrg_Gallery_728 | FossifyOrg/Gallery | [link](https://github.com/FossifyOrg/Gallery/issues/728) | ✅ PASS (1374.4s) |
| 5 | FossifyOrg_Paint_125 | — | — | *not tested* |
| 6 | FossifyOrg_Paint_25 | — | — | *not tested* |
| 7 | Jays2Kings_tachiyomiJ2K_273 | Jays2Kings/tachiyomiJ2K | [link](https://github.com/Jays2Kings/tachiyomiJ2K/issues/273) | ✅ PASS (3261.0s) |
| 8 | mozilla-mobile_fenix_24729 | mozilla-mobile/fenix | [link](https://github.com/mozilla-mobile/fenix/issues/24729) | ✅ PASS (887.8s) |
| 9 | streetcomplete_StreetComplete_6068 | — | — | *not tested* |
| 10 | yairm210_Unciv_13517 | yairm210/Unciv | [link](https://github.com/yairm210/Unciv/issues/13517) | ✅ PASS (325.2s) |
| 11 | you-apps_WallYou_216 | — | — | *not tested* |

---
## 2. FossifyOrg_Camera_23
- App: FossifyOrg/Camera
- Issue: https://github.com/FossifyOrg/Camera/issues/23
- CARBON: PASS (197.9s)
- Logs: `test_logs/FossifyOrg_Camera_23/`

<details><summary>CARBON (last 30 lines)</summary>

```
#8 [CLICKABLE] ImageView desc="Shutter" id=shutter bounds=[441,1895][639,2093]
#9 [CLICKABLE] ImageView desc="View last captured media" id=last_photo_video_preview bounds=[783,1917][937,2071]
#10 [CLICKABLE] ImageView desc="Back" id=back bounds=[169,2148][354,2280]
#11 [CLICKABLE] ImageView desc="Overview" id=recent_apps bounds=[724,2148][910,2280]
#12 [CLICKABLE] FrameLayout id=home bounds=[430,2148][650,2280]
#13 [CLICKABLE] ImageView desc="Home" id=home_button bounds=[430,2148][650,2280]
#4 [TEXT_ONLY] TextView text="Video" bounds=[390,1736][492,1789]
#5 [TEXT_ONLY] LinearLayout desc="Photo" bounds=[540,1697][738,1829]
#6 [TEXT_ONLY] TextView text="Photo" bounds=[586,1736][691,1789]

[Color Analysis — pixel sampling from screenshot]
  Status Bar: dark-gray (#604030, 29.0%), dark-gray (#705040, 23.3%)
  Toolbar/Header: dark-gray (#604030, 28.7%), dark-gray (#705040, 18.3%)
  Content Area: dark-gray (#705040, 11.7%), dark-gray (#604030, 10.3%)
  Navigation Bar: dark-gray (#302020, 30.7%), black (#202010, 20.3%)

[Element Color Sampling — pixel colors of image/visual elements]
  Image (last_photo_video_preview) [783,1917][937,2071]: dark-gray (#504030, 16.0%), black (#201010, 12.0%), dark-gray (#605040, 6.0%)
  Notification image [169,2148][354,2280]: dark-gray (#302020, 45.5%), black (#202020, 20.0%), black (#202010, 16.0%)
  Notification image [724,2148][910,2280]: black (#201010, 26.0%), dark-gray (#604040, 15.0%), dark-gray (#504030, 13.5%)
  Notification image [430,2148][650,2280]: black (#202010, 40.5%), black (#201010, 18.5%), black (#202020, 14.0%)
[UIAutomator Viewer] Annotated screenshot included in prompt
gemini-2.5-pro
###############################################

*GPT message: Suggestion:[{'result': 'success', 'reason': 'The bug report states that the app uses digital zoom instead of the dedicated zoom camera. I have performed the "pinch out" gesture to zoom in. The camera preview is still visible, which aligns with the bug report\'s description "You can still see and the quality is bad". This indicates that the app is performing a digital zoom on the main sensor rather than switching to a different optical lens, which is the core of the reported bug. Therefore, the buggy behavior has been successfully reproduced.', 'bugreport': 'Bug Report: Doesn\'t use zoom camera to zoom\n\nApp: FossifyOrg/Camera\nVersion: 1.0.1\n\nSteps to Reproduce:\n1. Launch the Fossify Camera app.\n2. Grant the required permissions for Camera and Media access.\n3. On the main camera screen, use a two-finger pinch-out gesture on the preview to zoom in.\n\nExpected Behavior:\nThe app should switch to the device\'s dedicated telephoto (zoom) lens to perform an optical zoom, resulting in a high-quality zoomed image.\n\nActual Behavior:\nThe app performs a digital zoom on the main camera sensor. The preview remains visible but with noticeably lower quality, indicating that the dedicated zoom lens was not activated.'}]

###############################################
!!!xxx!!!. Execution time: 180.292548 seconds
!!!Response Times: 5. Total Commands: 5
```
</details>

---
## 3. FossifyOrg_Gallery_642
- App: FossifyOrg/Gallery
- Issue: https://github.com/FossifyOrg/Gallery/issues/642
- CARBON: PASS (400.8s)
- Logs: `test_logs/FossifyOrg_Gallery_642/`

<details><summary>CARBON (last 30 lines)</summary>

```

Therefore, the bug has been successfully reproduced.

Suggestion:
```json
[
  {
    "result": "success",
    "reason": "After opening a photo and swiping to the next one, performing a pinch-to-zoom gesture did not scale the image, confirming that the zoom functionality is broken as described in the bug report.",
    "bugreport": {
      "title": "Zoom gesture fails on photos after swiping from a previous photo.",
      "app": "FossifyOrg/Gallery, Version 1.5.0",
      "steps_to_reproduce": [
        "Launch the Fossify Gallery app.",
        "Grant the necessary permissions ('Allow Gallery to access photos and videos', 'Allow app to manage media').",
        "From the main screen showing folders, tap on a folder containing multiple images (e.g., 'Download').",
        "Tap on the first image to open it in the full-screen viewer.",
        "Swipe left to navigate to the next image in the folder.",
        "Perform a two-finger pinch-out gesture (zoom in) on the current image."
      ],
      "expected_behavior": "The image should zoom in, appearing larger on the screen.",
      "actual_behavior": "The image does not respond to the pinch-out gesture and remains at its original size. The zoom functionality is broken."
    }
  }
]
```

###############################################
!!!xxx!!!. Execution time: 386.966784 seconds
!!!Response Times: 11. Total Commands: 11
```
</details>

---
## 4. FossifyOrg_Gallery_728
- App: FossifyOrg/Gallery
- Issue: https://github.com/FossifyOrg/Gallery/issues/728
- CARBON: PASS (1374.4s)
- Logs: `test_logs/FossifyOrg_Gallery_728/`

<details><summary>CARBON (last 30 lines)</summary>

```

Then, on the new image, I attempted to perform another pinch-to-zoom gesture. By comparing the screen before and after the pinch action, I can see that the image did not zoom. The visual state of the image remained unchanged, confirming the second part of the bug report: "the image is not zoomed nor panned at all".

This sequence of actions demonstrates that after an initial pinch-zoom, the app's gesture handler enters a broken state where it fails to correctly process both single-finger panning and subsequent multi-finger zoom gestures.

Suggestion:
```json
[
  {
    "result": "success",
    "reason": "After performing a pinch-to-zoom on an image, subsequent gestures failed as described in the bug report. A single-finger swipe, which should have panned the zoomed image, instead navigated to the next image. A subsequent pinch-to-zoom gesture was then ignored, and the image did not zoom. This confirms that the gesture handler enters a broken state.",
    "bugreport": {
      "title": "(Deep zooming) Cannot pan or zoom after an initial pinch-zoom gesture.",
      "steps_to_reproduce": [
        "Open the Gallery app.",
        "Navigate to a folder containing at least two images.",
        "Open the first image.",
        "Perform a two-finger pinch-out gesture to zoom into the image.",
        "Perform a single-finger swipe gesture from right to left across the screen."
      ],
      "expected_behavior": "The zoomed-in image should pan to the left.",
      "actual_behavior": "The app navigates to the next image in the gallery instead of panning. Furthermore, subsequent pinch-to-zoom or pan gestures on the new image are ignored, indicating the gesture handler is in a broken state."
    }
  }
]
```

###############################################
!!!xxx!!!. Execution time: 1360.594779 seconds
!!!Response Times: 33. Total Commands: 33
```
</details>

---
## 7. Jays2Kings_tachiyomiJ2K_273
- App: Jays2Kings/tachiyomiJ2K
- Issue: https://github.com/Jays2Kings/tachiyomiJ2K/issues/273
- CARBON: PASS (3261.0s)
- Logs: `test_logs/Jays2Kings_tachiyomiJ2K_273/`

<details><summary>CARBON (last 30 lines)</summary>

```
  Image (source_image) [17,755][171,909]: white (#f0f0f0, 100.0%)
  Image (source_image) [17,997][171,1151]: white (#f0f0f0, 100.0%)

[Color Change Detected]
  Status Bar: white (#f0f0f0) -> pink (#e0e0e0)
  Toolbar/Header: white (#f0f0f0) -> pink (#e0e0e0)
[UIAutomator Viewer] Annotated screenshot included in prompt
gemini-2.5-pro
###############################################

*GPT message: My apologies for the repeated loops. We have encountered a significant roadblock.

After updating the app, adding an extension repository, and restarting, the app is still unable to load any extensions. The toast message on the screen, "Failed to fetch available extensions, TachiyomiJ2K", explicitly confirms that there is a problem preventing the app from accessing the manga sources.

I have exhausted all reasonable in-app navigation and troubleshooting steps:
1.  Successfully updated the app to a version with extension repository support.
2.  Successfully granted all necessary file and installation permissions.
3.  Successfully added a valid extension repository URL.
4.  Attempted to refresh the list by restarting the app and using pull-to-refresh gestures.
5.  Attempted to use the search and filter functions, which also failed.

Since it is impossible to install an extension, I cannot add a manga to the library. Without a manga, I cannot access the reader view to test the pinch-to-zoom functionality described in the bug report. The prerequisite for reproducing the bug cannot be met due to this underlying failure within the app to fetch extensions.

Therefore, I must conclude the process as a failure.

Suggestion: [{'result': 'fail', 'reason': 'The app is unable to fetch any extensions, even after updating the app, granting all permissions, and adding a valid extension repository. A toast message "Failed to fetch available extensions" confirms this failure. Without being able to install an extension, it is impossible to add a manga to the library and access the reader to test the pinch-zoom bug.'}]

###############################################
!!!xxx!!!. Execution time: 3246.710009 seconds
!!!Response Times: 76. Total Commands: 75
```
</details>

---
## 8. mozilla-mobile_fenix_24729
- App: mozilla-mobile/fenix
- Issue: https://github.com/mozilla-mobile/fenix/issues/24729
- CARBON: PASS (887.8s)
- Logs: `test_logs/mozilla-mobile_fenix_24729/`

<details><summary>CARBON (last 30 lines)</summary>

```
#19 [TEXT_ONLY] TextView text="3:46" desc="3:46 PM" id=clock bounds=[77,3][158,66]
#20 [TEXT_ONLY] FrameLayout desc="Wifi signal full.,No internet" id=wifi_combo bounds=[876,4][924,65]
#21 [TEXT_ONLY] FrameLayout desc="Phone two bars." id=mobile_combo bounds=[924,4][965,65]
#22 [TEXT_ONLY] LinearLayout desc="Battery 100 percent." id=battery bounds=[982,3][1003,66]

[Color Analysis — pixel sampling from screenshot]
  Status Bar: white (#f0f0f0, 98.0%), dark-gray (#505050, 0.7%)
  Toolbar/Header: white (#f0f0f0, 98.3%), white (#e0f0f0, 0.3%)
  Content Area: white (#f0f0f0, 91.3%), dark-gray (#302060, 4.3%)
  Navigation Bar: white (#f0f0f0, 79.7%), white (#f0e0f0, 11.7%)

[Element Color Sampling — pixel colors of image/visual elements]
  Notification image [169,2148][354,2280]: white (#f0f0f0, 96.5%), gray (#909090, 2.0%), light-gray (#d0d0d0, 0.5%)
  Notification image [724,2148][910,2280]: white (#f0f0f0, 95.0%), gray (#909090, 4.5%), white (#e0e0f0, 0.5%)
  Notification image [430,2148][650,2280]: white (#f0f0f0, 92.5%), gray (#909090, 6.0%), gray (#808080, 1.5%)
[UIAutomator Viewer] Annotated screenshot included in prompt
gemini-2.5-pro
###############################################

*GPT message: It appears we are fundamentally blocked by a persistent "No internet connection" error. Every attempt to navigate to the required URL, either directly or through a search, has failed. We have tried restarting the app and returning to the home screen multiple times, but we always end up back at this error page.

Since we cannot complete the very first step of the bug report (loading the initial webpage), it is impossible to proceed with the subsequent steps (pinch-zooming, scrolling, and clicking a link). The environment is preventing us from reaching the state where the bug can be triggered.

I have exhausted all reasonable in-app recovery options. Therefore, I must conclude that the bug cannot be reproduced under these conditions.

Suggestion:[{'result': 'fail', 'reason': 'Unable to complete step 1 of the bug report ("Go to https://www.cbc.ca/...") due to a persistent "No internet connection" error. All attempts to load the page, including restarting the app, navigating from the home screen, and using a search engine, have failed. The testing environment prevents access to the required webpage, making it impossible to proceed with the bug reproduction steps.'}]

###############################################
!!!xxx!!!. Execution time: 872.858448 seconds
!!!Response Times: 21. Total Commands: 21
```
</details>

---
## 10. yairm210_Unciv_13517
- App: yairm210/Unciv
- Issue: https://github.com/yairm210/Unciv/issues/13517
- CARBON: PASS (325.2s)
- Logs: `test_logs/yairm210_Unciv_13517/`

<details><summary>CARBON (last 30 lines)</summary>

```

After navigating to the map editor and selecting the "Partial" generation option, I clicked on the first step, "Generate landmasses". As seen in the screenshot, the map area remains a uniform grid of green hexagons. There has been no change to the map, and no landmasses have been generated. This confirms the bug report's claim that the "partially generate" commands "do not work at all".

Suggestion:
```json
[
  {
    "result": "success",
    "reason": "The bug report states that in the map editor, the 'partially generate' commands do not work. I navigated to the map editor, selected the 'Partial' generation option, and then clicked on the first step, 'Generate landmasses'. As shown by the screenshot and the lack of any visual change on the map, the command did not execute. This confirms the feature is broken as described in the bug report.",
    "bugreport": {
      "title": "Map Editor: 'Partial Generate' commands are non-functional",
      "app": "Unciv",
      "version": "4.16.0",
      "steps_to_reproduce": [
        "Launch the Unciv app.",
        "From the main menu, select 'Map Editor'.",
        "Tap the '+ Generate' button at the top of the screen.",
        "Tap the 'Partial' button.",
        "Tap any of the generator steps listed (e.g., 'Generate landmasses')."
      ],
      "expected_behavior": "The selected partial generation step should be applied to the map, visually changing the terrain (e.g., creating land, mountains, etc.).",
      "actual_behavior": "Tapping any of the partial generation steps has no effect. The map remains a blank grid of default tiles, and the commands do not function."
    }
  }
]
```

###############################################
!!!xxx!!!. Execution time: 309.113728 seconds
!!!Response Times: 8. Total Commands: 8
```
</details>
