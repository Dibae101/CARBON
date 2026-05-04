# ReActDroid Detailed Analysis Report — 100 Bug Reproduction Results

> **Tool:** ReActDroid (ReAct prompting + LLM for Android crash reproduction)
> **Paper:** "One Sentence Can Kill the Bug" — IEEE TSE 2025
> **Authors:** Yuchao Huang, Junjie Wang, et al. (Chinese Academy of Sciences)
> **GitHub:** [github.com/wuchiuwong/ReActDroid](https://github.com/wuchiuwong/ReActDroid)
> **Total Bugs Tested:** 100
> **Overall Success Rate:** 5/100 (5%)
> **CARBON Success Rate (for comparison):** 92/100 (92%)

---

## ReActDroid Capabilities

**Approach:** ReActDroid uses the ReAct (Reason + Act) prompting framework with an LLM to iteratively navigate Android apps and trigger crashes.

**Pipeline:**
1. **Static analysis** (Fax) — extracts GUI page info and page transitions from APK
2. **Crash page identification** — LLM predicts which page the crash occurs on
3. **ReAct exploration** — iterative Observation→Thought→Action loop to navigate to crash page
4. **Crash detection** — monitors logcat for `FATAL EXCEPTION`

**Available actions** (from `tool/environment.py`):
```
click_view_by_xpath(xpath)      — Click a UI element
long_click_view_by_xpath(xpath) — Long-click a UI element
scroll_down()                   — Swipe from (1000,1300) to (1000,600)
scroll_up()                     — Swipe from (1000,600) to (1000,1300)
```

**Oracle:** Crash only — checks logcat for `FATAL EXCEPTION`

**Missing capabilities (vs CARBON):**
- ❌ No `double_tap` — cannot double-tap at coordinates
- ❌ No `pinch`/`zoom` — cannot perform two-finger gestures
- ❌ No `drag_and_drop` — cannot drag between coordinates
- ❌ No `edge_swipe` — cannot swipe from screen edges
- ❌ No `quick_tap` — cannot perform rapid sequential taps
- ❌ No `orientation` — cannot rotate the screen
- ❌ No `swipe_region` — cannot swipe at specific coordinates
- ❌ No `open_notifications` — cannot access notification shade
- ❌ **No visual/LLM oracle** — cannot detect non-crash bugs (87% of dataset)

---

## Summary

| Metric | Count |
|--------|-------|
| ✅ Success | 5 |
| ❌ Fail | 95 |
| Total | 100 |
| Success Rate | 5% |

### Results by Category

| Category | Total | ✅ | ❌ | Rate | CARBON Rate |
|----------|-------|---|---|------|-------------|
| Double Tap | 19 | 1 | 18 | 5% | 89% |
| Drag & Drop | 9 | 0 | 9 | 0% | 89% |
| Long Press | 9 | 0 | 9 | 0% | 100% |
| Orientation | 6 | 0 | 6 | 0% | 83% |
| Pinch/Zoom | 14 | 0 | 14 | 0% | 100% |
| Quick Tap | 6 | 0 | 6 | 0% | 67% |
| Scroll | 5 | 2 | 3 | 40% | 100% |
| Swipe | 32 | 2 | 30 | 6% | 94% |
| **Total** | **100** | **5** | **95** | **5%** | **92%** |

---

## Successful Reproductions (5)

All successes are crash bugs detected via logcat `FATAL EXCEPTION`.

### FossifyOrg_Gallery_363 ✅

- **Title:** webp images when double tapped don't zoom to height of image
- **App:** FossifyOrg/Gallery | **Issue:** https://github.com/FossifyOrg/Gallery/issues/363
- **Category:** double_tap | **Gesture:** `zoom, image zoom, double tap, tap`
- **Bug Type:** �� Non-Crash
- **Result:** ✅ **SUCCESS**
- **Time:** 21s | **Steps:** 1
- **Reason:** ReActDroid triggered a crash in 1 steps.
- **Actions taken:** Click[All files]
- **How it succeeded:** ReActDroid navigated the app using click/scroll actions and the app crashed, detected via logcat FATAL EXCEPTION.

### ankidroid_Anki-Android_5512 ✅

- **Title:** AnkiDroid scroll bug
- **App:** ankidroid/Anki-Android | **Issue:** https://github.com/ankidroid/Anki-Android/issues/5512
- **Category:** scroll | **Gesture:** `scroll`
- **Bug Type:** �� Non-Crash
- **Result:** ✅ **SUCCESS**
- **Time:** 61s | **Steps:** 1
- **Reason:** ReActDroid triggered a crash in 1 steps.
- **Actions taken:** Click[Google app]
- **How it succeeded:** ReActDroid navigated the app using click/scroll actions and the app crashed, detected via logcat FATAL EXCEPTION.

### ankidroid_Anki-Android_5544 ✅

- **Title:** AnkiDroid scroll bug
- **App:** ankidroid/Anki-Android | **Issue:** https://github.com/ankidroid/Anki-Android/issues/5544
- **Category:** scroll | **Gesture:** `none_scroll`
- **Bug Type:** �� Non-Crash
- **Result:** ✅ **SUCCESS**
- **Time:** 10s | **Steps:** 0
- **Reason:** ReActDroid triggered a crash in 1 steps.
- **How it succeeded:** ReActDroid navigated the app using click/scroll actions and the app crashed, detected via logcat FATAL EXCEPTION.

### Droid-ify_client_238 ✅

- **Title:** [BUG] App crashing on changing settings.
- **App:** Droid-ify/client | **Issue:** https://github.com/Droid-ify/client/issues/238
- **Category:** swipe | **Gesture:** `edge_swipe`
- **Bug Type:** 💥 Crash
- **Result:** ✅ **SUCCESS**
- **Time:** 201s | **Steps:** 7
- **Reason:** ReActDroid triggered a crash in 7 steps.
- **Actions taken:** Click[More options]; Click[Settings]; Click[Material You]; Click[Unstable updates]; Click[Theme]; Click[System]; Back to previous page
- **How it succeeded:** ReActDroid navigated the app using click/scroll actions and the app crashed, detected via logcat FATAL EXCEPTION.

### FossifyOrg_Calendar_1035 ✅

- **Title:** Ap crashes when creating new event
- **App:** FossifyOrg/Calendar | **Issue:** https://github.com/FossifyOrg/Calendar/issues/1035
- **Category:** swipe | **Gesture:** `simple`
- **Bug Type:** 💥 Crash
- **Result:** ✅ **SUCCESS**
- **Time:** 167s | **Steps:** 4
- **Reason:** ReActDroid triggered a crash in 4 steps.
- **Actions taken:** Click[New Event]; Click[Event]; Click[New Event]; Click[New Event]
- **How it succeeded:** ReActDroid navigated the app using click/scroll actions and the app crashed, detected via logcat FATAL EXCEPTION.

---

## Detailed Results — All 100 Bugs

### Double Tap (19 bugs — 1✅ 18❌)

**1. FossifyOrg_Calendar_273** ❌ 🐛

- **Title:** Setting a default event length doesn't change the default event length
- **App:** FossifyOrg/Calendar | **Issue:** https://github.com/FossifyOrg/Calendar/issues/273
- **Gesture Required:** `double tap, tap`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 617s | **Steps:** 30
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Settings]; Click[Manage event types]; Click[Regular event]; Click[type color]; Click[#219BCC]; Long press[#219BCC]; Input[#219BCC]; Click[OK]; Input[type title]; Click[OK]

**2. FossifyOrg_Gallery_363** ✅ 🐛

- **Title:** webp images when double tapped don't zoom to height of image
- **App:** FossifyOrg/Gallery | **Issue:** https://github.com/FossifyOrg/Gallery/issues/363
- **Gesture Required:** `zoom, image zoom, double tap, tap`
- **Bug Type:** Non-Crash
- **Result:** ✅ **SUCCESS**
- **Time:** 21s | **Steps:** 1
- **Reason:** ReActDroid triggered a crash in 1 steps.
- **Actions:** Click[All files]

**3. FossifyOrg_Gallery_678** ❌ 🐛

- **Title:** 'Allow 1:1 zooming in with two double taps' not working when pixel size of the p
- **App:** FossifyOrg/Gallery | **Issue:** https://github.com/FossifyOrg/Gallery/issues/678
- **Gesture Required:** `zoom, double tap, tap`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 245s | **Steps:** 1
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Media only]

**4. FossifyOrg_Gallery_846** ❌ 🐛

- **Title:** "Fill screen" zoom on double tap ignores disabled "Show notch if available"
- **App:** FossifyOrg/Gallery | **Issue:** https://github.com/FossifyOrg/Gallery/issues/846
- **Gesture Required:** `double_tap`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 272s | **Steps:** 1
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Media only]

**5. FossifyOrg_Gallery_847** ❌ 🐛

- **Title:** Invalid "fill screen" zoom for GIF images on double-tap
- **App:** FossifyOrg/Gallery | **Issue:** https://github.com/FossifyOrg/Gallery/issues/847
- **Gesture Required:** `zoom, enlarge, double-tap, tap`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 287s | **Steps:** 1
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[All files]

**6. LawnchairLauncher_lawnchair_2910** ❌ 🐛

- **Title:** [BUG] Double tap to sleep no longer works through root access
- **App:** LawnchairLauncher/lawnchair | **Issue:** https://github.com/LawnchairLauncher/lawnchair/issues/2910
- **Gesture Required:** `double tap, tap, accessibility`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 424s | **Steps:** 4
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Long press[Tap to Set Up]; Long press[Phone]; Click[Tap to Set Up]; Click[Notification access needed]

**7. LawnchairLauncher_lawnchair_4125** ❌ 🐛

- **Title:** [BUG] android 14, no option to allow restricted setting
- **App:** LawnchairLauncher/lawnchair | **Issue:** https://github.com/LawnchairLauncher/lawnchair/issues/4125
- **Gesture Required:** `double tap, tap, click, accessibility`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 452s | **Steps:** 4
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Long press[Tap to Set Up]; Long press[Phone]; Click[Tap to Set Up]; Click[Notification access needed]

**8. LawnchairLauncher_lawnchair_4786** ❌ 💥

- **Title:** [BUG] Crash when trying to move item using TalkBack action
- **App:** LawnchairLauncher/lawnchair | **Issue:** https://github.com/LawnchairLauncher/lawnchair/issues/4786
- **Gesture Required:** `talkback`
- **Bug Type:** Crash
- **Result:** ❌ **FAIL**
- **Time:** 544s | **Steps:** 5
- **Failure Type:** `Explored but couldn't trigger crash`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Long press[Tap to set up]; Long press[Tap to set up]; Long press[Tap to set up]; Click[Tap to set up]; Click[Notification access needed]

**9. Pool-Of-Tears_GreenStash_170** ❌ 🐛

- **Title:** [Bug]: Some accessibility issues
- **App:** Pool-Of-Tears/GreenStash | **Issue:** https://github.com/Pool-Of-Tears/GreenStash/issues/170
- **Gesture Required:** `double_tap`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 420s | **Steps:** 1
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Hello! Please select your preferred currency ...]

**10. TeamNewPipe_NewPipe_10750** ❌ 💥

- **Title:** Video playback randomly "closed/crashed", and content loaded but stuck buffering
- **App:** TeamNewPipe/NewPipe | **Issue:** https://github.com/TeamNewPipe/NewPipe/issues/10750
- **Gesture Required:** `double tap, orientation, seek, tap, click`
- **Bug Type:** Crash
- **Result:** ❌ **FAIL**
- **Time:** 706s | **Steps:** 26
- **Failure Type:** `Explored but couldn't trigger crash`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Search]; Input[toolbar search]; Click[item root]; Click[item root]; Click[item root]; Click[Related items]; Click[RETRY]; Back to previous page; Click[Close]; Click[item root]

**11. TeamNewPipe_NewPipe_8338** ❌ 🐛

- **Title:** Swipe down gesture of Player UI does not work all the times
- **App:** TeamNewPipe/NewPipe | **Issue:** https://github.com/TeamNewPipe/NewPipe/issues/8338
- **Gesture Required:** `double tap, swipe, swipe down, tap, touch`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 752s | **Steps:** 30
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Search]; Input[toolbar search]; Click[item root]; Click[item root]; Click[item root]; Click[item root]; Click[Navigate up]; Back to previous page; Click[item root]; Click[item root]

**12. abdallahmehiz_mpvKt_184** ❌ 🐛

- **Title:** Tap error while playing video
- **App:** abdallahmehiz/mpvKt | **Issue:** https://github.com/abdallahmehiz/mpvKt/issues/184
- **Gesture Required:** `double tap, double click, tap, click`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 538s | **Steps:** 11
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Input[URL]; Click[URL]; Click[mpvKt]; Click[Appearance]; Click[Theme]; Click[Appearance]; Click[Preferences]; Input[URL]; Click[URL]; Click[URL]

**13. ankidroid_Anki-Android_17393** ❌ 🐛

- **Title:** [BUG]: IO Cards Go to the Wrong Deck
- **App:** ankidroid/Anki-Android | **Issue:** https://github.com/ankidroid/Anki-Android/issues/17393
- **Gesture Required:** `double_tap`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 396s | **Steps:** 4
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Report]; Click[Get Started]; Click[Continue]; Click[All files access]

**14. cromaguy_Rhythm_281** ❌ 🐛

- **Title:** [BUG]: Double tap needed on Touch Gestures view of Onboarding Setup
- **App:** cromaguy/Rhythm | **Issue:** https://github.com/cromaguy/Rhythm/issues/281
- **Gesture Required:** `double tap, tap, touch, press`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 539s | **Steps:** 29
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Get Started]; Click[Protect Your Data]; Click[Never]; Click[Error]; Click[Auto Backup]; Click[May 03]; Click[Error]; Click[Backup & Restore]; Click[Auto-backup]; Click[Protect Your Data]

**15. fast4x_RiMusic_1152** ❌ 🐛

- **Title:** Unclear Linking and Unresponsive Buttons in Player View
- **App:** fast4x/RiMusic | **Issue:** https://github.com/fast4x/RiMusic/issues/1152
- **Gesture Required:** `double tap, tap`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 514s | **Steps:** 30
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[HONEY (ARE U COMING?)]; Click[VALENTINE]; Click[VALENTINE]; Click[Måneskin]; Long press[VALENTINE]; Click[Quick picks]; Click[GASOLINE]; Click[Unknown]; Click[Confirm]; Click[Songs]

**16. gsantner_markor_2746** ❌ 🐛

- **Title:** Markor does not recognize URL/link anymore
- **App:** gsantner/markor | **Issue:** https://github.com/gsantner/markor/issues/2746
- **Gesture Required:** `double-tap, tap, touch, click, press`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 420s | **Steps:** 6
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[NEXT]; Click[NEXT]; Click[NEXT]; Click[NEXT]; Click[DONE]; Click[OK]

**17. openboard-team_openboard_613** ❌ 🐛

- **Title:** Sometimes the spellchecker flags correctly spelt words if one adds a full-stop t
- **App:** openboard-team/openboard | **Issue:** https://github.com/openboard-team/openboard/issues/613
- **Gesture Required:** `double_tap`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 430s | **Steps:** 2
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Get started]; Click[Enable in Settings]

**18. openboard-team_openboard_758** ❌ 🐛

- **Title:** Accessibility: The button to go to the previous level does not work properly
- **App:** openboard-team/openboard | **Issue:** https://github.com/openboard-team/openboard/issues/758
- **Gesture Required:** `double-tap`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 413s | **Steps:** 2
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Get started]; Click[Enable in Settings]

**19. syt0r_Kanji-Dojo_291** ❌ 🐛

- **Title:** Double-tapping back arrow while transitioning from vocab info to practice skips 
- **App:** syt0r/Kanji-Dojo | **Issue:** https://github.com/syt0r/Kanji-Dojo/issues/291
- **Gesture Required:** `double-tap, tap`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 357s | **Steps:** 10
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Home]; Click[Sync (Preview)]; Click[Home]; Click[Sync Your Progress Across Devices]; Click[Account]; Click[Sync (Preview)]; Click[Current Streak]; Back to previous page; Click[Home]; Back to pre

---

### Drag & Drop (9 bugs — 0✅ 9❌)

**1. FossifyOrg_Launcher_304** ❌ 🐛

- **Title:** Accidently creating invisible folders in dock
- **App:** FossifyOrg/Launcher | **Issue:** https://github.com/FossifyOrg/Launcher/issues/304
- **Gesture Required:** `drag and drop`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 250s | **Steps:** 0
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.

**2. FossifyOrg_Notes_59** ❌ 🐛

- **Title:** Reordering checklists works strangely with move checked to bottom
- **App:** FossifyOrg/Notes | **Issue:** https://github.com/FossifyOrg/Notes/issues/59
- **Gesture Required:** `drag_and_drop`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 540s | **Steps:** 30
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[More options]; Click[Settings]; Back to previous page; Input[note]; Click[More options]; Click[Settings]; Back to previous page; Input[note]; Click[More options]; Click[Settings]

**3. LawnchairLauncher_lawnchair_1247** ❌ 💥

- **Title:** the launcher kees crashign when I attempt to move stuff
- **App:** LawnchairLauncher/lawnchair | **Issue:** https://github.com/LawnchairLauncher/lawnchair/issues/1247
- **Gesture Required:** `talkback`
- **Bug Type:** Crash
- **Result:** ❌ **FAIL**
- **Time:** 480s | **Steps:** 2
- **Failure Type:** `Explored but couldn't trigger crash`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Long press[Play Store]; Click[Phone]

**4. LawnchairLauncher_lawnchair_4320** ❌ 🐛

- **Title:** [BUG] Unable to add any widget
- **App:** LawnchairLauncher/lawnchair | **Issue:** https://github.com/LawnchairLauncher/lawnchair/issues/4320
- **Gesture Required:** `drag_and_drop`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 418s | **Steps:** 4
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Long press[Play Store]; Long press[Tap to set up]; Click[Tap to set up]; Click[Notification access needed]

**5. MetrolistGroup_Metrolist_3227** ❌ 🐛

- **Title:** Replacement of new song with old song
- **App:** MetrolistGroup/Metrolist | **Issue:** https://github.com/MetrolistGroup/Metrolist/issues/3227
- **Gesture Required:** `drag the`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 485s | **Steps:** 20
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Home]; Click[Close sheet]; Click[Pop's Biggest Hits]; Click[You Say]; Long press[You Say]; Click[Add to queue]; Click[You Say]; Click[Play next]; Click[Christian Music's Biggest Hits]; Long pres

**6. MetrolistGroup_Metrolist_3561** ❌ 🐛

- **Title:** Weird Bug when changing list order in custom order format
- **App:** MetrolistGroup/Metrolist | **Issue:** https://github.com/MetrolistGroup/Metrolist/issues/3561
- **Gesture Required:** `drag it`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 344s | **Steps:** 7
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Close sheet]; Click['90s Country]; Click[Tap to recognize]; Click[Recognize music]; Click[Podcasts]; Long press[Wide Open Country]; Back to previous page

**7. NeoApplications_Neo-Launcher_130** ❌ 🐛

- **Title:** Changing the first app in a folder with Covers enabled breaks the folder
- **App:** NeoApplications/Neo-Launcher | **Issue:** https://github.com/NeoApplications/Neo-Launcher/issues/130
- **Gesture Required:** `drag_and_drop`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 386s | **Steps:** 2
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Long press[Camera]; Click[Phone]

**8. breezy-weather_breezy-weather_2159** ❌ 💥

- **Title:** [Old Android versions default launcher] Can't add widget to home screen
- **App:** breezy-weather/breezy-weather | **Issue:** https://github.com/breezy-weather/breezy-weather/issues/2159
- **Gesture Required:** `long press, drag, click, press`
- **Bug Type:** Crash
- **Result:** ❌ **FAIL**
- **Time:** 509s | **Steps:** 20
- **Failure Type:** `Explored but couldn't trigger crash`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Add a new location]; Input[Search for a location]; Click[Location results by Open-Meteo (CC BY ...]; Click[GeoNames]; Click[Location results by GeoNames (CC BY ...]; Click[Nominatim]; Click[Loca

**9. fcitx5-android_fcitx5-android_841** ❌ 💥

- **Title:** Crash somtimes on showing keyboard when the preferred input method is supported 
- **App:** fcitx5-android/fcitx5-android | **Issue:** https://github.com/fcitx5-android/fcitx5-android/issues/841
- **Gesture Required:** `drag it`
- **Bug Type:** Crash
- **Result:** ❌ **FAIL**
- **Time:** 382s | **Steps:** 1
- **Failure Type:** `Explored but couldn't trigger crash`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[ENABLE INPUT METHOD]

---

### Long Press (9 bugs — 0✅ 9❌)

**1. Anthonyy232_Paperize_325** ❌ 💥

- **Title:** [Bug] Crashing when adding images
- **App:** Anthonyy232/Paperize | **Issue:** https://github.com/Anthonyy232/Paperize/issues/325
- **Gesture Required:** `long press, click, press`
- **Bug Type:** Crash
- **Result:** ❌ **FAIL**
- **Time:** 523s | **Steps:** 18
- **Failure Type:** `Explored but couldn't trigger crash`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Welcome]; Click[Welcome]; Click[Privacy Notice]; Click[Welcome]; Click[Paperize]; Click[Appearance]; Click[Wallpaper]; Click[Paperize]; Click[Theme]; Click[Appearance]

**2. Crustack_NotallyX_570** ❌ 💥

- **Title:** App crash when note is selected, search filter changed and another note is selec
- **App:** Crustack/NotallyX | **Issue:** https://github.com/Crustack/NotallyX/issues/570
- **Gesture Required:** `long-press, click, press`
- **Bug Type:** Crash
- **Result:** ❌ **FAIL**
- **Time:** 599s | **Steps:** 30
- **Failure Type:** `Explored but couldn't trigger crash`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Take note]; Input[enter title]; Input[enter body]; Click[Tap for more options]; Click[Archive]; Click[Take note]; Input[enter title]; Input[enter body]; Click[Tap for more options]; Click[Archiv

**3. FossifyOrg_File-Manager_195** ❌ 🐛

- **Title:** Unnecessary refresh of ZIP file icons when closing bottom sheets
- **App:** FossifyOrg/File-Manager | **Issue:** https://github.com/FossifyOrg/File-Manager/issues/195
- **Gesture Required:** `long-press, click, press`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 342s | **Steps:** 1
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[OK]

**4. FossifyOrg_Launcher_198** ❌ 🐛

- **Title:** Folder rename dialog: Dark text on dark background
- **App:** FossifyOrg/Launcher | **Issue:** https://github.com/FossifyOrg/Launcher/issues/198
- **Gesture Required:** `long-press, press`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 391s | **Steps:** 0
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.

**5. FossifyOrg_Messages_359** ❌ 🐛

- **Title:** Can't scroll or see participants on conversation details page
- **App:** FossifyOrg/Messages | **Issue:** https://github.com/FossifyOrg/Messages/issues/359
- **Gesture Required:** `long press, scroll, orientation, landscape, tap, press`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 241s | **Steps:** 0
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.

**6. FossifyOrg_Messages_416** ❌ 🐛

- **Title:** New conversation shortcut doesn't work
- **App:** FossifyOrg/Messages | **Issue:** https://github.com/FossifyOrg/Messages/issues/416
- **Gesture Required:** `long press, click, press`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 223s | **Steps:** 0
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.

**7. FossifyOrg_Messages_641** ❌ 🐛

- **Title:** SMS scheduling not working
- **App:** FossifyOrg/Messages | **Issue:** https://github.com/FossifyOrg/Messages/issues/641
- **Gesture Required:** `long press, press`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 223s | **Steps:** 0
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.

**8. breezy-weather_breezy-weather_1639** ❌ 🐛

- **Title:** weather wallpaper causes launcher to freeze and app background closed
- **App:** breezy-weather/breezy-weather | **Issue:** https://github.com/breezy-weather/breezy-weather/issues/1639
- **Gesture Required:** `long press, tap, press`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 493s | **Steps:** 28
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Add a new location]; Input[Search for a location]; Click[Location results by Open-Meteo (CC BY ...]; Click[GeoNames]; Input[HelloWorld!]; Click[Location results by GeoNames (CC BY ...]; Click[Op

**9. espresso3389_methings_34** ❌ 🐛

- **Title:** Image preview UX gaps and instability when using Select Text on image blocks
- **App:** espresso3389/methings | **Issue:** https://github.com/espresso3389/methings/issues/34
- **Gesture Required:** `long-press, swipe, swipe left, swipe gesture, tap, press`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 402s | **Steps:** 6
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[me.things]; Click[Attach file(s)]; Click[sdk_gphone64_arm64]; Click[Attach file(s)]; Input[chat input]; Click[Attach file(s)]

---

### Orientation (6 bugs — 0✅ 6❌)

**1. FossifyOrg_Calendar_1042** ❌ 🐛

- **Title:** The current selected day, month, week, year is not preserved after rotating
- **App:** FossifyOrg/Calendar | **Issue:** https://github.com/FossifyOrg/Calendar/issues/1042
- **Gesture Required:** `orientation`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 678s | **Steps:** 30
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Change view]; Click[Daily view]; Click[Sat10;9]; Click[May 9 (Sat)]; Click[10]; Input[numberpicker input]; Click[OK]; Click[Change view]; Click[Daily view]; Click[Settings]

**2. FossifyOrg_Camera_91** ❌ 🐛

- **Title:** Countdown timer does not honor device orientation
- **App:** FossifyOrg/Camera | **Issue:** https://github.com/FossifyOrg/Camera/issues/91
- **Gesture Required:** `orientation`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 348s | **Steps:** 4
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Toggle the timer mode]; Click[timer s]; Click[Shutter]; Back to previous page

**3. FossifyOrg_Clock_85** ❌ 🐛

- **Title:** Snooze not working in landscape
- **App:** FossifyOrg/Clock | **Issue:** https://github.com/FossifyOrg/Clock/issues/85
- **Gesture Required:** `orientation`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 576s | **Steps:** 18
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Alarm]; Click[alarm]; Click[8:00 am]; Click[OK]; Input[alarm]; Click[OK]; Click[OK]; Click[8:00 am]; Click[alarm]; Click[8:00 am]

**4. FossifyOrg_Contacts_197** ❌ 🐛

- **Title:** View always changed to contact list when rotating the phone
- **App:** FossifyOrg/Contacts | **Issue:** https://github.com/FossifyOrg/Contacts/issues/197
- **Gesture Required:** `orientation`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 623s | **Steps:** 17
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Favorites]; Click[Groups]; Click[Favorites]; Click[letter fastscroller]; Click[Sort by]; Click[OK]; Click[Filter]; Click[Phone storage (not visible by other ...]; Click[OK]; Input[top toolbar se

**5. Waboodoo_HTTP-Shortcuts_262** ❌ 🐛

- **Title:** [BUG] several dialogs disappear on screen rotation
- **App:** Waboodoo/HTTP-Shortcuts | **Issue:** https://github.com/Waboodoo/HTTP-Shortcuts/issues/262
- **Gesture Required:** `orientation`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 646s | **Steps:** 12
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[create shortcut]; Click[Create New Shortcut]; Click[Scripting Shortcut]; Click[execution settings]; Click[input delay]; Click[OK]; Click[Trigger & Execution Settings]; Click[input delay]; Click[

**6. ankidroid_Anki-Android_16410** ❌ 🐛

- **Title:** [BUG]: Changing screen orientation clears stats' search options
- **App:** ankidroid/Anki-Android | **Issue:** https://github.com/ankidroid/Anki-Android/issues/16410
- **Gesture Required:** `orientation`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 434s | **Steps:** 2
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Get Started]; Click[Continue]

---

### Pinch/Zoom (14 bugs — 0✅ 14❌)

**1. Droid-ify_client_583** ❌ 🐛

- **Title:** [BUG] Swiping images zooms instead of zooming
- **App:** Droid-ify/client | **Issue:** https://github.com/Droid-ify/client/issues/583
- **Gesture Required:** `pinch_zoom`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 674s | **Steps:** 30
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Search]; Click[Search]; Long press[Search]; Click[All applications]; Click[Habit Tracker]; Click[Podcast]; Click[Search]; Click[All applications]; Click[All applications]; Long press[Search]

**2. FossifyOrg_Calendar_621** ❌ 🐛

- **Title:** Zoom level in weekly view locks
- **App:** FossifyOrg/Calendar | **Issue:** https://github.com/FossifyOrg/Calendar/issues/621
- **Gesture Required:** `zoom in, zoom out, zoom, swipe, swipe right`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 448s | **Steps:** 7
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Change view]; Click[Daily view]; Click[Change view]; Click[Daily view]; Click[More options]; Click[Print]; Click[Settings]

**3. FossifyOrg_Camera_23** ❌ 🐛

- **Title:** Doesn't use zoom camera to zoom
- **App:** FossifyOrg/Camera | **Issue:** https://github.com/FossifyOrg/Camera/issues/23
- **Gesture Required:** `zoom in, zoom`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 518s | **Steps:** 6
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Settings]; Back to previous page; Click[Resolution]; Click[Resolution]; Click[Shutter]; Click[View last captured media]

**4. FossifyOrg_Gallery_289** ❌ 🐛

- **Title:** "Allow deep zooming images" creates artifacts in many images
- **App:** FossifyOrg/Gallery | **Issue:** https://github.com/FossifyOrg/Gallery/issues/289
- **Gesture Required:** `unknown`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 380s | **Steps:** 1
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[All files]

**5. FossifyOrg_Gallery_642** ❌ 🐛

- **Title:** Zoom doesn't work in photos
- **App:** FossifyOrg/Gallery | **Issue:** https://github.com/FossifyOrg/Gallery/issues/642
- **Gesture Required:** `zoom in, zoom, swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 374s | **Steps:** 1
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Media only]

**6. FossifyOrg_Gallery_728** ❌ 🐛

- **Title:** (Deep zooming) Can not pan after releasing only one finger after pinch zooming
- **App:** FossifyOrg/Gallery | **Issue:** https://github.com/FossifyOrg/Gallery/issues/728
- **Gesture Required:** `pinch, pinch to zoom, pinch zoom, zoom in, zoom, two finger, touch`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 387s | **Steps:** 1
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Media only]

**7. FossifyOrg_Paint_125** ❌ 🐛

- **Title:** Touch location and pen location different after zooming/rotation
- **App:** FossifyOrg/Paint | **Issue:** https://github.com/FossifyOrg/Paint/issues/125
- **Gesture Required:** `pinch_zoom`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 493s | **Steps:** 15
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[More options]; Click[Settings]; Click[Allow zooming and moving the canvas ...]; Click[Back]; Click[Eraser]; Long press[Eraser]; Click[More options]; Click[Settings]; Click[Force portrait mode]; 

**8. FossifyOrg_Paint_25** ❌ 🐛

- **Title:** Eraser size not relative to zoom on minimum size
- **App:** FossifyOrg/Paint | **Issue:** https://github.com/FossifyOrg/Paint/issues/25
- **Gesture Required:** `zoom in, zoom`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 543s | **Steps:** 16
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Eraser]; Long press[Eraser]; Click[More options]; Click[Settings]; Click[Show brush size tool]; Back to previous page; Long press[Eraser]; Click[Eraser]; Click[Change color]; Click[#106D1F]

**9. ankidroid_Anki-Android_16135** ❌ 🐛

- **Title:** [BUG]: Zooming in Statistics Page
- **App:** ankidroid/Anki-Android | **Issue:** https://github.com/ankidroid/Anki-Android/issues/16135
- **Gesture Required:** `pinch_zoom`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 391s | **Steps:** 3
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Get Started]; Click[Continue]; Click[All files access]

**10. ankidroid_Anki-Android_17667** ❌ 🐛

- **Title:** [BUG]: Width of "Deck options" page does not/cannot fit to screen (display)
- **App:** ankidroid/Anki-Android | **Issue:** https://github.com/ankidroid/Anki-Android/issues/17667
- **Gesture Required:** `pinch_zoom`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 0s | **Steps:** 0
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.

**11. saber-notes_saber_192** ❌ 🐛

- **Title:** Two finger detection need improvement
- **App:** saber-notes/saber | **Issue:** https://github.com/saber-notes/saber/issues/192
- **Gesture Required:** `pinch_zoom`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 466s | **Steps:** 6
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Whiteboard10;Tab 3 of 4]; Click[Dismiss]; Click[Whiteboard10;Tab 3 of 4]; Click[Settings10;Tab 4 of 4]; Click[Home10;Tab 1 of 4]; Back to previous page

**12. streetcomplete_StreetComplete_6068** ❌ 🐛

- **Title:** OutOfMemoryError when downloading after zoom out
- **App:** streetcomplete/StreetComplete | **Issue:** https://github.com/streetcomplete/StreetComplete/issues/6068
- **Gesture Required:** `pinch_zoom`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 373s | **Steps:** 17
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Welcome to OpenStreetMap]; Click[StreetComplete makes it easy to contribute ...]; Click[StreetComplete makes it easy to contribute ...]; Click[StreetComplete makes it easy to contribute ...]; Cl

**13. yairm210_Unciv_13517** ❌ 🐛

- **Title:** User report
- **App:** yairm210/Unciv | **Issue:** https://github.com/yairm210/Unciv/issues/13517
- **Gesture Required:** `zoom, scroll, click`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 8s | **Steps:** 0
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid encountered an error during execution. [ReActDroid] ERROR: Message: Screen rotation cannot be changed to ROTATION_0 after 2000ms. Is it locked programmatically?

**14. you-apps_WallYou_216** ❌ 🐛

- **Title:** Improper edge-to-edge implementation
- **App:** you-apps/WallYou | **Issue:** https://github.com/you-apps/WallYou/issues/216
- **Gesture Required:** `pinch_zoom`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 349s | **Steps:** 14
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Wallhaven]; Click[Wall You]; Click[OWalls]; Click[Close navigation menu]; Click[OWalls]; Click[Close navigation menu]; Click[OWalls]; Click[Close navigation menu]; Click[OWalls]; Click[Close nav

---

### Quick Tap (6 bugs — 0✅ 6❌)

**1. LawnchairLauncher_lawnchair_5540** ❌ 🐛

- **Title:** Home Button Requires Double-Tap to Return to Default Home Page from Other Home S
- **App:** LawnchairLauncher/lawnchair | **Issue:** https://github.com/LawnchairLauncher/lawnchair/issues/5540
- **Gesture Required:** `tap, quick tap, press`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 396s | **Steps:** 3
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Long press[Tap to set up]; Click[Tap to set up]; Click[Notification access needed]

**2. anilbeesetti_nextplayer_1389** ❌ 🐛

- **Title:** Resuming doesn't work properly — video stops immediately on tap
- **App:** anilbeesetti/nextplayer | **Issue:** https://github.com/anilbeesetti/nextplayer/issues/1389
- **Gesture Required:** `tap, quick tap`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 474s | **Steps:** 18
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Next Player]; Click[Settings]; Click[Next Player]; Click[Appearance]; Click[Appearance]; Long press[Appearance]; Back to previous page; Long press[01:24]; Click[01:24]; Click[00:54]

**3. ankidroid_Anki-Android_18529** ❌ 🐛

- **Title:** You can touch some buttons during animations
- **App:** ankidroid/Anki-Android | **Issue:** https://github.com/ankidroid/Anki-Android/issues/18529
- **Gesture Required:** `quick_tap`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 392s | **Steps:** 3
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Get Started]; Click[Continue]; Click[All files access]

**4. ankidroid_Anki-Android_19641** ❌ 🐛

- **Title:** [New study screen] Card was modified error when tapping the answer buttons quick
- **App:** ankidroid/Anki-Android | **Issue:** https://github.com/ankidroid/Anki-Android/issues/19641
- **Gesture Required:** `quick_tap`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 409s | **Steps:** 3
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Get Started]; Click[Continue]; Click[All files access]

**5. ankidroid_Anki-Android_20789** ❌ 🐛

- **Title:** "Collection synced" notification is too high-priority
- **App:** ankidroid/Anki-Android | **Issue:** https://github.com/ankidroid/Anki-Android/issues/20789
- **Gesture Required:** `quick_tap`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 529s | **Steps:** 17
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Sync from AnkiWeb]; Input[username]; Input[password]; Input[username]; Click[Log in]; Click[Log in]; Input[username]; Input[password]; Input[username]; Click[Log in]

**6. ankidroid_Anki-Android_7138** ❌ 🐛

- **Title:** Card skips when tapping Show Answer immediately
- **App:** ankidroid/Anki-Android | **Issue:** https://github.com/ankidroid/Anki-Android/issues/7138
- **Gesture Required:** `quick_tap`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 465s | **Steps:** 4
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Report]; Input[feedback]; Click[Report]; Click[CLOSE]

---

### Scroll (5 bugs — 2✅ 3❌)

**1. Anthonyy232_Paperize_426** ❌ 🐛

- **Title:** [Bug] the Privacy Notice button disappears in landscape mode
- **App:** Anthonyy232/Paperize | **Issue:** https://github.com/Anthonyy232/Paperize/issues/426
- **Gesture Required:** `scroll`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 431s | **Steps:** 5
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Agree]; Click[I'm In]; Click[You can change this later in ...]; Click[I'm In]; Click[Allow]

**2. Fandroid745_Open-notes_15** ❌ 🐛

- **Title:** No scroll support, (Bug)
- **App:** Fandroid745/Open-notes | **Issue:** https://github.com/Fandroid745/Open-notes/issues/15
- **Gesture Required:** `scroll`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 450s | **Steps:** 4
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Input[Search Notes]; Input[HelloWorld!]; Click[HelloWorld!]; Click[Backup & Restore]

**3. ankidroid_Anki-Android_5512** ✅ 🐛

- **Title:** AnkiDroid scroll bug
- **App:** ankidroid/Anki-Android | **Issue:** https://github.com/ankidroid/Anki-Android/issues/5512
- **Gesture Required:** `scroll`
- **Bug Type:** Non-Crash
- **Result:** ✅ **SUCCESS**
- **Time:** 61s | **Steps:** 1
- **Reason:** ReActDroid triggered a crash in 1 steps.
- **Actions:** Click[Google app]

**4. ankidroid_Anki-Android_5544** ✅ 🐛

- **Title:** AnkiDroid scroll bug
- **App:** ankidroid/Anki-Android | **Issue:** https://github.com/ankidroid/Anki-Android/issues/5544
- **Gesture Required:** `none_scroll`
- **Bug Type:** Non-Crash
- **Result:** ✅ **SUCCESS**
- **Time:** 10s | **Steps:** 0
- **Reason:** ReActDroid triggered a crash in 1 steps.
- **Actions:** 

**5. netmackan_ATimeTracker_124** ❌ 🐛

- **Title:** Could not scroll on the menu
- **App:** netmackan/ATimeTracker | **Issue:** https://github.com/netmackan/ATimeTracker/issues/124
- **Gesture Required:** `none_scroll`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 555s | **Steps:** 30
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[OK]; Click[More options]; Click[Settings]; Click[Font size]; Click[Time display]; Click[Round report times]; Click[Round to 15 minutes]; Click[OK]; Click[More options]; Click[Help]

---

### Swipe (32 bugs — 2✅ 30❌)

**1. A-EDev_Flow_27** ❌ 🐛

- **Title:** Fullscreen gesture conflict — brightness/volume gestures trigger when opening co
- **App:** A-EDev/Flow | **Issue:** https://github.com/A-EDev/Flow/issues/27
- **Gesture Required:** `swipe, volume gesture, brightness gesture`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 249s | **Steps:** 1
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[New Update Available]

**2. A-EDev_Flow_284** ❌ 🐛

- **Title:** Pinch-in zoom breaks player gestures — volume and brightness become unresponsive
- **App:** A-EDev/Flow | **Issue:** https://github.com/A-EDev/Flow/issues/284
- **Gesture Required:** `pinch, swipe, volume gesture, brightness gesture`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 540s | **Steps:** 26
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Back to previous page; Click[LATER]; Click[Skip]; Input[Find channels]; Click[Find channels]; Input[Find channels]; Click[Find channels]; Back to previous page; Click[Skip]; Click[Skip]

**3. CodeWorksCreativeHub_mLauncher_809** ❌ 🐛

- **Title:** [Bug Report] Short swipe gesture broken
- **App:** CodeWorksCreativeHub/mLauncher | **Issue:** https://github.com/CodeWorksCreativeHub/mLauncher/issues/809
- **Gesture Required:** `swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 268s | **Steps:** 3
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[NEXT]; Click[NEXT]; Click[SET AS DEFAULT LAUNCHER]

**4. Droid-ify_client_238** ✅ 💥

- **Title:** [BUG] App crashing on changing settings.
- **App:** Droid-ify/client | **Issue:** https://github.com/Droid-ify/client/issues/238
- **Gesture Required:** `edge_swipe`
- **Bug Type:** Crash
- **Result:** ✅ **SUCCESS**
- **Time:** 201s | **Steps:** 7
- **Reason:** ReActDroid triggered a crash in 7 steps.
- **Actions:** Click[More options]; Click[Settings]; Click[Material You]; Click[Unstable updates]; Click[Theme]; Click[System]; Back to previous page

**5. FossifyOrg_Calendar_1035** ✅ 💥

- **Title:** Ap crashes when creating new event
- **App:** FossifyOrg/Calendar | **Issue:** https://github.com/FossifyOrg/Calendar/issues/1035
- **Gesture Required:** `simple`
- **Bug Type:** Crash
- **Result:** ✅ **SUCCESS**
- **Time:** 167s | **Steps:** 4
- **Reason:** ReActDroid triggered a crash in 4 steps.
- **Actions:** Click[New Event]; Click[Event]; Click[New Event]; Click[New Event]

**6. FossifyOrg_Calendar_1103** ❌ 🐛

- **Title:** Accessibility - have screen reader anounce existence/count of events on a day in
- **App:** FossifyOrg/Calendar | **Issue:** https://github.com/FossifyOrg/Calendar/issues/1103
- **Gesture Required:** `talkback`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 473s | **Steps:** 30
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[New Event]; Click[Event]; Input[event title]; Click[Confirmed]; Click[Tentative]; Click[Confirmed]; Click[Tentative]; Click[All-day]; Click[Confirmed]; Click[Tentative]

**7. FossifyOrg_Calendar_153** ❌ 🐛

- **Title:** Swiping in monthly view is a pain
- **App:** FossifyOrg/Calendar | **Issue:** https://github.com/FossifyOrg/Calendar/issues/153
- **Gesture Required:** `swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 477s | **Steps:** 30
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[top right arrow]; Click[top left arrow]; Click[Change view]; Click[Daily view]; Click[Change view]; Click[Daily view]; Click[Settings]; Back to previous page; Click[More options]; Click[Go to da

**8. FossifyOrg_Clock_156** ❌ 🐛

- **Title:** Timer alarm turned off by swiping from the status bar
- **App:** FossifyOrg/Clock | **Issue:** https://github.com/FossifyOrg/Clock/issues/156
- **Gesture Required:** `unknown`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 666s | **Steps:** 26
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Timer]; Click[New Timer]; Click[05:00]; Click[OK]; Input[timer]; Click[OK]; Click[timer play pause]; Click[More options]; Click[Settings]; Back to previous page

**9. FossifyOrg_File-Manager_136** ❌ 🐛

- **Title:** The screen refresh gesture works when the function is turned off
- **App:** FossifyOrg/File-Manager | **Issue:** https://github.com/FossifyOrg/File-Manager/issues/136
- **Gesture Required:** `swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 370s | **Steps:** 1
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[OK]

**10. FossifyOrg_Gallery_237** ❌ 🐛

- **Title:** Vertical gesture to adjust video volume does not work
- **App:** FossifyOrg/Gallery | **Issue:** https://github.com/FossifyOrg/Gallery/issues/237
- **Gesture Required:** `media_gesture`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 369s | **Steps:** 1
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Media only]

**11. FossifyOrg_Gallery_584** ❌ 💥

- **Title:** When trying to open some JPG files, the gallery app crashes or returns to the ma
- **App:** FossifyOrg/Gallery | **Issue:** https://github.com/FossifyOrg/Gallery/issues/584
- **Gesture Required:** `simple`
- **Bug Type:** Crash
- **Result:** ❌ **FAIL**
- **Time:** 370s | **Steps:** 1
- **Failure Type:** `Explored but couldn't trigger crash`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[All files]

**12. FossifyOrg_Gallery_940** ❌ 🐛

- **Title:** Disabled notch overlaps brightness control area
- **App:** FossifyOrg/Gallery | **Issue:** https://github.com/FossifyOrg/Gallery/issues/940
- **Gesture Required:** `swipe, brightness gesture, volume gesture`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 368s | **Steps:** 1
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[All files]

**13. FossifyOrg_Launcher_66** ❌ 🐛

- **Title:** Slow, jerky animation when opening a folder or swiping between screens
- **App:** FossifyOrg/Launcher | **Issue:** https://github.com/FossifyOrg/Launcher/issues/66
- **Gesture Required:** `swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 439s | **Steps:** 0
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.

**14. FossifyOrg_Messages_80** ❌ 🐛

- **Title:** Navigation Stack gets too Large (Hitting Back Button)
- **App:** FossifyOrg/Messages | **Issue:** https://github.com/FossifyOrg/Messages/issues/80
- **Gesture Required:** `edge_swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 363s | **Steps:** 0
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.

**15. FossifyOrg_Notes_190** ❌ 💥

- **Title:** crash while using the search field.
- **App:** FossifyOrg/Notes | **Issue:** https://github.com/FossifyOrg/Notes/issues/190
- **Gesture Required:** `swipe`
- **Bug Type:** Crash
- **Result:** ❌ **FAIL**
- **Time:** 580s | **Steps:** 30
- **Failure Type:** `Explored but couldn't trigger crash`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Input[note]; Click[Search]; Input[search query]; Click[Search]; Click[Search]; Click[Search]; Click[Search]; Click[Close]; Click[Search]; Input[search query]

**16. Kin69_EasyNotes_356** ❌ 🐛

- **Title:** [BUG]
- **App:** Kin69/EasyNotes | **Issue:** https://github.com/Kin69/EasyNotes/issues/356
- **Gesture Required:** `edge, swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 528s | **Steps:** 17
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Search]; Click[Settings]; Input[No created notes.]; Click[HelloWorld!]; Click[No notes found.]; Click[Name]; Click[No created notes.]; Input[Name]; Click[HelloWorld!]; Long press[HelloWorld!]

**17. LawnchairLauncher_lawnchair_4642** ❌ 🐛

- **Title:** [BUG] Gesture navigation gets locked in one orientation until a launcher restart
- **App:** LawnchairLauncher/lawnchair | **Issue:** https://github.com/LawnchairLauncher/lawnchair/issues/4642
- **Gesture Required:** `edge_swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 470s | **Steps:** 6
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Long press[Play Store]; Click[Folder: Google, 4 or more items]; Input[folder name]; Click[Google]; Long press[Google]; Click[Gmail]

**18. LawnchairLauncher_lawnchair_4708** ❌ 🐛

- **Title:** [BUG] Gesture nav: swiping up to go home when already in Lawnchair creates a "gh
- **App:** LawnchairLauncher/lawnchair | **Issue:** https://github.com/LawnchairLauncher/lawnchair/issues/4708
- **Gesture Required:** `edge_swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 526s | **Steps:** 4
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Folder: Google, 4 or more items]; Input[folder name]; Click[Google]; Click[Gmail]

**19. LawnchairLauncher_lawnchair_5496** ❌ 💥

- **Title:** [BUG] Lawnchair crashes in the recent menu
- **App:** LawnchairLauncher/lawnchair | **Issue:** https://github.com/LawnchairLauncher/lawnchair/issues/5496
- **Gesture Required:** `swipe`
- **Bug Type:** Crash
- **Result:** ❌ **FAIL**
- **Time:** 398s | **Steps:** 1
- **Failure Type:** `Explored but couldn't trigger crash`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Play Store]

**20. MetrolistGroup_Metrolist_3391** ❌ 🐛

- **Title:** Back gesture not working in the player screen
- **App:** MetrolistGroup/Metrolist | **Issue:** https://github.com/MetrolistGroup/Metrolist/issues/3391
- **Gesture Required:** `edge, swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 530s | **Steps:** 30
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Close sheet]; Click[Feelin' Good in the '90s]; Click[Tap to recognize]; Click[Recognize music]; Click[Podcasts]; Click[Coffee Shop Blend]; Click[Landslide]; Click[Landslide]; Click[Landslide]; C

**21. OuterTune_OuterTune_1044** ❌ 🐛

- **Title:** Pressing Home or any button activates back gesture.
- **App:** OuterTune/OuterTune | **Issue:** https://github.com/OuterTune/OuterTune/issues/1044
- **Gesture Required:** `edge, swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 383s | **Steps:** 14
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Welcome to OuterTune]; Click[Home]; Click[Home]; Click[Podcasts]; Click[History]; Click[Home]; Click[Chill R&B]; Click[Home]; Click[Home]; Click[Home]

**22. anilbeesetti_nextplayer_1127** ❌ 🐛

- **Title:** Vertical swipe misbehaviour — volume/brightness gesture too sensitive in landsca
- **App:** anilbeesetti/nextplayer | **Issue:** https://github.com/anilbeesetti/nextplayer/issues/1127
- **Gesture Required:** `swipe, volume gesture, brightness gesture`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 125s | **Steps:** 5
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Open local video]; Click[Play next video]; Click[Show player controls]; Click[Screen Rotation]; Click[Open local video]

**23. ankidroid_Anki-Android_14934** ❌ 🐛

- **Title:** talkback can't see sometimes front, sometimes back and sometimes both sides of a
- **App:** ankidroid/Anki-Android | **Issue:** https://github.com/ankidroid/Anki-Android/issues/14934
- **Gesture Required:** `talkback`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 390s | **Steps:** 3
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Get Started]; Click[Continue]; Click[All files access]

**24. bartoostveen_ViTune_710** ❌ 🐛

- **Title:** Notification shows wrong album art for current song
- **App:** 25huizengek1/ViTune | **Issue:** https://github.com/25huizengek1/ViTune/issues/710
- **Gesture Required:** `swipe, notification`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 603s | **Steps:** 30
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Save Your Tears]; Click[São Paulo]; Click[Save Your Tears]; Click[São Paulo]; Click[Save Your Tears]; Click[Quick picks]; Long press[Save Your Tears]; Long press[Quick picks]; Back to previous p

**25. breezy-weather_breezy-weather_205** ❌ 🐛

- **Title:** [Location list] Swipe left animation stays after cancelling weather provider dia
- **App:** breezy-weather/breezy-weather | **Issue:** https://github.com/breezy-weather/breezy-weather/issues/205
- **Gesture Required:** `swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 552s | **Steps:** 13
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[No location added yet. Please tap ...]; Click[Open-Meteo]; Click[Current location]; Click[Location list]; Click[Current location]; Click[Location list]; Click[Tap to drag the list items ...]; Cl

**26. breezy-weather_breezy-weather_85** ❌ 🐛

- **Title:** Persistent notification setting - on / off is inverted
- **App:** breezy-weather/breezy-weather | **Issue:** https://github.com/breezy-weather/breezy-weather/issues/85
- **Gesture Required:** `swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 393s | **Steps:** 2
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Settings]; Click[Widgets & Live wallpaper]

**27. dessalines_thumb-key_371** ❌ 🐛

- **Title:** Swipe input eaten on capitalization/mode switch
- **App:** dessalines/thumb-key | **Issue:** https://github.com/dessalines/thumb-key/issues/371
- **Gesture Required:** `two, finger, swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 408s | **Steps:** 2
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[OK]; Click[Enable Thumb-Key]

**28. iamrasel_lunar-launcher_82** ❌ 💥

- **Title:** Random crashes when closing applications
- **App:** iamrasel/lunar-launcher | **Issue:** https://github.com/iamrasel/lunar-launcher/issues/82
- **Gesture Required:** `swipe`
- **Bug Type:** Crash
- **Result:** ❌ **FAIL**
- **Time:** 367s | **Steps:** 1
- **Failure Type:** `Explored but couldn't trigger crash`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Got it]

**29. libre-tube_LibreTube_8245** ❌ 🐛

- **Title:** Laggy animation when minimizing player with Back button (video & audio modes)
- **App:** libre-tube/LibreTube | **Issue:** https://github.com/libre-tube/LibreTube/issues/8245
- **Gesture Required:** `edge, swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 536s | **Steps:** 30
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Search]; Click[search src]; Click[More options]; Click[Settings]; Back to previous page; Click[Collapse]; Click[Subscriptions]; Click[Home]; Click[Retry]; Click[Change instance]

**30. msasikanth_twine_1566** ❌ 🐛

- **Title:** [BUG] Incomplete Predictive Back Animation
- **App:** msasikanth/twine | **Issue:** https://github.com/msasikanth/twine/issues/1566
- **Gesture Required:** `edge, swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 473s | **Steps:** 1
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Back to previous page

**31. you-apps_ClockYou_85** ❌ 🐛

- **Title:** App cycles through previously visited tabs on back gesture instead of closing
- **App:** you-apps/ClockYou | **Issue:** https://github.com/you-apps/ClockYou/issues/85
- **Gesture Required:** `edge_swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 614s | **Steps:** 30
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Clock]; Click[Clock]; Click[Clock]; Click[Clock]; Click[Clock]; Click[Clock]; Click[Clock]; Back to previous page; Click[Clock]; Back to previous page

**32. you-apps_ConnectYou_155** ❌ 🐛

- **Title:** Back on search bar quits the app.
- **App:** you-apps/ConnectYou | **Issue:** https://github.com/you-apps/ConnectYou/issues/155
- **Gesture Required:** `edge_swipe`
- **Bug Type:** Non-Crash
- **Result:** ❌ **FAIL**
- **Time:** 681s | **Steps:** 24
- **Failure Type:** `Non-crash bug (crash-only oracle cannot detect)`
- **Reason:** ReActDroid completed 30 steps without triggering the expected crash.
- **Actions attempted:** Click[Search]; Click[First name]; Click[Sort order]; Input[Search]; Click[HelloWorld!]; Input[Search]; Input[HelloWorld!]; Back to previous page; Click[HelloWorld!]; Click[Search]

---

## Appendix: Why ReActDroid Scores 5%

### Two Fundamental Limitations

1. **Crash-only oracle:** ReActDroid checks logcat for `FATAL EXCEPTION`. It cannot detect the 87 non-crash bugs (behavioral, visual, UI state bugs). This caps its theoretical maximum at 13%.

2. **No gesture commands:** Even for the 13 crash bugs, ReActDroid only has click, long_click, scroll_up, scroll_down. It cannot perform double_tap, pinch, drag_and_drop, edge_swipe, or orientation changes needed to reach many crash trigger points.

### Performance on Crash vs Non-Crash Bugs

| Bug Type | Total | Success | Rate |
|----------|-------|---------|------|
| 💥 Crash | 13 | 2 | 15% |
| 🐛 Non-Crash | 87 | 3 | 3% |
| **Total** | **100** | **5** | **5%** |

### Comparison with CARBON

| Aspect | ReActDroid | CARBON |
|--------|-----------|--------|
| LLM | GPT-3.5 (ReAct prompting) | Gemini 2.5 Pro (conversational) |
| UI Understanding | Text-only hierarchy | Annotated screenshots + text hierarchy |
| Gestures | click, long_click, scroll (4 actions) | 15+ gestures (pinch, drag, edge_swipe, etc.) |
| Oracle | Crash only (logcat) | Crash detection + Visual/LLM verification |
| Input | One-sentence crash overview | Full bug report text |
| Success Rate | 5% | 92% |
| Crash Bug Rate | 2/13 (15%) | 10/13 (77%) |
| Non-Crash Bug Rate | 3/87 (3%) | 82/87 (94%) |

---
*Report generated from ReActDroid test logs across 8 gesture categories.*