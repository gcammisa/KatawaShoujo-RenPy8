init -4 python:

    displayStrings = object()

    def switch_language(target):
        global displayStrings, gm_exit_to, s_scenes, save_name, np_current_language
        if target in available_languages:
            renpy.block_rollback()
            persistent.current_language = target
            np_current_language = target
            displayStrings = displayDict[target]
            s_scenes = make_s_scenes(target)
            store.readback_buffer = []
            save_name = last_scene_label
            named_config()
            initialize_prefs()
            define_characters()
            for this_style, this_property in displayStrings.styleoverrides.items():
                setattr(style.default, this_style, this_property)
            
            
            style.nvl_vbox.box_spacing = displayStrings.nvl_paragraph_distance
            
            style.rebuild()
            if last_visited_label:
                gm_exit_to = wrap_label(last_visited_label)
        return True

    def make_s_scenes(lang):
        if lang == master_language:
            return displayDict[master_language].s_scenes
        
        new_s_scenes = []
        for scene in displayDict[master_language].s_scenes:
            breakflag = False
            for langscene in displayDict[lang].s_scenes:
                if ((scene[1] == langscene[1]) and (langscene[1] != rp_actmark)) or ((scene[3] == langscene[3]) and (scene[1] == rp_actmark)):
                    new_s_scenes.append(langscene)
                    breakflag = True
                    break
            if not breakflag:
                new_s_scenes.append(scene)
        
        return new_s_scenes

    def init_language(lang):
        if lang == master_language:
            store.displayDict[lang] = object()
            return
        import copy
        store.displayDict[lang] = copy.deepcopy(displayDict[master_language])
        store.available_languages.append(lang)


    master_language = "en"

    available_languages = [master_language]

    if not persistent.current_language:
        persistent.current_language = master_language




    mainfont = "font/playtime.ttf"
    titlefont = mainfont
    interfacefont = mainfont
    srsfont = "font/gentium.ttf"

    config.font_replacement_map["font/playtime.ttf", True, False] = ("font/playtime_bold.ttf", False, False)




    displayDict = {}



init -2 python:




    def named_config():
        
        config.file_entry_format = "%(time)s // "+displayStrings.play_time_label+": %(playtime)s\n%(save_name)s"
        
        config.time_format = displayStrings.timeformat
        config.window_title = displayStrings.window_name
        
        
        config.main_menu = [
            ( displayStrings.main_menu_start, ui.jumps("start_from_mm", "game_main_transition"), 'True'),
            ( displayStrings.main_menu_load, ui.jumps("load_screen", "main_game_transition"), 'renpy.list_saved_games()' ),
            ( displayStrings.main_menu_extra, ui.jumps("extra_from_mm"), 'get_available_scenes() or get_available_music() or get_available_images()'),
            ( displayStrings.main_menu_config, ui.jumps("prefs_screen", "main_game_transition"), 'True' ),
            ( displayStrings.main_menu_quit, ui.jumps("softquit"), 'True' ),
            ]
        
        
        config.game_menu = [
           ( "return", displayStrings.game_menu_return, ui.jumps("_return"), 'True'),
           ( "gm_image", displayStrings.game_menu_show, ui.jumps("gm_image"), 'True'),
           ( "gm_image", displayStrings.game_menu_history,  ui.jumps("text_history_gm", "intra_transition"), 'True'),
           ( "skipping", displayStrings.game_menu_skip, ui.jumps("_return_skipping"), 'config.allow_skipping and not mm_context()'),
           ( "automode", displayStrings.game_menu_auto, ui.jumps("afm_on"), 'True'),
           ( "prefs", displayStrings.game_menu_config, ui.jumps("prefs_screen", "intra_transition"), 'True' ),
           ( "save", displayStrings.game_menu_save, ui.jumps("save_screen", "intra_transition"), 'playthroughflag and not mm_context()' ),
           ( "load", displayStrings.game_menu_load, ui.jumps("load_screen", "intra_transition"), 'renpy.list_saved_games()'),
           ( "mainmenu", displayStrings.game_menu_main, ui.jumps("confirm_mm", "intra_transition"), 'not mm_context()' ),
           ( "quit", displayStrings.game_menu_quit, ui.jumps("confirm_quit", "intra_transition"), 'True' ),
           ]
        
        config.joystick_keys = [
            (displayStrings.joy_left, 'joy_left'),
            (displayStrings.joy_right, 'joy_right'),
            (displayStrings.joy_up, 'joy_up'),
            (displayStrings.joy_down, 'joy_down'),
            (displayStrings.joy_dismiss, 'joy_dismiss'),
            (displayStrings.joy_rollback, 'joy_rollback'),
            (displayStrings.joy_holdskip, 'joy_holdskip'),
            (displayStrings.joy_toggleskip, 'joy_toggleskip'),
            (displayStrings.joy_hide, 'joy_hide'),
            (displayStrings.joy_menu, 'joy_menu'),
            ]


init 5 python:

    switch_language(persistent.current_language)




init 3 python:



    tl_notes = {}
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
