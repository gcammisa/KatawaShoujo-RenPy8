

label splashscreen:


    scene mmcache
    show black
    with None

    $ renpy.pause(0.2)

    $ renpy.movie_cutscene(vid_4ls)
    $ renpy.pause(0.5)
    $ from_splash = True

    return

label main_menu:


    python:
        if from_splash:
            renpy.transition(Dissolve(1.0))
            from_splash = False
        menu_init()
    jump main_menu_screen



label _custom_game_menu(_game_menu_screen=_game_menu_screen):
    if not _game_menu_screen:
        return



    call _enter_game_menu from _call__enter_game_menu_cgm

    if renpy.has_label("game_menu"):
        jump expression "game_menu"

    jump expression _game_menu_screen



label gm_bare:

    python:
        footerstring = ""
        if previous_language == None:
            previous_language = persistent.current_language
        gm_active = True
        config.skipping = None
        layout.navigation("gm_bare")
        if name_from_label(save_name):
            currentscenename = name_from_label(save_name)
            if not playthroughflag:
                currentscenename += " ("+ displayStrings.game_menu_replay_indicator +")"
            footerstring += displayStrings.play_time_label+": "+time_from_seconds(renpy.get_game_runtime())+"\n"+displayStrings.game_menu_current_scene+": "+currentscenename

        nowplaying = get_music_name()
        if nowplaying:
            footerstring += "\n"+displayStrings.game_menu_current_music+": "+nowplaying

        ui.text(footerstring, text_align=0.5, xalign=0.5, yalign=0.98, size=18)
        ui.interact()

label text_history:

    $ renpy.transition(config.main_game_transition)
    $ gm_active = True
    $ entered_from_game = True

label text_history_gm:
    python:

        layout.navigation(None)
        ui.image(style.gm_root.background)
        ui.image("ui/bg-config.png", xalign=0.5, yalign=0.5)

        yadj = ui.adjustment()

        if not current_line and len(readback_buffer) == 0:
            lines_to_show = []
        elif current_line and len(readback_buffer) == 0:
            lines_to_show = [current_line]
        elif current_line and current_line != readback_buffer[-1]:  
            lines_to_show = readback_buffer + [current_line]
        else:
            lines_to_show = readback_buffer

        ui.vbox(xpos=180, ypos=120, background=None)
        ui.text(displayStrings.text_history_caption, style="page_caption")
        ui.hbox(xpos=0)
        vp = ui.viewport(yadjustment=yadj, offsets=(0.0,1.0), mousewheel=False, draggable=False, xmaximum=415, ymaximum = 296, xalign=0.5, yalign=0.5)
        ui.vbox(xfill=True)
        for line in lines_to_show:
            if line[0] and line[0] != preparse_say_for_store(NARRATOR_NAME):
                ui.text(line[0], style="readback_label", **displayStrings.styleoverrides)
            ui.text(line[1], style="readback_text", **displayStrings.styleoverrides)
            ui.null(height=10)
        ui.close()
        ui.null(width=10)
        ui.vbox()
        ui.imagebutton(ib_base("ui/bt-vscrollup.png"), "ui/bt-vscrollup.png", clicked=decrease_rb_yoffset)
        ui.bar(adjustment=yadj, style='vscrollbar')
        ui.imagebutton(ib_base("ui/bt-vscrolldown.png"), "ui/bt-vscrolldown.png", clicked=increase_rb_yoffset)
        ui.close()
        ui.close()
        ui.close()
        ui.add(renpy.Keymap(t=ui.returns(True)))

        viewportkeys(decrease_rb_yoffset,increase_rb_yoffset)

        if not entered_from_game:
            return_func = _intra_jumps(_game_menu_screen, "intra_transition")
        else:
            entered_from_game = False
            return_func = ui.jumps("custom_return")

        ui.add(renpy.Keymap(t=return_func))
        return_button(return_func)

        ui.interact()

        renpy.jump("text_history_gm")

label image_key:
    $ renpy.transition(config.main_game_transition)
    $ gm_active = True
    $ entered_from_game = True

label gm_image:

    python:

        layout.navigation(None)

        renpy.transition(config.intra_transition)




        if entered_from_game:
            ui.add(renpy.Keymap(h=gm_image_return_to_game))
            ui.add(renpy.Keymap(mouseup_2=gm_image_return_to_game))
            ui.add(renpy.Keymap(joy_hide=gm_image_return_to_game))
            ui.add(renpy.Keymap(game_menu=gm_image_return_to_game))
            ui.add(renpy.Keymap(dismiss=gm_image_return_to_game))
        else:
            ui.add(renpy.Keymap(game_menu=ui.returns(True)))
            ui.add(renpy.Keymap(dismiss=ui.returns(True)))
        ui.interact()

        renpy.transition(config.intra_transition)
        renpy.jump(_game_menu_screen) 

label quit_from_os:
    python:
        renpy.jump("softquit")

label confirm_quit:

    python:
        if not ask_to_quit:
            renpy.jump("softquit")
        else:
            transition = config.intra_transition
            if not gm_active:
                transition = config.enter_transition
            gi_result = _yesno_prompt(None, displayStrings.yesno_quit, im.Image("ui/sd-hanako.png",xpos=515,ypos=305), transition=transition)
            if gi_result:
                renpy.jump("softquit")
            else:
                if quit_from_os_flag and gm_active:
                    quit_from_os_flag = False
                    renpy.jump("simple_return")
                elif gm_active:
                    quit_from_os_flag = False
                    renpy.jump(_game_menu_screen)
                else:
                    quit_from_os_flag = False
                    renpy.jump("_return")

label confirm_mm:

    python:
        layout.navigation(None)
        if playthroughflag:
            gi_result = _yesno_prompt(None, displayStrings.yesno_return_to_main, im.Image("ui/sd-shizune.png",xpos=195,ypos=275))
            if gi_result:
                renpy.music.stop()
                renpy.full_restart(transition=config.game_main_transition)
            else:
                renpy.jump(_game_menu_screen) 
        else:
            renpy.music.stop()
            renpy.full_restart(transition=config.game_main_transition)


label prefs_key:
    $ renpy.transition(config.main_game_transition)
    $ gm_active = True
    $ entered_from_game = True

label prefs_screen:

    python:
        animate_mm = False

        layout.navigation(None)
        if prefs_looped:
            renpy.transition(ImageDissolve(im.Tile("ui/tr-checkwipe.png"), 0.5, 8))
        elif (mm_context() or entered_from_game) and not coming_from_prefs_sub:
            renpy.transition(config.main_game_transition)
        else:
            renpy.transition(config.intra_transition)
        if mm_context(): 
            ui.image(style.mm_static.background)
        coming_from_prefs_sub = False
        ui.image(style.gm_root.background)
        prefs_looped = False 
        ui.image("ui/bg-config.png", xalign=0.5, yalign=0.5)

        group_spacing = 8

        ui.vbox(xpos = 180, ypos = 120)
        ui.text(displayStrings.config_page_caption, style="page_caption")
        ui.null(height=8)
        ui.hbox()
        ui.null(width=20)
        ui.vbox()
        if not persistent.hdisabled:
            checkboximage = "ui/bt-cf-unchecked.png"
        else:
            checkboximage = "ui/bt-cf-checked.png"
        widget_button(displayStrings.hdisabled_label, checkboximage, toggle_h, xsize=300, widgetyoffset=0)
        ui.null(height=group_spacing)

        fullscreen_p.render_preference(disabled=disallow_fullscreen)
        ui.null(height=group_spacing)
        unreadskip_p.render_preference()
        choiceskip_p.render_preference()
        ui.null(height=group_spacing)
        textspeed_p.render_preference()
        afm_p.render_preference()
        ui.null(height=group_spacing)
        musicvol_p.render_preference()
        ui.hbox()
        sfxvol_p.render_preference()
        ui.null(width=20)
        widget_button(displayStrings.config_sfxtest_label, "ui/bt-musicplay.png", test_sound)

        ui.close()
        ui.null(height=group_spacing)
        widget_button(displayStrings.config_language_sel, "ui/bt-language.png", ui.jumps("language_screen"), xsize=300, widgetyoffset=3)
        if renpy.display.joystick.enabled: 
            widget_button(displayStrings.config_gamepad_label, "ui/bt-gamepad.png", ui.jumps("joystick_screen"), xsize=300, widgetyoffset=3)


        ui.close()
        ui.close()
        ui.close()
        if entered_from_game:
            ui.add(renpy.Keymap(K_F4=gm_page_return_to_game))
        return_button(ui.returns("return"))

        if config.developer:
            ui.keymap(I=devlvl_I)
            ui.keymap(D=devlvl_D)
            ui.keymap(Q=devlvl_Q)
            ui.keymap(N=devlvl_N)


        gi_result = ui.interact()
        if gi_result == "return":
            if mm_context():
                renpy.jump("_return")
            elif entered_from_game:
                gm_page_return_to_game()
            else:
                renpy.transition(config.intra_transition)
                renpy.jump(_game_menu_screen)
        prefs_looped = True
        renpy.jump("prefs_screen")

label language_screen:
    python:
        coming_from_prefs_sub = True

        renpy.transition(config.intra_transition)
        if mm_context(): 
            ui.image(style.mm_static.background)
        ui.image(style.gm_root.background)
        ui.image("ui/bg-config.png", xalign=0.5, yalign=0.5)
        layout.navigation(None)
        ui.vbox(xpos = 180, ypos = 120)
        ui.text(displayStrings.config_language_caption, style="page_caption")
        ui.null(height=8)
        ui.hbox()
        ui.null(width=10)
        ui.vbox()

        for language in available_languages:
            
            tl_progress = make_percentage(len(displayDict[language].s_scenes), len(displayDict[master_language].s_scenes))
            if tl_progress >= 100:
                tl_percentage = ""
            else:
                tl_percentage = ", " + str(tl_progress) + "%"
            
            if language == persistent.current_language:
                button_label = displayDict[language].activeLanguage
                button_state = "active"
                button_image = "ui/bt-language.png"
                button_function = None
            else:
                if language in displayStrings.allLanguages:
                    button_label = displayDict[language].activeLanguage+" ("+ displayStrings.allLanguages[language] + tl_percentage + ")"
                else:
                    if tl_percentage:
                        tl_percentage = " (" + tl_percentage + ")"
                    button_label = displayDict[language].activeLanguage + tl_percentage
                button_state = "button"
                button_image = "ui/bt-blank.png"
                button_function = renpy.curry(switch_language)(target=language)
            widget_button(text=button_label, displayable=button_image, clicked=button_function, state=button_state, xsize=500, widgetyoffset=3)

        ui.close()
        ui.close()
        ui.close()

        if not mm_context():
            ui.text(displayStrings.config_language_restart_note, text_align=0.5, xalign=0.5, yalign=0.98, size=18)

        return_button(ui.jumps("prefs_screen"))

        ui.interact()

    jump language_screen

label joystick_screen:
    python:
        coming_from_prefs_sub = True
        renpy.transition(config.intra_transition)
        if mm_context(): 
            ui.image(style.mm_static.background)
        ui.image(style.gm_root.background)
        ui.image("ui/bg-config.png", xalign=0.5, yalign=0.5)
        layout.navigation(None)
        ui.vbox(xpos = 180, ypos = 120)
        ui.text(displayStrings.gamepad_caption, style="page_caption")
        ui.null(height=8)
        ui.hbox()
        ui.null(width=10)
        ui.vbox()
        for label, key in config.joystick_keys:
            joy_button(label, key)
        ui.close()
        ui.close()
        ui.close()

        return_button(ui.jumps("prefs_screen"))

        ui.interact()

    jump joystick_screen

label load_key:
    $ renpy.transition(config.main_game_transition)
    $ gm_active = True
    $ entered_from_game = True

label load_screen:
    $ animate_mm = False
    $ mode = "manual"

label load_screen_loop:

    python:
        if mm_context(): 
            mybackground = LiveComposite((800, 600),
                                         (0, 0), style.mm_static.background,
                                         (0, 0), style.gm_root.background,
                                         (150, 100), "ui/bg-config.png")
        else:
            mybackground = LiveComposite((800, 600),
                                         (0, 0), style.gm_root.background,
                                         (150, 100), "ui/bg-config.png")

        if entered_from_game:
            ui.add(renpy.Keymap(K_F2=gm_page_return_to_game))
        fn, exists = custom_file_picker("load", False, mode, mybackground)

        if fn == "return":
            if mm_context():
                renpy.jump("_return")
            elif entered_from_game:
                gm_page_return_to_game()
            else:
                renpy.transition(config.intra_transition)
                renpy.jump(_game_menu_screen)
        elif fn == "_setmode":
            mode = exists
            renpy.jump("load_screen_loop")
        elif fn == "delete":
            background = None
            if mm_context():
                background = style.mm_static.background
            if _yesno_prompt(None, displayStrings.yesno_delete_savegame, im.Image("ui/sd-emi.png",xpos=510,ypos=275), background=background):
                
                renpy.unlink_save(exists)
        else:
            if not mm_context() and playthroughflag and statechangesincesave:
                if _yesno_prompt(None, displayStrings.yesno_load_in_game, im.Image("ui/sd-emi.png",xpos=510,ypos=275)):
                    renpy.load(fn)
            else:
                renpy.load(fn)

        renpy.jump("load_screen")

label save_key:
    $ renpy.transition(config.main_game_transition)
    $ gm_active = True
    $ entered_from_game = True

label save_screen:

    python:
        mybackground = LiveComposite((800, 600),
                                     (0, 0), style.gm_root.background,
                                     (150, 100), "ui/bg-config.png")
        if entered_from_game:
            ui.add(renpy.Keymap(K_F3=gm_page_return_to_game))
        _fn, _exists = custom_file_picker("save", True, False, mybackground)

        if _fn == "return":
            if entered_from_game:
                gm_page_return_to_game()
            else:
                renpy.transition(config.intra_transition)
                renpy.jump(_game_menu_screen)
        elif _fn == "delete":
            if _yesno_prompt(None, displayStrings.yesno_delete_savegame, im.Image("ui/sd-emi.png",xpos=510,ypos=275)):
                
                renpy.unlink_save(_exists)
        else:
            if not _exists or _yesno_prompt(None, displayStrings.yesno_save_overwrite, im.Image("ui/sd-lilly.png",xpos=195,ypos=275)):
                minutes, seconds = divmod(int(renpy.get_game_runtime()), 60)
                if save_name:
                    full_save_name = save_name + "#" + str(renpy.get_game_runtime())
                else:
                    full_save_name = "#" + str(renpy.get_game_runtime())
                try:
                    renpy.save(_fn, full_save_name)
                except Exception as e:
                    if config.debug:
                        raise
                    message = ( _(u"The error message was:") + "\n\n" +
                                e.__class__.__name__  + ": " + unicode(e) + "\n\n" +
                                _(u"You may want to try saving in a different slot, or playing for a while and trying again later.") )
                    _show_exception(_(u"Save Failed."), message)
                else:
                    statechangesincesave = False
                    persistent.fpicker_yoffset = -1
                    
                    _prompt(None, displayStrings.yesno_savesuccess, im.Image("ui/sd-rin.png",xpos=510,ypos=165))
                renpy.jump(_game_menu_screen)
        renpy.jump("save_screen")

label extra_from_mm:

    $ renpy.transition(config.main_game_transition)
    $ renpy.music.play(music_menus, fadeout=0.5, if_changed=True)

label extra_menu:

    python:

        animate_mm = False


        gallery_predict()

        sceneselectstate = "disabled"
        if get_available_scenes():
            sceneselectstate = "button"
        gallerystate = "disabled"
        if get_available_images():
            gallerystate = "button"
        musicstate = "disabled"
        if get_available_music():
            musicstate = "button"
        videostate = "disabled"
        if ((len(persistent.seen_videos) >= 1) or has_devlvl()):
            videostate = "button"

        ui.image(LiveComposite((800, 600),
                               (0, 0), style.mm_static.background,
                               (0, 0), style.gm_root.background,
                               (150, 100), "ui/bg-config.png"))

        ui.vbox(xpos=180, ypos=120, background=None)
        ui.text(displayStrings.extra_menu_caption, style="page_caption")
        ui.null(height=10)
        ui.hbox(box_spacing=15)
        extra_button(displayStrings.extra_music_button_label,"ui/sd-lilly.png",clicked=ui.jumps("music_menu", "intra_transition"), state=musicstate)
        extra_button(displayStrings.extra_gallery_button_label,"ui/sd-rin.png",clicked=ui.jumps("cg_gallery", "intra_transition"), state=gallerystate)
        extra_button(displayStrings.extra_scene_button_label,"ui/sd-shizune.png",clicked=ui.jumps("scene_select", "intra_transition"), state=sceneselectstate)
        extra_button(displayStrings.extra_opening_button_label,"ui/sd-emi.png",clicked=ui.jumps("video_menu", "intra_transition"), state=videostate)
        ui.close()
        ui.close()
        ui.hbox(xpos=540, ypos=346)
        extra_button(displayStrings.return_button_text,"ui/sd-hanako.png", clicked=ui.jumps("main_menu", "game_main_transition"), state="return")
        ui.close()


        if has_devlvl() and renpy.has_label("cruise_control"):
            layout.button("[[ flow tests ]", "mm", clicked=ui.jumpsoutofcontext("cruise_control"), xpos=510, ypos=115)

        ui.add(renpy.Keymap(game_menu=ui.jumps("main_menu", "game_main_transition")))
        ui.interact()
        renpy.transition(ImageDissolve(im.Tile("ui/tr-checkwipe2.png"), 0.5, 8))
        renpy.jump("extra_menu")

label act_op_ex(this_video, is_black=False):
    if not is_black:
        scene videowhite
    else:
        scene black
    with config.game_main_transition
    python:
        renpy.movie_cutscene(this_video)
        renpy.transition(config.main_game_transition)
    return

label video_menu:

    python:

        ui.image(LiveComposite((800, 600),
                               (0, 0), style.mm_static.background,
                               (0, 0), style.gm_root.background,
                               (150, 100), "ui/bg-config.png"))

        ui.vbox(xpos=180, ypos=120, background=None)
        ui.text(displayStrings.video_page_caption, style="page_caption")
        ui.null(height=4)

        ui.grid(3,2, padding=20, xpos=35, ypos=55)
        for this_video in displayStrings.videos:
            
            this_tn = this_video[1].replace(".mp4", "_tn.jpg")
            
            button_base = LiveComposite((110, 85),
                                        (0, 0), ib_base("ui/bt-cg-locked.png"),
                                        (5, 5), im.MatrixColor(this_tn, im.matrix.desaturate()))
            button_hover = LiveComposite((110, 85),
                                         (0, 0), "ui/bt-cg-locked.png",
                                         (5, 5), this_tn)
            
            
            if this_video[1] in persistent.seen_videos or has_devlvl():
                
                ui.imagebutton(button_base,
                               button_hover,
                               clicked=ui.returns(this_video[1]))
            else:
                ui.image(ib_disabled("ui/bt-cg-locked.png"))

        ui.close()
        ui.close()

        return_button(_intra_jumps("extra_menu", "intra_transition"))
        result = ui.interact()
        is_black = False

    if ((not renpy.ios and result == "video/base_op_1.mp4") or (renpy.ios and result == "video/ios_op_1.mp4")):
        $ is_black = True
    call act_op_ex (result, is_black) from _call_act_op_ex
    $ renpy.music.play(music_menus, fadein=5.0, fadeout=0.5)
    jump video_menu

label music_menu:

    python:

        nowplaying = get_music_name()
        available_music = get_available_music()

label music_menu_loop:

    python:
        auto_offset = 34
        if not persistent.mpicker_yoffset:
            persistent.mpicker_yoffset = 0

        yadj = ui.adjustment(range=auto_offset * (len(ex_m_tracks) - 8), value=persistent.mpicker_yoffset, changed=store_m_yoffset)

        viewportkeys(decrease_m_yoffset,increase_m_yoffset)

        ui.image(LiveComposite((800, 600),
                               (0, 0), style.mm_static.background,
                               (0, 0), style.gm_root.background,
                               (150, 100), "ui/bg-config.png"))

        ui.vbox(xpos=180, ypos=120, background=None)
        ui.text(displayStrings.music_page_caption, style="page_caption")
        if nowplaying:
            ui.text(displayStrings.music_now_playing + ": " + nowplaying, style="prefs_label")
        else:
            ui.text(" ", style="prefs_label")
        ui.null(height=4)
        ui.hbox(xpos=4)
        vp = ui.viewport(yadjustment=yadj, mousewheel=False, draggable=False, xmaximum=415, ymaximum = 267, xalign=0.5, yalign=0.5)
        ui.vbox(xfill=True)
        for name, file in ex_m_tracks:
            if file in available_music:
                if file == "" or not renpy.loadable(file):
                    layout.button(name, "mm", clicked=None)
                else:
                    layout.button(name, "mm", clicked=ui.returns((name, file)))
                ui.null(height=1)
            else:
                ui.null(height=1)
                ui.image(ib_disabled("ui/bg-lockedtrack.png", xpos=14))
            
            ui.null(height=3+displayStrings.selector_padding)
        ui.close()
        ui.vbox()
        ui.imagebutton(ib_base("ui/bt-vscrollup.png"), "ui/bt-vscrollup.png", clicked=decrease_m_yoffset)
        ui.bar(style='vscrollbar2', adjustment = yadj, changed=store_m_yoffset)
        ui.imagebutton(ib_base("ui/bt-vscrolldown.png"), "ui/bt-vscrolldown.png", clicked=increase_m_yoffset)
        ui.close()
        ui.close()
        ui.close()

        ui.hbox(xpos=180, ypos=449)
        musicvol_p_jukebox.render_preference()
        ui.null(width=20)
        widget_button(displayStrings.music_stop_button_text, "ui/bt-musicstop.png", clicked=ui.returns(("", "")), xsize=80)
        ui.close()

        return_button(_intra_jumps("extra_menu", "intra_transition"))

        result = ui.interact()
        renpy.music.play(result[1], fadeout=0.5, if_changed=True)
        nowplaying = result[0]
        renpy.jump("music_menu_loop")

label scene_select:


    python:
        menu_init()
        ss_desc = ""
        if filter != "Act 1":
            persistent.spicker_yoffset = 0
        filter = "Act 1"

label scene_select_loop:

    python:
        ui.image(LiveComposite((800, 600),
                               (0, 0), style.mm_static.background,
                               (0, 0), style.gm_root.background,
                               (150, 100), "ui/bg-config.png"))

        available_scenes = get_available_scenes(filter, include_locked=True, include_acts=True) or ()

        scrollable = False
        if len(available_scenes) > 8:
            scrollable = True

        if scrollable:
            auto_offset = 1.0 / (len(available_scenes) - 8)
            
            auto_offset = 34
        else:
            auto_offset = 0

        if not persistent.spicker_yoffset:
            persistent.spicker_yoffset = 0.0

        ui.vbox(xpos=180, ypos=120, background=None)
        ui.text(displayStrings.scene_page_caption, style="page_caption")
        ui.hbox()
        shown_buttons = ("Act 1", "Emi", "Hanako", "Lilly", "Rin", "Shizune")

        for button in shown_buttons:
            if button == "Act 1":
                label = displayStrings.act_term + " 1"
            elif button == "Emi":
                label = displayStrings.name_emi
            elif button == "Hanako":
                label = displayStrings.name_ha
            elif button == "Lilly":
                label = displayStrings.name_li
            elif button == "Rin":
                label = displayStrings.name_rin
            else: 
                label = displayStrings.name_shi
            
            path = button
            
            if button == filter:
                layout.button(label, "rpa_active", clicked=None)
            elif get_available_scenes(path):
                layout.button(label, "rpa", clicked=ui.returns(("_setfilter",path)))
            else:
                layout.button(label, "rpa", clicked=None)
        ui.close()
        ui.hbox()


        open_acts = []
        for (name, label, display, path, unlocked) in available_scenes:
            if unlocked and path not in open_acts:
                open_acts.append(path)

        yadj = ui.adjustment(range=auto_offset * (len(available_scenes) - 8), value=persistent.spicker_yoffset, changed=store_s_yoffset)

        scene_indent = 15

        vp = ui.viewport(yadjustment=yadj, mousewheel=False, draggable=False, xmaximum=400, ymaximum = 270, xalign=0.5, yalign=0.5)
        ui.vbox(xfill=True)
        for (name, label, display, path, unlocked) in available_scenes:
            if label == rp_actmark:
                if path in open_acts:
                    ss_button("{color=00000066}" + name + "{/color}","", clicked=None)
                    ui.null(height=1)
            elif unlocked:
                if False: 
                    extension = " " + label
                else:
                    extension = ""
                ui.hbox()
                ui.null(width=scene_indent)
                ss_button(name+extension, display, clicked=ui.returns((name,label)))
                ui.close()
                ui.null(height=1)
            else:
                ui.null(height=1)
                ui.hbox()
                ui.null(width=scene_indent+12)
                ui.image(ib_disabled("ui/bg-lockedtrack.png"))
                ui.close()
            
            ui.null(height=3+displayStrings.selector_padding)

        viewportkeys(decrease_s_yoffset,increase_s_yoffset)

        ui.close()
        ui.null(width=20)
        ui.vbox(box_spacing=2)
        if scrollable:
            ui.imagebutton(ib_base("ui/bt-vscrollup.png"), "ui/bt-vscrollup.png", clicked=decrease_s_yoffset)
            ui.bar(style='vscrollbar2', adjustment = yadj, changed=store_s_yoffset)
            ui.imagebutton(ib_base("ui/bt-vscrolldown.png"), "ui/bt-vscrolldown.png", clicked=increase_s_yoffset)
        else:
            ui.imagebutton(ib_disabled("ui/bt-vscrollup.png"), "ui/bt-vscrollup.png", clicked=None)
            ui.bar(style='vscrollbar2_disabled')
            ui.imagebutton(ib_disabled("ui/bt-vscrolldown.png"), "ui/bt-vscrolldown.png", clicked=None)
        ui.close()
        ui.close()
        ui.close()

        return_button(ui.jumps("extra_menu", "intra_transition"))

        if has_devlvl():
            if playthroughflag:
                checkboximage = "ui/bt-cf-unchecked.png"
            else:
                checkboximage = "ui/bt-cf-checked.png"
            widget_button(displayStrings.scene_playthrough_label, checkboximage, toggle_playthrough, xsize=340, widgetyoffset=0, xpos=180, ypos=450)
        else:
            completion_percentage = get_completion_percentage()
            ui.text(displayStrings.scene_completion_label % completion_percentage, style="prefs_label", xpos=180, ypos=450)

        ui.add(DynamicDisplayable(refresh_label))


        what, where = ui.interact()


        readback_buffer = []
        if what not in ("_setfilter", "_pt_toggled"):
            
            
            
            
            init_vars()
            last_scene_label = where
            renpy.music.stop(fadeout=0.5)
            renpy.transition(config.game_main_transition)
            renpy.scene()
            renpy.show("black")
            renpy.block_rollback()
            ui.timer(1.0, ui.returns, kwargs={"value":True})
            ui.interact() 
            save_name = where
            if playthroughflag or not renpy.has_label("replay_"+where):
                jumptarget = where
            else:
                jumptarget = "replay_"+where
            ui.jumpsoutofcontext(jumptarget)() 
        elif what == "_setfilter":
            filter = where
            persistent.spicker_yoffset = 0
        elif what == "_pt_toggled":
            renpy.transition(ImageDissolve(im.Tile("ui/tr-checkwipe2.png"), 0.5, 8))

        renpy.jump("scene_select_loop")

label cg_gallery:

    python:
        if get_completion_percentage() >= 100 and persistent.bad and persistent.emi and persistent.emibad and persistent.lilly and persistent.lillybad and persistent.hanako and persistent.hanakosad and persistent.hanakorage and persistent.rin and persistent.rintrue and persistent.rinbad and persistent.shizune and persistent.shizunebad:
            ksgallery_unlock('completionbonus')

        mygallery = Gallery()
        mygallery.locked_background = "ui/bg-ex-gallery-lockedimage.png"
        mygallery.background = (LiveComposite((800, 600),
                                              (0, 0), style.mm_static.background,
                                              (0, 0), style.gm_root.background,
                                              (150, 100), "ui/bg-config.png"))
        mygallery.locked_button = ib_disabled("ui/bt-cg-locked.png")
        mygallery.grid_layout((4,3),(175,160),(115,90))
        i = 0
        page = 0
        for i_image in ex_g_images:
            if i == 0:
                page += 1
                
                mygallery.page(str(page))
                i = 0
            mygallery.autobutton(i_image)
            i += 1
            if i >= 12:
                i = 0
        if page == 0:
            mygallery.page(displayStrings.gallery_num_page_error)
        mygallery.show()


label simple_return:
    return

label custom_noisy_return:
    $ renpy.play(config.exit_sound)


label custom_return:
    $ gm_active = False
    $ statechangesincesave = True
    if mm_context():
        $ renpy.transition(config.game_main_transition)
        jump _main_menu_screen
    $ renpy.transition(config.exit_transition)
    if gm_exit_to and previous_language != persistent.current_language:
        nvl clear
        stop music fadeout 1.0
        $ temp_exit = gm_exit_to
        $ gm_exit_to = None
        $ previous_language = None
        $ renpy.jump_out_of_context(temp_exit)
    return

label custom_return_dissolve:
    $ gm_active = False
    $ statechangesincesave = True
    $ renpy.transition(config.intra_transition)
    return

label afm_on:

    python:
        turn_afm_on()
        renpy.jump("_return")

label start_from_mm:


    stop music fadeout 1.0

    scene black
    with config.game_main_transition

    python:
        playthroughflag = True
        init_vars()
        renpy.pause(2)
        renpy.jump_out_of_context("start")

label softquit:

    python:
        if _preferences.transitions != 0 :
            renpy.music.stop(fadeout=0.5)
            renpy.transition(dissolve)
            ui.image(Solid("#000"))
            renpy.pause(0.7)
        renpy.jump("_quit")


label scene_deleted(is_end=False):
    window hide

    $ oldambient = renpy.music.get_playing(channel="ambient")
    $ renpy.music.set_volume(0.05, 2.0, channel="music")

    play ambient sfx_heartfast fadein 0.5

    scene pink
    with dissolve


    $ prawn_image = "ui/" + renpy.random.choice(("prawns.jpg", "climatic.jpg", "cantaloupes.jpg", "cuddlefish.jpg"))

    scene expression prawn_image:
        zoom 1.0 xalign 0.5 yalign 0.5 subpixel True
        linear 0.05 zoom 1.05
        easein 0.7 zoom 1.0
        pause 0.118
        linear 0.02 zoom 1.025
        easein 0.3 zoom 1.0
        repeat
    show expression "ui/bt-logoonly.png":
        xanchor 0 yanchor 0 xpos 610 ypos 10
    with Dissolve(2.0)

    $ renpy.pause(2.0)

    scene white
    with Dissolve(6.0)

    stop music fadeout 1.0
    stop ambient fadeout 1.0
    $ renpy.pause(1.0)


    play ambient oldambient fadein 2.0

    $ renpy.transition(dissolve)
    if not is_end:
        window show
    else:
        stop music fadeout 1.0
        $ suppress_window_before_timeskip = True
        scene black
        with dissolve

    $ renpy.music.set_volume(1.0, 2.0, channel="music")

    return

label en_timeskip:

    if playthroughflag:
        stop sound fadeout 2.0
        stop music fadeout 2.0
        stop ambient fadeout 2.0
        if suppress_window_before_timeskip:
            window hide None
        else:
            window hide
        with Pause(2.0)

        play music music_timeskip

        show kslogo heart at Position(xalign=0.5, yalign=0.5)
        with clockwipe

        scene black
        show kslogo words at Position(xalign=0.5, yalign=0.5)
        with clockwipe

        with Pause(2.0)

        stop music fadeout 2.0

        scene black
        with clockwipe

        with Pause(2.0)

        if not suppress_window_after_timeskip:
            window show

    $ suppress_window_before_timeskip = False
    $ suppress_window_after_timeskip = False

    return


init 5 python:

    show_skipcredits_button = False

    def skipcredits_overlay():
        if not show_skipcredits_button:
            return
        
        def clicked():
            renpy.jump("after_credits")
        
        ui.keymap(K_ESCAPE=clicked)
        ui.textbutton("{color=#000}Skip{/color}",clicked=clicked, xpos=795, xanchor=1.0, ypos=595, yanchor=1.0, xpadding=6,
                      background=RoundRect((48, 48, 48, 255), 6),
                      hover_background=RoundRect((64, 64, 64, 255), 6),
                      color="#000",
                      )

    config.overlay_functions.append(skipcredits_overlay)


label credits(c_movie=False):


    window hide
    stop music
    stop ambient
    stop movie

    python:





        wdt_off()

        config.skipping = False

        old_game_menu_screen = _game_menu_screen
        _game_menu_screen = None

        this_rollback = config.rollback_enabled
        config.rollback_enabled = False

        config.allow_skipping = False

        ask_to_quit = False
        _preferences.afm_time = 0
        may_afm = False

        show_skipcredits_button = True

    scene videoblack
    show credits mask
    with Dissolve(2.0)

    $ renpy.pause(1.0, hard=True)

    python:

        creditstext_disp = Text(displayStrings.creditstring, color="#ffffff", text_align=0.5, min_width=800)


        logo_top = LiveComposite((800, 600),
                                 (313,233), "ui/cred_logo.png")

        logo_bottom = LiveComposite((800, 600),
                                    (311, 238), "ui/4lsl-small.png")

        if c_movie:
            creditstext_offs = HBox(Null(width=320), creditstext_disp)
        else:
            creditstext_offs = creditstext_disp

        credits_final = VBox(logo_top, creditstext_offs, logo_bottom)



    show expression credits_final as roll behind credits at Position(xalign=0.5, yalign=0.0)
    with Dissolve(2.0)

    $ renpy.pause(2.0, hard=True)





    if c_movie:
        $ renpy.music.play(music_credits, loop=False)

    show expression credits_final as roll behind credits:
        xalign 0.5 yalign 0.0 subpixel True
        acdc20_warp 60.0 yalign 1.0
    with None

    $ renpy.pause(8.0, hard=True)


    if c_movie:
        play movie c_movie
        show expression Movie(fps=30, size=(400, 300), yalign=0.5, xanchor=0.5, xpos=0.3) as themovie behind roll
    with None

    $ renpy.pause(52.0, hard=True)




    stop movie
    hide themovie
    with None


    show expression Text(u"©MMXV Four Leaf Studios", text_align=0.5, size=15) as copyright at Position(xalign=0.5, yalign=0.576)
    with Dissolve(2.0)
    $ renpy.pause(5.0, hard=True)

    $ renpy.music.set_volume(0.0,1.0)

    scene black
    with Dissolve(2.0)

    $ renpy.pause(1.0, hard=True)

label after_credits:


    $ config.allow_skipping = True
    $ config.rollback_enabled = this_rollback
    $ renpy.block_rollback()
    $ _game_menu_screen = old_game_menu_screen

    stop music
    stop movie
    hide themovie
    with None

    $ renpy.music.set_volume(1.0,0.0)
    $ may_afm = True
    $ show_skipcredits_button = False

    scene black
    with None

    return

label before_save:
    python:


        pass
    return


label after_load:
    python:
        initialize_prefs()
        ask_to_quit = True
        savegame_langage = np_current_language
        if persistent.current_language != savegame_langage:
            switch_language(persistent.current_language)
            renpy.pop_return()
            nvl_clear()
            renpy.jump(wrap_label(last_visited_label))



        persistent.breadcrumbs = copy.deepcopy(store.breadcrumbs)

    return



label start:


    stop music

    $ ask_to_quit = True

    $ renpy.scene()
    $ np_current_language = persistent.current_language
    $ renpy.block_rollback()
    $ readback_buffer = []
    nvl clear

    jump imachine

label en_op_vid1:
    $ wdt_off()
    $ renpy.movie_cutscene("video/"+vid_op)
    $ renpy.pause(1.0)
    $ wdt_on()
    return

label act_op(this_video):
    $ wdt_off()
    scene videowhite
    with Dissolve(2.0)
    python:

        _localized_tc = False
        renpy.pause(1.0)
        renpy.movie_cutscene("video/" + this_video)
        renpy.pause(0.1)

        act = this_video[6:7]
        char = this_video[8:-4]

        for count, (name, id, desc, sorts) in enumerate(s_scenes):
            if id == rp_actmark:
                if (sorts[0] == "Act " + act and sorts[1].lower() == char) or (act == "1" and sorts == "Act 1"):
                    if name != displayDict[master_language].s_scenes[count][0]:
                        _localized_tc = name
                        break

    call localized_tc (_localized_tc, True) from _call_localized_tc
    $ wdt_on()

    return

label localized_tc(tc_text, auto=False):

    if not tc_text or not playthroughflag or not auto:
        return

    show videowhite
    show expression Text("{b}{color=#908778}{size=36}"+tc_text+"{/size}{/color}{/b}", outlines=[]) as titlecard:
        subpixel True xalign 0.45 yalign 0.5
        linear 6.5 xalign 0.55
    with dissolve

    with Pause(4.0)

    hide titlecard
    with Dissolve(2.0)

    with Pause(0.5)

    return





label path_end(character="", is_good=False):

    if not playthroughflag:
        return

    window hide

    $ end_id = character
    if not is_good or not character:
        $ end_id += "bad"

    if character.endswith("true") or character.endswith("sad") or character.endswith("rage"):
        $ is_good = False

    $ setattr(persistent, end_id, getattr(persistent, end_id)+1)
    $ setattr(multipersistent, end_id, True)
    $ multipersistent.save()

    if not automode:
        if end_id == "bad":
            scene bloodred
            with Dissolve(4.0)
            call credits from _call_credits

        elif is_good:
            if renpy.loadable("video/base_credits_"+character+".mp4"):
                $ myvid = "video/base_credits_"+character+".mp4"
            elif renpy.loadable("video/ios_credits_"+character+".mp4"):
                $ myvid = "video/ios_credits_"+character+".mp4"
            else:
                $ myvid = False
            scene white
            with Dissolve(4.0)
            call credits (myvid) from _call_credits_1
        else:
            scene black
            with Dissolve(2.0)
            call credits from _call_credits_2
    return




label restart:
    if automode:
        $ init_vars()
        jump imachine
    elif notextmode:
        jump cruise_control
    else:
        $ renpy.full_restart()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
