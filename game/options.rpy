init python:
    build.name = "katawashoujo"
    build.directory_name = "katawashoujo"
    build.executable_name = "KatawaShoujo"
    build.include_update = False

    #archive for files common to all platforms
    build.archive("data", "all")
    build.archive("basevideos", "windows linux mac renpy android")
    build.archive("iosvideos", "ios")

    #Common files that need to be packaged for all platforms
    build.classify("game/presplash.*", "data")
    build.classify("game/bgm/**", "data")
    build.classify("game/bgs/**", "data")
    build.classify("game/event/**", "data")
    build.classify("game/font/**", "data")
    build.classify("game/sfx/**", "data")
    build.classify("game/sprites/**", "data")
    build.classify("game/ui/**", "data")
    build.classify("game/vfx/**", "data")

    #Packaging the base videos for all versions except iOS
    build.classify("game/video/base*.*", "basevideos")

    ##Android specific classifiers
    build.classify(".android.json", "android")
    build.classify("android-*.png", "android")
    build.classify("android-*.jpg", "android")

    ##iOS specific classifiers
    build.classify("ios-presplash.*", "ios")
    build.classify("game/video/ios*.*", "iosvideos")

    build.classify("ios-launchimage.png", None)
    build.classify("game/ios-icon.png", None)
    
    ##Removing savegames folder
    build.classify("game/saves/", None)

    ##Removing other not needed data
    build.classify("game/cache/", None)
    build.classify('**~', None)
    build.classify('.**', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**.rpy', None)
    build.classify('**z_dev.rpyc', None)
    build.classify('**/thumbs.db', None)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
