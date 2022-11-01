# What is this? And why did you do it?
This is a porting/refactor of the visual novel "[KatawaShoujo](https://www.katawa-shoujo.com/)" to allow it to **properly** run on **RenPy version 8**.

The objective of this porting is to have a clean source code base that compiles on all the platforms supported by RenPy 8 without requiring any hack, manual swapping of game assets/resources before compiling or "weird" custom wrappers.

As of now, this project, using RenPy 8.0.3, correctly compiles and runs on:
 - Desktop platforms: Windows, Linux, MacOS 
 - Mobile platforms: Android 5.0+, iOS 13+

Unfortunately compiling on iOS still requires a minor hack/fix described later in this readme.

Another reason this porting was made is that recently the youtuber Gigguk released [a video about this game](https://www.youtube.com/watch?v=8N5hgp0SMwM) that, despite/thanks to the clickbaity title, reignited the interest in the amazing storyline that this visual novel has.
Since it seems like many people that are trying to play Katawa Shoujo for the first time are having troubles finding a fully working version that runs on mobile devices, I thought it would be a good idea to spend some time to make one.


# How do I play it?
## Installation
- ### Desktop platforms:
	- **Windows:** download the release `katawashoujo-win.zip`, extract it and run `KatawaShoujo.exe`
	- **Linux:** download the release `katawashoujo-linux.tar.bz2`, extract it, give executable permissions (`chmod +x`) to `KatawaShoujo.sh` and run it
	-  **MacOS:** download the release `katawashoujo-mac.zip`, extract it and move the KatawaShoujo.app file to you Application folder. You can now run it.
	
- ### Mobile platforms:
	- **Android:** download the release `com.fls.katawashoujo-release.apk`, open it with your preferred file manager application and install it.  
	Google Play Protect may alert you that the app does not come from a trusted developer.  
	This is normal: the `.apk` file is not signed with a google issued developer key, but you can ignore the warning and install anyway.  
	- **iOS:** since on iOS sideloading isn't possible by default, installing the release requires a way to install unsigned `.ipa` files on your iDevice.  Some of the available options are:
		- **Using [TrollStore](https://github.com/opa334/TrollStore):** download the release `KatawaShoujo.ipa` on your device, open it with TrollStore and confirm the installation.
		- **Using [AltStore](https://altstore.io/):** setup AltStore on your computer and iDevice following the **[Getting Started guide](https://faq.altstore.io/)**. You can then download the release `KatawaShoujo.ipa` on your computer and install it on your iDevice using AltServer.
		- **Installing on a jailbroken device:** if you have a jailbroken device you already know how to install an `.ipa`

## Touch screen controls

 - **Open/close the in game menu:** swipe from the top to the bottom of the screen ⬇️
 - **Rewind / go back:** swipe from the right to the left of the screen ⬅️
 - **Skip video:**
	 -  **Android:** swipe from the bottom to the top of the screen while the video is playing ⬆️
	 - **iOS:** long press anywhere on the screen while the video is playing

# How do I compile it myself?

 1. Download the latest version of **RenPy 8.x** from **[HERE](https://www.renpy.org/)**
 2.  Clone this repo somewhere on your computer
 3. Open RenPy, go into `Preferences` and set the `Project Directory` to the folder where you cloned this git repo
 4. Hit `Refresh` and you should now see the project in the RenPy window
 5. On the bottom right of the RenPy windows you'll find the release build for the various platforms. 


For more details on compiling for **desktop platforms** please refer to the [**Building Distributions**](https://www.renpy.org/doc/html/build.html) page of the Renpy documentation for more details on compiling the project on desktop platforms.

For more details on compiling for **Android** please refer to the **[Building Android Applications](https://www.renpy.org/doc/html/android.html#building-android-applications)** section of the RenPy documentation.

## Compiling on iOS
If you're interested in compiling for **iOS** please make sure to thoroughly read the [**iOS page**](https://www.renpy.org/doc/html/ios.html) of the RenPy documentation
You should also have an at least basic knowledge of Xcode in relation to the iOS app compilation and signing process.

### iOS COMPILATION QUIRK:
After generating the Xcode project from RenPy the `VideoPlayer.m` file in the root of the Xcode project needs to be patched to:

 1. properly close the player when a video finishes playing
 2. add the "long tap to skip the video" feature

To do it, you need to either:

 - Apply **[THIS PATCH](https://gist.github.com/gcammisa/15b217a9566e3665e8c6b53af3135206)** to the `VideoPlayer.m` file
or
 - Replace the `VideoPlayer.m` file with [**THIS PREPATCHED ONE**](https://gist.github.com/gcammisa/cdfa8a242420f6ec1aa6142d5f01f454)

This patch was made using the VideoPlayer.m generated by RenPy 8.0.3.
Please keep in mind that future versions of RenPy might introduce changes to this.

# Ending notes:
## Testing
As of now, this porting has been tested on:
 - Windows 11
 - Arch Linux
 - MacOS Monterey
 - iPad 8th (iOS 5.0.1)
 - Motorola Edge+ (Android 12)
 - Motorola G4 Plus (Android 8.1)
 - ZTE Axon 7 (Android 7.1.2)
 - Android Emulator (MEMU - Android 5.1.1)
 
## Credits
All the assets belong to Four Leaf Studios, the original developers of Katawa Shoujo.  
This porting is not supported in any way by Four Leaf Studios and any problem with it **SHOULD NOT** be reported to them (open an issue on this github repo instead).
