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
| [cromaguy_Rhythm_281](Dataset/double_tap/cromaguy_Rhythm_281%20Tested) | cromaguy/Rhythm | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/double_tap/cromaguy_Rhythm_281%20Tested/Annotation/annotated.png) | **Tap/click gesture** → [BUG]: Double tap needed on Touch Gestures view of Onboarding Setup  | 1. Open the app after fresh install. 2. Follow Setup steps until Touch Gestures. 3. Tap Next Button. 4. Tap Back button.... |
| [FossifyOrg_Calendar_273](Dataset/double_tap/FossifyOrg_Calendar_273%20Tested) | FossifyOrg/Calendar | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/double_tap/FossifyOrg_Calendar_273%20Tested/Annotation/annotated.png) | **Double-tap gesture** → Setting a default event length doesn't change the default event length | 1. Set default event duration 35 minutes 2. Double tap calendar to make a new event (not using [+] button)... |
| [FossifyOrg_Gallery_363](Dataset/double_tap/FossifyOrg_Gallery_363%20Tested) | FossifyOrg/Gallery | ✅ | ❌ | ✅ | ✅ | ![screenshot](Dataset/double_tap/FossifyOrg_Gallery_363%20Tested/Annotation/annotated.png) | **Double-tap gesture** → webp images when double tapped don't zoom to height of image | 1. Open a .webp images 2. Double tap screen 3. Image doesn't fit to height of screen just zooms in further than edge of ... |
| [FossifyOrg_Gallery_678](Dataset/double_tap/FossifyOrg_Gallery_678%20Tested) | FossifyOrg/Gallery | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/double_tap/FossifyOrg_Gallery_678%20Tested/Annotation/annotated.png) | **Double-tap gesture** → 'Allow 1:1 zooming in with two double taps' not working when pixel size of the p | 1. 5.2 org.fossify.gallery 2. View a photo that has smaller x/y pixel size than that what the screen has, e.g a photo wi... |
| [FossifyOrg_Gallery_846](Dataset/double_tap/FossifyOrg_Gallery_846%20Tested) | FossifyOrg/Gallery | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/double_tap/FossifyOrg_Gallery_846%20Tested/Annotation/annotated.png) | **Double-tap gesture** → "Fill screen" zoom on double tap ignores disabled "Show notch if available" | 1. Disable "Show notch if available" 2. Open an image and double-tap so that the image is zoomed to fill the screen 3. D... |
| [FossifyOrg_Gallery_847](Dataset/double_tap/FossifyOrg_Gallery_847%20Tested) | FossifyOrg/Gallery | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/double_tap/FossifyOrg_Gallery_847%20Tested/Annotation/annotated.png) | **Double-tap gesture** → Invalid "fill screen" zoom for GIF images on double-tap | 1. Open any GIF image 2. Double-tap it... |
| [LawnchairLauncher_lawnchair_2910](Dataset/double_tap/LawnchairLauncher_lawnchair_2910%20Tested) | LawnchairLauncher/lawncha | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/double_tap/LawnchairLauncher_lawnchair_2910%20Tested/Annotation/annotated.png) | **Double-tap gesture** → [BUG] Double tap to sleep no longer works through root access | 1. Enable "suspend" function in gestures 2. Double tap to suspend... |
| [LawnchairLauncher_lawnchair_4125](Dataset/double_tap/LawnchairLauncher_lawnchair_4125%20Tested) | LawnchairLauncher/lawncha | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/double_tap/LawnchairLauncher_lawnchair_4125%20Tested/Annotation/annotated.png) | **Double-tap gesture** → [BUG] android 14, no option to allow restricted setting | 1. Go to - settings, change gestures, double tap to sleep 2. Click on - kebab 3 dot menu, no option to allow restrictive... |
| [LawnchairLauncher_lawnchair_4786](Dataset/double_tap/LawnchairLauncher_lawnchair_4786%20Tested%20F) | LawnchairLauncher/lawncha | ❌ | ❌ | ❌ | ✅ | ![screenshot](Dataset/double_tap/LawnchairLauncher_lawnchair_4786%20Tested%20F/Annotation/annotated.png) | **Double-tap gesture** → [BUG] Crash when trying to move item using TalkBack action | 1. Hover over a widget 2. With TalkBack enabled, press with 3 fingers to open the actions menu 3. Double-tap the first i... |
| [Pool-Of-Tears_GreenStash_170](Dataset/double_tap/Pool-Of-Tears_GreenStash_170%20Tested) | Pool-Of-Tears/GreenStash | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/double_tap/Pool-Of-Tears_GreenStash_170%20Tested/Annotation/annotated.png) | **[Bug]: Some accessibility issues** | Steps: 1. The red boxes in the image below indicate all the UI elements that can be accessed by visually impaired users using screen readers. The components ... |
| [TeamNewPipe_NewPipe_10750](Dataset/double_tap/TeamNewPipe_NewPipe_10750%20Tested) | TeamNewPipe/NewPipe | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/double_tap/TeamNewPipe_NewPipe_10750%20Tested/Annotation/annotated.png) | **Video playback randomly "closed/crashed", and content loaded but stuck buffering** | Steps: 2. Play couple videos. 3. At any moment, the video player might stuck buffering for couple seconds before it crash/close 4. Replay the video, now it s... |
| [TeamNewPipe_NewPipe_8338](Dataset/double_tap/TeamNewPipe_NewPipe_8338%20Tested) | TeamNewPipe/NewPipe | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/double_tap/TeamNewPipe_NewPipe_8338%20Tested/Annotation/annotated.png) | **Double-tap gesture** → Swipe down gesture of Player UI does not work all the times | 2. Keep a video running 3. Double tap video to pause it & immediately try to swipe down ### Expected behavior Player UI ... |
| [abdallahmehiz_mpvKt_184](Dataset/double_tap/abdallahmehiz_mpvKt_184%20Tested) | abdallahmehiz/mpvKt | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/double_tap/abdallahmehiz_mpvKt_184%20Tested/Annotation/annotated.png) | **Double-tap gesture** → Tap error while playing video | 1. Go to any video 2. make use of double tap once 3. Then if you single tap on left or right it will move forward or bac... |
| [ankidroid_Anki-Android_17393](Dataset/double_tap/ankidroid_Anki-Android_17393%20Tested) | ankidroid/Anki-Android | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/double_tap/ankidroid_Anki-Android_17393%20Tested/Annotation/annotated.png) | **Tap/click gesture** → [BUG]: IO Cards Go to the Wrong Deck | 1. Go to **Settings > General**. 2. Click **Deck for new cards** and select `use current deck`. 3. Go back to deck picke... |
| [FossifyOrg_Calendar_1035](Dataset/double_tap/FossifyOrg_Calendar_1035%20Tested) | FossifyOrg/Calendar | ✅ | ✅ | ✅ | ✅ | ![screenshot](Dataset/double_tap/FossifyOrg_Calendar_1035%20Tested/Annotation/annotated.png) | **Tap/click gesture** → Ap crashes when creating new event | 1. Open app 2. Click on the big + 3. Click on event Then it crashes... |
| [fast4x_RiMusic_1152](Dataset/double_tap/fast4x_RiMusic_1152%20Tested) | fast4x/RiMusic | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/double_tap/fast4x_RiMusic_1152%20Tested/Annotation/annotated.png) | **Tap/click gesture** → Unclear Linking and Unresponsive Buttons in Player View | 1. Open the player view. 2. Tap once on the song title or artist name. 3. 6.26.1... |
| [gsantner_markor_2746](Dataset/double_tap/gsantner_markor_2746%20Tested) | gsantner/markor | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/double_tap/gsantner_markor_2746%20Tested/Annotation/annotated.png) | **Double-tap gesture** → Markor does not recognize URL/link anymore | 1. When I had a link on Markor, I just had to double-tap on the link for Markor to select the entire link. 2. After sele... |
| [openboard-team_openboard_613](Dataset/double_tap/openboard-team_openboard_613%20Tested) | openboard-team/openboard | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/double_tap/openboard-team_openboard_613%20Tested/Annotation/annotated.png) | **Double-tap gesture** → Sometimes the spellchecker flags correctly spelt words if one adds a full-stop t | 1. Set spellcheck to Openboard. 2. In an SMS client - I use Textra - type `<properly spelt word>.` (manually typing the ... |
| [openboard-team_openboard_758](Dataset/double_tap/openboard-team_openboard_758%20Tested%20F) | openboard-team/openboard | ❌ | ❌ | ❌ | ✅ | ![screenshot](Dataset/double_tap/openboard-team_openboard_758%20Tested%20F/Annotation/annotated.png) | **Accessibility: The button to go to the previous level does not work properly** | Steps: 1. Install a screen reader (TalkBack or Jieshuo) on your device. Then - turn on the TalkBack or Jieshuo service in the accessibility settings; 2. open... |
| [syt0r_Kanji-Dojo_291](Dataset/double_tap/syt0r_Kanji-Dojo_291%20Tested) | syt0r/Kanji-Dojo | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/double_tap/syt0r_Kanji-Dojo_291%20Tested/Annotation/annotated.png) | **Tap/click gesture** → Double-tapping back arrow while transitioning from vocab info to practice skips  | 1. Start a new practice session and reveal the answer to the letter/vocab card. 2. Navigate to the vocab info screen (e.... |
| [yairm210_Unciv_13517](Dataset/double_tap/yairm210_Unciv_13517%20Tested) | yairm210/Unciv | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/double_tap/yairm210_Unciv_13517%20Tested/Annotation/annotated.png) | **User report** | Steps: 1. layered tiles, for example jungle on a hill seems to crash the game client when iterating ai movements. 2. in the "waiting for other players" code,... |

### Drag & Drop

| Bug ID | App | CARBON | ReBL | ReActDroid | AdbGPT | Screenshot | Remarks |
|--------|-----|--------|------|------------|--------|------------|---------|
| [FossifyOrg_Launcher_304](Dataset/drag_and_drop/FossifyOrg_Launcher_304%20Tested) | FossifyOrg/Launcher | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/drag_and_drop/FossifyOrg_Launcher_304%20Tested/Annotation/annotated.png) | **Drag and drop gesture** → Accidently creating invisible folders in dock | 1. Have a app on the bottom right most location on your app dock at home screen. 2. Drag and drop another app or same ap... |
| [FossifyOrg_Notes_59](Dataset/drag_and_drop/FossifyOrg_Notes_59%20Tested) | FossifyOrg/Notes | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/drag_and_drop/FossifyOrg_Notes_59%20Tested/Annotation/annotated.png) | **Tap/click gesture** → Reordering checklists works strangely with move checked to bottom | 1. Add a new checklist 2. Add items 3. Check some of the items 4. Make sure that the option "Move checked items to the b... |
| [LawnchairLauncher_lawnchair_1247](Dataset/drag_and_drop/LawnchairLauncher_lawnchair_1247%20Tested%20F) | LawnchairLauncher/lawncha | ❌ | ❌ | ❌ | ❌ | ![screenshot](Dataset/drag_and_drop/LawnchairLauncher_lawnchair_1247%20Tested%20F/Annotation/annotated.png) | **Tap/click gesture** → the launcher kees crashign when I attempt to move stuff | 1. Make sure launcher is set to launcheer. 2. Hit home and find an item you want to move 3. Bring up the talk back actio... |
| [LawnchairLauncher_lawnchair_4320](Dataset/drag_and_drop/LawnchairLauncher_lawnchair_4320%20Tested) | LawnchairLauncher/lawncha | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/drag_and_drop/LawnchairLauncher_lawnchair_4320%20Tested/Annotation/annotated.png) | **Drag and drop gesture** → [BUG] Unable to add any widget | 1. Open "widgets" tab 2. Select any widget 3. Drag and drop it to the home screen 4. Try to add it ### Expected behavior... |
| [MetrolistGroup_Metrolist_3227](Dataset/drag_and_drop/MetrolistGroup_Metrolist_3227%20Tested) | MetrolistGroup/Metrolist | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/drag_and_drop/MetrolistGroup_Metrolist_3227%20Tested/Annotation/annotated.png) | **Drag gesture** → Replacement of new song with old song | 1. Add a song to a playlist in custom orde 2. Drag the new song at the bottom to the top of the playlist... |
| [MetrolistGroup_Metrolist_3561](Dataset/drag_and_drop/MetrolistGroup_Metrolist_3561%20Tested) | MetrolistGroup/Metrolist | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/drag_and_drop/MetrolistGroup_Metrolist_3561%20Tested/Annotation/annotated.png) | **Drag gesture** → Weird Bug when changing list order in custom order format | 1. Create a playlist with some songs 2. Put the playlkst in custom order 3. Add a new song and drag it all the way to th... |
| [NeoApplications_Neo-Launcher_130](Dataset/drag_and_drop/NeoApplications_Neo-Launcher_130%20Tested) | NeoApplications/Neo-Launc | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/drag_and_drop/NeoApplications_Neo-Launcher_130%20Tested/Annotation/annotated.png) | **Changing the first app in a folder with Covers enabled breaks the folder** | Steps: 1. Change a folder with 2 apps in it into Covers (App-A and App-B) 2. Reorder the apps, so that the 2nd app (App-B) is now the first (and therefore sh... |
| [breezy-weather_breezy-weather_2159](Dataset/drag_and_drop/breezy-weather_breezy-weather_2159%20Tested) | breezy-weather/breezy-wea | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/drag_and_drop/breezy-weather_breezy-weather_2159%20Tested/Annotation/annotated.png) | **Long press gesture** → [Old Android versions default launcher] Can't add widget to home screen | 1. Long press empty area of home screen 2. Click "Widget" 3. Drag any Breezy Weather widget to the home screen 4. Click ... |
| [fcitx5-android_fcitx5-android_841](Dataset/drag_and_drop/fcitx5-android_fcitx5-android_841%20Tested) | fcitx5-android/fcitx5-and | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/drag_and_drop/fcitx5-android_fcitx5-android_841%20Tested/Annotation/annotated.png) | **Drag gesture** → Crash somtimes on showing keyboard when the preferred input method is supported  | 1. 安装额外的输入法插件（以中州韵为例）； 2. 打开应用中的“输入法”，启用“中州韵”并拖放到列表中第一个位置； 3. 日常使用，偶尔复现崩溃。 4. Install extra input method addon (such as ... |

### Long Press

| Bug ID | App | CARBON | ReBL | ReActDroid | AdbGPT | Screenshot | Remarks |
|--------|-----|--------|------|------------|--------|------------|---------|
| [Anthonyy232_Paperize_325](Dataset/long_press/Anthonyy232_Paperize_325%20Tested) | Anthonyy232/Paperize | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/long_press/Anthonyy232_Paperize_325%20Tested/Annotation/annotated.png) | **Tap/click gesture** → [Bug] Crashing when adding images | 1. Go to the library tab 2. Click on the plus sign to create an album 3. Name and create technical album 4. Click on the... |
| [Crustack_NotallyX_570](Dataset/long_press/Crustack_NotallyX_570%20Tested) | Crustack/NotallyX | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/long_press/Crustack_NotallyX_570%20Tested/Annotation/annotated.png) | **Long press gesture** → App crash when note is selected, search filter changed and another note is selec | 1. Add at least two notes. 2. Long-press to select one note (Note A). 3. Use the search function so that Note A disappea... |
| [FossifyOrg_File-Manager_195](Dataset/long_press/FossifyOrg_File-Manager_195%20Tested) | FossifyOrg/File-Manager | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/long_press/FossifyOrg_File-Manager_195%20Tested/Annotation/annotated.png) | **Long press gesture** → Unnecessary refresh of ZIP file icons when closing bottom sheets | 1. Open a folder in the _Files_ tab that contains at least one ZIP file 2. Long-press on a ZIP file 3. Click the **Open ... |
| [FossifyOrg_Launcher_198](Dataset/long_press/FossifyOrg_Launcher_198%20Tested) | FossifyOrg/Launcher | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/long_press/FossifyOrg_Launcher_198%20Tested/Annotation/annotated.png) | **Long press gesture** → Folder rename dialog: Dark text on dark background | 1. Long-press on a folder to rename it 2. The renaming dialog appears... |
| [FossifyOrg_Messages_359](Dataset/long_press/FossifyOrg_Messages_359%20Tested) | FossifyOrg/Messages | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/long_press/FossifyOrg_Messages_359%20Tested/Annotation/annotated.png) | **Long press gesture** → Can't scroll or see participants on conversation details page | 1. Long press on any conversation 2. Tap **More options** 3. Tap **Conversation details** 4. Switch to landscape mode (n... |
| [FossifyOrg_Messages_416](Dataset/long_press/FossifyOrg_Messages_416%20Tested) | FossifyOrg/Messages | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/long_press/FossifyOrg_Messages_416%20Tested/Annotation/annotated.png) | **Long press gesture** → New conversation shortcut doesn't work | 1. Long press app icon 2. Click `New conversation` shortcut... |
| [FossifyOrg_Messages_641](Dataset/long_press/FossifyOrg_Messages_641%20Tested) | FossifyOrg/Messages | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/long_press/FossifyOrg_Messages_641%20Tested/Annotation/annotated.png) | **Long press gesture** → SMS scheduling not working | 1. Open the app 2. Select any conversation 3. Write a message 4. Long press the send button 5. Select a date and time (s... |
| [breezy-weather_breezy-weather_1639](Dataset/long_press/breezy-weather_breezy-weather_1639%20Tested) | breezy-weather/breezy-wea | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/long_press/breezy-weather_breezy-weather_1639%20Tested/Annotation/annotated.png) | **weather wallpaper causes launcher to freeze and app background closed** | Steps: 1. set weather wallpaper as dynamic wallpaper for main screen and lock screen. 2. open a Vanadium(a fork of Chromium) incognito tab. 3. wait for wallp... |
| [espresso3389_methings_34](Dataset/long_press/espresso3389_methings_34%20Tested) | espresso3389/methings | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/long_press/espresso3389_methings_34%20Tested/Annotation/annotated.png) | **Long press gesture** → Image preview UX gaps and instability when using Select Text on image blocks | 1. Capture multiple images in a single chat message. 2. Tap one of the images to enter preview mode. 3. Swipe left or ri... |

### Orientation

| Bug ID | App | CARBON | ReBL | ReActDroid | AdbGPT | Screenshot | Remarks |
|--------|-----|--------|------|------------|--------|------------|---------|
| [FossifyOrg_Calendar_1042](Dataset/orientation/FossifyOrg_Calendar_1042%20Tested) | FossifyOrg/Calendar | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/orientation/FossifyOrg_Calendar_1042%20Tested/Annotation/annotated.png) | **Swipe gesture** → The current selected day, month, week, year is not preserved after rotating | 1. Go to the day view 2. Swipe or tap to the next day 3. Rotate the device... |
| [FossifyOrg_Camera_91](Dataset/orientation/FossifyOrg_Camera_91%20Tested) | FossifyOrg/Camera | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/orientation/FossifyOrg_Camera_91%20Tested/Annotation/annotated.png) | **Rotation/orientation change** → Countdown timer does not honor device orientation | 1. 0.2 (All versions are affected) 2. Open the app 3. Set the timer to 10 seconds 4. Tap the shutter button 5. Change de... |
| [FossifyOrg_Clock_85](Dataset/orientation/FossifyOrg_Clock_85%20Tested%20F) | FossifyOrg/Clock | ❌ | ❌ | ❌ | ✅ | ![screenshot](Dataset/orientation/FossifyOrg_Clock_85%20Tested%20F/Annotation/annotated.png) | **Swipe gesture** → Snooze not working in landscape | 1. Set an alarm 2. Turn off the screen to get full screen Alarm 3. When it goes off, rotate the device to landscape orie... |
| [FossifyOrg_Contacts_197](Dataset/orientation/FossifyOrg_Contacts_197%20Tested) | FossifyOrg/Contacts | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/orientation/FossifyOrg_Contacts_197%20Tested/Annotation/annotated.png) | **Rotation/orientation change** → View always changed to contact list when rotating the phone | 1. Open the app 2. Select either of ‘favourites’ or ‘groups’ tab, if not already selected 3. Rotate the phone by 90 degr... |
| [Waboodoo_HTTP-Shortcuts_262](Dataset/orientation/Waboodoo_HTTP-Shortcuts_262%20Tested) | Waboodoo/HTTP-Shortcuts | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/orientation/Waboodoo_HTTP-Shortcuts_262%20Tested/Annotation/annotated.png) | **Tap/click gesture** → [BUG] several dialogs disappear on screen rotation | 1. Go to the Main activity 2. Tap in add (plus in the right bottom) 3. A fragment similar to this will appear: <img src=... |
| [ankidroid_Anki-Android_16410](Dataset/orientation/ankidroid_Anki-Android_16410%20Tested) | ankidroid/Anki-Android | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/orientation/ankidroid_Anki-Android_16410%20Tested/Annotation/annotated.png) | **Rotation/orientation change** → [BUG]: Changing screen orientation clears stats' search options | 1. Go to statistics 2. Search something in the search bar. Or select collection over deck/all history over last twelve m... |

### Pinch/Zoom

| Bug ID | App | CARBON | ReBL | ReActDroid | AdbGPT | Screenshot | Remarks |
|--------|-----|--------|------|------------|--------|------------|---------|
| [FossifyOrg_Calendar_621](Dataset/pinch_zoom/FossifyOrg_Calendar_621%20Tested) | FossifyOrg/Calendar | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/pinch_zoom/FossifyOrg_Calendar_621%20Tested/Annotation/annotated.png) | **Pinch/zoom gesture** → Zoom level in weekly view locks | 1. Go to the Weekly view 2. Zoom out as far as you can vertically 3. Swipe right to get to the next week 4. Observe that... |
| [FossifyOrg_Camera_23](Dataset/pinch_zoom/FossifyOrg_Camera_23%20Tested) | FossifyOrg/Camera | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/pinch_zoom/FossifyOrg_Camera_23%20Tested/Annotation/annotated.png) | **Pinch/zoom gesture** → Doesn't use zoom camera to zoom | 1. On the preinstalled camera app, zoom in and cover the camera which blocks the zoom. 2. On fossify camera, zoom in wit... |
| [FossifyOrg_Gallery_289](Dataset/pinch_zoom/FossifyOrg_Gallery_289%20Tested) | FossifyOrg/Gallery | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/pinch_zoom/FossifyOrg_Gallery_289%20Tested/Annotation/annotated.png) | **Pinch/zoom gesture** → "Allow deep zooming images" creates artifacts in many images | 2. Have "Allow deep zooming images" enabled 3. Open an image 4. Exit the image or close the app 5. Open the image again ... |
| [FossifyOrg_Gallery_642](Dataset/pinch_zoom/FossifyOrg_Gallery_642%20Tested) | FossifyOrg/Gallery | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/pinch_zoom/FossifyOrg_Gallery_642%20Tested/Annotation/annotated.png) | **Pinch/zoom gesture** → Zoom doesn't work in photos | 1. Open a photo 2. Swipe to another photo 3. Try to zoom in... |
| [FossifyOrg_Gallery_728](Dataset/pinch_zoom/FossifyOrg_Gallery_728%20Tested) | FossifyOrg/Gallery | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/pinch_zoom/FossifyOrg_Gallery_728%20Tested/Annotation/annotated.png) | **Pinch/zoom gesture** → (Deep zooming) Can not pan after releasing only one finger after pinch zooming | 1. "Allow deep zooming images" must be enabled 2. Open a picture 3. With two fingers, (un)pinch to zoom in 4. Release on... |
| [FossifyOrg_Paint_125](Dataset/pinch_zoom/FossifyOrg_Paint_125%20Tested) | FossifyOrg/Paint | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/pinch_zoom/FossifyOrg_Paint_125%20Tested/Annotation/annotated.png) | **Pinch/zoom gesture** → Touch location and pen location different after zooming/rotation | sometimes paint goes to "draw to wrong place" bug mode. This happens typically after first drawing something with pencil... |
| [FossifyOrg_Paint_25](Dataset/pinch_zoom/FossifyOrg_Paint_25%20Tested) | FossifyOrg/Paint | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/pinch_zoom/FossifyOrg_Paint_25%20Tested/Annotation/annotated.png) | **Pinch/zoom gesture** → Eraser size not relative to zoom on minimum size | 1. Draw a line 2. Set brush size to the minimum 3. Run eraser through line 4. Zoom in/out 5. Run eraser through line at ... |
| [ankidroid_Anki-Android_16135](Dataset/pinch_zoom/ankidroid_Anki-Android_16135%20Tested) | ankidroid/Anki-Android | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/pinch_zoom/ankidroid_Anki-Android_16135%20Tested/Annotation/annotated.png) | **Pinch/zoom gesture** → [BUG]: Zooming in Statistics Page | 1. Open Statistics 2. Zoom in then Zoom Out 3. Scroll to the bottom... |
| [ankidroid_Anki-Android_17667](Dataset/pinch_zoom/ankidroid_Anki-Android_17667%20Tested) | ankidroid/Anki-Android | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/pinch_zoom/ankidroid_Anki-Android_17667%20Tested/Annotation/annotated.png) | **Long press gesture** → [BUG]: Width of "Deck options" page does not/cannot fit to screen (display) | 1. Open the app 2. Long press a deck 3. Tap "Deck options"... |
| [saber-notes_saber_192](Dataset/pinch_zoom/saber-notes_saber_192%20Tested) | saber-notes/saber | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/pinch_zoom/saber-notes_saber_192%20Tested/Annotation/annotated.png) | **Pinch/zoom gesture** → Two finger detection need improvement | 1. Toggle Finger Drawing mode 2. Select pen 3. Zoom in 4. Then Use two finger to navigate on page 5. You will be dot wil... |
| [streetcomplete_StreetComplete_6068](Dataset/pinch_zoom/streetcomplete_StreetComplete_6068%20Tested) | streetcomplete/StreetComp | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/pinch_zoom/streetcomplete_StreetComplete_6068%20Tested/Annotation/annotated.png) | **OutOfMemoryError when downloading after zoom out** | Steps: ... |
| [you-apps_WallYou_216](Dataset/pinch_zoom/you-apps_WallYou_216%20Tested) | you-apps/WallYou | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/pinch_zoom/you-apps_WallYou_216%20Tested/Annotation/annotated.png) | **Pinch/zoom gesture** → Improper edge-to-edge implementation | Open any picture in app Pinch zoom the picture until it's full screen size... |

### Quick Tap

| Bug ID | App | CARBON | ReBL | ReActDroid | AdbGPT | Screenshot | Remarks |
|--------|-----|--------|------|------------|--------|------------|---------|
| [LawnchairLauncher_lawnchair_5540](Dataset/quick_tap/LawnchairLauncher_lawnchair_5540%20Tested) | LawnchairLauncher/lawncha | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/quick_tap/LawnchairLauncher_lawnchair_5540%20Tested/Annotation/annotated.png) | **Swipe gesture** → Home Button Requires Double-Tap to Return to Default Home Page from Other Home S | 1. Set a specific home page as your default home screen in Lawnchair settings 2. Swipe or navigate to a different home p... |
| [anilbeesetti_nextplayer_1389](Dataset/quick_tap/anilbeesetti_nextplayer_1389%20Tested) | anilbeesetti/nextplayer | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/quick_tap/anilbeesetti_nextplayer_1389%20Tested/Annotation/annotated.png) | **Tap/click gesture** → Resuming doesn't work properly — video stops immediately on tap | 1. Set "Resume" to "Yes" in settings 2. Turn off "Autoplay" 3. Play or fast-forward a video to the end 4. Resume by tapp... |
| [ankidroid_Anki-Android_18529](Dataset/quick_tap/ankidroid_Anki-Android_18529%20Tested%20F) | ankidroid/Anki-Android | ❌ | ❌ | ❌ | ❌ | ![screenshot](Dataset/quick_tap/ankidroid_Anki-Android_18529%20Tested%20F/Annotation/annotated.png) | **Quick tap gesture** → You can touch some buttons during animations | 1. Tap and hold on a deck. 2. Using one finger tap on rename. 3. Using another finger quickly tap and hold on a deck.... |
| [ankidroid_Anki-Android_19641](Dataset/quick_tap/ankidroid_Anki-Android_19641%20Tested) | ankidroid/Anki-Android | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/quick_tap/ankidroid_Anki-Android_19641%20Tested/Annotation/annotated.png) | **[New study screen] Card was modified error when tapping the answer buttons quick** | Steps: 1. Open the new study screen with a few cards to review. 2. Spam the answer buttons or gestures.... |
| [ankidroid_Anki-Android_20789](Dataset/quick_tap/ankidroid_Anki-Android_20789%20Tested%20F) | ankidroid/Anki-Android | ❌ | ❌ | ❌ | ✅ | ![screenshot](Dataset/quick_tap/ankidroid_Anki-Android_20789%20Tested%20F/Annotation/annotated.png) | **Swipe gesture** → "Collection synced" notification is too high-priority | 1. Sync your collection through any means (e.g. swipe-up, tap the button) 2. Immediately lock the screen... |
| [ankidroid_Anki-Android_7138](Dataset/quick_tap/ankidroid_Anki-Android_7138%20Tested) | ankidroid/Anki-Android | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/quick_tap/ankidroid_Anki-Android_7138%20Tested/Annotation/annotated.png) | **Card skips when tapping Show Answer immediately** | Steps: ... |

### Scroll

| Bug ID | App | CARBON | ReBL | ReActDroid | AdbGPT | Screenshot | Remarks |
|--------|-----|--------|------|------------|--------|------------|---------|
| [Anthonyy232_Paperize_426](Dataset/scroll/Anthonyy232_Paperize_426%20Tested) | Anthonyy232/Paperize | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/scroll/Anthonyy232_Paperize_426%20Tested/Annotation/annotated.png) | **Scroll gesture** → [Bug] the Privacy Notice button disappears in landscape mode | (see full issue body) --- Full Issue Body --- **Describe the bug** After rotation, the Privacy Notice button disappears.... |
| [Fandroid745_Open-notes_15](Dataset/scroll/Fandroid745_Open-notes_15%20Tested) | Fandroid745/Open-notes | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/scroll/Fandroid745_Open-notes_15%20Tested/Annotation/annotated.png) | **No scroll support, (Bug)** | Steps: (see full issue body) --- Full Issue Body --- - [x] I’m using the latest OpenNotes version - [x] The device is rooted, and stuff has been removed via ... |
| [FossifyOrg_File-Manager_136](Dataset/scroll/FossifyOrg_File-Manager_136%20Tested) | FossifyOrg/File-Manager | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/scroll/FossifyOrg_File-Manager_136%20Tested/Annotation/annotated.png) | **Scroll gesture** → The screen refresh gesture works when the function is turned off | 1. Go to "Settings". 2. Scroll to "Scrolling" 3. Off "Enable pull-to-refresh from the top" 4. Select folder. 5. Cancel s... |
| [ankidroid_Anki-Android_5512](Dataset/scroll/ankidroid_Anki-Android_5512%20Tested) | ankidroid/Anki-Android | ✅ | ❌ | ✅ | ❌ | ![screenshot](Dataset/scroll/ankidroid_Anki-Android_5512%20Tested/Annotation/annotated.png) | **AnkiDroid scroll bug** | Steps: ... |
| [ankidroid_Anki-Android_5544](Dataset/scroll/ankidroid_Anki-Android_5544%20Tested) | ankidroid/Anki-Android | ✅ | ✅ | ✅ | ✅ | ![screenshot](Dataset/scroll/ankidroid_Anki-Android_5544%20Tested/Annotation/annotated.png) | **AnkiDroid scroll bug** | Steps: Result: The font size is much to large. Ankidroid versions: 2.9.1 and before Workaround: use a much smaller scaling, e. g. 30 or 40% to be able to sca... |
| [netmackan_ATimeTracker_124](Dataset/scroll/netmackan_ATimeTracker_124%20Tested) | netmackan/ATimeTracker | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/scroll/netmackan_ATimeTracker_124%20Tested/Annotation/annotated.png) | **Could not scroll on the menu** | Steps: ... |

### Swipe

| Bug ID | App | CARBON | ReBL | ReActDroid | AdbGPT | Screenshot | Remarks |
|--------|-----|--------|------|------------|--------|------------|---------|
| [A-EDev_Flow_27](Dataset/swipe/A-EDev_Flow_27%20Tested) | A-EDev/Flow | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/A-EDev_Flow_27%20Tested/Annotation/annotated.png) | **Swipe gesture** → Fullscreen gesture conflict — brightness/volume gestures trigger when opening co | 1. Play a video in fullscreen mode 2. Try to open the control panel (swipe down from top for notifications)... |
| [A-EDev_Flow_284](Dataset/swipe/A-EDev_Flow_284%20Tested) | A-EDev/Flow | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/A-EDev_Flow_284%20Tested/Annotation/annotated.png) | **Pinch/zoom gesture** → Pinch-in zoom breaks player gestures — volume and brightness become unresponsive | 1. Open Flow and navigate to any video 2. Start playback 3. Perform a pinch-to-zoom gesture on the video (zoom the video... |
| [CodeWorksCreativeHub_mLauncher_809](Dataset/swipe/CodeWorksCreativeHub_mLauncher_809%20Tested) | CodeWorksCreativeHub/mLau | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/swipe/CodeWorksCreativeHub_mLauncher_809%20Tested/Annotation/annotated.png) | **Long press gesture** → [Bug Report] Short swipe gesture broken | 1. 10.7.5 2. Go to homescreen. 3. Use swipe gesture without long press. 4. No response.... |
| [Droid-ify_client_238](Dataset/swipe/Droid-ify_client_238%20Tested) | Droid-ify/client | ✅ | ✅ | ✅ | ✅ | ![screenshot](Dataset/swipe/Droid-ify_client_238%20Tested/Annotation/annotated.png) | **Tap/click gesture** → [BUG] App crashing on changing settings. | 1. Open the app and go to the settings section. 2. Click on any settings toggle to alter it. I faced this issue for the ... |
| [Droid-ify_client_583](Dataset/swipe/Droid-ify_client_583%20Tested) | Droid-ify/client | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/Droid-ify_client_583%20Tested/Annotation/annotated.png) | **Pinch/zoom gesture** → [BUG] Swiping images zooms instead of zooming | Go to https://www.f-droid.org/packages/io.github.muntashirakon.Music/ Click on any preview image Touch the screen to swi... |
| [FossifyOrg_Calendar_1103](Dataset/swipe/FossifyOrg_Calendar_1103%20Tested) | FossifyOrg/Calendar | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/swipe/FossifyOrg_Calendar_1103%20Tested/Annotation/annotated.png) | **Accessibility - have screen reader anounce existence/count of events on a day in** | Steps: 1. Enable the TalkBack screen reader. 2. Open the calendar app and navigate to the monthly view. 3. Move through the days of the month using TalkBack ... |
| [FossifyOrg_Calendar_153](Dataset/swipe/FossifyOrg_Calendar_153%20Tested) | FossifyOrg/Calendar | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/swipe/FossifyOrg_Calendar_153%20Tested/Annotation/annotated.png) | **Swipe gesture** → Swiping in monthly view is a pain | 1. Open monthly view 2. Swipe right or left to the next month 3. It snaps back to the currently displayed month in 8 of ... |
| [FossifyOrg_Clock_156](Dataset/swipe/FossifyOrg_Clock_156%20Tested%20F) | FossifyOrg/Clock | ❌ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/FossifyOrg_Clock_156%20Tested%20F/Annotation/annotated.png) | **Timer alarm turned off by swiping from the status bar** | Steps: 1. Set up any timer and start it 2. Wait for the alarm sound 3. Pull down from the status bar 4. You'll not be able to silence the timer alarm by push... |
| [FossifyOrg_Gallery_237](Dataset/swipe/FossifyOrg_Gallery_237%20Tested) | FossifyOrg/Gallery | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/FossifyOrg_Gallery_237%20Tested/Annotation/annotated.png) | **Swipe gesture** → Vertical gesture to adjust video volume does not work | 1. The option to adjust brightness and volume with gestures is enabled 2. Opening a video file 3. I swipe my finger on t... |
| [FossifyOrg_Gallery_584](Dataset/swipe/FossifyOrg_Gallery_584%20Tested%20F) | FossifyOrg/Gallery | ❌ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/FossifyOrg_Gallery_584%20Tested%20F/Annotation/image.png) | **Tap/click gesture** → When trying to open some JPG files, the gallery app crashes or returns to the ma | 1. Go to any folder with certain photos 2. Click on jpg file 3. The app either crashes or returns to main screen... |
| [FossifyOrg_Gallery_940](Dataset/swipe/FossifyOrg_Gallery_940%20Tested) | FossifyOrg/Gallery | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/FossifyOrg_Gallery_940%20Tested/Annotation/annotated.png) | **Rotation/orientation change** → Disabled notch overlaps brightness control area | 1. Disable "Show notch if available" in settings 2. Enable "Allow controlling photo brightness with vertical gestures" 3... |
| [FossifyOrg_Launcher_66](Dataset/swipe/FossifyOrg_Launcher_66%20Tested) | FossifyOrg/Launcher | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/FossifyOrg_Launcher_66%20Tested/Annotation/annotated.png) | **Swipe gesture** → Slow, jerky animation when opening a folder or swiping between screens | 1. Set Fossify Launcher as the main launcher app. 2. Add app icons in at least 2 screens 3. Swipe left and right 4. Crea... |
| [FossifyOrg_Messages_80](Dataset/swipe/FossifyOrg_Messages_80%20Tested) | FossifyOrg/Messages | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/FossifyOrg_Messages_80%20Tested/Annotation/annotated.png) | **Long press gesture** → Navigation Stack gets too Large (Hitting Back Button) | 1. Click on the + icon to compose a new message 2. Select a random contact and wait for conversation screen to pop up 3.... |
| [FossifyOrg_Notes_190](Dataset/swipe/FossifyOrg_Notes_190%20Tested) | FossifyOrg/Notes | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/swipe/FossifyOrg_Notes_190%20Tested/Annotation/annotated.png) | **Swipe gesture** → crash while using the search field. | 1. in a long note, search -> 'any text'. 2. use the arrows until the screen drops. 3. swipe right or left to the next no... |
| [Kin69_EasyNotes_356](Dataset/swipe/Kin69_EasyNotes_356%20Tested) | Kin69/EasyNotes | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/Kin69_EasyNotes_356%20Tested/Annotation/annotated.png) | **[BUG]** | Steps: (see full issue body) --- Full Issue Body --- - [x] I’m using the latest EasyNotes version - [x] The device is not rooted, and nothing has been remove... |
| [LawnchairLauncher_lawnchair_4642](Dataset/swipe/LawnchairLauncher_lawnchair_4642%20Tested) | LawnchairLauncher/lawncha | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/swipe/LawnchairLauncher_lawnchair_4642%20Tested/Annotation/annotated.png) | **Rotation/orientation change** → [BUG] Gesture navigation gets locked in one orientation until a launcher restart | 1. Start launchair 2. Switch orientation 3. Notice the recents screen won't open 4. Restart launchair while staying at t... |
| [LawnchairLauncher_lawnchair_4708](Dataset/swipe/LawnchairLauncher_lawnchair_4708%20Tested) | LawnchairLauncher/lawncha | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/LawnchairLauncher_lawnchair_4708%20Tested/Annotation/annotated.png) | **Swipe gesture** → [BUG] Gesture nav: swiping up to go home when already in Lawnchair creates a "gh | 1. Ensure gesture navigation is enabled 2. Ensure Lawnchair is set as the default launcher app 3. Go to the homescreen 4... |
| [LawnchairLauncher_lawnchair_5496](Dataset/swipe/LawnchairLauncher_lawnchair_5496%20Tested) | LawnchairLauncher/lawncha | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/swipe/LawnchairLauncher_lawnchair_5496%20Tested/Annotation/annotated.png) | **Swipe gesture** → [BUG] Lawnchair crashes in the recent menu | 1. Open any application (not the home screen). 2. Try to open the Recents menu: Via gesture (swipe up and hold) or via t... |
| [MetrolistGroup_Metrolist_3391](Dataset/swipe/MetrolistGroup_Metrolist_3391%20Tested) | MetrolistGroup/Metrolist | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/swipe/MetrolistGroup_Metrolist_3391%20Tested/Annotation/annotated.png) | **Back gesture not working in the player screen** | Steps: (see full issue body) --- Full Issue Body --- - [x]  I am able to reproduce the bug with the [latest debug version](https://github.com/MetrolistGroup/... |
| [OuterTune_OuterTune_1044](Dataset/swipe/OuterTune_OuterTune_1044%20Tested) | OuterTune/OuterTune | ✅ | ✅ | ❌ | ❌ | ![screenshot](Dataset/swipe/OuterTune_OuterTune_1044%20Tested/Annotation/annotated.png) | **Pressing Home or any button activates back gesture.** | Steps: (see full issue body) --- Full Issue Body --- - [x] I am able to reproduce the bug with the [latest debug version](https://github.com/OuterTune/OuterT... |
| [anilbeesetti_nextplayer_1127](Dataset/swipe/anilbeesetti_nextplayer_1127%20Tested) | anilbeesetti/nextplayer | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/anilbeesetti_nextplayer_1127%20Tested/Annotation/annotated.png) | **Swipe gesture** → Vertical swipe misbehaviour — volume/brightness gesture too sensitive in landsca | 1. Open a video in landscape mode 2. Try to swipe down from the top to open the notification drawer 3. Observe that the ... |
| [ankidroid_Anki-Android_14934](Dataset/swipe/ankidroid_Anki-Android_14934%20Tested%20F) | ankidroid/Anki-Android | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/ankidroid_Anki-Android_14934%20Tested%20F/Annotation/annotated.png) | **Swipe gesture** → talkback can't see sometimes front, sometimes back and sometimes both sides of a | 1. enable talkback 2. open ankidroid as usual (or doesn't matter if you do the steps 1 and 2 in refersed order) 3. touch... |
| [bartoostveen_ViTune_710](Dataset/swipe/bartoostveen_ViTune_710%20Tested) | 25huizengek1/ViTune | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/bartoostveen_ViTune_710%20Tested/Annotation/annotated.png) | **Swipe gesture** → Notification shows wrong album art for current song | 1. Play a song in ViTune 2. Swipe down to open notification panel 3. Observe the notification shows wrong album art... |
| [breezy-weather_breezy-weather_205](Dataset/swipe/breezy-weather_breezy-weather_205%20Tested) | breezy-weather/breezy-wea | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/breezy-weather_breezy-weather_205%20Tested/Annotation/annotated.png) | **Swipe gesture** → [Location list] Swipe left animation stays after cancelling weather provider dia | 1. Add the current location in the location list. 2. Swipe left on the current location to open the dialog for selecting... |
| [breezy-weather_breezy-weather_85](Dataset/swipe/breezy-weather_breezy-weather_85%20Tested) | breezy-weather/breezy-wea | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/swipe/breezy-weather_breezy-weather_85%20Tested/Annotation/annotated.png) | **Persistent notification setting - on / off is inverted** | Steps: 1. Go into settings -> widgets. 2. Activate the notification widget. 3. Leave the persistent option disabled. 4. 0.4-alpha... |
| [dessalines_thumb-key_371](Dataset/swipe/dessalines_thumb-key_371%20Tested) | dessalines/thumb-key | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/dessalines_thumb-key_371%20Tested/Annotation/annotated.png) | **Swipe gesture** → Swipe input eaten on capitalization/mode switch | (see full issue body) --- Full Issue Body --- **Thumb-Key Version** 1.12.0 **Describe the bug** If you hit capitalize, n... |
| [iamrasel_lunar-launcher_82](Dataset/swipe/iamrasel_lunar-launcher_82%20Tested) | iamrasel/lunar-launcher | ✅ | ❌ | ❌ | ✅ | ![screenshot](Dataset/swipe/iamrasel_lunar-launcher_82%20Tested/Annotation/annotated.png) | **Swipe gesture** → Random crashes when closing applications | 1. Have application open and being used 2. Swipe up to put current application in background 3. Lunar crashes 4. Occurre... |
| [libre-tube_LibreTube_8245](Dataset/swipe/libre-tube_LibreTube_8245%20Tested) | libre-tube/LibreTube | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/libre-tube_LibreTube_8245%20Tested/Annotation/annotated.png) | **Tap/click gesture** → Laggy animation when minimizing player with Back button (video & audio modes) | (see full issue body) --- Full Issue Body --- 1. Open the app and start playback (video mode) of any item. 2. While play... |
| [msasikanth_twine_1566](Dataset/swipe/msasikanth_twine_1566%20Tested) | msasikanth/twine | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/msasikanth_twine_1566%20Tested/Annotation/annotated.png) | **[BUG] Incomplete Predictive Back Animation** | Steps: (see full issue body) --- Full Issue Body --- **Describe the bug** When you open a post and then close it using back gesture, it starts with the predi... |
| [you-apps_ClockYou_85](Dataset/swipe/you-apps_ClockYou_85%20Tested) | you-apps/ClockYou | ✅ | ✅ | ❌ | ✅ | ![screenshot](Dataset/swipe/you-apps_ClockYou_85%20Tested/Annotation/annotated.png) | **App cycles through previously visited tabs on back gesture instead of closing** | Steps: 1. Open the app. 2. Navigate to any other tab. 3. Perform a back gesture.... |
| [you-apps_ConnectYou_155](Dataset/swipe/you-apps_ConnectYou_155%20Tested) | you-apps/ConnectYou | ✅ | ❌ | ❌ | ❌ | ![screenshot](Dataset/swipe/you-apps_ConnectYou_155%20Tested/Annotation/annotated.png) | **Tap/click gesture** → Back on search bar quits the app. | 1. Click the search bar 2. press the back gesture/button ### Expected behavior The app should get out of the search func... |

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