# Cross-Tool Performance: Crash vs Non-Crash Bug Analysis

---

## Summary

| Bug Type | Total | CARBON ✅ | CARBON Rate |
|----------|-------|-----------|-------------|
| 💥 Crash Bugs | 13 | 10 | 77% |
| 🐛 Non-Crash Bugs | 87 | 82 | 94% |
| **Total** | **100** | **92** | **92%** |

## Cross-Tool Comparison: Crash vs Non-Crash

| Tool | Crash Bugs (13) | Non-Crash Bugs (87) | Total | Oracle |
|------|----------------|--------------------|-----------| ------------|
| **CARBON** | 10/13 (77%) | 82/87 (94%) | 92/100 (92%) | Crash + Visual/LLM |
| **AdbGPT** | 8/13 (62%) | 46/87 (53%) | 54/100 (54%) | Step completion only |
| **ReBL** | 4/13 (31%) | 28/87 (32%) | 32/100 (32%) | Crash + LLM |
| **ReActDroid** | 2/13 (15%) | 3/87 (3%) | 5/100 (5%) | Crash only |

---

## 💥 Crash Bugs (13 total)

| # | Category | Bug | App | CARBON | AdbGPT | ReBL | ReActDroid |
|---|----------|-----|-----|--------|--------|------|------------|
| 1 | double_tap | LawnchairLauncher_lawnchair_4786 | LawnchairLauncher/lawnchair | ❌ | ✅ | ❌ | ❌ |
| 2 | double_tap | TeamNewPipe_NewPipe_10750 | TeamNewPipe/NewPipe | ✅ | ❌ | ❌ | ❌ |
| 3 | drag_and_drop | LawnchairLauncher_lawnchair_1247 | LawnchairLauncher/lawnchair | ❌ | ❌ | ❌ | ❌ |
| 4 | drag_and_drop | breezy-weather_breezy-weather_2159 | breezy-weather/breezy-weather | ✅ | ❌ | ❌ | ❌ |
| 5 | drag_and_drop | fcitx5-android_fcitx5-android_841 | fcitx5-android/fcitx5-android | ✅ | ✅ | ❌ | ❌ |
| 6 | long_press | Anthonyy232_Paperize_325 | Anthonyy232/Paperize | ✅ | ❌ | ❌ | ❌ |
| 7 | long_press | Crustack_NotallyX_570 | Crustack/NotallyX | ✅ | ✅ | ❌ | ❌ |
| 8 | swipe | Droid-ify_client_238 | Droid-ify/client | ✅ | ✅ | ✅ | ✅ |
| 9 | swipe | FossifyOrg_Calendar_1035 | FossifyOrg/Calendar | ✅ | ✅ | ✅ | ✅ |
| 10 | swipe | FossifyOrg_Gallery_584 | FossifyOrg/Gallery | ❌ | ❌ | ❌ | ❌ |
| 11 | swipe | FossifyOrg_Notes_190 | FossifyOrg/Notes | ✅ | ✅ | ✅ | ❌ |
| 12 | swipe | LawnchairLauncher_lawnchair_5496 | LawnchairLauncher/lawnchair | ✅ | ✅ | ✅ | ❌ |
| 13 | swipe | iamrasel_lunar-launcher_82 | iamrasel/lunar-launcher | ✅ | ✅ | ❌ | ❌ |

## 🐛 Non-Crash Bugs (87 total)

| # | Category | Bug | App | CARBON | AdbGPT | ReBL | ReActDroid |
|---|----------|-----|-----|--------|--------|------|------------|
| 1 | double_tap | FossifyOrg_Calendar_273 | FossifyOrg/Calendar | ✅ | ✅ | ❌ | ❌ |
| 2 | double_tap | FossifyOrg_Gallery_363 | FossifyOrg/Gallery | ✅ | ✅ | ❌ | ✅ |
| 3 | double_tap | FossifyOrg_Gallery_678 | FossifyOrg/Gallery | ✅ | ✅ | ❌ | ❌ |
| 4 | double_tap | FossifyOrg_Gallery_846 | FossifyOrg/Gallery | ✅ | ❌ | ❌ | ❌ |
| 5 | double_tap | FossifyOrg_Gallery_847 | FossifyOrg/Gallery | ✅ | ✅ | ❌ | ❌ |
| 6 | double_tap | LawnchairLauncher_lawnchair_2910 | LawnchairLauncher/lawnchair | ✅ | ❌ | ❌ | ❌ |
| 7 | double_tap | LawnchairLauncher_lawnchair_4125 | LawnchairLauncher/lawnchair | ✅ | ✅ | ❌ | ❌ |
| 8 | double_tap | Pool-Of-Tears_GreenStash_170 | Pool-Of-Tears/GreenStash | ✅ | ❌ | ❌ | ❌ |
| 9 | double_tap | TeamNewPipe_NewPipe_8338 | TeamNewPipe/NewPipe | ✅ | ❌ | ❌ | ❌ |
| 10 | double_tap | abdallahmehiz_mpvKt_184 | abdallahmehiz/mpvKt | ✅ | ✅ | ❌ | ❌ |
| 11 | double_tap | ankidroid_Anki-Android_17393 | ankidroid/Anki-Android | ✅ | ❌ | ✅ | ❌ |
| 12 | double_tap | cromaguy_Rhythm_281 | cromaguy/Rhythm | ✅ | ❌ | ✅ | ❌ |
| 13 | double_tap | fast4x_RiMusic_1152 | fast4x/RiMusic | ✅ | ✅ | ❌ | ❌ |
| 14 | double_tap | gsantner_markor_2746 | gsantner/markor | ✅ | ❌ | ❌ | ❌ |
| 15 | double_tap | openboard-team_openboard_613 | openboard-team/openboard | ✅ | ❌ | ❌ | ❌ |
| 16 | double_tap | openboard-team_openboard_758 | openboard-team/openboard | ❌ | ✅ | ❌ | ❌ |
| 17 | double_tap | syt0r_Kanji-Dojo_291 | syt0r/Kanji-Dojo | ✅ | ✅ | ✅ | ❌ |
| 18 | drag_and_drop | FossifyOrg_Launcher_304 | FossifyOrg/Launcher | ✅ | ✅ | ❌ | ❌ |
| 19 | drag_and_drop | FossifyOrg_Notes_59 | FossifyOrg/Notes | ✅ | ✅ | ❌ | ❌ |
| 20 | drag_and_drop | LawnchairLauncher_lawnchair_4320 | LawnchairLauncher/lawnchair | ✅ | ✅ | ❌ | ❌ |
| 21 | drag_and_drop | MetrolistGroup_Metrolist_3227 | MetrolistGroup/Metrolist | ✅ | ❌ | ❌ | ❌ |
| 22 | drag_and_drop | MetrolistGroup_Metrolist_3561 | MetrolistGroup/Metrolist | ✅ | ❌ | ❌ | ❌ |
| 23 | drag_and_drop | NeoApplications_Neo-Launcher_130 | NeoApplications/Neo-Launcher | ✅ | ✅ | ❌ | ❌ |
| 24 | long_press | FossifyOrg_File-Manager_195 | FossifyOrg/File-Manager | ✅ | ✅ | ✅ | ❌ |
| 25 | long_press | FossifyOrg_Launcher_198 | FossifyOrg/Launcher | ✅ | ❌ | ❌ | ❌ |
| 26 | long_press | FossifyOrg_Messages_359 | FossifyOrg/Messages | ✅ | ❌ | ✅ | ❌ |
| 27 | long_press | FossifyOrg_Messages_416 | FossifyOrg/Messages | ✅ | ❌ | ✅ | ❌ |
| 28 | long_press | FossifyOrg_Messages_641 | FossifyOrg/Messages | ✅ | ❌ | ✅ | ❌ |
| 29 | long_press | breezy-weather_breezy-weather_1639 | breezy-weather/breezy-weather | ✅ | ❌ | ✅ | ❌ |
| 30 | long_press | espresso3389_methings_34 | espresso3389/methings | ✅ | ✅ | ✅ | ❌ |
| 31 | orientation | FossifyOrg_Calendar_1042 | FossifyOrg/Calendar | ✅ | ✅ | ✅ | ❌ |
| 32 | orientation | FossifyOrg_Camera_91 | FossifyOrg/Camera | ✅ | ❌ | ✅ | ❌ |
| 33 | orientation | FossifyOrg_Clock_85 | FossifyOrg/Clock | ❌ | ✅ | ❌ | ❌ |
| 34 | orientation | FossifyOrg_Contacts_197 | FossifyOrg/Contacts | ✅ | ❌ | ✅ | ❌ |
| 35 | orientation | Waboodoo_HTTP-Shortcuts_262 | Waboodoo/HTTP-Shortcuts | ✅ | ✅ | ✅ | ❌ |
| 36 | orientation | ankidroid_Anki-Android_16410 | ankidroid/Anki-Android | ✅ | ✅ | ✅ | ❌ |
| 37 | pinch_zoom | Droid-ify_client_583 | Droid-ify/client | ✅ | ✅ | ❌ | ❌ |
| 38 | pinch_zoom | FossifyOrg_Calendar_621 | FossifyOrg/Calendar | ✅ | ✅ | ❌ | ❌ |
| 39 | pinch_zoom | FossifyOrg_Camera_23 | FossifyOrg/Camera | ✅ | ✅ | ❌ | ❌ |
| 40 | pinch_zoom | FossifyOrg_Gallery_289 | FossifyOrg/Gallery | ✅ | ✅ | ✅ | ❌ |
| 41 | pinch_zoom | FossifyOrg_Gallery_642 | FossifyOrg/Gallery | ✅ | ✅ | ❌ | ❌ |
| 42 | pinch_zoom | FossifyOrg_Gallery_728 | FossifyOrg/Gallery | ✅ | ✅ | ❌ | ❌ |
| 43 | pinch_zoom | FossifyOrg_Paint_125 | FossifyOrg/Paint | ✅ | ✅ | ❌ | ❌ |
| 44 | pinch_zoom | FossifyOrg_Paint_25 | FossifyOrg/Paint | ✅ | ✅ | ❌ | ❌ |
| 45 | pinch_zoom | ankidroid_Anki-Android_16135 | ankidroid/Anki-Android | ✅ | ❌ | ❌ | ❌ |
| 46 | pinch_zoom | ankidroid_Anki-Android_17667 | ankidroid/Anki-Android | ✅ | ❌ | ✅ | ❌ |
| 47 | pinch_zoom | saber-notes_saber_192 | saber-notes/saber | ✅ | ❌ | ❌ | ❌ |
| 48 | pinch_zoom | streetcomplete_StreetComplete_6068 | streetcomplete/StreetComplete | ✅ | ❌ | ❌ | ❌ |
| 49 | pinch_zoom | yairm210_Unciv_13517 | yairm210/Unciv | ✅ | ❌ | ❌ | ❌ |
| 50 | pinch_zoom | you-apps_WallYou_216 | you-apps/WallYou | ✅ | ❌ | ❌ | ❌ |
| 51 | quick_tap | LawnchairLauncher_lawnchair_5540 | LawnchairLauncher/lawnchair | ✅ | ✅ | ❌ | ❌ |
| 52 | quick_tap | anilbeesetti_nextplayer_1389 | anilbeesetti/nextplayer | ✅ | ✅ | ❌ | ❌ |
| 53 | quick_tap | ankidroid_Anki-Android_18529 | ankidroid/Anki-Android | ❌ | ❌ | ❌ | ❌ |
| 54 | quick_tap | ankidroid_Anki-Android_19641 | ankidroid/Anki-Android | ✅ | ✅ | ❌ | ❌ |
| 55 | quick_tap | ankidroid_Anki-Android_20789 | ankidroid/Anki-Android | ❌ | ✅ | ❌ | ❌ |
| 56 | quick_tap | ankidroid_Anki-Android_7138 | ankidroid/Anki-Android | ✅ | ❌ | ❌ | ❌ |
| 57 | scroll | Anthonyy232_Paperize_426 | Anthonyy232/Paperize | ✅ | ❌ | ✅ | ❌ |
| 58 | scroll | Fandroid745_Open-notes_15 | Fandroid745/Open-notes | ✅ | ✅ | ❌ | ❌ |
| 59 | scroll | ankidroid_Anki-Android_5512 | ankidroid/Anki-Android | ✅ | ❌ | ❌ | ✅ |
| 60 | scroll | ankidroid_Anki-Android_5544 | ankidroid/Anki-Android | ✅ | ✅ | ✅ | ✅ |
| 61 | scroll | netmackan_ATimeTracker_124 | netmackan/ATimeTracker | ✅ | ✅ | ✅ | ❌ |
| 62 | swipe | A-EDev_Flow_27 | A-EDev/Flow | ✅ | ❌ | ❌ | ❌ |
| 63 | swipe | A-EDev_Flow_284 | A-EDev/Flow | ✅ | ❌ | ❌ | ❌ |
| 64 | swipe | CodeWorksCreativeHub_mLauncher_809 | CodeWorksCreativeHub/mLauncher | ✅ | ✅ | ✅ | ❌ |
| 65 | swipe | FossifyOrg_Calendar_1103 | FossifyOrg/Calendar | ✅ | ❌ | ✅ | ❌ |
| 66 | swipe | FossifyOrg_Calendar_153 | FossifyOrg/Calendar | ✅ | ✅ | ✅ | ❌ |
| 67 | swipe | FossifyOrg_Clock_156 | FossifyOrg/Clock | ❌ | ✅ | ❌ | ❌ |
| 68 | swipe | FossifyOrg_File-Manager_136 | FossifyOrg/File-Manager | ✅ | ❌ | ✅ | ❌ |
| 69 | swipe | FossifyOrg_Gallery_237 | FossifyOrg/Gallery | ✅ | ✅ | ❌ | ❌ |
| 70 | swipe | FossifyOrg_Gallery_940 | FossifyOrg/Gallery | ✅ | ❌ | ❌ | ❌ |
| 71 | swipe | FossifyOrg_Launcher_66 | FossifyOrg/Launcher | ✅ | ❌ | ❌ | ❌ |
| 72 | swipe | FossifyOrg_Messages_80 | FossifyOrg/Messages | ✅ | ❌ | ❌ | ❌ |
| 73 | swipe | Kin69_EasyNotes_356 | Kin69/EasyNotes | ✅ | ❌ | ❌ | ❌ |
| 74 | swipe | LawnchairLauncher_lawnchair_4642 | LawnchairLauncher/lawnchair | ✅ | ✅ | ✅ | ❌ |
| 75 | swipe | LawnchairLauncher_lawnchair_4708 | LawnchairLauncher/lawnchair | ✅ | ✅ | ❌ | ❌ |
| 76 | swipe | MetrolistGroup_Metrolist_3391 | MetrolistGroup/Metrolist | ✅ | ❌ | ✅ | ❌ |
| 77 | swipe | OuterTune_OuterTune_1044 | OuterTune/OuterTune | ✅ | ❌ | ✅ | ❌ |
| 78 | swipe | anilbeesetti_nextplayer_1127 | anilbeesetti/nextplayer | ✅ | ✅ | ❌ | ❌ |
| 79 | swipe | ankidroid_Anki-Android_14934 | ankidroid/Anki-Android | ✅ | ✅ | ❌ | ❌ |
| 80 | swipe | bartoostveen_ViTune_710 | 25huizengek1/ViTune | ✅ | ✅ | ❌ | ❌ |
| 81 | swipe | breezy-weather_breezy-weather_205 | breezy-weather/breezy-weather | ✅ | ✅ | ❌ | ❌ |
| 82 | swipe | breezy-weather_breezy-weather_85 | breezy-weather/breezy-weather | ✅ | ✅ | ✅ | ❌ |
| 83 | swipe | dessalines_thumb-key_371 | dessalines/thumb-key | ✅ | ❌ | ❌ | ❌ |
| 84 | swipe | libre-tube_LibreTube_8245 | libre-tube/LibreTube | ✅ | ❌ | ❌ | ❌ |
| 85 | swipe | msasikanth_twine_1566 | msasikanth/twine | ✅ | ❌ | ❌ | ❌ |
| 86 | swipe | you-apps_ClockYou_85 | you-apps/ClockYou | ✅ | ✅ | ✅ | ❌ |
| 87 | swipe | you-apps_ConnectYou_155 | you-apps/ConnectYou | ✅ | ❌ | ❌ | ❌ |

---
*Report generated from verified test logs across all four tools.*
