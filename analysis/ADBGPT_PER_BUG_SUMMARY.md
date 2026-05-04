# AdbGPT — Complete Per-Bug Summary (All 100 Bugs)

> **Total:** 54 SUCCESS / 46 FAIL = 54%
> **Note:** SUCCESS = step completion only (no bug verification oracle)
> **AdbGPT actions:** tap, input, scroll, double tap, long tap

---

## Double Tap (19 bugs — 10✅ 9❌)

### 1. FossifyOrg_Calendar_273 ✅

- **App:** FossifyOrg/Calendar
- **Title:** Setting a default event length doesn't change the default event length
- **Result:** ✅ **SUCCESS**
- **Time:** 110s
- **Steps completed:** 4/4
- **Actions executed:** 6 total (Taps: 6, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 6
- **Extracted S2R steps:**
  1. [Input] [default event duration] [35 minutes]
  2. [Double tap] [calendar]
  3. [Input] [default event duration] [35 minutes]
  4. [Double tap] [calendar]
- **Reason:** AdbGPT completed all 4 extracted S2R steps without errors.

### 2. FossifyOrg_Gallery_363 ✅

- **App:** FossifyOrg/Gallery
- **Title:** webp images when double tapped don't zoom to height of image
- **Result:** ✅ **SUCCESS**
- **Time:** 128s
- **Steps completed:** 4/4
- **Actions executed:** 6 total (Taps: 6, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 8
- **Extracted S2R steps:**
  1. [Tap] [.webp images]
  2. [Double tap] [screen]
  3. [Tap] [.webp images]
  4. [Double tap] [screen]
- **Reason:** AdbGPT completed all 4 extracted S2R steps without errors.

### 3. FossifyOrg_Gallery_678 ✅

- **App:** FossifyOrg/Gallery
- **Title:** 'Allow 1:1 zooming in with two double taps' not working when pixel size of the p
- **Result:** ✅ **SUCCESS**
- **Time:** 143s
- **Steps completed:** 6/6
- **Actions executed:** 10 total (Taps: 10, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 6
- **Extracted S2R steps:**
  1. [Tap] [photo]
  2. [Double tap] [photo]
  3. [Double tap] [photo]
  4. [Tap] [photo]
  5. [Double tap] [photo]
  6. [Double tap] [photo]
- **Reason:** AdbGPT completed all 6 extracted S2R steps without errors.

### 4. FossifyOrg_Gallery_846 ❌

- **App:** FossifyOrg/Gallery
- **Title:** "Fill screen" zoom on double tap ignores disabled "Show notch if available"
- **Result:** ❌ **FAIL**
- **Time:** 193s
- **Steps completed:** 0/8
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [Show notch if available]
  2. [Tap] [image]
  3. [Double tap] [image]
  4. [Scroll] [up/down]
  5. [Tap] [Show notch if available]
  6. [Tap] [image]
  7. [Double tap] [image]
  8. [Scroll] [up/down]
- **Reason:** AdbGPT only completed 0/8 steps. Could not match remaining steps to GUI elements.

### 5. FossifyOrg_Gallery_847 ✅

- **App:** FossifyOrg/Gallery
- **Title:** Invalid "fill screen" zoom for GIF images on double-tap
- **Result:** ✅ **SUCCESS**
- **Time:** 102s
- **Steps completed:** 4/4
- **Actions executed:** 6 total (Taps: 6, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 8
- **Extracted S2R steps:**
  1. [Tap] [GIF image]
  2. [Double tap] [GIF image]
  3. [Tap] [GIF image]
  4. [Double tap] [GIF image]
- **Reason:** AdbGPT completed all 4 extracted S2R steps without errors.

### 6. LawnchairLauncher_lawnchair_2910 ❌

- **App:** LawnchairLauncher/lawnchair
- **Title:** [BUG] Double tap to sleep no longer works through root access
- **Result:** ❌ **FAIL**
- **Time:** 218s
- **Steps completed:** 0/4
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 10
- **Extracted S2R steps:**
  1. [Tap] [suspend' function]
  2. [Double tap] [screen]
  3. [Tap] [suspend' function]
  4. [Double tap] [screen]
- **Reason:** AdbGPT only completed 0/4 steps. Could not match remaining steps to GUI elements.

### 7. LawnchairLauncher_lawnchair_4125 ✅

- **App:** LawnchairLauncher/lawnchair
- **Title:** [BUG] android 14, no option to allow restricted setting
- **Result:** ✅ **SUCCESS**
- **Time:** 182s
- **Steps completed:** 8/8
- **Actions executed:** 8 total (Taps: 8, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 16
- **Extracted S2R steps:**
  1. [Tap] [settings]
  2. [Tap] [gestures]
  3. [Tap] [double tap to sleep]
  4. [Tap] [kebab 3 dot menu]
  5. [Tap] [settings]
  6. [Tap] [gestures]
  7. [Tap] [double tap to sleep]
  8. [Tap] [kebab 3 dot menu]
- **Reason:** AdbGPT completed all 8 extracted S2R steps without errors.

### 8. LawnchairLauncher_lawnchair_4786 ✅

- **App:** LawnchairLauncher/lawnchair
- **Title:** [BUG] Crash when trying to move item using TalkBack action
- **Result:** ✅ **SUCCESS**
- **Time:** 300s
- **Steps completed:** 12/12
- **Actions executed:** 20 total (Taps: 20, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 12
- **Extracted S2R steps:**
  1. [Tap] [widget]
  2. [Double tap] [Actions]
  3. [Double tap] [Move item]
  4. [Tap] [widget]
  5. [Double tap] [Actions]
  6. [Double tap] [Move item]
  7. [Tap] [widget]
  8. [Double tap] [Actions]
  9. [Double tap] [Move item]
  10. [Tap] [widget]
  11. [Double tap] [Actions]
  12. [Double tap] [Move item]
- **Reason:** AdbGPT completed all 12 extracted S2R steps without errors.

### 9. Pool-Of-Tears_GreenStash_170 ❌

- **App:** Pool-Of-Tears/GreenStash
- **Title:** [Bug]: Some accessibility issues
- **Result:** ❌ **FAIL**
- **Time:** 32s
- **Steps completed:** 0/0
- **Actions executed:** 0 total (Taps: 0, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 0
- **Extracted S2R steps:**
  (no steps extracted)
- **Reason:** AdbGPT failed to extract any S2R steps from the bug report. The LLM response could not be parsed into actionable steps.

### 10. TeamNewPipe_NewPipe_10750 ❌

- **App:** TeamNewPipe/NewPipe
- **Title:** Video playback randomly "closed/crashed", and content loaded but stuck buffering
- **Result:** ❌ **FAIL**
- **Time:** 194s
- **Steps completed:** 0/6
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [video]
  2. [Tap] [video]
  3. [Double tap] [side of video player]
  4. [Tap] [video]
  5. [Tap] [video]
  6. [Double tap] [side of video player]
- **Reason:** AdbGPT only completed 0/6 steps. Could not match remaining steps to GUI elements.

### 11. TeamNewPipe_NewPipe_8338 ❌

- **App:** TeamNewPipe/NewPipe
- **Title:** Swipe down gesture of Player UI does not work all the times
- **Result:** ❌ **FAIL**
- **Time:** 183s
- **Steps completed:** 0/4
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Double tap] [video]
  2. [Scroll] [down]
  3. [Double tap] [video]
  4. [Scroll] [down]
- **Reason:** AdbGPT only completed 0/4 steps. Could not match remaining steps to GUI elements.

### 12. abdallahmehiz_mpvKt_184 ✅

- **App:** abdallahmehiz/mpvKt
- **Title:** Tap error while playing video
- **Result:** ✅ **SUCCESS**
- **Time:** 178s
- **Steps completed:** 6/6
- **Actions executed:** 8 total (Taps: 8, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 6
- **Extracted S2R steps:**
  1. [Tap] [any video]
  2. [Double tap] [video player]
  3. [Tap] [video player]
  4. [Tap] [any video]
  5. [Double tap] [video player]
  6. [Tap] [video player]
- **Reason:** AdbGPT completed all 6 extracted S2R steps without errors.

### 13. ankidroid_Anki-Android_17393 ❌

- **App:** ankidroid/Anki-Android
- **Title:** [BUG]: IO Cards Go to the Wrong Deck
- **Result:** ❌ **FAIL**
- **Time:** 211s
- **Steps completed:** 0/22
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [Settings]
  2. [Tap] [General]
  3. [Tap] [Deck for new cards]
  4. [Tap] [use current deck]
  5. [Tap] [back]
  6. [Tap] [deck]
  7. [Double tap] [＋]
  8. [Tap] [IO note type]
  9. [Tap] [deck]
  10. [Tap] [deck]
  11. [Tap] [Create]
  12. [Tap] [Settings]
  13. [Tap] [General]
  14. [Tap] [Deck for new cards]
  15. [Tap] [use current deck]
  16. [Tap] [back]
  17. [Tap] [deck]
  18. [Double tap] [+]
  19. [Tap] [IO note type]
  20. [Tap] [deck]
  21. [Tap] [deck]
  22. [Tap] [Create]
- **Reason:** AdbGPT only completed 0/22 steps. Could not match remaining steps to GUI elements.

### 14. cromaguy_Rhythm_281 ❌

- **App:** cromaguy/Rhythm
- **Title:** [BUG]: Double tap needed on Touch Gestures view of Onboarding Setup
- **Result:** ❌ **FAIL**
- **Time:** 236s
- **Steps completed:** 1/4
- **Actions executed:** 11 total (Taps: 1, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 11
- **Extracted S2R steps:**
  1. [Tap] [Next Button]
  2. [Tap] [Back button]
  3. [Tap] [Next Button]
  4. [Tap] [Back button]
- **Reason:** AdbGPT only completed 1/4 steps. Could not match remaining steps to GUI elements.

### 15. fast4x_RiMusic_1152 ✅

- **App:** fast4x/RiMusic
- **Title:** Unclear Linking and Unresponsive Buttons in Player View
- **Result:** ✅ **SUCCESS**
- **Time:** 131s
- **Steps completed:** 4/4
- **Actions executed:** 4 total (Taps: 4, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 4
- **Extracted S2R steps:**
  1. [Tap] [player view]
  2. [Tap] [song title]
  3. [Tap] [player view]
  4. [Tap] [song title]
- **Reason:** AdbGPT completed all 4 extracted S2R steps without errors.

### 16. gsantner_markor_2746 ❌

- **App:** gsantner/markor
- **Title:** Markor does not recognize URL/link anymore
- **Result:** ❌ **FAIL**
- **Time:** 197s
- **Steps completed:** 0/4
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Input] [text editor] [a simple URL]
  2. [Double tap] [URL]
  3. [Input] [text editor] [a simple URL]
  4. [Double tap] [URL]
- **Reason:** AdbGPT only completed 0/4 steps. Could not match remaining steps to GUI elements.

### 17. openboard-team_openboard_613 ❌

- **App:** openboard-team/openboard
- **Title:** Sometimes the spellchecker flags correctly spelt words if one adds a full-stop t
- **Result:** ❌ **FAIL**
- **Time:** 211s
- **Steps completed:** 0/2
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Input] [text input field] [<properly spelt word>.]
  2. [Input] [text input field] [<properly spelt word>.]
- **Reason:** AdbGPT only completed 0/2 steps. Could not match remaining steps to GUI elements.

### 18. openboard-team_openboard_758 ✅

- **App:** openboard-team/openboard
- **Title:** Accessibility: The button to go to the previous level does not work properly
- **Result:** ✅ **SUCCESS**
- **Time:** 141s
- **Steps completed:** 6/6
- **Actions executed:** 8 total (Taps: 8, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 10
- **Extracted S2R steps:**
  1. [Tap] [Open Board settings]
  2. [Tap] [any settings section]
  3. [Double tap] [button in the upper left corner]
  4. [Tap] [Open Board settings]
  5. [Tap] [any settings section]
  6. [Double tap] [button in the upper left corner]
- **Reason:** AdbGPT completed all 6 extracted S2R steps without errors.

### 19. syt0r_Kanji-Dojo_291 ✅

- **App:** syt0r/Kanji-Dojo
- **Title:** Double-tapping back arrow while transitioning from vocab info to practice skips 
- **Result:** ✅ **SUCCESS**
- **Time:** 224s
- **Steps completed:** 8/8
- **Actions executed:** 10 total (Taps: 10, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 8
- **Extracted S2R steps:**
  1. [Tap] [new practice session]
  2. [Tap] [letter/vocab card]
  3. [Tap] [diagonal arrow]
  4. [Double tap] [back arrow]
  5. [Tap] [new practice session]
  6. [Tap] [letter/vocab card]
  7. [Tap] [diagonal arrow]
  8. [Double tap] [back arrow]
- **Reason:** AdbGPT completed all 8 extracted S2R steps without errors.

---

## Drag & Drop (9 bugs — 5✅ 4❌)

### 1. FossifyOrg_Launcher_304 ✅

- **App:** FossifyOrg/Launcher
- **Title:** Accidently creating invisible folders in dock
- **Result:** ✅ **SUCCESS**
- **Time:** 201s
- **Steps completed:** 8/8
- **Actions executed:** 8 total (Taps: 2, Swipes: 6, Keys: 0, Text: 0)
- **MISSING steps:** 8
- **Extracted S2R steps:**
  1. [Long tap] [app]
  2. [Long tap] [app]
  3. [Long tap] [app in the invisible folder]
  4. [Tap] [remove button]
  5. [Long tap] [app]
  6. [Long tap] [app]
  7. [Long tap] [app in the invisible folder]
  8. [Tap] [remove button]
- **Reason:** AdbGPT completed all 8 extracted S2R steps without errors.

### 2. FossifyOrg_Notes_59 ✅

- **App:** FossifyOrg/Notes
- **Title:** Reordering checklists works strangely with move checked to bottom
- **Result:** ✅ **SUCCESS**
- **Time:** 317s
- **Steps completed:** 14/14
- **Actions executed:** 14 total (Taps: 12, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 22
- **Extracted S2R steps:**
  1. [Tap] [new checklist]
  2. [Input] [item text field] [item 1]
  3. [Input] [item text field] [item 2]
  4. [Tap] [checkbox]
  5. [Tap] [Sort by]
  6. [Tap] [Move checked items to the bottom]
  7. [Long tap] [unchecked item]
  8. [Tap] [new checklist]
  9. [Input] [item text field] [item 1]
  10. [Input] [item text field] [item 2]
  11. [Tap] [checkbox]
  12. [Tap] [Sort by]
  13. [Tap] [Move checked items to the bottom]
  14. [Long tap] [unchecked item]
- **Reason:** AdbGPT completed all 14 extracted S2R steps without errors.

### 3. LawnchairLauncher_lawnchair_1247 ❌

- **App:** LawnchairLauncher/lawnchair
- **Title:** the launcher kees crashign when I attempt to move stuff
- **Result:** ❌ **FAIL**
- **Time:** 258s
- **Steps completed:** 1/6
- **Actions executed:** 11 total (Taps: 0, Swipes: 1, Keys: 10, Text: 0)
- **MISSING steps:** 11
- **Extracted S2R steps:**
  1. [Long tap] [item]
  2. [Tap] [move]
  3. [Tap] [new place]
  4. [Long tap] [item]
  5. [Tap] [move]
  6. [Tap] [new place]
- **Reason:** AdbGPT only completed 1/6 steps. Could not match remaining steps to GUI elements.

### 4. LawnchairLauncher_lawnchair_4320 ✅

- **App:** LawnchairLauncher/lawnchair
- **Title:** [BUG] Unable to add any widget
- **Result:** ✅ **SUCCESS**
- **Time:** 110s
- **Steps completed:** 4/4
- **Actions executed:** 4 total (Taps: 2, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 4
- **Extracted S2R steps:**
  1. [Tap] [widget]
  2. [Long tap] [widget]
  3. [Tap] [widget]
  4. [Long tap] [widget]
- **Reason:** AdbGPT completed all 4 extracted S2R steps without errors.

### 5. MetrolistGroup_Metrolist_3227 ❌

- **App:** MetrolistGroup/Metrolist
- **Title:** Replacement of new song with old song
- **Result:** ❌ **FAIL**
- **Time:** 204s
- **Steps completed:** 0/8
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [add button]
  2. [Tap] [song]
  3. [Long tap] [new song]
  4. [Scroll] [up]
  5. [Tap] [add button]
  6. [Tap] [song]
  7. [Long tap] [new song]
  8. [Scroll] [up]
- **Reason:** AdbGPT only completed 0/8 steps. Could not match remaining steps to GUI elements.

### 6. MetrolistGroup_Metrolist_3561 ❌

- **App:** MetrolistGroup/Metrolist
- **Title:** Weird Bug when changing list order in custom order format
- **Result:** ❌ **FAIL**
- **Time:** 205s
- **Steps completed:** 0/13
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [create playlist]
  2. [Tap] [song]
  3. [Long tap] [song]
  4. [Tap] [add song]
  5. [Tap] [song]
  6. [Long tap] [song]
  7. [Tap] [create playlist]
  8. [Tap] [song]
  9. [Tap] [song]
  10. [Long tap] [song]
  11. [Tap] [add song]
  12. [Tap] [song]
  13. [Long tap] [song]
- **Reason:** AdbGPT only completed 0/13 steps. Could not match remaining steps to GUI elements.

### 7. NeoApplications_Neo-Launcher_130 ✅

- **App:** NeoApplications/Neo-Launcher
- **Title:** Changing the first app in a folder with Covers enabled breaks the folder
- **Result:** ✅ **SUCCESS**
- **Time:** 217s
- **Steps completed:** 0/20
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Long tap] [folder]
  2. [Tap] [Covers]
  3. [Tap] [folder]
  4. [Long tap] [App-B]
  5. [Long tap] [folder]
  6. [Tap] [Covers]
  7. [Tap] [folder]
  8. [Tap] [desktop]
  9. [Tap] [folder]
  10. [Scroll] [folder]
  11. [Long tap] [folder]
  12. [Tap] [Covers]
  13. [Tap] [folder]
  14. [Long tap] [App-B]
  15. [Long tap] [folder]
  16. [Tap] [Covers]
  17. [Tap] [folder]
  18. [Tap] [desktop]
  19. [Tap] [folder]
  20. [Scroll] [folder]
- **Reason:** AdbGPT triggered a crash detected in logcat (FATAL EXCEPTION for com.saggitt.omega).

### 8. breezy-weather_breezy-weather_2159 ❌

- **App:** breezy-weather/breezy-weather
- **Title:** [Old Android versions default launcher] Can't add widget to home screen
- **Result:** ❌ **FAIL**
- **Time:** 208s
- **Steps completed:** 0/8
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 10
- **Extracted S2R steps:**
  1. [Long tap] [home screen empty area]
  2. [Tap] [Widget]
  3. [Tap] [Breezy Weather widget]
  4. [Tap] [Done]
  5. [Long tap] [home screen empty area]
  6. [Tap] [Widget]
  7. [Tap] [Breezy Weather widget]
  8. [Tap] [Done]
- **Reason:** AdbGPT only completed 0/8 steps. Could not match remaining steps to GUI elements.

### 9. fcitx5-android_fcitx5-android_841 ✅

- **App:** fcitx5-android/fcitx5-android
- **Title:** Crash somtimes on showing keyboard when the preferred input method is supported 
- **Result:** ✅ **SUCCESS**
- **Time:** 142s
- **Steps completed:** 6/6
- **Actions executed:** 6 total (Taps: 4, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 6
- **Extracted S2R steps:**
  1. [Tap] [Input method]
  2. [Tap] [RIME]
  3. [Long tap] [RIME]
  4. [Tap] [Input method]
  5. [Tap] [RIME]
  6. [Long tap] [RIME]
- **Reason:** AdbGPT completed all 6 extracted S2R steps without errors.

---

## Long Press (9 bugs — 3✅ 6❌)

### 1. Anthonyy232_Paperize_325 ❌

- **App:** Anthonyy232/Paperize
- **Title:** [Bug] Crashing when adding images
- **Result:** ❌ **FAIL**
- **Time:** 208s
- **Steps completed:** 0/14
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [library tab]
  2. [Tap] [plus sign]
  3. [Input] [name] [technical album]
  4. [Tap] [create button]
  5. [Tap] [plus sign]
  6. [Long tap] [image]
  7. [Tap] [plus icon]
  8. [Tap] [library tab]
  9. [Tap] [plus sign]
  10. [Input] [name] [technical album]
  11. [Tap] [create button]
  12. [Tap] [plus sign]
  13. [Long tap] [image]
  14. [Tap] [plus icon]
- **Reason:** AdbGPT only completed 0/14 steps. Could not match remaining steps to GUI elements.

### 2. Crustack_NotallyX_570 ✅

- **App:** Crustack/NotallyX
- **Title:** App crash when note is selected, search filter changed and another note is selec
- **Result:** ✅ **SUCCESS**
- **Time:** 337s
- **Steps completed:** 16/16
- **Actions executed:** 16 total (Taps: 12, Swipes: 4, Keys: 0, Text: 0)
- **MISSING steps:** 24
- **Extracted S2R steps:**
  1. [Tap] [add note]
  2. [Input] [note content] [Note A]
  3. [Tap] [add note]
  4. [Input] [note content] [Note B]
  5. [Long tap] [Note A]
  6. [Tap] [search]
  7. [Input] [search input field] [Note B]
  8. [Long tap] [Note B]
  9. [Tap] [add note]
  10. [Input] [note content] [Note A]
  11. [Tap] [add note]
  12. [Input] [note content] [Note B]
  13. [Long tap] [Note A]
  14. [Tap] [search]
  15. [Input] [search input field] [Note B]
  16. [Long tap] [Note B]
- **Reason:** AdbGPT completed all 16 extracted S2R steps without errors.

### 3. FossifyOrg_File-Manager_195 ✅

- **App:** FossifyOrg/File-Manager
- **Title:** Unnecessary refresh of ZIP file icons when closing bottom sheets
- **Result:** ✅ **SUCCESS**
- **Time:** 211s
- **Steps completed:** 10/10
- **Actions executed:** 10 total (Taps: 8, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [Files tab]
  2. [Tap] [folder]
  3. [Long tap] [ZIP file]
  4. [Tap] [Open with icon]
  5. [Tap] [close button]
  6. [Tap] [Files tab]
  7. [Tap] [folder]
  8. [Long tap] [ZIP file]
  9. [Tap] [Open with icon]
  10. [Tap] [close button]
- **Reason:** AdbGPT completed all 10 extracted S2R steps without errors.

### 4. FossifyOrg_Launcher_198 ❌

- **App:** FossifyOrg/Launcher
- **Title:** Folder rename dialog: Dark text on dark background
- **Result:** ❌ **FAIL**
- **Time:** 196s
- **Steps completed:** 0/2
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 10
- **Extracted S2R steps:**
  1. [Long tap] [folder]
  2. [Long tap] [folder]
- **Reason:** AdbGPT only completed 0/2 steps. Could not match remaining steps to GUI elements.

### 5. FossifyOrg_Messages_359 ❌

- **App:** FossifyOrg/Messages
- **Title:** Can't scroll or see participants on conversation details page
- **Result:** ❌ **FAIL**
- **Time:** 194s
- **Steps completed:** 0/8
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Long tap] [conversation]
  2. [Tap] [More options]
  3. [Tap] [Conversation details]
  4. [Scroll] [down]
  5. [Long tap] [conversation]
  6. [Tap] [More options]
  7. [Tap] [Conversation details]
  8. [Scroll] [down]
- **Reason:** AdbGPT only completed 0/8 steps. Could not match remaining steps to GUI elements.

### 6. FossifyOrg_Messages_416 ❌

- **App:** FossifyOrg/Messages
- **Title:** New conversation shortcut doesn't work
- **Result:** ❌ **FAIL**
- **Time:** 209s
- **Steps completed:** 1/4
- **Actions executed:** 11 total (Taps: 0, Swipes: 1, Keys: 10, Text: 0)
- **MISSING steps:** 11
- **Extracted S2R steps:**
  1. [Long tap] [app icon]
  2. [Tap] [`New conversation` shortcut]
  3. [Long tap] [app icon]
  4. [Tap] [`New conversation` shortcut]
- **Reason:** AdbGPT only completed 1/4 steps. Could not match remaining steps to GUI elements.

### 7. FossifyOrg_Messages_641 ❌

- **App:** FossifyOrg/Messages
- **Title:** SMS scheduling not working
- **Result:** ❌ **FAIL**
- **Time:** 202s
- **Steps completed:** 0/12
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 10
- **Extracted S2R steps:**
  1. [Tap] [conversation]
  2. [Input] [message input field] [a message]
  3. [Long tap] [send button]
  4. [Tap] [date]
  5. [Tap] [time]
  6. [Tap] [confirm button]
  7. [Tap] [conversation]
  8. [Input] [message input field] [a message]
  9. [Long tap] [send button]
  10. [Tap] [date]
  11. [Tap] [time]
  12. [Tap] [confirm button]
- **Reason:** AdbGPT only completed 0/12 steps. Could not match remaining steps to GUI elements.

### 8. breezy-weather_breezy-weather_1639 ❌

- **App:** breezy-weather/breezy-weather
- **Title:** weather wallpaper causes launcher to freeze and app background closed
- **Result:** ❌ **FAIL**
- **Time:** 219s
- **Steps completed:** 0/8
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 10
- **Extracted S2R steps:**
  1. [Tap] [weather wallpaper]
  2. [Tap] [set for main screen and lock screen]
  3. [Tap] [Vanadium]
  4. [Tap] [new incognito tab]
  5. [Tap] [weather wallpaper]
  6. [Tap] [set for main screen and lock screen]
  7. [Tap] [Vanadium]
  8. [Tap] [new incognito tab]
- **Reason:** AdbGPT only completed 0/8 steps. Could not match remaining steps to GUI elements.

### 9. espresso3389_methings_34 ✅

- **App:** espresso3389/methings
- **Title:** Image preview UX gaps and instability when using Select Text on image blocks
- **Result:** ✅ **SUCCESS**
- **Time:** 147s
- **Steps completed:** 9/9
- **Actions executed:** 9 total (Taps: 4, Swipes: 5, Keys: 0, Text: 0)
- **MISSING steps:** 6
- **Extracted S2R steps:**
  1. [Tap] [image]
  2. [Scroll] [left]
  3. [Scroll] [right]
  4. [Long tap] [image]
  5. [Tap] [menu option]
  6. [Tap] [image]
  7. [Scroll] [left]
  8. [Long tap] [image]
  9. [Tap] [menu option]
- **Reason:** AdbGPT completed all 9 extracted S2R steps without errors.

---

## Orientation (6 bugs — 4✅ 2❌)

### 1. FossifyOrg_Calendar_1042 ✅

- **App:** FossifyOrg/Calendar
- **Title:** The current selected day, month, week, year is not preserved after rotating
- **Result:** ✅ **SUCCESS**
- **Time:** 77s
- **Steps completed:** 4/4
- **Actions executed:** 4 total (Taps: 2, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 2
- **Extracted S2R steps:**
  1. [Tap] [day view]
  2. [Scroll] [left]
  3. [Tap] [day view]
  4. [Scroll] [left]
- **Reason:** AdbGPT completed all 4 extracted S2R steps without errors.

### 2. FossifyOrg_Camera_91 ❌

- **App:** FossifyOrg/Camera
- **Title:** Countdown timer does not honor device orientation
- **Result:** ❌ **FAIL**
- **Time:** 198s
- **Steps completed:** 0/4
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 10
- **Extracted S2R steps:**
  1. [Input] [timer] [10 seconds]
  2. [Tap] [shutter button]
  3. [Input] [timer] [10 seconds]
  4. [Tap] [shutter button]
- **Reason:** AdbGPT only completed 0/4 steps. Could not match remaining steps to GUI elements.

### 3. FossifyOrg_Clock_85 ✅

- **App:** FossifyOrg/Clock
- **Title:** Snooze not working in landscape
- **Result:** ✅ **SUCCESS**
- **Time:** 74s
- **Steps completed:** 5/5
- **Actions executed:** 5 total (Taps: 2, Swipes: 3, Keys: 0, Text: 0)
- **MISSING steps:** 2
- **Extracted S2R steps:**
  1. [Tap] [alarm]
  2. [Scroll] [Direction]
  3. [Scroll] [right]
  4. [Tap] [alarm]
  5. [Scroll] [right]
- **Reason:** AdbGPT completed all 5 extracted S2R steps without errors.

### 4. FossifyOrg_Contacts_197 ❌

- **App:** FossifyOrg/Contacts
- **Title:** View always changed to contact list when rotating the phone
- **Result:** ❌ **FAIL**
- **Time:** 201s
- **Steps completed:** 0/2
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [favourites tab]
  2. [Tap] [favourites tab]
- **Reason:** AdbGPT only completed 0/2 steps. Could not match remaining steps to GUI elements.

### 5. Waboodoo_HTTP-Shortcuts_262 ✅

- **App:** Waboodoo/HTTP-Shortcuts
- **Title:** [BUG] several dialogs disappear on screen rotation
- **Result:** ✅ **SUCCESS**
- **Time:** 121s
- **Steps completed:** 4/4
- **Actions executed:** 4 total (Taps: 4, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 6
- **Extracted S2R steps:**
  1. [Tap] [Main activity]
  2. [Tap] [add button]
  3. [Tap] [Main activity]
  4. [Tap] [add button]
- **Reason:** AdbGPT completed all 4 extracted S2R steps without errors.

### 6. ankidroid_Anki-Android_16410 ✅

- **App:** ankidroid/Anki-Android
- **Title:** [BUG]: Changing screen orientation clears stats' search options
- **Result:** ✅ **SUCCESS**
- **Time:** 185s
- **Steps completed:** 8/8
- **Actions executed:** 8 total (Taps: 8, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 16
- **Extracted S2R steps:**
  1. [Tap] [statistics]
  2. [Input] [search bar] [something]
  3. [Tap] [collection]
  4. [Tap] [all history]
  5. [Tap] [statistics]
  6. [Input] [search bar] [something]
  7. [Tap] [collection]
  8. [Tap] [all history]
- **Reason:** AdbGPT completed all 8 extracted S2R steps without errors.

---

## Pinch/Zoom (14 bugs — 8✅ 6❌)

### 1. Droid-ify_client_583 ✅

- **App:** Droid-ify/client
- **Title:** [BUG] Swiping images zooms instead of zooming
- **Result:** ✅ **SUCCESS**
- **Time:** 74s
- **Steps completed:** 4/4
- **Actions executed:** 4 total (Taps: 2, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 2
- **Extracted S2R steps:**
  1. [Tap] [preview image]
  2. [Scroll] [left]
  3. [Tap] [preview image]
  4. [Scroll] [left]
- **Reason:** AdbGPT completed all 4 extracted S2R steps without errors.

### 2. FossifyOrg_Calendar_621 ✅

- **App:** FossifyOrg/Calendar
- **Title:** Zoom level in weekly view locks
- **Result:** ✅ **SUCCESS**
- **Time:** 88s
- **Steps completed:** 6/6
- **Actions executed:** 6 total (Taps: 2, Swipes: 4, Keys: 0, Text: 0)
- **MISSING steps:** 4
- **Extracted S2R steps:**
  1. [Tap] [Weekly view]
  2. [Scroll] [down]
  3. [Scroll] [right]
  4. [Tap] [Weekly view]
  5. [Scroll] [down]
  6. [Scroll] [right]
- **Reason:** AdbGPT completed all 6 extracted S2R steps without errors.

### 3. FossifyOrg_Camera_23 ✅

- **App:** FossifyOrg/Camera
- **Title:** Doesn't use zoom camera to zoom
- **Result:** ✅ **SUCCESS**
- **Time:** 32s
- **Steps completed:** 2/2
- **Actions executed:** 2 total (Taps: 0, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 0
- **Extracted S2R steps:**
  1. [Scroll] [camera view]
  2. [Scroll] [camera view]
- **Reason:** AdbGPT completed all 2 extracted S2R steps without errors.

### 4. FossifyOrg_Gallery_289 ✅

- **App:** FossifyOrg/Gallery
- **Title:** "Allow deep zooming images" creates artifacts in many images
- **Result:** ✅ **SUCCESS**
- **Time:** 179s
- **Steps completed:** 8/8
- **Actions executed:** 8 total (Taps: 8, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 10
- **Extracted S2R steps:**
  1. [Tap] [Allow deep zooming images]
  2. [Tap] [image]
  3. [Tap] [back button]
  4. [Tap] [image]
  5. [Tap] [Allow deep zooming images]
  6. [Tap] [image]
  7. [Tap] [back button]
  8. [Tap] [image]
- **Reason:** AdbGPT completed all 8 extracted S2R steps without errors.

### 5. FossifyOrg_Gallery_642 ✅

- **App:** FossifyOrg/Gallery
- **Title:** Zoom doesn't work in photos
- **Result:** ✅ **SUCCESS**
- **Time:** 102s
- **Steps completed:** 6/6
- **Actions executed:** 8 total (Taps: 6, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 4
- **Extracted S2R steps:**
  1. [Tap] [photo]
  2. [Scroll] [to another photo]
  3. [Double tap] [photo]
  4. [Tap] [photo]
  5. [Scroll] [to another photo]
  6. [Double tap] [photo]
- **Reason:** AdbGPT completed all 6 extracted S2R steps without errors.

### 6. FossifyOrg_Gallery_728 ✅

- **App:** FossifyOrg/Gallery
- **Title:** (Deep zooming) Can not pan after releasing only one finger after pinch zooming
- **Result:** ✅ **SUCCESS**
- **Time:** 115s
- **Steps completed:** 10/10
- **Actions executed:** 10 total (Taps: 2, Swipes: 8, Keys: 0, Text: 0)
- **MISSING steps:** 2
- **Extracted S2R steps:**
  1. [Tap] [picture]
  2. [Scroll] [zoom in]
  3. [Scroll] [pan]
  4. [Scroll] [zoom in/out]
  5. [Scroll] [pan]
  6. [Tap] [picture]
  7. [Scroll] [zoom in]
  8. [Scroll] [pan]
  9. [Scroll] [zoom in/out]
  10. [Scroll] [pan]
- **Reason:** AdbGPT completed all 10 extracted S2R steps without errors.

### 7. FossifyOrg_Paint_125 ✅

- **App:** FossifyOrg/Paint
- **Title:** Touch location and pen location different after zooming/rotation
- **Result:** ✅ **SUCCESS**
- **Time:** 82s
- **Steps completed:** 3/3
- **Actions executed:** 3 total (Taps: 1, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 1
- **Extracted S2R steps:**
  1. [Scroll] [canvas]
  2. [Scroll] [canvas]
  3. [Tap] [canvas]
- **Reason:** AdbGPT completed all 3 extracted S2R steps without errors.

### 8. FossifyOrg_Paint_25 ✅

- **App:** FossifyOrg/Paint
- **Title:** Eraser size not relative to zoom on minimum size
- **Result:** ✅ **SUCCESS**
- **Time:** 154s
- **Steps completed:** 6/6
- **Actions executed:** 8 total (Taps: 8, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 6
- **Extracted S2R steps:**
  1. [Input] [brush size] [minimum]
  2. [Tap] [eraser]
  3. [Double tap] [canvas]
  4. [Input] [brush size] [minimum]
  5. [Tap] [eraser]
  6. [Double tap] [canvas]
- **Reason:** AdbGPT completed all 6 extracted S2R steps without errors.

### 9. ankidroid_Anki-Android_16135 ❌

- **App:** ankidroid/Anki-Android
- **Title:** [BUG]: Zooming in Statistics Page
- **Result:** ❌ **FAIL**
- **Time:** 204s
- **Steps completed:** 0/8
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [Statistics]
  2. [Double tap] [screen]
  3. [Double tap] [screen]
  4. [Scroll] [bottom]
  5. [Tap] [Statistics]
  6. [Double tap] [screen]
  7. [Double tap] [screen]
  8. [Scroll] [bottom]
- **Reason:** AdbGPT only completed 0/8 steps. Could not match remaining steps to GUI elements.

### 10. ankidroid_Anki-Android_17667 ❌

- **App:** ankidroid/Anki-Android
- **Title:** [BUG]: Width of "Deck options" page does not/cannot fit to screen (display)
- **Result:** ❌ **FAIL**
- **Time:** 0s
- **Steps completed:** 0/0
- **Actions executed:** 0 total (Taps: 0, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 0
- **Extracted S2R steps:**
  (no steps extracted)
- **Reason:** AdbGPT failed to extract any S2R steps from the bug report. The LLM response could not be parsed into actionable steps.

### 11. saber-notes_saber_192 ❌

- **App:** saber-notes/saber
- **Title:** Two finger detection need improvement
- **Result:** ❌ **FAIL**
- **Time:** 201s
- **Steps completed:** 0/8
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [Finger Drawing mode button]
  2. [Tap] [pen button]
  3. [Tap] [Zoom in button]
  4. [Scroll] [down]
  5. [Tap] [Finger Drawing mode button]
  6. [Tap] [pen button]
  7. [Tap] [Zoom in button]
  8. [Scroll] [down]
- **Reason:** AdbGPT only completed 0/8 steps. Could not match remaining steps to GUI elements.

### 12. streetcomplete_StreetComplete_6068 ❌

- **App:** streetcomplete/StreetComplete
- **Title:** OutOfMemoryError when downloading after zoom out
- **Result:** ❌ **FAIL**
- **Time:** 36s
- **Steps completed:** 2/2
- **Actions executed:** 2 total (Taps: 0, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 0
- **Extracted S2R steps:**
  1. [Scroll] [out]
  2. [Scroll] [out]
- **Reason:** AdbGPT completed steps but encountered errors: /Users/darshan/Library/Python/3.9/lib/python/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8

### 13. yairm210_Unciv_13517 ❌

- **App:** yairm210/Unciv
- **Title:** User report
- **Result:** ❌ **FAIL**
- **Time:** 178s
- **Steps completed:** 0/6
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 10
- **Extracted S2R steps:**
  1. [Tap] [...]
  2. [Tap] [...]
  3. [Scroll] [down]
  4. [Tap] [...]
  5. [Tap] [...]
  6. [Scroll] [down]
- **Reason:** AdbGPT only completed 0/6 steps. Could not match remaining steps to GUI elements.

### 14. you-apps_WallYou_216 ❌

- **App:** you-apps/WallYou
- **Title:** Improper edge-to-edge implementation
- **Result:** ❌ **FAIL**
- **Time:** 16s
- **Steps completed:** 0/0
- **Actions executed:** 0 total (Taps: 0, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 0
- **Extracted S2R steps:**
  (no steps extracted)
- **Reason:** AdbGPT failed to extract any S2R steps from the bug report. The LLM response could not be parsed into actionable steps.

---

## Quick Tap (6 bugs — 4✅ 2❌)

### 1. LawnchairLauncher_lawnchair_5540 ✅

- **App:** LawnchairLauncher/lawnchair
- **Title:** Home Button Requires Double-Tap to Return to Default Home Page from Other Home S
- **Result:** ✅ **SUCCESS**
- **Time:** 94s
- **Steps completed:** 6/6
- **Actions executed:** 8 total (Taps: 6, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 4
- **Extracted S2R steps:**
  1. [Scroll] [left]
  2. [Tap] [home button]
  3. [Double tap] [home button]
  4. [Scroll] [left]
  5. [Tap] [home button]
  6. [Double tap] [home button]
- **Reason:** AdbGPT completed all 6 extracted S2R steps without errors.

### 2. anilbeesetti_nextplayer_1389 ✅

- **App:** anilbeesetti/nextplayer
- **Title:** Resuming doesn't work properly — video stops immediately on tap
- **Result:** ✅ **SUCCESS**
- **Time:** 181s
- **Steps completed:** 8/8
- **Actions executed:** 8 total (Taps: 8, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 14
- **Extracted S2R steps:**
  1. [Input] [Resume] [Yes]
  2. [Input] [Autoplay] [Off]
  3. [Tap] [play button]
  4. [Tap] [last played video]
  5. [Input] [Resume] [Yes]
  6. [Input] [Autoplay] [Off]
  7. [Tap] [play button]
  8. [Tap] [last played video]
- **Reason:** AdbGPT completed all 8 extracted S2R steps without errors.

### 3. ankidroid_Anki-Android_18529 ❌

- **App:** ankidroid/Anki-Android
- **Title:** You can touch some buttons during animations
- **Result:** ❌ **FAIL**
- **Time:** 181s
- **Steps completed:** 0/6
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Long tap] [deck]
  2. [Tap] [rename]
  3. [Long tap] [deck]
  4. [Long tap] [deck]
  5. [Tap] [rename]
  6. [Long tap] [deck]
- **Reason:** AdbGPT only completed 0/6 steps. Could not match remaining steps to GUI elements.

### 4. ankidroid_Anki-Android_19641 ✅

- **App:** ankidroid/Anki-Android
- **Title:** [New study screen] Card was modified error when tapping the answer buttons quick
- **Result:** ✅ **SUCCESS**
- **Time:** 87s
- **Steps completed:** 4/4
- **Actions executed:** 4 total (Taps: 4, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 6
- **Extracted S2R steps:**
  1. [Tap] [new study screen]
  2. [Tap] [answer buttons]
  3. [Tap] [new study screen]
  4. [Tap] [answer buttons]
- **Reason:** AdbGPT completed all 4 extracted S2R steps without errors.

### 5. ankidroid_Anki-Android_20789 ✅

- **App:** ankidroid/Anki-Android
- **Title:** "Collection synced" notification is too high-priority
- **Result:** ✅ **SUCCESS**
- **Time:** 73s
- **Steps completed:** 3/3
- **Actions executed:** 3 total (Taps: 2, Swipes: 1, Keys: 0, Text: 0)
- **MISSING steps:** 2
- **Extracted S2R steps:**
  1. [Scroll] [up]
  2. [Tap] [sync button]
  3. [Tap] [sync button]
- **Reason:** AdbGPT completed all 3 extracted S2R steps without errors.

### 6. ankidroid_Anki-Android_7138 ❌

- **App:** ankidroid/Anki-Android
- **Title:** Card skips when tapping Show Answer immediately
- **Result:** ❌ **FAIL**
- **Time:** 184s
- **Steps completed:** 0/1
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [Show Answer]
- **Reason:** AdbGPT only completed 0/1 steps. Could not match remaining steps to GUI elements.

---

## Scroll (5 bugs — 3✅ 2❌)

### 1. Anthonyy232_Paperize_426 ❌

- **App:** Anthonyy232/Paperize
- **Title:** [Bug] the Privacy Notice button disappears in landscape mode
- **Result:** ❌ **FAIL**
- **Time:** 31s
- **Steps completed:** 0/0
- **Actions executed:** 0 total (Taps: 0, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 0
- **Extracted S2R steps:**
  (no steps extracted)
- **Reason:** AdbGPT failed to extract any S2R steps from the bug report. The LLM response could not be parsed into actionable steps.

### 2. Fandroid745_Open-notes_15 ✅

- **App:** Fandroid745/Open-notes
- **Title:** No scroll support, (Bug)
- **Result:** ✅ **SUCCESS**
- **Time:** 106s
- **Steps completed:** 6/6
- **Actions executed:** 6 total (Taps: 4, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 6
- **Extracted S2R steps:**
  1. [Tap] [new note button]
  2. [Input] [note content] [a long text with many newlines]
  3. [Scroll] [down]
  4. [Tap] [new note button]
  5. [Input] [note content] [a long text with many newlines]
  6. [Scroll] [down]
- **Reason:** AdbGPT completed all 6 extracted S2R steps without errors.

### 3. ankidroid_Anki-Android_5512 ❌

- **App:** ankidroid/Anki-Android
- **Title:** AnkiDroid scroll bug
- **Result:** ❌ **FAIL**
- **Time:** 208s
- **Steps completed:** 0/6
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [Card browser]
  2. [Input] [Card browser font scaling] [50%]
  3. [Scroll] [down]
  4. [Tap] [Card browser]
  5. [Input] [Card browser font scaling] [50%]
  6. [Scroll] [down]
- **Reason:** AdbGPT only completed 0/6 steps. Could not match remaining steps to GUI elements.

### 4. ankidroid_Anki-Android_5544 ✅

- **App:** ankidroid/Anki-Android
- **Title:** AnkiDroid scroll bug
- **Result:** ✅ **SUCCESS**
- **Time:** 62s
- **Steps completed:** 3/3
- **Actions executed:** 3 total (Taps: 0, Swipes: 3, Keys: 0, Text: 0)
- **MISSING steps:** 0
- **Extracted S2R steps:**
  1. [Scroll] [Direction]
  2. [Scroll] [down]
  3. [Scroll] [down]
- **Reason:** AdbGPT completed all 3 extracted S2R steps without errors.

### 5. netmackan_ATimeTracker_124 ✅

- **App:** netmackan/ATimeTracker
- **Title:** Could not scroll on the menu
- **Result:** ✅ **SUCCESS**
- **Time:** 28s
- **Steps completed:** 3/3
- **Actions executed:** 3 total (Taps: 0, Swipes: 3, Keys: 0, Text: 0)
- **MISSING steps:** 0
- **Extracted S2R steps:**
  1. [Scroll] [Direction]
  2. [Scroll] [menu]
  3. [Scroll] [menu]
- **Reason:** AdbGPT completed all 3 extracted S2R steps without errors.

---

## Swipe (32 bugs — 17✅ 15❌)

### 1. A-EDev_Flow_27 ❌

- **App:** A-EDev/Flow
- **Title:** Fullscreen gesture conflict — brightness/volume gestures trigger when opening co
- **Result:** ❌ **FAIL**
- **Time:** 188s
- **Steps completed:** 0/4
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 10
- **Extracted S2R steps:**
  1. [Tap] [video]
  2. [Scroll] [down]
  3. [Tap] [video]
  4. [Scroll] [down]
- **Reason:** AdbGPT only completed 0/4 steps. Could not match remaining steps to GUI elements.

### 2. A-EDev_Flow_284 ❌

- **App:** A-EDev/Flow
- **Title:** Pinch-in zoom breaks player gestures — volume and brightness become unresponsive
- **Result:** ❌ **FAIL**
- **Time:** 225s
- **Steps completed:** 1/10
- **Actions executed:** 11 total (Taps: 1, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 11
- **Extracted S2R steps:**
  1. [Tap] [Flow]
  2. [Tap] [video]
  3. [Tap] [play button]
  4. [Scroll] [Up/Down]
  5. [Scroll] [Left/Right]
  6. [Tap] [Flow]
  7. [Tap] [video]
  8. [Tap] [play button]
  9. [Scroll] [Up/Down]
  10. [Scroll] [Left/Right]
- **Reason:** AdbGPT only completed 1/10 steps. Could not match remaining steps to GUI elements.

### 3. CodeWorksCreativeHub_mLauncher_809 ✅

- **App:** CodeWorksCreativeHub/mLauncher
- **Title:** [Bug Report] Short swipe gesture broken
- **Result:** ✅ **SUCCESS**
- **Time:** 60s
- **Steps completed:** 4/4
- **Actions executed:** 4 total (Taps: 2, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 2
- **Extracted S2R steps:**
  1. [Tap] [homescreen]
  2. [Scroll] [Direction]
  3. [Tap] [homescreen]
  4. [Scroll] [Direction]
- **Reason:** AdbGPT completed all 4 extracted S2R steps without errors.

### 4. Droid-ify_client_238 ✅

- **App:** Droid-ify/client
- **Title:** [BUG] App crashing on changing settings.
- **Result:** ✅ **SUCCESS**
- **Time:** 128s
- **Steps completed:** 6/6
- **Actions executed:** 6 total (Taps: 6, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 12
- **Extracted S2R steps:**
  1. [Tap] [settings section]
  2. [Tap] [notify new versions toggle]
  3. [Tap] [back arrow]
  4. [Tap] [settings section]
  5. [Tap] [notify new versions toggle]
  6. [Tap] [back arrow]
- **Reason:** AdbGPT completed all 6 extracted S2R steps without errors.

### 5. FossifyOrg_Calendar_1035 ✅

- **App:** FossifyOrg/Calendar
- **Title:** Ap crashes when creating new event
- **Result:** ✅ **SUCCESS**
- **Time:** 114s
- **Steps completed:** 4/4
- **Actions executed:** 4 total (Taps: 4, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 4
- **Extracted S2R steps:**
  1. [Tap] [+]
  2. [Tap] [event]
  3. [Tap] [+]
  4. [Tap] [event]
- **Reason:** AdbGPT completed all 4 extracted S2R steps without errors.

### 6. FossifyOrg_Calendar_1103 ❌

- **App:** FossifyOrg/Calendar
- **Title:** Accessibility - have screen reader anounce existence/count of events on a day in
- **Result:** ❌ **FAIL**
- **Time:** 228s
- **Steps completed:** 0/6
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [calendar app]
  2. [Tap] [monthly view]
  3. [Scroll] [right]
  4. [Tap] [calendar app]
  5. [Tap] [monthly view]
  6. [Scroll] [right]
- **Reason:** AdbGPT only completed 0/6 steps. Could not match remaining steps to GUI elements.

### 7. FossifyOrg_Calendar_153 ✅

- **App:** FossifyOrg/Calendar
- **Title:** Swiping in monthly view is a pain
- **Result:** ✅ **SUCCESS**
- **Time:** 89s
- **Steps completed:** 6/6
- **Actions executed:** 6 total (Taps: 2, Swipes: 4, Keys: 0, Text: 0)
- **MISSING steps:** 2
- **Extracted S2R steps:**
  1. [Tap] [monthly view]
  2. [Scroll] [right]
  3. [Scroll] [left]
  4. [Tap] [monthly view]
  5. [Scroll] [right]
  6. [Scroll] [left]
- **Reason:** AdbGPT completed all 6 extracted S2R steps without errors.

### 8. FossifyOrg_Clock_156 ✅

- **App:** FossifyOrg/Clock
- **Title:** Timer alarm turned off by swiping from the status bar
- **Result:** ✅ **SUCCESS**
- **Time:** 143s
- **Steps completed:** 8/8
- **Actions executed:** 8 total (Taps: 6, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 8
- **Extracted S2R steps:**
  1. [Input] [timer] [any value]
  2. [Tap] [start]
  3. [Scroll] [status bar]
  4. [Tap] [status bar area]
  5. [Input] [timer] [any value]
  6. [Tap] [start]
  7. [Scroll] [status bar]
  8. [Tap] [status bar area]
- **Reason:** AdbGPT completed all 8 extracted S2R steps without errors.

### 9. FossifyOrg_File-Manager_136 ❌

- **App:** FossifyOrg/File-Manager
- **Title:** The screen refresh gesture works when the function is turned off
- **Result:** ❌ **FAIL**
- **Time:** 197s
- **Steps completed:** 0/12
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 10
- **Extracted S2R steps:**
  1. [Tap] [Settings]
  2. [Scroll] [down]
  3. [Tap] [Enable pull-to-refresh from the top]
  4. [Tap] [folder]
  5. [Tap] [Cancel]
  6. [Tap] [folder]
  7. [Tap] [Settings]
  8. [Scroll] [down]
  9. [Tap] [Enable pull-to-refresh from the top]
  10. [Tap] [folder]
  11. [Tap] [Cancel]
  12. [Tap] [folder]
- **Reason:** AdbGPT only completed 0/12 steps. Could not match remaining steps to GUI elements.

### 10. FossifyOrg_Gallery_237 ✅

- **App:** FossifyOrg/Gallery
- **Title:** Vertical gesture to adjust video volume does not work
- **Result:** ✅ **SUCCESS**
- **Time:** 77s
- **Steps completed:** 6/6
- **Actions executed:** 6 total (Taps: 2, Swipes: 4, Keys: 0, Text: 0)
- **MISSING steps:** 4
- **Extracted S2R steps:**
  1. [Tap] [video file]
  2. [Scroll] [left side of the screen]
  3. [Scroll] [right side of the screen]
  4. [Tap] [video file]
  5. [Scroll] [left side of the screen]
  6. [Scroll] [right side of the screen]
- **Reason:** AdbGPT completed all 6 extracted S2R steps without errors.

### 11. FossifyOrg_Gallery_584 ❌

- **App:** FossifyOrg/Gallery
- **Title:** When trying to open some JPG files, the gallery app crashes or returns to the ma
- **Result:** ❌ **FAIL**
- **Time:** 185s
- **Steps completed:** 0/4
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [folder]
  2. [Tap] [jpg file]
  3. [Tap] [folder]
  4. [Tap] [jpg file]
- **Reason:** AdbGPT only completed 0/4 steps. Could not match remaining steps to GUI elements.

### 12. FossifyOrg_Gallery_940 ❌

- **App:** FossifyOrg/Gallery
- **Title:** Disabled notch overlaps brightness control area
- **Result:** ❌ **FAIL**
- **Time:** 235s
- **Steps completed:** 0/8
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [Show notch if available]
  2. [Tap] [Allow controlling photo brightness with vertical gestures]
  3. [Tap] [image]
  4. [Scroll] [up]
  5. [Tap] [Show notch if available]
  6. [Tap] [Allow controlling photo brightness with vertical gestures]
  7. [Tap] [image]
  8. [Scroll] [up]
- **Reason:** AdbGPT only completed 0/8 steps. Could not match remaining steps to GUI elements.

### 13. FossifyOrg_Launcher_66 ❌

- **App:** FossifyOrg/Launcher
- **Title:** Slow, jerky animation when opening a folder or swiping between screens
- **Result:** ❌ **FAIL**
- **Time:** 211s
- **Steps completed:** 3/8
- **Actions executed:** 13 total (Taps: 0, Swipes: 3, Keys: 10, Text: 0)
- **MISSING steps:** 11
- **Extracted S2R steps:**
  1. [Scroll] [left]
  2. [Scroll] [right]
  3. [Long tap] [app icon]
  4. [Tap] [folder]
  5. [Scroll] [left]
  6. [Scroll] [right]
  7. [Long tap] [app icon]
  8. [Tap] [folder]
- **Reason:** AdbGPT only completed 3/8 steps. Could not match remaining steps to GUI elements.

### 14. FossifyOrg_Messages_80 ❌

- **App:** FossifyOrg/Messages
- **Title:** Navigation Stack gets too Large (Hitting Back Button)
- **Result:** ❌ **FAIL**
- **Time:** 222s
- **Steps completed:** 0/17
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 10
- **Extracted S2R steps:**
  1. [Tap] [+ icon]
  2. [Tap] [contact]
  3. [Tap] [home button]
  4. [Long tap] [Fossify Messages app icon]
  5. [Tap] [New Conversation]
  6. [Tap] [contact]
  7. [Tap] [back button]
  8. [Tap] [+ icon]
  9. [Tap] [contact]
  10. [Tap] [home button]
  11. [Long tap] [Fossify Messages app icon]
  12. [Tap] [New Conversation]
  13. [Tap] [contact]
  14. [Tap] [back button]
  15. [Tap] [back button]
  16. [Tap] [back button]
  17. [Tap] [back button]
- **Reason:** AdbGPT only completed 0/17 steps. Could not match remaining steps to GUI elements.

### 15. FossifyOrg_Notes_190 ✅

- **App:** FossifyOrg/Notes
- **Title:** crash while using the search field.
- **Result:** ✅ **SUCCESS**
- **Time:** 196s
- **Steps completed:** 10/10
- **Actions executed:** 11 total (Taps: 8, Swipes: 2, Keys: 0, Text: 1)
- **MISSING steps:** 8
- **Extracted S2R steps:**
  1. [Tap] [search]
  2. [Input] [search field] [any text]
  3. [Tap] [down arrow]
  4. [Scroll] [right]
  5. [Input] [search field] [anything]
  6. [Tap] [search]
  7. [Input] [search field] [any text]
  8. [Tap] [down arrow]
  9. [Scroll] [right]
  10. [Input] [search field] [anything]
- **Reason:** AdbGPT completed all 10 extracted S2R steps without errors.

### 16. Kin69_EasyNotes_356 ❌

- **App:** Kin69/EasyNotes
- **Title:** [BUG]
- **Result:** ❌ **FAIL**
- **Time:** 219s
- **Steps completed:** 1/4
- **Actions executed:** 11 total (Taps: 1, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 12
- **Extracted S2R steps:**
  1. [Input] [note text field] [anything]
  2. [Tap] [back]
  3. [Input] [note text field] [anything]
  4. [Tap] [back]
- **Reason:** AdbGPT only completed 1/4 steps. Could not match remaining steps to GUI elements.

### 17. LawnchairLauncher_lawnchair_4642 ✅

- **App:** LawnchairLauncher/lawnchair
- **Title:** [BUG] Gesture navigation gets locked in one orientation until a launcher restart
- **Result:** ✅ **SUCCESS**
- **Time:** 122s
- **Steps completed:** 4/4
- **Actions executed:** 4 total (Taps: 4, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 8
- **Extracted S2R steps:**
  1. [Tap] [launchair]
  2. [Tap] [launchair]
  3. [Tap] [launchair]
  4. [Tap] [launchair]
- **Reason:** AdbGPT completed all 4 extracted S2R steps without errors.

### 18. LawnchairLauncher_lawnchair_4708 ✅

- **App:** LawnchairLauncher/lawnchair
- **Title:** [BUG] Gesture nav: swiping up to go home when already in Lawnchair creates a "gh
- **Result:** ✅ **SUCCESS**
- **Time:** 94s
- **Steps completed:** 8/8
- **Actions executed:** 8 total (Taps: 2, Swipes: 6, Keys: 0, Text: 0)
- **MISSING steps:** 2
- **Extracted S2R steps:**
  1. [Scroll] [home bar]
  2. [Scroll] [home bar]
  3. [Tap] [different app]
  4. [Scroll] [home bar]
  5. [Scroll] [home bar]
  6. [Scroll] [home bar]
  7. [Tap] [different app]
  8. [Scroll] [home bar]
- **Reason:** AdbGPT completed all 8 extracted S2R steps without errors.

### 19. LawnchairLauncher_lawnchair_5496 ✅

- **App:** LawnchairLauncher/lawnchair
- **Title:** [BUG] Lawnchair crashes in the recent menu
- **Result:** ✅ **SUCCESS**
- **Time:** 108s
- **Steps completed:** 5/5
- **Actions executed:** 5 total (Taps: 4, Swipes: 1, Keys: 0, Text: 0)
- **MISSING steps:** 4
- **Extracted S2R steps:**
  1. [Tap] [any application]
  2. [Tap] [Recent button]
  3. [Scroll] [up]
  4. [Tap] [any application]
  5. [Tap] [Recent button]
- **Reason:** AdbGPT completed all 5 extracted S2R steps without errors.

### 20. MetrolistGroup_Metrolist_3391 ❌

- **App:** MetrolistGroup/Metrolist
- **Title:** Back gesture not working in the player screen
- **Result:** ❌ **FAIL**
- **Time:** 200s
- **Steps completed:** 0/6
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [song]
  2. [Tap] [mini-player]
  3. [Scroll] [left]
  4. [Tap] [song]
  5. [Tap] [mini-player]
  6. [Scroll] [left]
- **Reason:** AdbGPT only completed 0/6 steps. Could not match remaining steps to GUI elements.

### 21. OuterTune_OuterTune_1044 ❌

- **App:** OuterTune/OuterTune
- **Title:** Pressing Home or any button activates back gesture.
- **Result:** ❌ **FAIL**
- **Time:** 202s
- **Steps completed:** 0/4
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [playlist]
  2. [Tap] [Home/Library button]
  3. [Tap] [playlist]
  4. [Tap] [Home/Library button]
- **Reason:** AdbGPT only completed 0/4 steps. Could not match remaining steps to GUI elements.

### 22. anilbeesetti_nextplayer_1127 ✅

- **App:** anilbeesetti/nextplayer
- **Title:** Vertical swipe misbehaviour — volume/brightness gesture too sensitive in landsca
- **Result:** ✅ **SUCCESS**
- **Time:** 66s
- **Steps completed:** 4/4
- **Actions executed:** 4 total (Taps: 2, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 2
- **Extracted S2R steps:**
  1. [Tap] [video]
  2. [Scroll] [down]
  3. [Tap] [video]
  4. [Scroll] [down]
- **Reason:** AdbGPT completed all 4 extracted S2R steps without errors.

### 23. ankidroid_Anki-Android_14934 ✅

- **App:** ankidroid/Anki-Android
- **Title:** talkback can't see sometimes front, sometimes back and sometimes both sides of a
- **Result:** ✅ **SUCCESS**
- **Time:** 113s
- **Steps completed:** 8/8
- **Actions executed:** 8 total (Taps: 4, Swipes: 4, Keys: 0, Text: 0)
- **MISSING steps:** 6
- **Extracted S2R steps:**
  1. [Tap] [ankidroid]
  2. [Tap] [deck]
  3. [Scroll] [right]
  4. [Scroll] [right]
  5. [Tap] [ankidroid]
  6. [Tap] [deck]
  7. [Scroll] [right]
  8. [Scroll] [right]
- **Reason:** AdbGPT completed all 8 extracted S2R steps without errors.

### 24. bartoostveen_ViTune_710 ✅

- **App:** 25huizengek1/ViTune
- **Title:** Notification shows wrong album art for current song
- **Result:** ✅ **SUCCESS**
- **Time:** 54s
- **Steps completed:** 4/4
- **Actions executed:** 4 total (Taps: 2, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 2
- **Extracted S2R steps:**
  1. [Tap] [a song]
  2. [Scroll] [down]
  3. [Tap] [a song]
  4. [Scroll] [down]
- **Reason:** AdbGPT completed all 4 extracted S2R steps without errors.

### 25. breezy-weather_breezy-weather_205 ✅

- **App:** breezy-weather/breezy-weather
- **Title:** [Location list] Swipe left animation stays after cancelling weather provider dia
- **Result:** ✅ **SUCCESS**
- **Time:** 98s
- **Steps completed:** 6/6
- **Actions executed:** 6 total (Taps: 4, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 4
- **Extracted S2R steps:**
  1. [Tap] [add location button]
  2. [Scroll] [left]
  3. [Tap] [cancel]
  4. [Tap] [add location button]
  5. [Scroll] [left]
  6. [Tap] [cancel]
- **Reason:** AdbGPT completed all 6 extracted S2R steps without errors.

### 26. breezy-weather_breezy-weather_85 ✅

- **App:** breezy-weather/breezy-weather
- **Title:** Persistent notification setting - on / off is inverted
- **Result:** ✅ **SUCCESS**
- **Time:** 142s
- **Steps completed:** 6/6
- **Actions executed:** 6 total (Taps: 6, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 6
- **Extracted S2R steps:**
  1. [Tap] [settings]
  2. [Tap] [widgets]
  3. [Tap] [notification widget]
  4. [Tap] [settings]
  5. [Tap] [widgets]
  6. [Tap] [notification widget]
- **Reason:** AdbGPT completed all 6 extracted S2R steps without errors.

### 27. dessalines_thumb-key_371 ❌

- **App:** dessalines/thumb-key
- **Title:** Swipe input eaten on capitalization/mode switch
- **Result:** ❌ **FAIL**
- **Time:** 234s
- **Steps completed:** 0/4
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 10
- **Extracted S2R steps:**
  1. [Long tap] [letter key]
  2. [Tap] [capitalize]
  3. [Long tap] [letter key]
  4. [Tap] [capitalize]
- **Reason:** AdbGPT only completed 0/4 steps. Could not match remaining steps to GUI elements.

### 28. iamrasel_lunar-launcher_82 ✅

- **App:** iamrasel/lunar-launcher
- **Title:** Random crashes when closing applications
- **Result:** ✅ **SUCCESS**
- **Time:** 23s
- **Steps completed:** 2/2
- **Actions executed:** 2 total (Taps: 0, Swipes: 2, Keys: 0, Text: 0)
- **MISSING steps:** 0
- **Extracted S2R steps:**
  1. [Scroll] [up]
  2. [Scroll] [up]
- **Reason:** AdbGPT completed all 2 extracted S2R steps without errors.

### 29. libre-tube_LibreTube_8245 ❌

- **App:** libre-tube/LibreTube
- **Title:** Laggy animation when minimizing player with Back button (video & audio modes)
- **Result:** ❌ **FAIL**
- **Time:** 260s
- **Steps completed:** 1/14
- **Actions executed:** 11 total (Taps: 1, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 11
- **Extracted S2R steps:**
  1. [Tap] [any item]
  2. [Tap] [Android Back button]
  3. [Tap] [any item]
  4. [Scroll] [player]
  5. [Tap] [Audio mode]
  6. [Tap] [any item]
  7. [Tap] [Android Back button]
  8. [Tap] [any item]
  9. [Tap] [Android Back button]
  10. [Tap] [any item]
  11. [Scroll] [player]
  12. [Tap] [Audio mode]
  13. [Tap] [any item]
  14. [Tap] [Android Back button]
- **Reason:** AdbGPT only completed 1/14 steps. Could not match remaining steps to GUI elements.

### 30. msasikanth_twine_1566 ❌

- **App:** msasikanth/twine
- **Title:** [BUG] Incomplete Predictive Back Animation
- **Result:** ❌ **FAIL**
- **Time:** 211s
- **Steps completed:** 0/4
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 20
- **Extracted S2R steps:**
  1. [Tap] [Post]
  2. [Tap] [back]
  3. [Tap] [Post]
  4. [Tap] [back]
- **Reason:** AdbGPT only completed 0/4 steps. Could not match remaining steps to GUI elements.

### 31. you-apps_ClockYou_85 ✅

- **App:** you-apps/ClockYou
- **Title:** App cycles through previously visited tabs on back gesture instead of closing
- **Result:** ✅ **SUCCESS**
- **Time:** 95s
- **Steps completed:** 4/4
- **Actions executed:** 4 total (Taps: 4, Swipes: 0, Keys: 0, Text: 0)
- **MISSING steps:** 4
- **Extracted S2R steps:**
  1. [Tap] [tab]
  2. [Tap] [back]
  3. [Tap] [tab]
  4. [Tap] [back]
- **Reason:** AdbGPT completed all 4 extracted S2R steps without errors.

### 32. you-apps_ConnectYou_155 ❌

- **App:** you-apps/ConnectYou
- **Title:** Back on search bar quits the app.
- **Result:** ❌ **FAIL**
- **Time:** 179s
- **Steps completed:** 0/4
- **Actions executed:** 10 total (Taps: 0, Swipes: 0, Keys: 10, Text: 0)
- **MISSING steps:** 10
- **Extracted S2R steps:**
  1. [Tap] [search bar]
  2. [Tap] [back button]
  3. [Tap] [search bar]
  4. [Tap] [back button]
- **Reason:** AdbGPT only completed 0/4 steps. Could not match remaining steps to GUI elements.

---
