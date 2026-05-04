# CARBON

**Contextual Automated Reproduction of Bugs On Android**

CARBON is an LLM-driven system for automatically reproducing Android bug reports. It connects to an Android emulator, captures annotated screenshots with color-coded bounding boxes, and uses Gemini 2.5 Pro to iteratively follow bug reproduction steps — including complex gestures like pinch-to-zoom, double-tap, edge swipes, and coordinate-based interactions that previous tools could not handle.


#  Evaluation: CARBON vs ReBL vs ReActDroid vs AdbGPT

> **Dataset:** 100 gesture-related Android bugs | **13 crash, 87 non-crash** | **8 categories**
> **LLM:** Gemini 2.5 Pro via Vertex AI (same for all tools)
> **Device:** Android 13 emulator (Pixel 4)

---

## Overall Results

| Tool | Venue | Success | Fail | Rate | Oracle |
|------|-------|---------|------|------|--------|
| **CARBON** | — | 92 | 8 | **92%** | Crash + Visual/LLM |
| **AdbGPT** | ICSE 2024 | 54 | 46 | **54%*** | None (step completion) |
| **ReBL** | ISSTA 2024 | 32 | 68 | **32%** | Crash + LLM |
| **ReActDroid** | TSE 2025 | 5 | 95 | **5%** | Crash only |

*AdbGPT has no oracle — SUCCESS means step completion only, not bug verification.*

---

## Results by Category

| Category | Bugs | CARBON | ReBL | ReActDroid | AdbGPT* |
|----------|------|--------|------|-----------|---------|
| Double Tap | 19 | 17/19 (89%) | 3/19 (16%) | 1/19 (5%) | 10/19 (53%) |
| Drag & Drop | 9 | 8/9 (89%) | 0/9 (0%) | 0/9 (0%) | 5/9 (56%) |
| Long Press | 9 | 9/9 (100%) | 6/9 (67%) | 0/9 (0%) | 3/9 (33%) |
| Orientation | 6 | 5/6 (83%) | 5/6 (83%) | 0/6 (0%) | 4/6 (67%) |
| Pinch/Zoom | 14 | 14/14 (100%) | 2/14 (14%) | 0/14 (0%) | 8/14 (57%) |
| Quick Tap | 6 | 4/6 (67%) | 0/6 (0%) | 0/6 (0%) | 4/6 (67%) |
| Scroll | 5 | 5/5 (100%) | 3/5 (60%) | 2/5 (40%) | 3/5 (60%) |
| Swipe | 32 | 30/32 (94%) | 13/32 (41%) | 2/32 (6%) | 17/32 (53%) |
| **Total** | **100** | **92%** | **32%** | **5%** | **54%*** |

---

## Crash vs Non-Crash Bug Performance

| Bug Type | Total | CARBON | ReBL | ReActDroid | AdbGPT* |
|----------|-------|--------|------|-----------|---------|
| 💥 Crash | 13 | 10/13 (77%) | 4/13 (31%) | 2/13 (15%) | 8/13 (62%) |
| 🐛 Non-Crash | 87 | 82/87 (94%) | 28/87 (32%) | 3/87 (3%) | 46/87 (53%) |

---

## All 100 Bugs — Per-Bug Comparison

| # | Category | Bug | App | Issue | Type | CARBON | ReBL | ReActDroid | AdbGPT* |
|---|----------|-----|-----|-------|------|--------|------|-----------|---------|
| 1 | Double Tap | LawnchairLauncher_lawnchair_4786 | LawnchairLauncher/lawnchair | [Link](https://github.com/LawnchairLauncher/lawnchair/issues/4786) | � | ❌ | ❌ | ❌ | ✅ |
| 2 | Double Tap | FossifyOrg_Gallery_363 | FossifyOrg/Gallery | [Link](https://github.com/FossifyOrg/Gallery/issues/363) | 🐛 | ✅ | ❌ | ✅ | ✅ |
| 3 | Double Tap | FossifyOrg_Gallery_678 | FossifyOrg/Gallery | [Link](https://github.com/FossifyOrg/Gallery/issues/678) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 4 | Double Tap | FossifyOrg_Gallery_846 | FossifyOrg/Gallery | [Link](https://github.com/FossifyOrg/Gallery/issues/846) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 5 | Double Tap | FossifyOrg_Gallery_847 | FossifyOrg/Gallery | [Link](https://github.com/FossifyOrg/Gallery/issues/847) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 6 | Double Tap | LawnchairLauncher_lawnchair_2910 | LawnchairLauncher/lawnchair | [Link](https://github.com/LawnchairLauncher/lawnchair/issues/2910) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 7 | Double Tap | LawnchairLauncher_lawnchair_4125 | LawnchairLauncher/lawnchair | [Link](https://github.com/LawnchairLauncher/lawnchair/issues/4125) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 8 | Double Tap | FossifyOrg_Calendar_273 | FossifyOrg/Calendar | [Link](https://github.com/FossifyOrg/Calendar/issues/273) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 9 | Double Tap | Pool-Of-Tears_GreenStash_170 | Pool-Of-Tears/GreenStash | [Link](https://github.com/Pool-Of-Tears/GreenStash/issues/170) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 10 | Double Tap | TeamNewPipe_NewPipe_10750 | TeamNewPipe/NewPipe | [Link](https://github.com/TeamNewPipe/NewPipe/issues/10750) | 💥 | ✅ | ❌ | ❌ | ❌ |
| 11 | Double Tap | TeamNewPipe_NewPipe_8338 | TeamNewPipe/NewPipe | [Link](https://github.com/TeamNewPipe/NewPipe/issues/8338) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 12 | Double Tap | abdallahmehiz_mpvKt_184 | abdallahmehiz/mpvKt | [Link](https://github.com/abdallahmehiz/mpvKt/issues/184) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 13 | Double Tap | ankidroid_Anki-Android_17393 | ankidroid/Anki-Android | [Link](https://github.com/ankidroid/Anki-Android/issues/17393) | 🐛 | ✅ | ✅ | ❌ | ❌ |
| 14 | Double Tap | cromaguy_Rhythm_281 | cromaguy/Rhythm | [Link](https://github.com/cromaguy/Rhythm/issues/281) | 🐛 | ✅ | ✅ | ❌ | ❌ |
| 15 | Double Tap | fast4x_RiMusic_1152 | fast4x/RiMusic | [Link](https://github.com/fast4x/RiMusic/issues/1152) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 16 | Double Tap | gsantner_markor_2746 | gsantner/markor | [Link](https://github.com/gsantner/markor/issues/2746) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 17 | Double Tap | openboard-team_openboard_613 | openboard-team/openboard | [Link](https://github.com/openboard-team/openboard/issues/613) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 18 | Double Tap | openboard-team_openboard_758 | openboard-team/openboard | [Link](https://github.com/openboard-team/openboard/issues/758) | 🐛 | ❌ | ❌ | ❌ | ✅ |
| 19 | Double Tap | syt0r_Kanji-Dojo_291 | syt0r/Kanji-Dojo | [Link](https://github.com/syt0r/Kanji-Dojo/issues/291) | 🐛 | ✅ | ✅ | ❌ | ✅ |
| 20 | Drag & Drop | FossifyOrg_Launcher_304 | FossifyOrg/Launcher | [Link](https://github.com/FossifyOrg/Launcher/issues/304) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 21 | Drag & Drop | FossifyOrg_Notes_59 | FossifyOrg/Notes | [Link](https://github.com/FossifyOrg/Notes/issues/59) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 22 | Drag & Drop | LawnchairLauncher_lawnchair_1247 | LawnchairLauncher/lawnchair | [Link](https://github.com/LawnchairLauncher/lawnchair/issues/1247) | 💥 | ❌ | ❌ | ❌ | ❌ |
| 23 | Drag & Drop | LawnchairLauncher_lawnchair_4320 | LawnchairLauncher/lawnchair | [Link](https://github.com/LawnchairLauncher/lawnchair/issues/4320) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 24 | Drag & Drop | MetrolistGroup_Metrolist_3227 | MetrolistGroup/Metrolist | [Link](https://github.com/MetrolistGroup/Metrolist/issues/3227) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 25 | Drag & Drop | MetrolistGroup_Metrolist_3561 | MetrolistGroup/Metrolist | [Link](https://github.com/MetrolistGroup/Metrolist/issues/3561) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 26 | Drag & Drop | NeoApplications_Neo-Launcher_130 | NeoApplications/Neo-Launcher | [Link](https://github.com/NeoApplications/Neo-Launcher/issues/130) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 27 | Drag & Drop | breezy-weather_breezy-weather_2159 | breezy-weather/breezy-weather | [Link](https://github.com/breezy-weather/breezy-weather/issues/2159) | 💥 | ✅ | ❌ | ❌ | ❌ |
| 28 | Drag & Drop | fcitx5-android_fcitx5-android_841 | fcitx5-android/fcitx5-android | [Link](https://github.com/fcitx5-android/fcitx5-android/issues/841) | 💥 | ✅ | ❌ | ❌ | ✅ |
| 29 | Long Press | Anthonyy232_Paperize_325 | Anthonyy232/Paperize | [Link](https://github.com/Anthonyy232/Paperize/issues/325) | 💥 | ✅ | ❌ | ❌ | ❌ |
| 30 | Long Press | Crustack_NotallyX_570 | Crustack/NotallyX | [Link](https://github.com/Crustack/NotallyX/issues/570) | 💥 | ✅ | ❌ | ❌ | ✅ |
| 31 | Long Press | FossifyOrg_File-Manager_195 | FossifyOrg/File-Manager | [Link](https://github.com/FossifyOrg/File-Manager/issues/195) | 🐛 | ✅ | ✅ | ❌ | ✅ |
| 32 | Long Press | FossifyOrg_Launcher_198 | FossifyOrg/Launcher | [Link](https://github.com/FossifyOrg/Launcher/issues/198) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 33 | Long Press | FossifyOrg_Messages_359 | FossifyOrg/Messages | [Link](https://github.com/FossifyOrg/Messages/issues/359) | 🐛 | ✅ | ✅ | ❌ | ❌ |
| 34 | Long Press | FossifyOrg_Messages_416 | FossifyOrg/Messages | [Link](https://github.com/FossifyOrg/Messages/issues/416) | 🐛 | ✅ | ✅ | ❌ | ❌ |
| 35 | Long Press | FossifyOrg_Messages_641 | FossifyOrg/Messages | [Link](https://github.com/FossifyOrg/Messages/issues/641) | 🐛 | ✅ | ✅ | ❌ | ❌ |
| 36 | Long Press | breezy-weather_breezy-weather_1639 | breezy-weather/breezy-weather | [Link](https://github.com/breezy-weather/breezy-weather/issues/1639) | 🐛 | ✅ | ✅ | ❌ | ❌ |
| 37 | Long Press | espresso3389_methings_34 | espresso3389/methings | [Link](https://github.com/espresso3389/methings/issues/34) | 🐛 | ✅ | ✅ | ❌ | ✅ |
| 38 | Orientation | FossifyOrg_Calendar_1042 | FossifyOrg/Calendar | [Link](https://github.com/FossifyOrg/Calendar/issues/1042) | 🐛 | ✅ | ✅ | ❌ | ✅ |
| 39 | Orientation | FossifyOrg_Camera_91 | FossifyOrg/Camera | [Link](https://github.com/FossifyOrg/Camera/issues/91) | 🐛 | ✅ | ✅ | ❌ | ❌ |
| 40 | Orientation | FossifyOrg_Clock_85 | FossifyOrg/Clock | [Link](https://github.com/FossifyOrg/Clock/issues/85) | 🐛 | ❌ | ❌ | ❌ | ✅ |
| 41 | Orientation | FossifyOrg_Contacts_197 | FossifyOrg/Contacts | [Link](https://github.com/FossifyOrg/Contacts/issues/197) | 🐛 | ✅ | ✅ | ❌ | ❌ |
| 42 | Orientation | Waboodoo_HTTP-Shortcuts_262 | Waboodoo/HTTP-Shortcuts | [Link](https://github.com/Waboodoo/HTTP-Shortcuts/issues/262) | 🐛 | ✅ | ✅ | ❌ | ✅ |
| 43 | Orientation | ankidroid_Anki-Android_16410 | ankidroid/Anki-Android | [Link](https://github.com/ankidroid/Anki-Android/issues/16410) | 🐛 | ✅ | ✅ | ❌ | ✅ |
| 44 | Pinch/Zoom | Droid-ify_client_583 | Droid-ify/client | [Link](https://github.com/Droid-ify/client/issues/583) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 45 | Pinch/Zoom | FossifyOrg_Calendar_621 | FossifyOrg/Calendar | [Link](https://github.com/FossifyOrg/Calendar/issues/621) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 46 | Pinch/Zoom | FossifyOrg_Camera_23 | FossifyOrg/Camera | [Link](https://github.com/FossifyOrg/Camera/issues/23) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 47 | Pinch/Zoom | FossifyOrg_Gallery_289 | FossifyOrg/Gallery | [Link](https://github.com/FossifyOrg/Gallery/issues/289) | 🐛 | ✅ | ✅ | ❌ | ✅ |
| 48 | Pinch/Zoom | FossifyOrg_Gallery_642 | FossifyOrg/Gallery | [Link](https://github.com/FossifyOrg/Gallery/issues/642) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 49 | Pinch/Zoom | FossifyOrg_Gallery_728 | FossifyOrg/Gallery | [Link](https://github.com/FossifyOrg/Gallery/issues/728) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 50 | Pinch/Zoom | FossifyOrg_Paint_125 | FossifyOrg/Paint | [Link](https://github.com/FossifyOrg/Paint/issues/125) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 51 | Pinch/Zoom | FossifyOrg_Paint_25 | FossifyOrg/Paint | [Link](https://github.com/FossifyOrg/Paint/issues/25) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 52 | Pinch/Zoom | ankidroid_Anki-Android_16135 | ankidroid/Anki-Android | [Link](https://github.com/ankidroid/Anki-Android/issues/16135) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 53 | Pinch/Zoom | ankidroid_Anki-Android_17667 | ankidroid/Anki-Android | [Link](https://github.com/ankidroid/Anki-Android/issues/17667) | 🐛 | ✅ | ✅ | ❌ | ❌ |
| 54 | Pinch/Zoom | saber-notes_saber_192 | saber-notes/saber | [Link](https://github.com/saber-notes/saber/issues/192) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 55 | Pinch/Zoom | streetcomplete_StreetComplete_6068 | streetcomplete/StreetComplete | [Link](https://github.com/streetcomplete/StreetComplete/issues/6068) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 56 | Pinch/Zoom | yairm210_Unciv_13517 | yairm210/Unciv | [Link](https://github.com/yairm210/Unciv/issues/13517) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 57 | Pinch/Zoom | you-apps_WallYou_216 | you-apps/WallYou | [Link](https://github.com/you-apps/WallYou/issues/216) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 58 | Quick Tap | LawnchairLauncher_lawnchair_5540 | LawnchairLauncher/lawnchair | [Link](https://github.com/LawnchairLauncher/lawnchair/issues/5540) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 59 | Quick Tap | anilbeesetti_nextplayer_1389 | anilbeesetti/nextplayer | [Link](https://github.com/anilbeesetti/nextplayer/issues/1389) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 60 | Quick Tap | ankidroid_Anki-Android_18529 | ankidroid/Anki-Android | [Link](https://github.com/ankidroid/Anki-Android/issues/18529) | 🐛 | ❌ | ❌ | ❌ | ❌ |
| 61 | Quick Tap | ankidroid_Anki-Android_19641 | ankidroid/Anki-Android | [Link](https://github.com/ankidroid/Anki-Android/issues/19641) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 62 | Quick Tap | ankidroid_Anki-Android_20789 | ankidroid/Anki-Android | [Link](https://github.com/ankidroid/Anki-Android/issues/20789) | 🐛 | ❌ | ❌ | ❌ | ✅ |
| 63 | Quick Tap | ankidroid_Anki-Android_7138 | ankidroid/Anki-Android | [Link](https://github.com/ankidroid/Anki-Android/issues/7138) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 64 | Scroll | Anthonyy232_Paperize_426 | Anthonyy232/Paperize | [Link](https://github.com/Anthonyy232/Paperize/issues/426) | 🐛 | ✅ | ✅ | ❌ | ❌ |
| 65 | Scroll | Fandroid745_Open-notes_15 | Fandroid745/Open-notes | [Link](https://github.com/Fandroid745/Open-notes/issues/15) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 66 | Scroll | ankidroid_Anki-Android_5512 | ankidroid/Anki-Android | [Link](https://github.com/ankidroid/Anki-Android/issues/5512) | 🐛 | ✅ | ❌ | ✅ | ❌ |
| 67 | Scroll | ankidroid_Anki-Android_5544 | ankidroid/Anki-Android | [Link](https://github.com/ankidroid/Anki-Android/issues/5544) | 🐛 | ✅ | ✅ | ✅ | ✅ |
| 68 | Scroll | netmackan_ATimeTracker_124 | netmackan/ATimeTracker | [Link](https://github.com/netmackan/ATimeTracker/issues/124) | 🐛 | ✅ | ✅ | ❌ | ✅ |
| 69 | Swipe | A-EDev_Flow_27 | A-EDev/Flow | [Link](https://github.com/A-EDev/Flow/issues/27) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 70 | Swipe | A-EDev_Flow_284 | A-EDev/Flow | [Link](https://github.com/A-EDev/Flow/issues/284) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 71 | Swipe | CodeWorksCreativeHub_mLauncher_809 | CodeWorksCreativeHub/mLauncher | [Link](https://github.com/CodeWorksCreativeHub/mLauncher/issues/809) | 🐛 | ✅ | ✅ | ❌ | ✅ |
| 72 | Swipe | Droid-ify_client_238 | Droid-ify/client | [Link](https://github.com/Droid-ify/client/issues/238) | 💥 | ✅ | ✅ | ✅ | ✅ |
| 73 | Swipe | FossifyOrg_Calendar_1035 | FossifyOrg/Calendar | [Link](https://github.com/FossifyOrg/Calendar/issues/1035) | 💥 | ✅ | ✅ | ✅ | ✅ |
| 74 | Swipe | FossifyOrg_Calendar_1103 | FossifyOrg/Calendar | [Link](https://github.com/FossifyOrg/Calendar/issues/1103) | 🐛 | ✅ | ✅ | ❌ | ❌ |
| 75 | Swipe | FossifyOrg_Calendar_153 | FossifyOrg/Calendar | [Link](https://github.com/FossifyOrg/Calendar/issues/153) | 🐛 | ✅ | ✅ | ❌ | ✅ |
| 76 | Swipe | FossifyOrg_Clock_156 | FossifyOrg/Clock | [Link](https://github.com/FossifyOrg/Clock/issues/156) | 🐛 | ❌ | ❌ | ❌ | ✅ |
| 77 | Swipe | FossifyOrg_File-Manager_136 | FossifyOrg/File-Manager | [Link](https://github.com/FossifyOrg/File-Manager/issues/136) | 🐛 | ✅ | ✅ | ❌ | ❌ |
| 78 | Swipe | FossifyOrg_Gallery_237 | FossifyOrg/Gallery | [Link](https://github.com/FossifyOrg/Gallery/issues/237) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 79 | Swipe | FossifyOrg_Gallery_584 | FossifyOrg/Gallery | [Link](https://github.com/FossifyOrg/Gallery/issues/584) | 💥 | ❌ | ❌ | ❌ | ❌ |
| 80 | Swipe | FossifyOrg_Gallery_940 | FossifyOrg/Gallery | [Link](https://github.com/FossifyOrg/Gallery/issues/940) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 81 | Swipe | FossifyOrg_Launcher_66 | FossifyOrg/Launcher | [Link](https://github.com/FossifyOrg/Launcher/issues/66) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 82 | Swipe | FossifyOrg_Messages_80 | FossifyOrg/Messages | [Link](https://github.com/FossifyOrg/Messages/issues/80) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 83 | Swipe | FossifyOrg_Notes_190 | FossifyOrg/Notes | [Link](https://github.com/FossifyOrg/Notes/issues/190) | 💥 | ✅ | ✅ | ❌ | ✅ |
| 84 | Swipe | Kin69_EasyNotes_356 | Kin69/EasyNotes | [Link](https://github.com/Kin69/EasyNotes/issues/356) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 85 | Swipe | LawnchairLauncher_lawnchair_4642 | LawnchairLauncher/lawnchair | [Link](https://github.com/LawnchairLauncher/lawnchair/issues/4642) | 🐛 | ✅ | ✅ | ❌ | ✅ |
| 86 | Swipe | LawnchairLauncher_lawnchair_4708 | LawnchairLauncher/lawnchair | [Link](https://github.com/LawnchairLauncher/lawnchair/issues/4708) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 87 | Swipe | LawnchairLauncher_lawnchair_5496 | LawnchairLauncher/lawnchair | [Link](https://github.com/LawnchairLauncher/lawnchair/issues/5496) | 💥 | ✅ | ✅ | ❌ | ✅ |
| 88 | Swipe | MetrolistGroup_Metrolist_3391 | MetrolistGroup/Metrolist | [Link](https://github.com/MetrolistGroup/Metrolist/issues/3391) | 🐛 | ✅ | ✅ | ❌ | ❌ |
| 89 | Swipe | OuterTune_OuterTune_1044 | OuterTune/OuterTune | [Link](https://github.com/OuterTune/OuterTune/issues/1044) | 🐛 | ✅ | ✅ | ❌ | ❌ |
| 90 | Swipe | anilbeesetti_nextplayer_1127 | anilbeesetti/nextplayer | [Link](https://github.com/anilbeesetti/nextplayer/issues/1127) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 91 | Swipe | ankidroid_Anki-Android_14934 | ankidroid/Anki-Android | [Link](https://github.com/ankidroid/Anki-Android/issues/14934) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 92 | Swipe | bartoostveen_ViTune_710 | 25huizengek1/ViTune | [Link](https://github.com/25huizengek1/ViTune/issues/710) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 93 | Swipe | breezy-weather_breezy-weather_205 | breezy-weather/breezy-weather | [Link](https://github.com/breezy-weather/breezy-weather/issues/205) | 🐛 | ✅ | ❌ | ❌ | ✅ |
| 94 | Swipe | breezy-weather_breezy-weather_85 | breezy-weather/breezy-weather | [Link](https://github.com/breezy-weather/breezy-weather/issues/85) | 🐛 | ✅ | ✅ | ❌ | ✅ |
| 95 | Swipe | dessalines_thumb-key_371 | dessalines/thumb-key | [Link](https://github.com/dessalines/thumb-key/issues/371) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 96 | Swipe | iamrasel_lunar-launcher_82 | iamrasel/lunar-launcher | [Link](https://github.com/iamrasel/lunar-launcher/issues/82) | 💥 | ✅ | ❌ | ❌ | ✅ |
| 97 | Swipe | libre-tube_LibreTube_8245 | libre-tube/LibreTube | [Link](https://github.com/libre-tube/LibreTube/issues/8245) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 98 | Swipe | msasikanth_twine_1566 | msasikanth/twine | [Link](https://github.com/msasikanth/twine/issues/1566) | 🐛 | ✅ | ❌ | ❌ | ❌ |
| 99 | Swipe | you-apps_ClockYou_85 | you-apps/ClockYou | [Link](https://github.com/you-apps/ClockYou/issues/85) | 🐛 | ✅ | ✅ | ❌ | ✅ |
| 100 | Swipe | you-apps_ConnectYou_155 | you-apps/ConnectYou | [Link](https://github.com/you-apps/ConnectYou/issues/155) | 🐛 | ✅ | ❌ | ❌ | ❌ |

*Legend: ✅ Success, ❌ Fail, — Not tested, 💥 Crash, 🐛 Non-Crash*
*\*AdbGPT: no oracle — success = step completion only*

---
*Report generated from verified test logs.*