
init -1 python:


    Position = Transform


    layout.provides("load_save")
    layout.provides("yesno_prompt")
    layout.provides("preferences")
    layout.button_menu()
    theme.roundrect()

    config.locked = False
    config.time_format = "%b %d, %H:%M"
    config.file_entry_format = "" 
    config.preferences = { }
    config.all_preferences = { }
    config.minimumvolume = 0.0
    
    config.script_version = (6,10,2)










    config.screenshot_callback = None
    config.locked = True

init -101 python:
    config.developer = False

init 1:



    python:
        if config.developer:
            config.searchpath.append('archived')
        config.window_title = u""
        release_is_demo = False 

        config.has_autosave = False
        config.nvl_show_display_say = say_wrapper



    transform center_pro:
        xalign 0.5
        yalign 1.0
        rotate None
        zoom 1.0
        alpha 1.0
        around (0.0,0.0)
        alignaround (0.0,0.0)
        crop None
        corner1 None
        corner2 None
        size None

    transform twoleft:
        xpos 0.3 xanchor 0.5 ypos 1.0 yanchor 1.0

    transform tworight:
        xpos 0.7 xanchor 0.5 ypos 1.0 yanchor 1.0

    transform closeleft:
        xpos 0.25 xanchor 0.5 ypos 1.0 yanchor 1.0

    transform closeright:
        xpos 0.75 xanchor 0.5 ypos 1.0 yanchor 1.0

    transform twoleftoff:
        xpos 0.32 xanchor 0.5 ypos 1.0 yanchor 1.0

    transform tworightoff:
        xpos 0.68 xanchor 0.5 ypos 1.0 yanchor 1.0

    transform centeroff:
        xpos 0.52 xanchor 0.5 ypos 1.0 yanchor 1.0

    transform bgleft:
        xpos 0.4 xanchor 0.5 ypos 1.0 yanchor 1.0

    transform bgright:
        xpos 0.6 xanchor 0.5 ypos 1.0 yanchor 1.0

    transform Alphaout(var_time):
        alpha 1.0
        linear var_time alpha 0.0

    transform Alphain(var_time):
        alpha 0.0
        linear var_time alpha 1.0

    transform Slide(start_pos, start_anchor, end_pos, end_anchor, my_time, time_warp=_ease_in_time_warp):
        xpos start_pos xanchor start_anchor yalign 1.0
        warp time_warp my_time xpos end_pos xanchor end_anchor

    transform titlecard_screen(mid_image, mid_imagetrans, final_disp):
        Solid("#FFF")
        4.0
        "ui/tc-neutral.png" with Dissolve(1.0)
        1.0
        mid_image with ImageDissolve(mid_imagetrans, 5.0)
        6.5
        final_disp with wiperight
        6.0
        Solid("#FFF") with Dissolve(3.0)

    transform note_enter:
        xalign 0.5 yanchor 0.5 ypos 0.8 alpha 0.0
        0.2
        easein 0.5 ypos 0.5 alpha 1.0

    transform note_exit:
        xalign 0.5 yalign 0.5 alpha 1.0
        easeout 0.5 ypos 0.8 alpha 0.0


    transform move_ltr(my_time, my_warper, is_subpixel):
        xalign 0.0 yalign 0.5 subpixel is_subpixel
        warp my_warper my_time xalign 1.0

    transform move_rtl(my_time, my_warper, is_subpixel):
        xalign 1.0 yalign 0.5 subpixel is_subpixel
        warp my_warper my_time xalign 0.0

    transform move_ttb(my_time, my_warper, is_subpixel):
        xalign 0.5 yalign 0.0 subpixel is_subpixel
        warp my_warper my_time yalign 1.0

    transform move_btt(my_time, my_warper, is_subpixel):
        xalign 0.5 yalign 1.0 subpixel is_subpixel
        warp my_warper my_time yalign 0.0

    python:
        def Fullpan(time, dir="right", time_warp=acdc_warp, subpixel=True):
            if dir == "right":
                return move_ltr(time, time_warp, subpixel)
            elif dir == "down":
                return move_ttb(time, time_warp, subpixel)
            elif dir == "up":
                return move_btt(time, time_warp, subpixel)
            else:
                return move_rtl(time, time_warp, subpixel)




        use_new_sprites = False

        def make_sprite_path(char, expr, suffix='', close=False):
            
            if suffix:
                suffix = '_' + suffix
            close_dir = '/'
            close_mod = ''
            if close:
                close_dir = '/close/'
                close_mod = '_close'
            
            return 'sprites/' + char + close_dir + char + '_' + expr + suffix + close_mod + '.png'

        def ks_sprite(char, expr_name, suffix_list=[]):
            
            missingsprite = 'sprites/others/generic_missing.png'
            
            
            regular_files = [(make_sprite_path(char,expr_name),expr_name),
                             (make_sprite_path(char,expr_name,close=True),expr_name+'_close')]
            
            
            
            for suffix in suffix_list:
                regular_files.append((make_sprite_path(char,expr_name, suffix),expr_name+'_'+suffix))
                regular_files.append((make_sprite_path(char,expr_name,suffix,True),expr_name+'_'+suffix+'_close'))
            
            
            
            for filename, mod_expr_name in regular_files:
                if not renpy.loadable(filename):
                    continue
                
                else:
                    checked_filename = filename
                renpy.image((char,mod_expr_name), checked_filename)
                for filter, filtersuffix in sp_filters:
                    renpy.image((char,mod_expr_name+"_"+filtersuffix), filter(checked_filename))

        def make_sprites(char, expr_list, suffix_list=[]):
            
            if use_new_sprites:
                return
            
            alpha_done = {'close':False,'regular':False}
            
            for expr in expr_list:
                ks_sprite(char, expr, suffix_list)
                
                
                for distance in ('close', 'regular'):
                    if not alpha_done[distance]:
                        is_close = False
                        target_expr = 'invis'
                        loadname = ''
                        if distance == 'close':
                            is_close = True
                            target_expr = 'invis_close'
                        basename = make_sprite_path(char, expr, close=is_close)
                        if renpy.loadable(basename):
                            loadname = basename
                        if not loadname and len(suffix_list):
                            for suffix in suffix_list:
                                this_base = make_sprite_path(char, expr, suffix, is_close)
                                if renpy.loadable(this_base):
                                    loadname = this_base
                                    break
                        if loadname:
                            renpy.image((char,target_expr), im.Alpha(loadname, 0.0))
                            alpha_done[distance] = True



        def load_sjpg(file):
            width, height = disp_size(file)
            return im.AlphaMask(im.Crop(file,0,0,width/2,height),im.Crop(file,width/2,0,width/2,height))

        def sjpg_set(basechar, expressions, defoffset=None, defoffset_close=None, suffix_list=None, alias=None):
            
            if not use_new_sprites:
                return
            
            basefolder = 'jsprites/'
            invis_set = {'close':False,'regular':False}
            char = basechar
            
            if not isinstance(expressions, dict):
                expressions = {'':(expressions,defoffset,defoffset_close)}
            
            if not suffix_list:
                suffix_list = ['']
            else:
                suffix_list.append('')
            if alias:
                char, suffix_list = alias
            
            for pose, metadata in expressions.iteritems():
                baseoffset_close = None
                baseoffset = None
                if isinstance(metadata, list):
                    expr_list = metadata
                
                elif len(metadata) == 3:
                    expr_list, baseoffset, baseoffset_close = metadata
                else:
                    expr_list, baseoffset = metadata
                distance_list = ['regular']
                if baseoffset_close:
                    distance_list.append('close')
                
                pose_disp = ''
                if pose:
                    pose_disp = pose + '_'
                    pose = '_' + pose
                for distance in distance_list:
                    offset = baseoffset
                    folder = basefolder + basechar + '/'
                    name_mod = ''
                    if distance == 'close':
                        folder += 'close/'
                        name_mod = '_' + distance
                        offset = baseoffset_close
                    for suffix in suffix_list:
                        if len(suffix):
                            suffix = '_' + suffix
                        suffix_path = suffix
                        if alias:
                            suffix_path = ''
                        basefile = folder + basechar + pose + suffix_path + name_mod + '_BASE.jpg'
                        alphafile = folder + basechar + pose + suffix_path + name_mod + '_ALPHA.png'
                        invisfile = ''
                        can_dynamic = False
                        if renpy.loadable(basefile) and renpy.loadable(alphafile):
                            can_dynamic = True
                        else:
                            invisfile = basefile
                        
                        expr_checked = []
                        for expr in expr_list:
                            expr_static = folder + basechar + pose + '_' + expr + suffix_path + name_mod + '.png'
                            expr_jstatic = folder + basechar + pose + '_' + expr + suffix_path + name_mod + '.a.jpg'
                            if renpy.loadable(expr_jstatic):
                                expr_checked.append((expr,"jpg"))
                                if not invisfile:
                                    invisfile = load_sjpg(expr_jstatic)
                            elif renpy.loadable(expr_static):
                                expr_checked.append((expr,"png"))
                                if not invisfile:
                                    invisfile = expr_static
                            elif can_dynamic:
                                expr_checked.append((expr,"comp"))
                        if not len(expr_checked):
                            continue
                        
                        if not invis_set[distance]:
                            sjpg_image((char,'invis' + name_mod), im.Alpha(invisfile, 0.0))
                            invis_set[distance] = True
                        
                        for expr, is_static in expr_checked:
                            if is_static == "comp":
                                expr_comp = folder + basechar + pose + '_' + expr + name_mod + '_COMP.jpg'
                                if not renpy.loadable(expr_comp):
                                    continue
                                curr_comp = im.Composite(None,(0,0),basefile,offset, expr_comp)
                                curr_disp = im.AlphaMask(curr_comp,alphafile)
                            elif is_static == "png":
                                curr_disp = folder + basechar + pose + '_' + expr + suffix_path + name_mod + '.png'
                            else: 
                                curr_disp = load_sjpg(folder + basechar + pose + '_' + expr + suffix_path + name_mod + '.a.jpg')
                            sjpg_image((char,pose_disp+expr+suffix+name_mod), curr_disp)
                            for filter, filtersuffix in sp_filters:
                                sjpg_image((char,pose_disp+expr+suffix+name_mod+'_'+filtersuffix), filter(curr_disp))

        def sjpg_image(alias, what):
            
            renpy.image(alias, what)




        def ks_bg(bgid):
            
            path = "bgs/"
            tag = "bg"
            
            base_image = path + bgid + ".jpg"
            
            if not renpy.loadable(base_image):
                base_image = "bgs/_bg_missing.png"
            renpy.image((tag,bgid), base_image)
            for filter, filtersuffix in bg_filters:
                prefiltered = path + bgid + "_" + filtersuffix + ".jpg"
                if renpy.loadable(prefiltered):
                    renpy.image((tag,bgid+"_"+filtersuffix), prefiltered)
                else:
                    renpy.image((tag,bgid+"_"+filtersuffix), filter(base_image))




        ks_bg("city_alley")
        ks_bg("city_graveyard")
        ks_bg("city_karaokeext")
        ks_bg("city_karaokeint")
        ks_bg("city_othello")
        ks_bg("city_street1")
        ks_bg("city_street1_blurred")
        ks_bg("city_street2")
        ks_bg("city_street3")
        ks_bg("city_street4")
        ks_bg("city_subway")
        ks_bg("city_station")
        ks_bg("city_restaurant")
        ks_bg("city_clubint")
        ks_bg("city_clubpool")


        ks_bg("emi_dining")
        ks_bg("emi_houseext")
        ks_bg("emi_kitchen")


        ks_bg("gallery_atelier")
        ks_bg("gallery_ext")
        ks_bg("gallery_int")
        ks_bg("gallery_staircase")
        ks_bg("gallery_exhibition")


        ks_bg("hok_houseext")
        ks_bg("hok_kitchen")
        ks_bg("hok_lounge")
        ks_bg("hok_road")
        ks_bg("hok_wheat")
        ks_bg("hok_bath")

        ks_bg("lilly_hilltop")


        ks_bg("hosp_ceiling")
        ks_bg("hosp_ext")
        ks_bg("hosp_hallway")
        ks_bg("hosp_room")
        ks_bg("hosp_room2")


        ks_bg("misc_sky")
        ks_bg("misc_ceiling")
        ks_bg("misc_ceiling_blur")


        ks_bg("op_snowywoods")


        ks_bg("school_auditorium")
        ks_bg("school_backexit")
        ks_bg("school_backstage")
        ks_bg("school_cafeteria")
        ks_bg("school_classroomart")
        ks_bg("school_council")
        ks_bg("school_courtyard")
        ks_bg("school_dormbathroom")
        ks_bg("school_dormemi")

        ks_bg("school_dormext")
        ks_bg("school_dormext_start")
        ks_bg("school_dormext_half")
        ks_bg("school_dormext_full")

        ks_bg("school_dormhallground")
        ks_bg("school_dormhallway")
        ks_bg("school_girlsdormhall")
        ks_bg("school_dormhisao")
        ks_bg("school_dormhisao_blurred")

        ks_bg("school_dormkenji")
        ks_bg("school_dormlilly")
        ks_bg("school_dormrin")
        ks_bg("school_dormshizune")
        ks_bg("school_dormhanako")
        ks_bg("school_forest1")
        ks_bg("school_forest2")
        ks_bg("school_forestclearing")

        ks_bg("school_gate")

        ks_bg("school_gardens")
        ks_bg("school_gardens2")
        ks_bg("school_gardens3")
        ks_bg("school_greathall")
        ks_bg("school_hallway2")
        ks_bg("school_hallway3")
        ks_bg("school_hallway3_blurred")
        ks_bg("school_hallwayextra")
        ks_bg("school_hilltop_border")
        ks_bg("school_hilltop_border_summer")
        ks_bg("school_hilltop_spring")
        ks_bg("school_hilltop_summer")
        ks_bg("school_library")
        ks_bg("school_lobby")
        ks_bg("school_musicroom")
        ks_bg("school_nursehall")
        ks_bg("school_nurseoffice")
        ks_bg("school_principal")
        ks_bg("school_roof")
        ks_bg("school_roof_blurred")
        ks_bg("school_scienceroom")
        ks_bg("school_sportsstoreroom")
        ks_bg("school_sportsstoreext")
        ks_bg("school_staircase1")
        ks_bg("school_staircase2")
        ks_bg("school_stalls1")
        ks_bg("school_stalls2")
        ks_bg("school_track")
        ks_bg("school_track_on")
        ks_bg("school_track_running")
        ks_bg("school_road")
        ks_bg("school_miyagi")
        ks_bg("school_miyagi_blurred")
        ks_bg("school_room32")
        ks_bg("school_room34")
        ks_bg("school_parkinglot")
        ks_bg("school_nomiya")


        ks_bg("shizu_houseext")
        ks_bg("shizu_houseext_lights")
        ks_bg("shizu_living")
        ks_bg("shizu_guestbed")
        ks_bg("shizu_guesthisao")
        ks_bg("shizu_fishing")
        ks_bg("shizu_park")
        ks_bg("shizu_garden")


        ks_bg("suburb_konbiniext")
        ks_bg("suburb_konbiniint")
        ks_bg("suburb_park")
        ks_bg("suburb_roadcenter")
        ks_bg("suburb_shanghaiext")
        ks_bg("suburb_shanghaiint")
        ks_bg("suburb_tanabata")



    image completionbonus = "event/completionbonus.jpg"



    image heartattack alpha = im.Alpha("vfx/heart_attack.png", 0.3)
    image heartattack residual = im.Alpha("vfx/heart_attack.png", 0.17)
    image heartattack = "vfx/heart_attack.png"







    python:
        emi_list = ['basic_happy',
                    'basic_happyblush',
                    'basic_confused',
                    'basic_concentrate',
                    'basic_shock',
                    'basic_annoyed',
                    'basic_hes',
                    'basic_grin',
                    'basic_closedhappy',
                    'basic_closedgrin',
                    'basic_closedsweat',
                    'excited_laugh',
                    'excited_amused',
                    'excited_joy',
                    'excited_happy',
                    'excited_happyblush',
                    'excited_hesitant',
                    'excited_proud',
                    'excited_circle',
                    'excited_sad',
                    'excited_smile',
                    'excited_happy',
                    'sad_angry',
                    'sad_annoyed',
                    'sad_pout',
                    'sad_shy',
                    'sad_shyblush',
                    'sad_depressed',
                    'sad_grit',
                    'sad_grin',
                    ]
        make_sprites('emi',emi_list, ['gym'])



        emi_list_new = {'basic':(['happy','happyblush','confused','concentrate','shock','annoyed','hes','grin','closedhappy','closedgrin','closedsweat'],(94,209),(110,140)),
                        'excited':(['laugh','amused','joy','happy','happyblush','hesitant','proud','circle','sad','smile','happy'],(88,222),(105,168)),
                        'sad':(['angry','annoyed','pout','shy','shyblush','depressed','grit','grin'],(87,212),(99,150))}



        emicas_list = ['angry',
                       'awayfrown',
                       'blush',
                       'closedsmile',
                       'evil',
                       'frown',
                       'grin',
                       'grit',
                       'happy',
                       'neutral',
                       'pout',
                       'sad',
                       'smile',
                       'weaksmile',
                       'wink',
                       ]
        make_sprites('emicas',emicas_list, ['up'])
        make_sprites('emiwheel',emicas_list)
        make_sprites('eminude',emicas_list)



        def scaled_runtime(length, expired):
            return min((float(expired) / float(length)), 1.0)

        def tremble_general(time, xpos, ypos, xanchor, yanchor, d, st, at):
            import math, random
            
            if not time:
                n = st - int(st)
            else:
                n = scaled_runtime(time, st)
            
            jitter = 0.0002 * (random.randint(-1,1))
            m = math.sin(n*math.pi*40) * 0.001 + jitter
            d.xanchor = xanchor
            d.yanchor = yanchor
            d.xpos = xpos + m
            d.ypos = ypos + jitter
            return 0

        def tf_centertremble_loop(d, st, at):
            return tremble_general(False, 0.5, 1.0, 0.5, 1.0, d, st, at)

        def tf_centertremble(d, st, at):
            return tremble_general(1.0, 0.5, 1.0, 0.5, 1.0, d, st, at)

        def tf_centertremble_sit(d, st, at):
            return tremble_general(1.0, 0.5, 1.09, 0.5, 1.0, d, st, at)

        centertremble_sit = Transform(function=tf_centertremble_sit)

        def tf_lefttremble(d, st, at):
            return tremble_general(1.0, 0.3, 1.0, 0.5, 1.0, d, st, at)

        def bounce_general(time, amplitude, num, d, st, at):
            import math
            n = scaled_runtime(time, st)
            m = -math.fabs(math.sin(n*math.pi*num))
            d.yanchor = 0.0
            d.ypos = m*amplitude
            return 0

        def tf_fourbounce60(d, st, at):
            return bounce_general(2.1, 0.1, 4, d, st, at)

        def tf_fourbounce30(d, st, at):
            return bounce_general(1.8, 0.04, 4, d, st, at)

        def tf_onebounce(d, st, at):
            return bounce_general(0.5, 0.04, 1, d, st, at)

        def tf_leftrock(d, st, at):
            import math
            n = scaled_runtime(4.0, st)
            m = math.sin(n*math.pi*8) * (1-n)
            d.xpos = 0.3+(m*0.05)
            d.ypos = 1.0
            d.xanchor = 0.5
            d.yanchor = 0.9
            return 0


        emigymbouncecomp = im.Composite ((295,630),
                                         (0,0),"sprites/emi/emi_basic_grin_gym.png",
                                         (0,600),"vfx/emi_gym_30pxlegs.png")

        emigymclosedbouncecomp = im.Composite ((295,630),
                                         (0,0),"sprites/emi/emi_basic_closedgrin_gym.png",
                                         (0,600),"vfx/emi_gym_30pxlegs.png")

        emigymconcentratebouncecomp = im.Composite ((295,630),
                                         (0,0),"sprites/emi/emi_basic_concentrate_gym.png",
                                         (0,600),"vfx/emi_gym_30pxlegs.png")

        emiannoyedbouncecomp = im.Composite ((295,660),
                                         (0,0),"sprites/emi/emi_basic_annoyed.png",
                                         (0,600),"vfx/emi_uni_60pxlegs.png")

        emihappybouncecomp = im.Composite ((295,630),
                                         (0,0),"sprites/emi/emi_basic_closedhappy.png",
                                         (0,600),"vfx/emi_uni_60pxlegs.png")


    image emi annoyedbounce = At(emiannoyedbouncecomp,Transform(function=tf_fourbounce60))
    image emi gymbounce = At(emigymbouncecomp,Transform(function=tf_fourbounce30))
    image emi gymconcentratebounce = At(emigymconcentratebouncecomp,Transform(function=tf_fourbounce30))
    image emi gymbounceclosed = At(emigymclosedbouncecomp,Transform(function=tf_fourbounce30))
    image emi gymbounce_once = At(emigymclosedbouncecomp,Transform(function=tf_onebounce))
    image emi happybounce = At(emihappybouncecomp,Transform(function=tf_fourbounce30))


    image emi blur = "vfx/emi_blur.png"

    image bg school_track_fb = past("bgs/school_track.jpg")
    image emi basic_closedhappy_gym_fb = past("sprites/emi/emi_basic_closedhappy_gym.png")
    image emi basic_grin_gym_fb = past("sprites/emi/emi_basic_grin_gym.png")
    image emi sad_grin_gym_fb = past("sprites/emi/emi_sad_grin_gym.png")
    image emi excited_proud_gym_fb = past("sprites/emi/emi_excited_proud_gym.png")




    python:
        rin_list = ['basic_absent',
                    'basic_amused',
                    'basic_awayabsent',
                    'basic_blush',
                    'basic_delight',
                    'basic_lucid',
                    'basic_sad',
                    'basic_surprised',
                    'basic_upset',
                    'basic_crying',
                    'basic_deadpanupset',
                    'basic_deadpan',
                    'basic_deadpanamused',
                    'basic_deadpancontemplation',
                    'basic_deadpandelight',
                    'basic_deadpannormal',
                    'basic_deadpansurprised',
                    'negative_angry',
                    'negative_annoyed',
                    'negative_confused',
                    'negative_crying',
                    'negative_sad',
                    'negative_spaciness',
                    'negative_worried',
                    'relaxed_boredom',
                    'relaxed_disgust',
                    'relaxed_doubt',
                    'relaxed_nonchalant',
                    'relaxed_sleepy',
                    'relaxed_surprised',
                    'back',
                    ]
        make_sprites('rin',rin_list, ['cas'])
        make_sprites('rinpan', rin_list)



        rin_list_new = {'basic':(['absent','basic_amused','awayabsent','blush','delight','lucid','sad','surprised','upset','crying','deadpanupset','deadpan','deadpanamused','deadpancontemplation','deadpandelight','deadpannormal','deadpansurprised'],(34,134),(100,77)),
                        'negative':(['angry','annoyed','confused','crying','sad','spaciness','worried'],(30,139),(86,99)),
                        'relaxed':(['boredom','disgust','doubt','nonchalant','sleepy','surprised'],(72,130),(158,83)),
                        '':(['back'],(0,0),(0,0))}


        lilly_list = ['basic_ara',
                    'basic_arablush',
                    'basic_cheerful',
                    'basic_cheerfulblush',
                    'basic_concerned',
                    'basic_displeased',
                    'basic_emb',
                    'basic_giggle',
                    'basic_listen',
                    'basic_oops',
                    'basic_planned',
                    'basic_pout',
                    'basic_reminisce',
                    'basic_sad',
                    'basic_satisfied',
                    'basic_sleepy',
                    'basic_smile',
                    'basic_smileclosed',
                    'basic_surprised',
                    'basic_veryemb',
                    'basic_weaksmile',
                    'behind_cheerful',
                    'behind_displeased',
                    'behind_emb',
                    'behind_cheerful',
                    'behind_giggle',
                    'behind_listen',
                    'behind_cheerful',
                    'behind_pout',
                    'behind_cheerful',
                    'behind_reminisce',
                    'behind_sleepy',
                    'behind_smile',
                    'behind_smileclosed',
                    'behind_weaksmile',
                    'cane_ara',
                    'cane_arablush',
                    'cane_cheerful',
                    'cane_cheerfulblush',
                    'cane_concerned',
                    'cane_displeased',
                    'cane_emb',
                    'cane_giggle',
                    'cane_listen',
                    'cane_mad',
                    'cane_oops',
                    'cane_planned',
                    'cane_pout',
                    'cane_reminisce',
                    'cane_sad',
                    'cane_satisfied',
                    'cane_sleepy',
                    'cane_smile',
                    'cane_smileclosed',
                    'cane_surprised',
                    'cane_weaksmile',
                    'back_devious',
                    'back_giggle',
                    'back_listen',
                    'back_pout',
                    'back_smile',
                    'back_smileclosed',
                    'back_surprise',
                    'back_sad',
                    ]
        make_sprites('lilly',lilly_list,['paj','cas','che','nak'])

        lilly_list_new = {'basic':(['ara','arablush','cheerful','cheerfulblush','concerned','displeased','emb','giggle','listen','oops','planned','pout','reminisce','sad','satisfied','sleepy','smile','smileclosed','surprised','veryemb','weaksmile'],(85,98),()),
                          'behind':(['cheerful','displeased','emb','cheerful','giggle','listen','cheerful','pout','cheerful','reminisce','sleepy','smile','smileclosed','weaksmile'],(85,98),()),
                          'cane':(['ara','arablush','cheerful','cheerfulblush','concerned','displeased','emb','giggle','listen','mad','oops','planned','pout','reminisce','sad','satisfied','sleepy','smile','smileclosed','surprised','weaksmile'],(85,98),()),
                          'back':(['devious','giggle','listen','pout','smile','smileclosed','surprise','sad'],(124,94),())}




        hana_list = ['basic_bashful',
                    'basic_distant',
                    'basic_normal',
                    'basic_smile',
                    'basic_worry',
                    'cover_bashful',
                    'cover_distant',
                    'cover_smile',
                    'cover_worry',
                    'def_shock',
                    'def_strain',
                    'def_worry',
                    'defarms_shock',
                    'defarms_strain',
                    'defarms_worry',
                    'emb_blushing',
                    'emb_blushtimid',
                    'emb_downsad',
                    'emb_downsmile',
                    'emb_downtimid',
                    'emb_emb',
                    'emb_sad',
                    'emb_smile',
                    'emb_timid',
                    ]
        make_sprites('hanako',hana_list,['cas'])

        hana_list_new = {'basic':(['bashful','distant','normal','smile','worry'],(113,129),(186,84)),
                         'cover':(['bashful','distant','smile','worry'],(113,129),(186,84)),
                         'def':(['def_shock','def_strain','def_worry'],(106,130),(171,77)),
                         'defarms':(['shock','strain','worry'],(106,130),(171,77)),
                         'emb':(['blushing','blushtimid','downsad','downsmile','downtimid','emb','sad','smile','timid'],(97,141),(155,93)),}


        hanag_list = ['distant',
                    'drunkdistant',
                    'drunkgiggle',
                    'drunknormal',
                    'drunkpout',
                    'drunksad',
                    'drunksmile',
                    'drunkworry',
                    'stockdistant',
                    'stocknormal',
                    'stockworry',
                    'worry',
                    'normal',
                    'irritated',
                    'smile',
                    'worry',
                    ]
        make_sprites('hanagown',hanag_list,['blush'])


        hanag_list_new = ['distant',
                    'distant_blush',
                    'drunkdistant',
                    'drunkgiggle',
                    'drunknormal',
                    'drunkpout',
                    'drunksad',
                    'drunksmile',
                    'drunkworry',
                    'stockdistant_blush',
                    'stocknormal_blush',
                    'stockworry_blush',
                    'worry',
                    'normal',
                    'normal_blush',
                    'irritated',
                    'smile',
                    'worry',
                    'worry_blush',
                    ]




    $ centertremble = Transform(function=tf_centertremble_loop)
    $ centertremble_nl = Transform(function=tf_centertremble)

    image hanako tremble = At("sprites/hanako/hanako_def_shock.png",Transform(function=tf_centertremble))
    image hanako emb_downtimid_tremble = At("sprites/hanako/hanako_emb_downtimid.png",Transform(function=tf_centertremble_loop))




    python:
        shizu_list = ['adjust_happy',
                    'adjust_angry',
                    'adjust_blush',
                    'adjust_smug',
                    'adjust_frown',
                    'adjust_noglasses',
                    'basic_normal',
                    'basic_normal2',
                    'basic_frown',
                    'basic_happy',
                    'basic_angry',
                    'basic_sparkle',
                    'behind_blank',
                    'behind_frown',
                    'behind_frustrated',
                    'behind_sad',
                    'behind_smile',
                    'behind_smilelow',
                    'cross_angry',
                    'cross_rage',
                    'cross_rageclosed',
                    'cross_shock',
                    'cross_stunned',
                    'cross_wut',
                    'out_serious',
                    ]

        shizu_list_new = {'adjust':(['happy','angry','blush','smug','frown','noglasses'],(66,161),(98,108)),
                          'basic':(['normal','normal2','frown','happy','angry','sparkle'],(136,171),(204,131)),
                          'behind':(['blank','frown','frustrated','sad','smile','smilelow'],(68,173),(103,131)),
                          'cross':(['angry','rage','rageclosed','shock','stunned','wut'],(84,193),(125,163)),
                          'out':(['serious'],(0,0),(0,0))}

        make_sprites('shizu',shizu_list,['cas','nak'])

        shizuyu_list = ['basic_angry',
                        'basic_aside',
                        'basic_blush',
                        'basic_happy',
                        'cross_angry',
                        'cross_aside',
                        'cross_blush',
                        'cross_happy',
                        ]
        make_sprites('shizuyu',shizuyu_list)

        shizuyu_list_new = {'basic':(['angry','aside','blush','happy'],(84,167),(150,110)),
                            'cross':(['angry','aside','blush','happy'],(84,167),(150,110))}



        misha_list = ['perky_sad',
                    'perky_confused',
                    'perky_smile',
                    'sign_sad',
                    'sign_confused',
                    'sign_smile',
                    'hips_frown',
                    'hips_laugh',
                    'hips_grin',
                    'hips_smile',
                    'cross_frown',
                    'cross_laugh',
                    'cross_grin',
                    'cross_smile',
                    ]
        make_sprites('misha',misha_list,['cas','yuk'])
        make_sprites('mishashort',misha_list,['cas'])

        misha_list_new = {'perky':(['sad','confused','smile'],(103,163),(150,110)),
                          'sign':(['sad','confused','smile'],(103,164),(150,110)),
                          'hips':(['frown','laugh','grin','smile'],(102,168),(150,110)),
                          'cross':(['frown','laugh','grin','smile'],(101,164),(150,110))}


        yuuko_list = ['closedhappy',
                      'cry',
                      'happy',
                      'neurotic',
                      'neutral',
                      'panic',
                      'smile',
                      'worried',
                      'noglasses',
                      ]
        make_sprites('yuuko',yuuko_list,['up','down'])
        make_sprites('yuukoshang',yuuko_list,['up','down'])

        make_sprites('akira',['basic_smile','basic_lost','basic_kill','basic_annoyed','basic_resigned','basic_boo', 'basic_distant','basic_laugh','basic_ending','basic_evil'])
        make_sprites('hideaki',['angry','angry_up','bored','bored_up','closed_up','confused','darkside','disapproves','evil','happy','happy_up','kiss','normal','normal_up','ohshit','sad','surprise','surprise_up','thinking','serious','serious_up','triangle'])
        make_sprites('jigoro',['angry','laugh','neutral','smug'])
        make_sprites('kenji',['neutral','happy','tsun','rage'], ['naked'])
        make_sprites('nurse',['neutral','concern','fabulous','grin'])
        make_sprites('muto',['normal','smile','irritated'])
        make_sprites('nomiya',['dreamy','frown','serious','smile','stern','talk','talktongue','veryhappy'])
        make_sprites('sae',['neutral','smile','scowl','doubt','scold'], ['smoke'])
        make_sprites('meiko',['happy','serious','smile','wink','worry'])
        make_sprites('shopkeep',['happy', 'neutral', 'surprised', 'thinking'])
        make_sprites('miki',['angry','confused','grin','grinclosed','serious','smile','whistle','wink'])




















































    image ev other_iwanako_start:
        "event/other_iwanako_nosnow.jpg"
        xalign 0.5 yalign 0.9 zoom 1.2 subpixel True
        acdc_warp 20.0 zoom 1.0 yalign 0.5

    image ev other_iwanako = "event/other_iwanako_nosnow.jpg"
    image evul other_iwanako = "event/other_iwanako.jpg"

    image ev hisao_class_start = im.Crop("event/hisao_class.jpg", 0, 0, 800, 600)

    image ev hisao_class_move:
        "event/hisao_class.jpg"
        xalign 0.0 subpixel True
        acdc_warp 40.0 xalign 1.0

    image ev hisao_class_end = im.Crop("event/hisao_class.jpg", 800, 0, 800, 600)


    image ev emi_knockeddown = "event/emi_knockeddown.jpg"

    image ev emi_knockeddown_facepullout:
        "event/emi_knockeddown_large.jpg"
        size (800,600) crop (840, 50, 800, 600) subpixel True
        easeout 10.0 crop (840, 50, 880, 660)

    image ev emi_knockeddown_largepullout:
        "event/emi_knockeddown.jpg"
        size (800,600) crop (40, 30, 720, 540) subpixel True
        easein 10.0 crop (0, 0, 800, 600)

    image ev emi_knockeddown_face = im.Crop("event/emi_knockeddown_large.jpg", 840, 50, 800, 600)

    image ev emi_knockeddown_legs:
        size None crop None subpixel True
        "event/emi_knockeddown_large.jpg"
        xpos 2350 ypos 1010 xanchor 2400 yanchor 1800
        ease 8.0 xpos 1900 ypos 900

    image ev emi_run_face_zoomin:
        "event/emi_run_face.jpg"
        size (800,600) crop (0, 0, 800, 600) subpixel True
        ease 10.0 crop (40, 30, 720, 540)

    image ev emi_run_face = "event/emi_run_face.jpg"

    image ev emi_run_face_zoomout_ss:
        sunset("event/emi_run_face.jpg")
        size (800,600) crop (40, 30, 720, 540) subpixel True
        ease 10.0 crop (0, 0, 800, 600)

    image ev emi_firstkiss = "event/emi_firstkiss.jpg"

    image insert startpistol = "vfx/startpistol.png"

    image ev emitrack_running = "event/emitrack_running.jpg"
    image ev emitrack_blocks:
        "event/emitrack_blocks.jpg"
        xalign 0.0
    image ev emitrack_blocks_close = "event/emitrack_blocks_close.jpg"
    image ev emitrack_blocks_close_grin = "event/emitrack_blocks_close_grin.jpg"
    image ev emitrack_finishtop = "event/emitrack_finishtop.jpg"
    image ev emitrack_finish = "event/emitrack_finish.jpg"

    image ev emi_sleepy = "event/emi_sleepy.jpg"
    image ev emi_sleepy_face = "event/emi_sleepy_face.jpg"
    image ev emi_sleepy_legs = "event/emi_sleepy_legs.jpg"

    image ev emi_bed_frown = "event/emi_bed_frown.jpg"
    image ev emi_bed_happy = "event/emi_bed_happy.jpg"

    image ev emi_bed_normal = "event/emi_bed_normal.jpg"
    image ev emi_bed_smile = "event/emi_bed_smile.jpg"
    image ev emi_bed_unsure = "event/emi_bed_unsure.jpg"

    image ev emi_forehead = "event/emi_forehead.jpg"

    image ev emi_sleep_cry = "event/emi_sleep_cry.jpg"
    image ev emi_sleep_normal = "event/emi_sleep_normal.jpg"
    image ev emi_sleep_unsure = "event/emi_sleep_unsure.jpg"
    image ev emi_sleep_weep = "event/emi_sleep_weep.jpg"

    image ev emi_parkback = "event/emi_parkback.jpg"
    image ev emi_parkback_frown = "event/emi_parkback_frown.jpg"

    image ev emi_ending_smile = "event/emi_ending_smile.jpg"
    image ev emi_ending_serious = "event/emi_ending_serious.jpg"
    image ev emi_ending_glad = "event/emi_ending_glad.jpg"

    image ev picnic_normal:
        "event/picnic_normal.jpg"
        xalign 0.5 yalign 0.0
    image ev picnic_rain:
        "event/picnic_rain.jpg"
        xalign 0.5 yalign 0.0

    python:
        def slow_out(trans, st, at):
            trans.yalign = 0.5
            trans.xalign = 0.5
            n = scaled_runtime(60.0, at)
            trans.zoom = 0.8 + (((-1.0 * acdc_warp(n)) + 1.0 ) * 0.2)
            return 0

    transform slow_out_tf:
        subpixel True
        function slow_out
        repeat

    image ev emi_cry_down = "event/emi_cry_down.jpg"
    image evul emi_cry_down:
        "event/emi_cry_down.jpg"
        zoom 0.8
    image ev emi_grave = "event/emi_grave.jpg"

    image evh emi_grinding_victorytall = "event/emi_grinding/emi_grinding_victorytall.jpg"
    image evh emi_grinding_victory = "event/emi_grinding/emi_grinding_victory.jpg"
    image evh emi_grinding_wink = "event/emi_grinding/emi_grinding_wink.jpg"
    image evh emi_grinding_grin = "event/emi_grinding/emi_grinding_grin.jpg"
    image evh emi_grinding_half_undress = "event/emi_grinding/emi_grinding_half_undress.jpg"
    image evh emi_grinding_half_grin = "event/emi_grinding/emi_grinding_half_grin.jpg"
    image evh emi_grinding_off_yawn = "event/emi_grinding/emi_grinding_off_yawn.jpg"
    image evh emi_grinding_off_closesurprise = "event/emi_grinding/emi_grinding_off_closesurprise.jpg"
    image evh emi_grinding_off_closearoused = "event/emi_grinding/emi_grinding_off_closearoused.jpg"
    image evh emi_grinding_off_aroused = "event/emi_grinding/emi_grinding_off_aroused.jpg"
    image evh emi_grinding_off_arousedclosed = "event/emi_grinding/emi_grinding_off_arousedclosed.jpg"
    image evh emi_grinding_off_come = "event/emi_grinding/emi_grinding_off_come.jpg"
    image evh emi_grinding_off_end = "event/emi_grinding/emi_grinding_off_end.jpg"

    image evh emi_shed_base1 = "event/emi_shed/emi_shed_base1.jpg"
    image evh emi_shed_base2 = "event/emi_shed/emi_shed_base2.jpg"
    image evh emi_shed_base3 = "event/emi_shed/emi_shed_base3.jpg"
    image evh emi_shed_base4 = "event/emi_shed/emi_shed_base4.jpg"

    image evh_l emi_shed_up = "event/emi_shed/emi_shed_lhand_up.png"
    image evh_l emi_shed_down = "event/emi_shed/emi_shed_lhand_down.png"

    image evh_r emi_shed_up = "event/emi_shed/emi_shed_rhand_up.png"
    image evh_r emi_shed_down = "event/emi_shed/emi_shed_rhand_down.png"

    image hisao emi_shed_closed = "event/emi_shed/emi_shed_hisao_closed.png"
    image hisao emi_shed_neutral = "event/emi_shed/emi_shed_hisao_neutral.png"
    image hisao emi_shed_sweat = "event/emi_shed/emi_shed_hisao_sweat.png"

    image emi emi_shed_closed = "event/emi_shed/emi_shed_emi_closed.png"
    image emi emi_shed_grin = "event/emi_shed/emi_shed_emi_grin.png"
    image emi emi_shed_hesitant = "event/emi_shed/emi_shed_emi_hesitant.png"
    image emi emi_shed_shock = "event/emi_shed/emi_shed_emi_shock.png"

    image evh emi_miss_closed = "event/emi_miss_closed.jpg"
    image evh emi_miss_open = "event/emi_miss_open.jpg"



    image prop rin_cigarette = "vfx/prop_rin_cigarette.png"
    image prop rin_cigarette_close = "vfx/prop_rin_cigarette_close.png"

    image ev rin_eating = "event/rin_eating.jpg"

    image ev rin_eating_zoomout:
        "event/rin_eating.jpg"
        size (800,600) crop (159,0,640,480) subpixel True
        acdc_warp 10.0 crop (0, 0, 800, 600)

    image ev rin_artclass1:
        "event/rin_artclass1.jpg"
        yalign 0.5 xalign 1.0
    image ev rin_artclass2:
        "event/rin_artclass2.jpg"
        yalign 0.5 xalign 1.0
    image ev rin_artclass3:
        "event/rin_artclass3.jpg"
        yalign 0.5 xalign 1.0
    image ev rin_artclass4:
        "event/rin_artclass4.jpg"
        yalign 0.5 xalign 1.0 subpixel True
        0.5
        acdc_warp 10.0 xalign 0.0

    python:
        def slide_left_p(trans, st, at):
            trans.xalign = _ease_in_time_warp(scaled_runtime(6.0, at))
            return 0

        def generic_rotateloop(length, dir, has_zoom, trans, st, at):
            trans.yalign = 0.5
            trans.xalign = 0.5
            n = 0.0
            if has_zoom:
                n = scaled_runtime(60.0, at)
            trans.zoom = 0.834 + (((-1.0 * acdc_warp(n)) + 1.0 ) * 0.266)
            trans.rotate = 360 / (length / (at + 0.1)) * dir
            return 0

        def wisp_func(trans, st, at):
            return generic_rotateloop(180, 1, True, trans, st, at)

        def smoke_func(trans, st, at):
            return generic_rotateloop(180, -1, False, trans, st, at)

    transform slide_left:
        subpixel True
        function slide_left_p

    transform wispturn:
        subpixel True
        function wisp_func
        repeat

    transform smoketurn:
        subpixel True
        function smoke_func
        repeat

    transform wispturn_old:
        rotate 0 zoom 1.0 xalign 0.5 yalign 0.5 subpixel True
        linear 180 rotate 360
        repeat

    transform smoketurn_old:
        rotate 0 zoom 1.3 xalign 0.5 yalign 0.5
        linear 180 rotate -360
        repeat

    image ev rin_wisp1:
        "event/rin_wisp1.jpg"
        truecenter
    image ev rin_wisp2:
        "event/rin_wisp2.jpg"
        truecenter
    image ev rin_wisp3:
        "event/rin_wisp3.jpg"
        truecenter
    image ev rin_wisp4:
        "event/rin_wisp4.jpg"
        truecenter
    image ev rin_wisp5:
        "event/rin_wisp5.jpg"
        truecenter
    image ev rin_wisp_blurred:
        "event/rin_wisp_blurred.jpg"
        truecenter
    image smoke focused = "event/rin_wisp_smoke_focused.png"
    image smoke blurred = "event/rin_wisp_smoke_blurred.png"

    image ovl rinbyhisao = "vfx/rinbyhisao.png"
    image ovl hisaobyrin = "vfx/hisaobyrin.png"

    python:
        def roofcomposite(comppath):
            return im.Composite(None,
                                (0,0), "event/rin_roof/rin_roof_boredom.jpg",
                                (300, 200), comppath)

    image ev hisao_mirror = "event/hisao_mirror.jpg"
    image ev hisao_mirror_800 = im.FactorScale("event/hisao_mirror.jpg", 0.8)

    image ev busride = "event/busride.jpg"
    image ev busride_ni = "event/busride_ni.jpg"

    image ev rin_roof_boredom = "event/rin_roof/rin_roof_boredom.jpg"
    image ev rin_roof_disgust = roofcomposite("event/rin_roof/rin_roof_disgust.jpg")
    image ev rin_roof_doubt = roofcomposite("event/rin_roof/rin_roof_doubt.jpg")
    image ev rin_roof_nonchalant = roofcomposite("event/rin_roof/rin_roof_nonchalant.jpg")
    image ev rin_roof_surprised = roofcomposite("event/rin_roof/rin_roof_surprised.jpg")

    image hisao rin_roof = "event/rin_roof/hisao_shadow.png"
    image emi rin_roof = "event/rin_roof/emi_shadow.png"

    image ev hisaobird_0 = "event/hisaobird/bird_0.jpg"
    image ev hisaobird_1 = "event/hisaobird/bird_1.jpg"
    image ev hisaobird_2 = "event/hisaobird/bird_2.jpg"
    image ev hisaobird_3 = "event/hisaobird/bird_3.jpg"
    image ev hisaobird_4 = "event/hisaobird/bird_4.jpg"
    image ev hisaobird_5 = "event/hisaobird/bird_5.jpg"
    image ev hisaobird_6 = "event/hisaobird/bird_6.jpg"
    image ev hisaobird_7 = "event/hisaobird/bird_7.jpg"
    image ev hisaobird_8 = "event/hisaobird/bird_8.jpg"
    image ev hisaobird_9 = "event/hisaobird/bird_9.jpg"

    image ev watch_black = "event/watch_black.jpg"
    image ev watch_worn = "vfx/watch_worn.png"
    image ev watch_worn_330 = night("vfx/watch_worn_330.png")
    image bg watchhallway_blur = "vfx/watchhallway_blur.jpg"

    image bg worrytree = "vfx/worrytree.jpg"
    image bg worrytree_ss = sunset("vfx/worrytree.jpg")

    image ev rin_painting_base = "event/rin_painting_base.jpg"
    image ev rin_painting_reply = "event/rin_painting_reply.jpg"
    image ev rin_painting_concerned = "event/rin_painting_concerned.jpg"
    image ev rin_painting_foot = "event/rin_painting_foot.jpg"
    image ev rin_painting_faceconcerned = "event/rin_painting_faceconcerned.jpg"

    image ev hisao_letter_closed = "event/hisao_letter_closed.jpg"
    image ev hisao_letter_open = "event/hisao_letter_open.jpg"
    image ev hisao_letter_open_2 = "event/hisao_letter_open_2.jpg"

    image ev rin_rain_away = "event/rin_rain_away.jpg"
    image ev rin_rain_towards = "event/rin_rain_towards.jpg"
    image ev rin_rain_away_close = "event/rin_rain_away_close.jpg"
    image ev rin_rain_towards_close = "event/rin_rain_towards_close.jpg"

    image ovl rin_rain_hisaotowards_close = im.Crop("event/rin_rain_towards_close.jpg", 400,0,400,1200)
    image ovl rin_rain_hisaotowards = im.Crop("event/rin_rain_towards.jpg", 400,0,400,600)

    image rin basic_deadpan_superclose = "sprites/rin/superclose/rin_basic_deadpan_superclose.png"
    image rin basic_deadpannormal_superclose = "sprites/rin/superclose/rin_basic_deadpannormal_superclose.png"
    image rin basic_lucid_superclose = "sprites/rin/superclose/rin_basic_lucid_superclose.png"
    image rin basic_crying_superclose_ss = sunset("sprites/rin/superclose/rin_basic_crying_superclose.png")
    image rin relaxed_doubt_superclose = "sprites/rin/superclose/rin_relaxed_doubt_superclose.png"
    image rin relaxed_sleepy_superclose = "sprites/rin/superclose/rin_relaxed_sleepy_superclose.png"
    image rin relaxed_surprised_superclose = "sprites/rin/superclose/rin_relaxed_surprised_superclose.png"
    image rin negative_crying_superclose = "sprites/rin/superclose/rin_negative_crying_superclose.png"
    image rin negative_crying_superclose_ss = sunset("sprites/rin/superclose/rin_negative_crying_superclose.png")

    image bg gallery_atelier_close = "vfx/gallery_atelier_close.jpg"
    image rin back_cas_superclose = "sprites/rin/superclose/rin_back_cas_superclose.png"


    image ev rin_kiss = "event/rin_kiss.jpg"

    image ev rin_high_frown = "event/rin_high_frown.jpg"
    image ev rin_high_grin = "event/rin_high_grin.jpg"
    image ev rin_high_grinwide = "event/rin_high_grinwide.jpg"
    image ev rin_high_oneeye = "event/rin_high_oneeye.jpg"
    image ev rin_high_open = "event/rin_high_open.jpg"
    image ev rin_high_sleep = "event/rin_high_sleep.jpg"
    image ev rin_high_smile = "event/rin_high_smile.jpg"

    image ev dandelion = "vfx/dandelion.jpg"

    image dandelion full = "vfx/dandelion_full.png"
    image dandelion gone = "vfx/dandelion_gone.png"
    image dandelionbg = "vfx/dandelionbg.jpg"


    image ev rin_nap_close_hand = "event/rin_nap_close_hand.jpg"
    image ev rin_nap_close_nohand = "event/rin_nap_close_nohand.jpg"
    image ev rin_nap_close_tears = "event/rin_nap_close_tears.png"
    image ev rin_nap_close_wind = "event/rin_nap_close_wind.jpg"
    image ev rin_nap_close = "event/rin_nap_close.jpg"
    image ev rin_nap_total_tears = "event/rin_nap_total_tears.png"
    image ev rin_nap_total_wind = "event/rin_nap_total_wind.jpg"
    image ev rin_nap_total = "event/rin_nap_total.jpg"

    image ev rin_nap_total_awind:
        "ev rin_nap_total"
        block:
            0.2
            "ev rin_nap_total_wind" with Dissolve(0.4)
            0.2
            "ev rin_nap_total" with Dissolve(0.4)
            repeat

    image ev rin_nap_close_awind:
        "ev rin_nap_close"
        block:
            0.2
            "ev rin_nap_close_wind" with Dissolve(0.4)
            0.2
            "ev rin_nap_close" with Dissolve(0.4)
            repeat

    image ev rin_nap_total_awind_tears = LiveComposite((800,600),
                                                       (0,0), "ev rin_nap_total_awind",
                                                       (0,0), "ev rin_nap_total_tears")
    image ev rin_nap_close_awind_tears = LiveComposite((800,600),
                                                       (0,0), "ev rin_nap_close_awind",
                                                       (0,0), "ev rin_nap_close_tears")


    image ev rin_masturbate_away = "event/rin_masturbate_away.jpg"
    image ev rin_masturbate_surprise = "event/rin_masturbate_surprise.jpg"
    image ev rin_masturbate_frown = "event/rin_masturbate_frown.jpg"
    image ev rin_masturbate_doubt = "event/rin_masturbate_doubt.jpg"
    image ev rin_masturbate_hug = "event/rin_masturbate_hug.jpg"

    image ovl rin_galleryskylight = "event/rin_galleryskylight.jpg"

    image ev rin_orange = "event/rin_orange.jpg"
    image ev rin_orange_large = "event/rin_orange_large.jpg"

    image evh rin_relief_up = "event/rin_relief_up.jpg"
    image evh rin_relief_up_large = "event/rin_relief_up_large.jpg"
    image evh rin_relief_down = "event/rin_relief_down.jpg"
    image evh rin_relief_down_large = "event/rin_relief_down_large.jpg"

    image ev rin_gallery:
        truecenter
        "event/rin_gallery.jpg"

    image doodlewhite = im.MatrixColor("vfx/rin_doodle.png",im.matrix.brightness(1))

    image ev rin_doodle:
        "doodlewhite"
        xalign 0.0 yalign 0.0 subpixel True
        parallel:
            acdc_warp 20.0 xalign 1.0 yalign 1.0
        parallel:
            1.0
            "vfx/rin_doodle.png" with ImageDissolve("vfx/rin_doodle_tr.png", 19.0, 32, alpha=True)

    image ev rin_doodle_all:
        "vfx/rin_doodle.png"
        truecenter
        zoom 0.9 subpixel True
        easein 12.0 zoom 0.75

    image bg misc_sky_rays = "bgs/misc_sky_rays.jpg"

    python:
        def rin_trueend_comp(list_in):
            baselist = [None, (0,0), "event/rin_trueend/rin_trueend_gone.jpg"]
            for offset, item in list_in:
                baselist.append(offset)
                baselist.append("event/rin_trueend/rin_trueend_"+item+".jpg")
            return im.Composite(*baselist)

    image ev rin_trueend_gone = "event/rin_trueend/rin_trueend_gone.jpg"
    image ev rin_trueend_gone_ni = night("event/rin_trueend/rin_trueend_gone.jpg")
    image ev rin_trueend_normal = rin_trueend_comp([((113,124),"normal")])
    image ev rin_trueend_closed = rin_trueend_comp([((113,124),"normal"), ((177,129),"closed")])
    image ev rin_trueend_sad = rin_trueend_comp([((113,124),"normal"), ((177,129),"sad")])
    image ev rin_trueend_smile = rin_trueend_comp([((113,124),"normal"), ((177,129),"smile")])
    image ev rin_trueend_weaksmile = rin_trueend_comp([((113,124),"normal"), ((177,129),"weaksmile")])
    image ev rin_trueend_hug = rin_trueend_comp([((335,51),"hug")])
    image ev rin_trueend_hugclosed = rin_trueend_comp([((335,51),"hug"), ((484,154), "hugclosed")])

    image ev rin_wet_pan_down = "event/rin_wet/rin_wet_pan_down.jpg"
    image ev rin_wet_arms = "event/rin_wet/rin_wet_arms.jpg"
    image ev rin_wet_face_up = "event/rin_wet/rin_wet_face_up.jpg"
    image ev rin_wet_face_down = "event/rin_wet/rin_wet_face_down.jpg"
    image ev rin_wet_towel_up = "event/rin_wet/rin_wet_towel_up.jpg"
    image ev rin_wet_towel_down = "event/rin_wet/rin_wet_towel_down.jpg"
    image ev rin_wet_towel_touch = "event/rin_wet/rin_wet_towel_touch.jpg"

    image ev rin_pair_base = "event/rin_pair/rin_pair_base.jpg"
    image ev rin_pair_base_clothes = im.Composite(None,
                                                  (0,0),"event/rin_pair/rin_pair_base.jpg",
                                                  (0,0),"event/rin_pair/rin_pair_hisao_clothes.png")

    image rp_hisao normal = Solid("#00000000")
    image rp_hisao frown = "event/rin_pair/rin_pair_hisao_frown.png"
    image rp_hisao smile = "event/rin_pair/rin_pair_hisao_smile.png"
    image rp_rin normal = Solid("#00000000")
    image rp_rin closed = "event/rin_pair/rin_pair_rin_closed.png"
    image rp_rin frown = "event/rin_pair/rin_pair_rin_frown.png"
    image rp_rin smile = "event/rin_pair/rin_pair_rin_smile.png"
    image rp_rin talk = "event/rin_pair/rin_pair_rin_talk.png"

    $ d_rin_h2_pan_surprise = im.Composite((800,900),
                                           (0,0), "event/rin_h2/rin_h2_u_surprise.jpg",
                                           (0,300), "event/rin_h2/rin_h2_l_pan.jpg")
    image evh rin_h2_pan_surprise = d_rin_h2_pan_surprise
    image unlock_evh rin_h2_pan_surprise = im.Crop(d_rin_h2_pan_surprise,0,0,800,600)

    $ d_rin_h2_pan_away = im.Composite((800,900),
                                       (0,0), "event/rin_h2/rin_h2_u_away.jpg",
                                       (0,300), "event/rin_h2/rin_h2_l_pan.jpg")
    image evh rin_h2_pan_away = d_rin_h2_pan_away
    image unlock_evh rin_h2_pan_away = im.Crop(d_rin_h2_pan_away,0,0,800,600)

    $ d_rin_h2_pan_closed = im.Composite((800,900),
                                         (0,0), "event/rin_h2/rin_h2_u_closed.jpg",
                                         (0,300), "event/rin_h2/rin_h2_l_pan.jpg")
    image evh rin_h2_pan_closed = d_rin_h2_pan_closed
    image unlock_evh rin_h2_pan_closed = im.Crop(d_rin_h2_pan_closed,0,0,800,600)

    image evh rin_h2_nopan_closed = im.Composite((800,900),
                                     (0,0), "event/rin_h2/rin_h2_u_closed.jpg",
                                     (0,300), "event/rin_h2/rin_h2_l_nopan.jpg")

    image evh rin_h2_hisao_surprise = im.Composite((800,900),
                                     (0,0), "event/rin_h2/rin_h2_u_surprise.jpg",
                                     (0,300), "event/rin_h2/rin_h2_l_hisao.jpg")

    image evh rin_h2_hisao_away = im.Composite((800,900),
                                     (0,0), "event/rin_h2/rin_h2_u_away.jpg",
                                     (0,300), "event/rin_h2/rin_h2_l_hisao.jpg")

    image evh rin_h2_hisao_closed = im.Composite((800,900),
                                     (0,0), "event/rin_h2/rin_h2_u_closed.jpg",
                                     (0,300), "event/rin_h2/rin_h2_l_hisao.jpg")

    python:
        def rin_h_comp(im_in, is_close=False):
            closer = ""
            if is_close:
                closer = "_close"
            return im.Composite(None,
                                (0,0), "event/rin_h/rin_h_closed"+closer+".jpg",
                                (0,0), "event/rin_h/rin_h_"+im_in+closer+".png")
    image evh rin_h_closed = "event/rin_h/rin_h_closed.jpg"
    image evh rin_h_left = rin_h_comp("left")
    image evh rin_h_normal = rin_h_comp("normal")
    image evh rin_h_right = rin_h_comp("right")
    image evh rin_h_strain = rin_h_comp("strain")

    image evh rin_h_closed_close = "event/rin_h/rin_h_closed_close.jpg"
    image evh rin_h_left_close = rin_h_comp("left", True)
    image evh rin_h_normal_close = rin_h_comp("normal", True)
    image evh rin_h_right_close = rin_h_comp("right", True)
    image evh rin_h_strain_close = rin_h_comp("strain", True)

    image ev rin_goodend_1 = "event/rin_goodend/rin_goodend_1.jpg"
    image ev rin_goodend_1b = "event/rin_goodend/rin_goodend_1b.jpg"
    image ev rin_goodend_2 = "event/rin_goodend/rin_goodend_2.jpg"

    image evbg rin_goodend_base = "event/rin_goodend/rin_goodend_base.jpg"
    image rin goodend_1 = "event/rin_goodend/rin_goodend_1.png"
    image rin goodend_1b = "event/rin_goodend/rin_goodend_1b.png"
    image rin goodend_2 = "event/rin_goodend/rin_goodend_2.png"
    image rin goodend_2_hires = "event/rin_goodend/rin_goodend_2_hires.png"
    image evfg rin_goodend = "event/rin_goodend/rin_goodend_fg.png"



    image ev lilly_tearoom = "event/lilly_tearoom.jpg"
    image ev lilly_tearoom_open = "event/lilly_tearoom_open.jpg"

    image ev lilly_crane = "event/lilly_crane.jpg"

    image ev lilly_touch_uni = "event/lilly_touch_uni.jpg"
    image ev lilly_touch_cas = sunset("event/lilly_touch_cas.jpg")
    image ev lilly_touch_cheong = "event/lilly_touch_cheong.jpg"

    image ev braille = "vfx/braille.jpg"
    image ev icecream = "vfx/icecream.jpg"

    image evfg lilly_sunsetwalk = sunset("event/lilly_sunsetwalk_fg.png")
    image evbg lilly_sunsetwalk = "event/lilly_sunsetwalk_bg.jpg"

    image ev lilly_bedroom = "event/lilly_bedroom.jpg"
    image ev lilly_bedroom_large = "event/lilly_bedroom_large.jpg"

    image ev lilly_hanako_hug = "event/lilly_hanako_hug.jpg"
    image unlock_ev lilly_hanako_hug_end:
        "event/lilly_hanako_hug.jpg"
        xalign 0.5 yalign 1.0 subpixel True
        easein 6.0 yalign 0.0

    image ev lilly_kissing = "event/lilly_kissing.jpg"

    image ev lilly_sleeping = "event/lilly_sleeping.jpg"
    image ev lilly_sleeping_smile = "event/lilly_sleeping_smile.jpg"

    image train_scenery:
        "event/lilly_train/train_scenery.jpg"
        xalign 0.0
        linear 2.0 xalign 1.0
        repeat

    image train_scenery_fg:
        "event/lilly_train/train_scenery_fg.png"
        offscreenright
        linear 0.3 offscreenleft
        4.0
        repeat

    image evfg lilly_trainride = "event/lilly_train/lilly_trainride.png"
    image evfg lilly_trainride_smiles = im.Composite(None,
                                                (0,0), "event/lilly_train/lilly_trainride.png",
                                                (338,301), "event/lilly_train/lilly_trainride_smile.png",
                                                (573,331), "event/lilly_train/lilly_trainride_hanasmile.png")

    image ev lilly_trainride = "event/lilly_train/lilly_trainride.jpg"
    image ev lilly_trainride_smiles = "event/lilly_train/lilly_trainride_smiles.jpg"

    image train_scenery_ni:
        "event/lilly_train/train_scenery_ni.jpg"
        xalign 0.0
        linear 2.0 xalign 1.0
        repeat

    image train_scenery_fg_ni:
        "event/lilly_train/train_scenery_fg_ni.png"
        offscreenright
        linear 0.3 offscreenleft
        4.0
        repeat

    python:
        def trainwave(trans, st, at):
            import math
            trans.yalign = (math.sin(((at/2.0) % 2.0)*math.pi) + 1.0) / 2
            return 0

    transform train_shake:
        subpixel True
        function trainwave
        repeat

    image lilly_trainride_ni norm = "event/lilly_train/lilly_trainride_ni_norm.png"

    python:
        def traincomposite(comppath):
            return im.Composite(None,
                                (0,0), "event/lilly_train/lilly_trainride_ni_norm.png",
                                (321, 200), comppath)

    image lilly_trainride_ni ara = traincomposite("event/lilly_train/lilly_trainride_ni_ara.png")
    image lilly_trainride_ni opensmile = traincomposite("event/lilly_train/lilly_trainride_ni_opensmile.png")
    image lilly_trainride_ni pout = traincomposite("event/lilly_train/lilly_trainride_ni_pout.png")
    image lilly_trainride_ni smile = traincomposite("event/lilly_train/lilly_trainride_ni_smile.png")
    image lilly_trainride_ni weaksmile = traincomposite("event/lilly_train/lilly_trainride_ni_weaksmile.png")


    image ev lilly_trainride_ni = "event/lilly_train/lilly_trainride_ni.jpg"

    image ev lilly_wheat_large = "event/lilly_wheat_large.jpg"
    image ovl lilly_wheat_foreground = "event/lilly_wheat_foreground.png"

    image unlock_ev lilly_wheat_close = im.Crop("event/lilly_wheat_large.jpg", 500,0,800,600)
    image ev lilly_wheat_small = "event/lilly_wheat_small.jpg"


    python:
        def restaurant_out_f(trans, st, at):
            trans.yalign = 0.5
            trans.xalign = 0.5
            n = scaled_runtime(20.0, at)
            trans.zoom = 0.834 + (((-1.0 * acdc_warp(n)) + 1.0 ) * 0.266)
            return 0

    transform restaurant_out:
        subpixel True
        function restaurant_out_f

    image ev lilly_restaurant_listen = "event/lilly_restaurant_listen.jpg"
    image ev lilly_restaurant_sheepish = "event/lilly_restaurant_sheepish.jpg"

    image evul lilly_restaurant_listen:
        "event/lilly_restaurant_listen.jpg"
        zoom 0.8
    image evul lilly_restaurant_sheepish:
        "event/lilly_restaurant_sheepish.jpg"
        zoom 0.8

    image ev lilly_restaurant_wine = "event/lilly_restaurant_wine.jpg"
    image ev lilly_restaurant_eat = "event/lilly_restaurant_eat.jpg"
    image ev lilly_restaurant_chew = "event/lilly_restaurant_chew.jpg"

    image ev hisao_teacup = "event/hisao_teacup.jpg"
    image evul hisao_teacup:
        "event/hisao_teacup.jpg"
        zoom 0.8

    image ev akira_park = "event/akira_park.jpg"
    image evul akira_park:
        "event/akira_park.jpg"
        zoom 0.8

    image ev lilly_sheets = "event/lilly_sheets.jpg"

    image ev lilly_hospitalwindow = "event/lilly_hospitalwindow.jpg"


    image origami_hand = night("vfx/origami_hand.png")

    image ev lilly_airport = "event/lilly_airport.jpg"
    image ev lilly_airport_end = "event/lilly_airport_end.jpg"

    image bg school_dormhisao_ni_fb = past("bgs/school_dormhisao_blurred_ni.jpg")
    image origami_fb = past_night("vfx/origami_hand.png")
    image bg shizu_houseext_lights_fb = past("bgs/shizu_houseext_lights.jpg")
    image hideaki serious_up_fb = past_night("sprites/hideaki/hideaki_serious_up.png")
    image bg hosp_ext_fb = past_night("bgs/hosp_ext.jpg")
    image crowd_still1_fb = past_night("vfx/crowd1.png")
    image crowd_still2_fb = past_night("vfx/crowd2.png")
    image ev lilly_airport_end_fb = past("event/lilly_airport_end.jpg")


    python:
        def l_hosp_out_f(trans, st, at):
            trans.yalign = 0.5
            trans.xalign = 0.5
            n = scaled_runtime(30.0, at)
            trans.zoom = 0.8 + (((-1.0 * acdc_warp(n)) + 1.0 ) * 0.2)
            return 0

    transform l_hosp_out:
        subpixel True
        function l_hosp_out_f

    image unlock_ev lilly_hospital:
        "event/lilly_hospital.jpg"
        zoom 0.8
    image ev lilly_hospital = "event/lilly_hospital.jpg"
    image unlock_ev lilly_hospitalclosed:
        "event/lilly_hospitalclosed.jpg"
        zoom 0.8
    image ev lilly_hospitalclosed = "event/lilly_hospitalclosed.jpg"

    image unlock_ev lilly_goodend:
        "event/lilly_goodend.jpg"
        zoom 0.8
    image ev lilly_goodend = "event/lilly_goodend.jpg"
    image evbg lilly_goodend = "event/lilly_goodend_bg.jpg"
    image evfg lilly_goodend = "event/lilly_goodend_fg.png"


    image evhunlock lilly_handjob_chest_frown_small:
        "event/lilly_handjob/lilly_hcg_handjob_chest_frown.jpg"
        zoom 0.667
    image evhunlock lilly_handjob_chest_normal_small:
        "event/lilly_handjob/lilly_hcg_handjob_chest_normal.jpg"
        zoom 0.667

    image evh lilly_handjob_chest_frown = "event/lilly_handjob/lilly_hcg_handjob_chest_frown.jpg"
    image evh lilly_handjob_chest_normal = "event/lilly_handjob/lilly_hcg_handjob_chest_normal.jpg"
    image evh lilly_handjob_stroke_normopen = "event/lilly_handjob/lilly_hcg_handjob_stroke_normopen.jpg"

    image evh lilly_handjob_stroke_flustopen_small = "event/lilly_handjob/lilly_hcg_handjob_stroke_flustopen_small.jpg"
    image evh lilly_handjob_stroke_normopen_small = "event/lilly_handjob/lilly_hcg_handjob_stroke_normopen_small.jpg"
    image evh lilly_handjob_stroke_normshut_small = "event/lilly_handjob/lilly_hcg_handjob_stroke_normshut_small.jpg"

    image evh lilly_cowgirl_cry_small = "event/lilly_cowgirl/lilly_hcg_cowgirl_cry_small.jpg"
    image evh lilly_cowgirl_frown_small = "event/lilly_cowgirl/lilly_hcg_cowgirl_frown_small.jpg"
    image evh lilly_cowgirl_smile_small = "event/lilly_cowgirl/lilly_hcg_cowgirl_smile_small.jpg"
    image evh lilly_cowgirl_strain_small = "event/lilly_cowgirl/lilly_hcg_cowgirl_strain_small.jpg"
    image evh lilly_cowgirl_weaksmile_small = "event/lilly_cowgirl/lilly_hcg_cowgirl_weaksmile_small.jpg"

    image evh lilly_bath_emb_small = "event/lilly_bath/lilly_hcg_bath_emb_small.jpg"
    image evh lilly_bath_grab_small = "event/lilly_bath/lilly_hcg_bath_grab_small.jpg"
    image evh lilly_bath_moan_small = "event/lilly_bath/lilly_hcg_bath_moan_small.jpg"
    image evh lilly_bath_open_small = "event/lilly_bath/lilly_hcg_bath_open_small.jpg"
    image evh lilly_bath_smile_small = "event/lilly_bath/lilly_hcg_bath_smile_small.jpg"

    image evh lilly_afterbath_open_small = "event/lilly_afterbath/lilly_hcg_afterbath_open_small.jpg"
    image evh lilly_afterbath_shut_small = "event/lilly_afterbath/lilly_hcg_afterbath_shut_small.jpg"

    image evh lilly_masturbate = "event/lilly_masturbate.jpg"
    image evh lilly_masturbate_come = "event/lilly_masturbate_come.jpg"
    image evh lilly_masturbate_come_face = "event/lilly_masturbate_come_face.jpg"



    image ev hana_library_read = sunset("event/hana_library_read.jpg")
    image ev hana_library = sunset("event/hana_library.jpg")
    image ev hana_library_gasp = sunset("event/hana_library_gasp.jpg")
    image ev hana_library_smile = sunset("event/hana_library_smile.jpg")

    image ev hana_library_read_std = "event/hana_library_read.jpg"
    image ev hana_library_std = "event/hana_library.jpg"
    image ev hana_library_gasp_std = "event/hana_library_gasp.jpg"
    image ev hana_library_smile_std = "event/hana_library_smile.jpg"

    image ev hanako_presents1 = "event/hanako_presents1.jpg"
    image ev hanako_presents2 = "event/hanako_presents2.jpg"

    image evbg hanako_breakdown = "event/hanako_breakdown/hanako_breakdown_bg.jpg"
    image evfg hanako_breakdown_down = "event/hanako_breakdown/hanako_breakdown_down.png"
    image evfg hanako_breakdown_up = im.Composite(None,
                                                  (0,0),"event/hanako_breakdown/hanako_breakdown_down.png",
                                                  (588,71),"event/hanako_breakdown/hanako_breakdown_up.jpg")
    image evfg hanako_breakdown_closed = im.Composite(None,
                                                      (0,0),"event/hanako_breakdown/hanako_breakdown_down.png",
                                                      (588,71),"event/hanako_breakdown/hanako_breakdown_closed.jpg")

    image evul hanako_breakdown_down = im.Composite(None,
                                                  (0,0), "event/hanako_breakdown/hanako_breakdown_bg.jpg",
                                                  (0,0),"event/hanako_breakdown/hanako_breakdown_down.png")
    image evul hanako_breakdown_up = im.Composite(None,
                                                  (0,0), "event/hanako_breakdown/hanako_breakdown_bg.jpg",
                                                  (0,0),"event/hanako_breakdown/hanako_breakdown_down.png",
                                                  (588,71),"event/hanako_breakdown/hanako_breakdown_up.jpg")
    image evul hanako_breakdown_closed = im.Composite(None,
                                                  (0,0), "event/hanako_breakdown/hanako_breakdown_bg.jpg",
                                                  (0,0),"event/hanako_breakdown/hanako_breakdown_down.png",
                                                  (588,71),"event/hanako_breakdown/hanako_breakdown_closed.jpg")


    image ev hanako_crayon1 = "event/hanako_crayon1.jpg"
    image ev hanako_crayon2 = "event/hanako_crayon2.jpg"

    image ev hanako_cry_open = "event/hanako_cry_open.jpg"
    image ev hanako_cry_closed = "event/hanako_cry_closed.jpg"
    image ev hanako_cry_away = "event/hanako_cry_away.jpg"

    image ev hanako_cry_closed_fb = past("event/hanako_cry_closed.jpg")

    image hanako_door_base = "vfx/hanako_door_base.jpg"
    image hanako_door_door = "vfx/hanako_door_door.jpg"

    image ev hanako_billiards_break = "event/hanako_billiards_break.jpg"

    image ev hanako_billiards_distant:
        "event/hanako_billiards_distant.jpg"
        zoom 0.8
    image ev hanako_billiards_distant_med:
        "event/hanako_billiards_distant.jpg"
        yanchor 0.0 ypos -0.1 xalign 1.0

    image ev hanako_billiards_serious:
        "event/hanako_billiards_serious.jpg"
        zoom 0.8
    image ev hanako_billiards_serious_med:
        "event/hanako_billiards_serious.jpg"
        yanchor 0.0 ypos -0.1 xalign 1.0

    image ev hanako_billiards_smile:
        "event/hanako_billiards_smile.jpg"
        zoom 0.8
    image ev hanako_billiards_smile_med:
        "event/hanako_billiards_smile.jpg"
        yanchor 0.0 ypos -0.1 xalign 1.0

    image ev hanako_billiards_smile_close:
        "event/hanako_billiards_smile_close.jpg"

    image ev hanako_billiards_timid:
        "event/hanako_billiards_timid.jpg"
        zoom 0.8
    image ev hanako_billiards_timid_med:
        "event/hanako_billiards_timid.jpg"
        yanchor 0.0 ypos -0.1 xalign 1.0

    image evul hanako_emptyclassroom = im.FactorScale(im.Composite(None,
                                                                 (0,0), "event/hanako_emptyclassroom_bg.jpg",
                                                                 (0,0), "event/hanako_emptyclassroom_fg.png"), 0.8)

    image evbg hanako_emptyclassroom = "event/hanako_emptyclassroom_bg.jpg"
    image evfg hanako_emptyclassroom = "event/hanako_emptyclassroom_fg.png"


    image ev hanako_dolls = "event/hanako_dolls.jpg"

    image ev hanako_rage = "event/hanako_rage.jpg"
    image ev hanako_rage_sad = "event/hanako_rage_sad.jpg"

    image ev hanako_eye = "vfx/hanako_eye.jpg"

    image ev hisao_scar_large = "event/hisao_scar_large.jpg"
    image ev hisao_scar = "event/hisao_scar.jpg"

    image ev hanako_scars_large = "event/hanako_scars_large.jpg"
    image ev hanako_scars = "event/hanako_scars.jpg"

    image evh hanako_bed_boobs_blush = "event/hanako_bed_boobs_blush.jpg"
    image evh hanako_bed_boobs_glance = "event/hanako_bed_boobs_glance.jpg"
    image evh hanako_bed_crotch_blush = "event/hanako_bed_crotch_blush.jpg"
    image evh hanako_bed_crotch_glance = "event/hanako_bed_crotch_glance.jpg"

    image evh hanako_missionary_underwear = "event/hanako_missionary_underwear.jpg"
    image evh hanako_missionary_open = "event/hanako_missionary_open.jpg"
    image evh hanako_missionary_closed = "event/hanako_missionary_closed.jpg"
    image evh hanako_missionary_clench = "event/hanako_missionary_clench.jpg"

    image ev hanako_after_worry = "event/hanako_after_worry.jpg"
    image ev hanako_after_smile = "event/hanako_after_smile.jpg"

    image ev hanako_park_alone = "event/hanako_park_alone.jpg"
    image ev hanako_park_away = "event/hanako_park_away.jpg"
    image ev hanako_park_closed = "event/hanako_park_closed.jpg"
    image ev hanako_park_look = "event/hanako_park_look.jpg"

    image ev hanako_goodend_close = "event/hanako_goodend_close.jpg"
    image ev hanako_goodend_muffin = "event/hanako_goodend_muffin.jpg"
    image ev hanako_goodend = "event/hanako_goodend.jpg"

    image unlock_ev hanako_goodend_close:
        "event/hanako_goodend_close.jpg"
        zoom 0.8
    image unlock_ev hanako_goodend_muffin:
        "event/hanako_goodend_muffin.jpg"
        zoom 0.8
    image unlock_ev hanako_goodend:
        "event/hanako_goodend.jpg"
        xalign 0.5 yalign 0.0
        zoom 0.85


    image ev shizu_shanghai = "event/shizu_shanghai.jpg"
    image ev shizu_shanghai_boredlaugh = "event/shizu_shanghai_boredlaugh.jpg"
    image ev shizu_shanghai_borednormal = "event/shizu_shanghai_borednormal.jpg"
    image ev shizu_shanghai_normallaugh = "event/shizu_shanghai_normallaugh.jpg"
    image ev shizu_shanghai_smirklaugh = "event/shizu_shanghai_smirklaugh.jpg"
    image ev shizu_shanghai_smirknormal = "event/shizu_shanghai_smirknormal.jpg"


    image ev shizuconfess_normal = "event/shizu_yukata/shizuconfess_normal.jpg"
    image ev shizuconfess_smile = "event/shizu_yukata/shizuconfess_smile.jpg"
    image ev shizuconfess_closed = "event/shizu_yukata/shizuconfess_closed.jpg"

    python:
        def zoomin_generic_f(trans, st, at):
            trans.xalign = 0.5
            trans.yalign = 0.5
            n = scaled_runtime(20.0, at)
            trans.zoom = 0.95 - (acdc_warp(n) * 0.15)
            return 0

    transform kenji_mg_out:
        subpixel True
        function zoomin_generic_f

    image evbg kenji_glasses = "event/kenji_glasses/kenji_glasses_bg.jpg"
    image evmg kenji_glasses_normal = "event/kenji_glasses/kenji_glasses_mg.png"
    image evmg kenji_glasses_frown = im.Composite(None,
                                          (0,0), "event/kenji_glasses/kenji_glasses_mg.png",
                                          (400,190), "event/kenji_glasses/kenji_glasses_frown.png")
    image evmg kenji_glasses_closed = im.Composite(None,
                                          (0,0), "event/kenji_glasses/kenji_glasses_mg.png",
                                          (400,190), "event/kenji_glasses/kenji_glasses_closed.png")
    image evfg kenji_glasses = "event/kenji_glasses/kenji_glasses_fg.png"


    image evul kenji_glasses_normal = im.FactorScale(im.Composite(None,
                                          (0,0), "event/kenji_glasses/kenji_glasses_bg.jpg",
                                          (0,0), "event/kenji_glasses/kenji_glasses_mg.png",
                                          (0,0), "event/kenji_glasses/kenji_glasses_fg.png"),0.8)
    image evul kenji_glasses_frown = im.FactorScale(im.Composite(None,
                                          (0,0), "event/kenji_glasses/kenji_glasses_bg.jpg",
                                          (0,0), "event/kenji_glasses/kenji_glasses_mg.png",
                                          (400,190), "event/kenji_glasses/kenji_glasses_frown.png",
                                          (0,0), "event/kenji_glasses/kenji_glasses_fg.png"),0.8)
    image evul kenji_glasses_closed = im.FactorScale(im.Composite(None,
                                          (0,0), "event/kenji_glasses/kenji_glasses_bg.jpg",
                                          (0,0), "event/kenji_glasses/kenji_glasses_mg.png",
                                          (400,190), "event/kenji_glasses/kenji_glasses_closed.png",
                                          (0,0), "event/kenji_glasses/kenji_glasses_fg.png"),0.8)


    image ev shizutanabata = "event/shizu_yukata/shizutanabata.jpg"

    image ev shizu_flashback = "event/shizu_flashback.jpg"

    image ev shizu_hands = "event/shizu_hands.jpg"

    image ev shizune_car:
        "event/shizune_car.jpg"
        subpixel True yalign 0.5 xalign 0.0
        easein 12.0 xalign 1.0

    image ev shizu_fishing_sl = "event/shizu_fishing_sl.jpg"
    image ev shizu_fishing_ah = "event/shizu_fishing_ah.jpg"

    image ev shizu_couch = "event/shizu_couch.jpg"

    python:
        def shizu_roof_in_f(trans, st, at):
            trans.xalign = 0.5
            trans.yalign = 1.0
            n = scaled_runtime(60.0, at)
            trans.zoom = 0.8 + (acdc_warp(n) * 0.2)
            return 0

    transform shizu_roof_in:
        subpixel True
        function shizu_roof_in_f

    image ev shizu_roof = "event/shizu_roof/shizu_roof.jpg"
    image ev shizu_roof_towardsangry = im.Composite(None,
                                            (0,0),  "event/shizu_roof/shizu_roof.jpg",
                                            (299,296), "event/shizu_roof/shizu_roof_towardsangry.jpg")
    image ev shizu_roof_towardsnormal = im.Composite(None,
                                            (0,0),  "event/shizu_roof/shizu_roof.jpg",
                                            (299,296), "event/shizu_roof/shizu_roof_towardsnormal.jpg")
    image ev shizu_roof_smile = im.Composite(None,
                                            (0,0),  "event/shizu_roof/shizu_roof.jpg",
                                            (299,296), "event/shizu_roof/shizu_roof_smile.jpg")

    image ev shizu_roof2 = im.Composite(None,
                                            (0,0),  "event/shizu_roof/shizu_roof.jpg",
                                            (601,316), "event/shizu_roof/shizu_roof_hisao2.jpg")
    image ev shizu_roof2_towardsangry = im.Composite(None,
                                            (0,0),  "event/shizu_roof/shizu_roof.jpg",
                                            (601,316), "event/shizu_roof/shizu_roof_hisao2.jpg",
                                            (299,296), "event/shizu_roof/shizu_roof_towardsangry.jpg")
    image ev shizu_roof2_towardsnormal = im.Composite(None,
                                            (0,0),  "event/shizu_roof/shizu_roof.jpg",
                                            (601,316), "event/shizu_roof/shizu_roof_hisao2.jpg",
                                            (299,296), "event/shizu_roof/shizu_roof_towardsnormal.jpg")
    image ev shizu_roof2_smile = im.Composite(None,
                                            (0,0),  "event/shizu_roof/shizu_roof.jpg",
                                            (601,316), "event/shizu_roof/shizu_roof_hisao2.jpg",
                                            (299,296), "event/shizu_roof/shizu_roof_smile.jpg")

    image evh shizune_hcg_tied_blush_small = "event/shizune_hcg_tied/shizune_hcg_tied_blush_small.jpg"
    image evh shizune_hcg_tied_blush = "event/shizune_hcg_tied/shizune_hcg_tied_blush.jpg"
    image evh shizune_hcg_tied_close_small = "event/shizune_hcg_tied/shizune_hcg_tied_close_small.jpg"
    image evh shizune_hcg_tied_close = "event/shizune_hcg_tied/shizune_hcg_tied_close.jpg"
    image evh shizune_hcg_tied_kinky1_small = "event/shizune_hcg_tied/shizune_hcg_tied_kinky1_small.jpg"

    image evh shizune_hcg_tied_kinky2_small = "event/shizune_hcg_tied/shizune_hcg_tied_kinky2_small.jpg"
    image evh shizune_hcg_tied_kinky2 = "event/shizune_hcg_tied/shizune_hcg_tied_kinky2.jpg"
    image evh shizune_hcg_tied_kinky3_small = "event/shizune_hcg_tied/shizune_hcg_tied_kinky3_small.jpg"

    image evh shizune_hcg_tied_smile_small = "event/shizune_hcg_tied/shizune_hcg_tied_smile_small.jpg"

    image evh shizune_hcg_tied_stare_small = "event/shizune_hcg_tied/shizune_hcg_tied_stare_small.jpg"
    image evh shizune_hcg_tied_stare = "event/shizune_hcg_tied/shizune_hcg_tied_stare.jpg"

    image evh_hi shizune_hcg_tied_hisao2 = im.Composite((1600,1200),
                                                        (1080,290),"event/shizune_hcg_tied/shizune_hcg_tied_hisao2.png")
    image evh_hi shizune_hcg_tied_hisao2_small = im.Composite((800,600),
                                                              (540,145),"event/shizune_hcg_tied/shizune_hcg_tied_hisao2_small.png")


    image evhul shizune_hcg_tied_hisao2_small = im.Composite((800,600),
                                                             (0,0), "event/shizune_hcg_tied/shizune_hcg_tied_kinky3_small.jpg",
                                                             (540,145),"event/shizune_hcg_tied/shizune_hcg_tied_hisao2_small.png")


    image evh shizu_undressing_clothed_stare = "event/shizu_undressing/shizu_undressing_clothed_stare.jpg"
    image evh shizu_undressing_clothed_kiss = "event/shizu_undressing/shizu_undressing_clothed_kiss.jpg"
    image evh shizu_undressing_clothed_blush = "event/shizu_undressing/shizu_undressing_clothed_blush.jpg"
    image evh shizu_undressing_unclothed_blush = "event/shizu_undressing/shizu_undressing_unclothed_blush.jpg"
    image evh shizu_undressing_unclothed_closed = "event/shizu_undressing/shizu_undressing_unclothed_closed.jpg"
    image evh shizu_undressing_unclothed_kiss = "event/shizu_undressing/shizu_undressing_unclothed_kiss.jpg"
    image evh shizu_undressing_unclothed_talk = "event/shizu_undressing/shizu_undressing_unclothed_talk.jpg"

    image evh shizu_pushdown = "event/shizu_pushdown.jpg"

    image evh shizu_straddle_open:
        "event/shizu_straddle_open.jpg"
        xalign 0.7 yalign 1.0 subpixel True
        easein 16.0 xalign 0.0 yalign 0.0
    image evh shizu_straddle_tease = "event/shizu_straddle_tease.jpg"
    image evh shizu_straddle_closed = "event/shizu_straddle_closed.jpg"
    image evh shizu_straddle_smile = "event/shizu_straddle_smile.jpg"
    image evh shizu_straddle_come = "event/shizu_straddle_come.jpg"

    image evh shizu_table_smile = "event/shizu_table_smile.jpg"
    image evh shizu_table_normal = "event/shizu_table_normal.jpg"
    image evh shizu_table_comeopen = "event/shizu_table_comeopen.jpg"
    image evh shizu_table_comeclosed = "event/shizu_table_comeclosed.jpg"

    image ev misha_sad = "event/misha_sad.jpg"

    image ev misha_nightclass = "event/misha_nightclass.jpg"
    image ovl misha_nightclass_aperture = "vfx/misha_nightclass_aperture.png"

    image evh misha_naked:
        "event/misha_naked.jpg"
        xalign 0.0 yalign 0.0
    image evh misha_sex_aside = "event/misha_sex_aside.jpg"
    image evh misha_sex_closed = "event/misha_sex_closed.jpg"

    image ev misha_roof_normal:
        "event/misha_roof_normal.jpg"
        xalign 0.5 yalign 0.0
    image ev misha_roof_angry = "event/misha_roof_angry.jpg"
    image ev misha_roof_closed = "event/misha_roof_closed.jpg"
    image ev misha_roof_sad = "event/misha_roof_sad.jpg"

    image aoi_keiko = sunset("vfx/aoi_keiko.png")

    image ev shizu_goodend:
        "event/shizu_goodend.jpg"
        xalign 0.5 yalign 1.0 subpixel True

    image ev shizu_goodend_pan:
        "event/shizu_goodend.jpg"
        xalign 0.5 yalign 1.0 subpixel True
        0.5
        acdc_warp 15.0 yalign 0.0

    image ev shizu_badend = "event/shizu_badend.jpg"


    image ev showdown = "event/lilly_shizu_showdown.jpg"
    image ev showdown_large = "event/lilly_shizu_showdown_large.jpg"
    image ev showdown_lilly = im.Crop("event/lilly_shizu_showdown_large.jpg", 280,100,800,600)
    image ev showdown_shizu = im.Crop("event/lilly_shizu_showdown_large.jpg", 1400,160,800,600)

    image showdown_lilly_slice = im.Crop("event/lilly_shizu_showdown_large.jpg", 440,260,800,299)
    image showdown_shizu_slice = im.Crop("event/lilly_shizu_showdown_large.jpg", 1360,320,800,299)


    image ev kenji_rooftop = "event/kenji_rooftop.jpg"
    image ev kenji_rooftop_large = "event/kenji_rooftop_large.jpg"
    image ev kenji_rooftop_kenji = im.Crop("event/kenji_rooftop_large.jpg", 288,376,800,600)




    $ ex_g_images = (("thumb/other_iwanako.jpg", "evul other_iwanako"),
                     ("thumb/hisao_class.jpg","ev hisao_class_start","ev hisao_class_move","ev hisao_class_end"),
                     ("thumb/kenji_rooftop.jpg","ev kenji_rooftop"),
                     ("thumb/hisao_teacup.jpg","evul hisao_teacup"),
                     ("thumb/hisao_letter.jpg","ev hisao_letter_closed", "ev hisao_letter_open", "ev hisao_letter_open_2"),
                     ("thumb/akira_park.jpg","evul akira_park"),
                     ("thumb/emi_knockeddown.jpg","ev emi_knockeddown"),
                     ("thumb/emi_run_face.jpg","ev emi_run_face"),
                     ("thumb/emitrack_blocks.jpg", "ev emitrack_blocks", "ev emitrack_blocks_close", "ev emitrack_blocks_close_grin"),
                     ("thumb/emitrack_running.jpg", "ev emitrack_running"),
                     ("thumb/emitrack_finishtop.jpg","ev emitrack_finishtop"),
                     ("thumb/emitrack_finish.jpg","ev emitrack_finish"),
                     ("thumb/picnic.jpg", "ev picnic_normal", "ev picnic_rain"),
                     ("thumb/emi_sleep.jpg","ev emi_sleep_unsure", "ev emi_sleep_normal", "ev emi_sleep_weep", "ev emi_sleep_cry"),
                     ("thumb/emi_sleepy.jpg","ev emi_sleepy", "ev emi_sleepy_face", "ev emi_sleepy_legs"),
                     ("thumb/emi_firstkiss.jpg","ev emi_firstkiss"),
                     ("thumb/emi_bed.jpg","ev emi_bed_normal", "ev emi_bed_smile", "ev emi_bed_happy", "ev emi_bed_unsure", "ev emi_bed_frown", "ev emi_parkback", "ev emi_parkback_frown"),
                     ("thumb/emi_forehead.jpg","ev emi_forehead"),
                     ("thumb/emi_grinding.jpg","evh emi_grinding_victory", "evh emi_grinding_wink", "evh emi_grinding_grin", "evh emi_grinding_half_undress", "evh emi_grinding_half_grin", "evh emi_grinding_off_yawn", "evh emi_grinding_off_closesurprise", "evh emi_grinding_off_closearoused", "evh emi_grinding_off_aroused", "evh emi_grinding_off_arousedclosed", "evh emi_grinding_off_come", "evh emi_grinding_off_end"),
                     ("thumb/emi_shed.jpg","evh emi_shed_base1","evh emi_shed_base3","evh emi_shed_base3","evh emi_shed_base4",),
                     ("thumb/emi_grave.jpg","ev emi_grave"),
                     ("thumb/emi_cry_down.jpg","evul emi_cry_down"),
                     ("thumb/emi_miss.jpg","evh emi_miss_closed", "evh emi_miss_open"),
                     ("thumb/emi_ending.jpg","ev emi_ending_smile", "ev emi_ending_serious", "ev emi_ending_glad"),
                     ("thumb/hana_library.jpg","ev hana_library","ev hana_library_read","ev hana_library_gasp"),
                     ("thumb/hanako_shanghaiwindow.jpg","ev hanako_shanghaiwindow"),
                     ("ev hanako_presents1", "ev hanako_presents2"),
                     ("thumb/hanako_crayon.jpg","ev hanako_crayon1", "ev hanako_crayon2"),
                     ("thumb/hanako_breakdown.jpg","evul hanako_breakdown_down", "evul hanako_breakdown_up", "evul hanako_breakdown_closed"),
                     ("thumb/hanako_cry.jpg","ev hanako_cry_closed", "ev hanako_cry_open", "ev hanako_cry_away"),
                     ("thumb/hanako_billiards.jpg", "ev hanako_billiards_distant", "ev hanako_billiards_serious", "ev hanako_billiards_timid","ev hanako_billiards_smile","ev hanako_billiards_smile_close"),
                     ("thumb/hanako_emptyclassroom.jpg", "evul hanako_emptyclassroom"),
                     ("thumb/hanako_rage.jpg","ev hanako_rage", "ev hanako_rage_sad"),
                     ("thumb/hisao_scar.jpg","ev hisao_scar"),
                     ("thumb/hanako_scars.jpg","ev hanako_scars"),
                     ("thumb/hanako_bed.jpg","evh hanako_bed_boobs_blush", "evh hanako_bed_boobs_glance", "evh hanako_bed_crotch_blush", "evh hanako_bed_crotch_glance"),
                     ("thumb/hanako_missionary.jpg","evh hanako_missionary_underwear", "evh hanako_missionary_open", "evh hanako_missionary_closed", "evh hanako_missionary_clench"),
                     ("thumb/hanako_after.jpg","ev hanako_after_worry","ev hanako_after_smile"),
                     ("thumb/hanako_park.jpg","ev hanako_park_alone","ev hanako_park_away","ev hanako_park_look","ev hanako_park_closed"),
                     ("thumb/hanako_goodend.jpg","unlock_ev hanako_goodend_close","unlock_ev hanako_goodend","unlock_ev hanako_goodend_muffin"),
                     ("thumb/lilly_tearoom.jpg","ev lilly_tearoom", "ev lilly_tearoom_open"),
                     ("thumb/lilly_touch.jpg","ev lilly_touch_uni", "ev lilly_touch_cheong", "ev lilly_touch_cas"),
                     ("thumb/lilly_crane.jpg","ev lilly_crane"),
                     ("thumb/lilly_bedroom.jpg","ev lilly_bedroom"),
                     ("thumb/lilly_hanako_hug.jpg","unlock_ev lilly_hanako_hug_end"),
                     ("thumb/lilly_sleeping.jpg","ev lilly_sleeping", "ev lilly_sleeping_smile"),
                     ("thumb/lilly_trainride.jpg","ev lilly_trainride","ev lilly_trainride_smiles","ev lilly_trainride_ni"),
                     ("thumb/lilly_wheat.jpg","unlock_ev lilly_wheat_close","ev lilly_wheat_small"),
                     ("thumb/lilly_handjob.jpg","evhunlock lilly_handjob_chest_frown_small","evhunlock lilly_handjob_chest_normal_small","evh lilly_handjob_stroke_flustopen_small","evh lilly_handjob_stroke_normopen_small","evh lilly_handjob_stroke_normshut_small"),
                     ("thumb/lilly_cowgirl.jpg","evh lilly_cowgirl_cry_small", "evh lilly_cowgirl_frown_small", "evh lilly_cowgirl_smile_small", "evh lilly_cowgirl_strain_small", "evh lilly_cowgirl_weaksmile_small"),
                     ("thumb/lilly_bath.jpg","evh lilly_bath_emb_small", "evh lilly_bath_grab_small", "evh lilly_bath_moan_small", "evh lilly_bath_open_small", "evh lilly_bath_smile_small"),
                     ("thumb/lilly_afterbath.jpg","evh lilly_afterbath_open_small", "evh lilly_afterbath_shut_small"),
                     ("thumb/lilly_kissing.jpg","ev lilly_kissing"),
                     ("thumb/lilly_masturbate.jpg","evh lilly_masturbate", "evh lilly_masturbate_come", "evh lilly_masturbate_come_face"),
                     ("thumb/lilly_restaurant.jpg","evul lilly_restaurant_listen", "evul lilly_restaurant_sheepish", "ev lilly_restaurant_eat", "ev lilly_restaurant_chew", "ev lilly_restaurant_wine"),
                     ("thumb/lilly_sheets.jpg","ev lilly_sheets"),
                     ("thumb/lilly_airport.jpg","ev lilly_airport", "ev lilly_airport_end"),
                     ("thumb/lilly_hospitalwindow.jpg","ev lilly_hospitalwindow"),
                     ("thumb/lilly_hospital.jpg", "unlock_ev lilly_hospitalclosed", "unlock_ev lilly_hospital"),
                     ("thumb/lilly_goodend.jpg", "unlock_ev lilly_goodend"),
                     ("thumb/rin_eating.jpg","ev rin_eating"),
                     ("thumb/rin_artclass.jpg", "ev rin_artclass1", "ev rin_artclass2", "ev rin_artclass3", "ev rin_artclass4"),
                     ("thumb/hisao_mirror.jpg","ev hisao_mirror_800"),
                     ("thumb/rin_painting.jpg","ev rin_painting_base", "ev rin_painting_foot", "ev rin_painting_faceconcerned", "ev rin_painting_concerned", "ev rin_painting_reply"),
                     ("thumb/rin_rain.jpg","ev rin_rain_away", "ev rin_rain_towards"),
                     ("thumb/rin_high.jpg","ev rin_high_frown", "ev rin_high_grin", "ev rin_high_grinwide", "ev rin_high_oneeye", "ev rin_high_open", "ev rin_high_smile", "ev rin_high_sleep"),
                     ("thumb/rin_kiss.jpg","ev rin_kiss"),
                     ("thumb/rin_nap.jpg","ev rin_nap_total", "ev rin_nap_total_awind", "ev rin_nap_close_awind", "ev rin_nap_close_awind_tears"),
                     ("thumb/rin_wisp.jpg", "ev rin_wisp1", "ev rin_wisp2", "ev rin_wisp3", "ev rin_wisp4", "ev rin_wisp5"),
                     ("thumb/rin_galleryskylight.jpg","ovl rin_galleryskylight"),
                     ("thumb/rin_orange.jpg","ev rin_orange", "ev rin_orange_large"),
                     ("thumb/rin_masturbate.jpg","ev rin_masturbate_away","ev rin_masturbate_surprise", "ev rin_masturbate_frown", "ev rin_masturbate_doubt", "ev rin_masturbate_hug"),
                     ("thumb/rin_relief.jpg","evh rin_relief_down", "evh rin_relief_up"),
                     ("thumb/rin_gallery.jpg", "ev rin_gallery"),
                     ("thumb/rin_trueend.jpg","ev rin_trueend_normal", "ev rin_trueend_smile", "ev rin_trueend_weaksmile", "ev rin_trueend_sad", "ev rin_trueend_closed", "ev rin_trueend_hug", "ev rin_trueend_hugclosed", "ev rin_trueend_gone"),
                     ("thumb/rin_wet.jpg", "ev rin_wet_pan_down", "ev rin_wet_arms", "ev rin_wet_face_up", "ev rin_wet_face_down", "ev rin_wet_towel_up", "ev rin_wet_towel_down", "ev rin_wet_towel_touch"),
                     ("thumb/rin_h2.jpg","unlock_evh rin_h2_pan_surprise", "unlock_evh rin_h2_pan_away", "unlock_evh rin_h2_pan_closed", "evh rin_h2_pan_closed", "evh rin_h2_nopan_closed", "evh rin_h2_hisao_closed"),
                     ("thumb/rin_pair.jpg","ev rin_pair_base_clothes","ev rin_pair_base"),
                     ("thumb/rin_h.jpg","evh rin_h_closed","evh rin_h_left","evh rin_h_normal","evh rin_h_right","evh rin_h_strain","evh rin_h_closed_close","evh rin_h_left_close","evh rin_h_normal_close","evh rin_h_right_close","evh rin_h_strain_close"),
                     ("thumb/rin_goodend.jpg","ev rin_goodend_1","ev rin_goodend_1b","ev rin_goodend_2"),
                     ("thumb/shizu_shanghai.jpg","ev shizu_shanghai", "ev shizu_shanghai_borednormal", "ev shizu_shanghai_smirknormal", "ev shizu_shanghai_smirklaugh"),
                     ("thumb/showdown.jpg","ev showdown"),
                     ("thumb/shizu_chess.jpg","ev shizu_chess_base", "ev shizu_chess_base3", "ev shizu_chess_base2"),
                     ("thumb/kenji_glasses.jpg", "evul kenji_glasses_closed", "evul kenji_glasses_frown", "evul kenji_glasses_normal"),
                     ("thumb/shizu_tanabata.jpg","ev shizutanabata"),
                     ("thumb/shizu_confess.jpg","ev shizuconfess_normal", "ev shizuconfess_closed", "ev shizuconfess_smile"),
                     ("thumb/shizu_hands.jpg","ev shizu_hands"),
                     ("thumb/shizu_couch.jpg","ev shizu_couch"),
                     ("thumb/shizune_car.jpg", "ev shizune_car"),
                     ("thumb/shizu_fishing.jpg","ev shizu_fishing_ah", "ev shizu_fishing_sl"),
                     ("thumb/shizune_tied.jpg","evh shizune_hcg_tied_blush_small", "evh shizune_hcg_tied_smile_small", "evh shizune_hcg_tied_stare_small", "evh shizune_hcg_tied_close_small", "evh shizune_hcg_tied_kinky1_small", "evh shizune_hcg_tied_kinky2_small", "evh shizune_hcg_tied_kinky3_small", "evhul shizune_hcg_tied_hisao2_small"),
                     ("thumb/misha_sad.jpg","ev misha_sad"),
                     ("thumb/misha_naked.jpg", "evh misha_naked"),
                     ("thumb/misha_sex.jpg","evh misha_sex_aside", "evh misha_sex_closed"),
                     ("thumb/misha_roof.jpg", "ev misha_roof_closed","ev misha_roof_angry","ev misha_roof_normal","ev misha_roof_sad"),
                     ("thumb/shizu_roof.jpg", "ev shizu_roof","ev shizu_roof_smile", "ev shizu_roof_towardsnormal", "ev shizu_roof_towardsangry", "ev shizu_roof2_towardsangry"),
                     ("thumb/shizu_flashback.jpg","ev shizu_flashback"),
                     ("thumb/shizu_undressing.jpg","evh shizu_undressing_clothed_stare", "evh shizu_undressing_clothed_kiss", "evh shizu_undressing_clothed_blush", "evh shizu_undressing_unclothed_blush", "evh shizu_undressing_unclothed_closed", "evh shizu_undressing_unclothed_kiss", "evh shizu_undressing_unclothed_talk"),
                     ("thumb/shizu_pushdown.jpg","evh shizu_pushdown"),
                     ("thumb/shizu_straddle.jpg","evh shizu_straddle_open", "evh shizu_straddle_tease", "evh shizu_straddle_closed","evh shizu_straddle_smile","evh shizu_straddle_come"),
                     ("thumb/shizu_table.jpg","evh shizu_table_smile","evh shizu_table_normal", "evh shizu_table_comeopen", "evh shizu_table_comeclosed"),
                     ("thumb/misha_nightclass.jpg","ev misha_nightclass"),
                     ("thumb/shizu_badend.jpg","ev shizu_badend"),
                     ("thumb/shizu_goodend.jpg", "ev shizu_goodend", "ev shizu_goodend_pan"),
                     ("thumb/cutin.png","pills","stuffedcat","teaset","shangpai", "wine", "musicbox closed", "musicbox open", "hanaphone", "phonestrap", "hanaphonestrap", "insert startpistol","invite", "sc_comp", "brailler", "chessboard", "kenjibox", "jigorocard", "letter_insert", "letter_open_insert", "letter_open_insert_2","stallphoto_insert"),
                     ("thumb/completionbonus.jpg","completionbonus"))






    image bg tearoom_lillyhisao_noon = "event/Lilly_supercg/tearoom_lillyhisao_noon.jpg"
    image bg tearoom_lillyhisao_sunset = "event/Lilly_supercg/tearoom_lillyhisao_sunset.jpg"

    image tearoom_hisao calm = "event/Lilly_supercg/tearoom_hisao_calm.png"
    image tearoom_hisao oops = "event/Lilly_supercg/tearoom_hisao_oops.png"
    image tearoom_hisao outside = "event/Lilly_supercg/tearoom_hisao_outside.png"
    image tearoom_hisao relief = "event/Lilly_supercg/tearoom_hisao_relief.png"
    image tearoom_hisao sigh = "event/Lilly_supercg/tearoom_hisao_sigh.png"
    image tearoom_hisao smile = "event/Lilly_supercg/tearoom_hisao_smile.png"
    image tearoom_hisao think = "event/Lilly_supercg/tearoom_hisao_think.png"
    image tearoom_hisao thinkclosed = "event/Lilly_supercg/tearoom_hisao_thinkclosed.png"
    image tearoom_hisao unsure = "event/Lilly_supercg/tearoom_hisao_unsure.png"

    image tearoom_lilly ara = "event/Lilly_supercg/tearoom_lilly_ara.png"
    image tearoom_lilly giggle = "event/Lilly_supercg/tearoom_lilly_giggle.png"
    image tearoom_lilly smileclosed = "event/Lilly_supercg/tearoom_lilly_smileclosed.png"
    image tearoom_lilly thinking = "event/Lilly_supercg/tearoom_lilly_thinking.png"
    image tearoom_lilly weaksmile = "event/Lilly_supercg/tearoom_lilly_weaksmile.png"

    image bg tearoom_everyone_noon = "event/Lilly_supercg/tearoom_everyone_noon.jpg"

    image tearoom_hanae happy = "event/Lilly_supercg/tearoom_hanae_happy.png"
    image tearoom_hanae open = "event/Lilly_supercg/tearoom_hanae_open.png"
    image tearoom_hanae sad = "event/Lilly_supercg/tearoom_hanae_sad.png"
    image tearoom_hanae shy = "event/Lilly_supercg/tearoom_hanae_shy.png"

    image tearoom_lillye ara = "event/Lilly_supercg/tearoom_lillye_ara.png"
    image tearoom_lillye giggle = "event/Lilly_supercg/tearoom_lillye_giggle.png"
    image tearoom_lillye smileclosed = "event/Lilly_supercg/tearoom_lillye_smileclosed.png"
    image tearoom_lillye thinking = "event/Lilly_supercg/tearoom_lillye_thinking.png"
    image tearoom_lillye weaksmile = "event/Lilly_supercg/tearoom_lillye_weaksmile.png"
    image tearoom_lillye smile = "event/Lilly_supercg/tearoom_lillye_smile.png"

    image tearoom_hisaoe calm = "event/Lilly_supercg/tearoom_hisaoe_calm.png"
    image tearoom_hisaoe outside = "event/Lilly_supercg/tearoom_hisaoe_outside.png"
    image tearoom_hisaoe sigh = "event/Lilly_supercg/tearoom_hisaoe_sigh.png"
    image tearoom_hisaoe thinkclosed = "event/Lilly_supercg/tearoom_hisaoe_thinkclosed.png"
    image tearoom_hisaoe hoops = "event/Lilly_supercg/tearoom_hisaoe_hoops.png"
    image tearoom_hisaoe hrelief = "event/Lilly_supercg/tearoom_hisaoe_hrelief.png"
    image tearoom_hisaoe hsmile = "event/Lilly_supercg/tearoom_hisaoe_hsmile.png"
    image tearoom_hisaoe hthink = "event/Lilly_supercg/tearoom_hisaoe_hthink.png"
    image tearoom_hisaoe hunsure = "event/Lilly_supercg/tearoom_hisaoe_hunsure.png"
    image tearoom_hisaoe loops = "event/Lilly_supercg/tearoom_hisaoe_loops.png"
    image tearoom_hisaoe relief = "event/Lilly_supercg/tearoom_hisaoe_relief.png"
    image tearoom_hisaoe lsmile = "event/Lilly_supercg/tearoom_hisaoe_lsmile.png"
    image tearoom_hisaoe lthink = "event/Lilly_supercg/tearoom_hisaoe_lthink.png"
    image tearoom_hisaoe lunsure = "event/Lilly_supercg/tearoom_hisaoe_lunsure.png"

    image tearoom_chess = "event/Lilly_supercg/tearoom_chess.png"



    image ev shizu_chess_large = "event/shizu_supercg/shizu_chess_large.jpg"
    image ev shizu_chess_base = "event/shizu_supercg/shizu_chess_base.jpg"
    image ev shizu_chess_base2 = "event/shizu_supercg/shizu_chess_base2.jpg"
    image ev shizu_chess_base3 = "event/shizu_supercg/shizu_chess_base3.jpg"

    image sc_shiz normal = im.Crop("event/shizu_supercg/shizu_chess_base3.jpg", 400, 0, 400, 600)






    python:
        def silhouette(disp, color=0):
            return im.Map(disp, rmap=im.ramp(color, color), gmap=im.ramp(color, color), bmap=im.ramp(color, color))

    image kenji silhouette = silhouette("sprites/kenji/kenji_neutral.png")
    image kenji silhouette_naked = silhouette("sprites/kenji/kenji_neutral_naked.png",10)
    image hanako silhouette = silhouette("sprites/hanako/hanako_basic_bashful.png")
    image rin silhouette = silhouette("sprites/rin/rin_relaxed_surprised.png")

    python:
        shizuepiccomp = im.Composite ((874,836),
                                  (0,0),sp_night("sprites/shizu/close/shizu_out_serious_close.png"),
                                  (2.5,600),sp_night("vfx/shizu_out_serious_legs.png"))

        shizuepiccomp_sil = im.Composite ((874,836),
                                  (0,0),silhouette("sprites/shizu/close/shizu_out_serious_close.png"),
                                  (2.5,600),silhouette("vfx/shizu_out_serious_legs.png"))

    image shizu epictransition:
        zoom 1.0 xalign 0.5 yalign 0.0
        parallel:
            shizuepiccomp
            pause 0.2
            shizuepiccomp_sil with Dissolve(1.8, alpha=True)
        parallel:
            ease 2.0 zoom 0.1 ypos 0.665

    image ksgallerybg = "ui/tc-neutral.png"

    image bloodred = Solid("#d00")
    image white = Solid("#fff")
    image pink = Solid("#FF7FD4")
    image videowhite = Solid("#FFFFFF")
    image videoblack = Solid("#0d0d0d")
    image darkgrey = Solid("#0D0D0D")
    image bg school_roof_ni_crop = im.Crop("bgs/school_roof_ni.jpg",200,0,800,600)
    image n_vignette = "vfx/narrowvignette.png"

    image fw_screen = Solid("#000000CC")

    image fakenvltextbox = "ui/bg-nvl.png"

    image hisaowindow = "vfx/hisaowindow.png"

    image alivetext = renpy.ParameterizedText(yalign=0.5, xanchor=0, xpos = 130, style="alive_text", drop_shadow=None, color="#666666")
    image alivetext_j = renpy.ParameterizedText(yalign=0.5, xanchor=0, xpos = 70, style="alive_text", drop_shadow=None, color="#666666")

    image bg mural_start = "vfx/mural_start.jpg"
    image bg mural_unfinished = "vfx/mural_unfinished.jpg"
    image bg mural_part = At("vfx/mural.jpg", Transform(xalign=0.0))
    image mural all = "vfx/mural_wide.jpg"
    image bg mural = "vfx/mural.jpg"
    image bg mural_ss = sunset("vfx/mural.jpg")
    image mural pan = At("vfx/mural.jpg",Fullpan(60.0, dir="left"))

    image rin_exhibition_paintings = At("vfx/rin_exhibition_paintings.jpg",Fullpan(40.0, dir="right"))
    image rin_exhibition_sold = "vfx/rin_exhibition_sold.jpg"
    image rin_exhibition_c = "vfx/rin_exhibition_c.jpg"

    transform shadowalpha:
        alpha 0.7

    image rin_shadow basic = At(silhouette("sprites/rin/close/rin_basic_deadpan_close.png"), shadowalpha)
    image rin_shadow negative = At(silhouette("sprites/rin/close/rin_negative_spaciness_close.png"), shadowalpha)

    image nightsky rotation:
        "bgs/misc_sky_ni.jpg"
        xalign 0.5 yalign 0.5 rotate 0 zoom 1.5 alpha 0.0
        parallel:
            linear 40 rotate 360
            repeat
        parallel:
            linear 10 zoom 3.0
        parallel:
            linear 5.0 alpha 1.0

    image cityscape zoom:
        "vfx/cityscape.png"
        xpos -0.25 ypos 1.0 xanchor 0.0 yanchor 0.0 zoom 1.5
        ease 2.0 xpos 0.0 ypos 1.0 xanchor 0.0 yanchor 1.0 zoom 1.0

    image hill enter:
        "vfx/hillouette.png"
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.0
        ease 2.0 xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0

    image hill pairtouch = "vfx/hillpair1.png"
    image hill pairnotouch = "vfx/hillpair2.png"

    image nightwash = "vfx/nightwash.png"

    python:
        def noisetile(bitmap, opacity=0.1):
            return im.Tile(im.Alpha(bitmap,opacity))

    image noiseoverlay:
        noisetile("vfx/noise1.png")
        pause 0.1
        noisetile("vfx/noise2.png")
        pause 0.1
        noisetile("vfx/noise3.png")
        pause 0.1
        repeat

    image comic vfx1 = "vfx/comic_vfx1.png"
    image comic vfx2 = "vfx/comic_vfx2.png"
    image comic vfx3 = "vfx/comic_vfx3.png"
    image comic vfx4 = "vfx/comic_vfx4.png"

    image ev emi_bed_full = LiveComposite((800,1280),
                                        (0,0),"event/emi_bed_normal.jpg",
                                        (0,600),"event/emi_bed_legs.jpg")

    image passoutOP1:
        Solid("#0000")
        Solid("#000") with ImageDissolve("ui/tr-flashback.png", 6.0, 32, alpha=True)


    image wine = "vfx/wine.png"
    image musicbox open = "vfx/musicbox_open.png"
    image musicbox closed = "vfx/musicbox_closed.png"
    image boxstrip = "vfx/boxstrip.png"
    image teaset = "vfx/teaset.png"
    image stuffedcat = "vfx/stuffedcat.png"
    image chessboard = "vfx/chessboard.png"
    image shangpai = "vfx/shangpai.png"
    image pills = "vfx/pills.png"
    image invite = "vfx/invite.png"
    image brailler = "vfx/brailler.png"
    image sc_comp = "vfx/sc_comp.png"
    image letter_insert = "vfx/letter_insert.png"
    image letter_open_insert = "vfx/letter_open_insert.png"
    image letter_open_insert_2 = "vfx/letter_open_insert_2.png"

    image hanaphone = "vfx/hanaphone.png"
    image phonestrap = "vfx/phonestrap.png"
    image hanaphonestrap = "vfx/hanaphonestrap.png"

    image kenjibox = "vfx/kenjibox.png"

    image jigorocard = "vfx/jigorocard.png"

    image stallphoto_insert = "vfx/stallphoto_insert.png"

    image lilly superclose = "vfx/lilly_superclose.png"
    image lilly superclose_ouch = "vfx/lilly_superclose_ouch.png"
    image lilly superclose_shock = "vfx/lilly_superclose_shock.png"


    image blanknote = "vfx/note_blur.png" 

    image lillyprop back_cane = "vfx/prop_lilly_back_cane.png"
    image lillyprop back_cane_close = "vfx/prop_lilly_back_cane_close.png"
    image lillyprop back_cane_ss = sp_sunset("vfx/prop_lilly_back_cane.png")
    image lillyprop back_cane_ni = sp_night("vfx/prop_lilly_back_cane.png")

    image bg gallery_atelier_bw = im.Grayscale("bgs/gallery_atelier.jpg")
    image bg school_scienceroom_bw = im.Grayscale("bgs/school_scienceroom.jpg")
    image bg school_library_bw = im.Grayscale("bgs/school_library.jpg")
    image bg city_street4_bw = im.Grayscale("bgs/city_street4.jpg")
    image bg city_street3_bw = im.Grayscale("bgs/city_street3.jpg")
    image bg school_council_bw = im.Grayscale("bgs/school_council.jpg")
    image bg school_dormhisao_bw = im.Grayscale("bgs/school_dormhisao.jpg")




    image fw_blank = Solid("#00000000")
    image fw_flash = Solid("#FFFFFF66")

    $ fw_dis_fast = Dissolve(0.04, alpha=True)
    $ fw_dis_medium = Dissolve(0.2, alpha=True)
    $ fw_dis_slow = Dissolve(3.0, alpha=True)
    $ fw_sparkle_out = ImageDissolve(im.Tile("vfx/tr-pronoise.png"), 3.0, 32, alpha=True)

    transform fw_constructor(my_image):
        "fw_blank"
        choice 15:
            0.2
        choice:
            "fw_flash" with fw_dis_fast
            0.2
            choice:
                my_image with fw_dis_medium
                "fw_blank" with fw_dis_slow
                6.0
            choice:
                my_image with fw_dis_medium
                "fw_blank" with fw_sparkle_out
                6.0

        repeat


    image fireworks = LiveComposite((800,600),
                                  (0,0), fw_constructor("vfx/fw1.png"),
                                  (0,0), fw_constructor("vfx/fw2.png"),
                                  (0,0), fw_constructor("vfx/fw3.png"),
                                  (0,0), fw_constructor("vfx/fw4.png"),
                                  (0,0), fw_constructor("vfx/fw5.png"),
                                  (0,0), fw_constructor("vfx/fw6.png"),
                                  (0,0), fw_constructor("vfx/fw7.png"),
                                  (0,0), fw_constructor("vfx/fw8.png"),
                                  (0,0), fw_constructor("vfx/fw9.png"))

    transform fw_constructor_nosparkle(my_image):
        "fw_blank"
        choice 15:
            0.2
        choice:
            "fw_flash" with fw_dis_fast
            0.2
            my_image with fw_dis_medium
            "fw_blank" with fw_dis_slow
            6.0
        repeat

    image fireshine = LiveComposite((800,600),
                                  (0,0), fw_constructor_nosparkle(Solid("#FF000009")),
                                  (0,0), fw_constructor_nosparkle(Solid("#00FF0009")),
                                  (0,0), fw_constructor_nosparkle(Solid("#0000FF09")),
                                  (0,0), fw_constructor_nosparkle(Solid("#CC00CC09")),
                                  (0,0), fw_constructor_nosparkle(Solid("#CCCC0009")),
                                  (0,0), fw_constructor_nosparkle(Solid("#0000CC09")))

    transform hanako_fw_constructor(in_r, in_g, in_b):
        alpha 0.0
        "fw_blank"
        choice 15:
            0.2
        choice:
            parallel:
                linear 0.04 alpha 1.0
                linear 3.0 alpha 0.0
            parallel:
                "fw_flash" with fw_dis_fast
                0.05
                im.MatrixColor("event/hanako_fw_flash.jpg", im.matrix.tint(in_r, in_g, in_b)) with fw_dis_medium
                8.0
        repeat

    image hanako_fw = LiveComposite((800,600),
                                    (0,0), hanako_fw_constructor(1.0, 1.0, 1.0),
                                    (0,0), hanako_fw_constructor(1.1, 0.9, 0.9),
                                    (0,0), hanako_fw_constructor(0.9, 1.1, 0.9),
                                    (0,0), hanako_fw_constructor(0.9, 0.9, 1.1),
                                    (0,0), hanako_fw_constructor(0.9, 1.05, 1.05),
                                    (0,0), hanako_fw_constructor(1.05, 0.9, 1.05),
                                    (0,0), hanako_fw_constructor(1.05, 1.05, 0.9))

    image ev hanako_shanghaiwindow = "event/hanako_fw.jpg"

    image bg school_library_yuuko_blurred = "vfx/school_library_yuuko_blurred.jpg"

    image phone mobile = "vfx/mobile-sprite.png"

    $ rain_trans = Dissolve(0.1, alpha=True)

    transform rainAnim_tf(my_offset, my_zoom, my_alpha):
        xalign 0.5 yalign 1.0 zoom my_zoom alpha my_alpha
        "fw_blank"
        my_offset
        block:
            choice:
                "vfx/fx-rain-bg1.png" with rain_trans
                0.2
            choice:
                "vfx/fx-rain-bg2.png" with rain_trans
                0.2
            choice:
                "vfx/fx-rain-bg3.png" with rain_trans
                0.2
            choice:
                "vfx/fx-rain-bg4.png" with rain_trans
                0.2
            choice:
                "vfx/fx-rain-bg5.png" with rain_trans
                0.2
            choice:
                "vfx/fx-rain-bg6.png" with rain_trans
                0.2
            repeat

    python:

        def rainAnim(my_offset=0.0, zoom=1.0, alpha=1.0):
            return rainAnim_tf(my_offset, zoom, alpha)


    image rain normal = LiveComposite((800, 600),
                             (0,0), rainAnim(),
                             (0,0), rainAnim(my_offset=0.1, zoom=1.2),
                             )


    image rain light = LiveComposite((800, 600),
                             (0,0), rainAnim(alpha=0.3),
                             (0,0), rainAnim(my_offset=0.1, zoom=1.2, alpha=0.3),
                             )

    image rain medium = LiveComposite((800, 600),
                             (0,0), rainAnim(alpha=0.6),
                             (0,0), rainAnim(my_offset=0.1, zoom=1.2, alpha=0.6),
                             )

    transform mm_widget_in(my_disp, my_delay):
        my_disp
        xalign 0.0 yanchor 0.0 ypos 0.2 subpixel True alpha 0.0
        my_delay
        easein 0.3 ypos 0.0 alpha 1.0



    $ crowdtrans = Dissolve(0.3, alpha=True)

    transform crowdgen(img1, img2, img3):
        img1
        block:
            1.0
            img2 with crowdtrans
            1.0
            img3 with crowdtrans
            1.0
            img1 with crowdtrans
            repeat

    image crowd = crowdgen("vfx/crowd1.png","vfx/crowd2.png","vfx/crowd3.png")
    image crowd_ss = crowdgen(sunset("vfx/crowd1.png"),sunset("vfx/crowd2.png"),sunset("vfx/crowd3.png"))
    image crowd_ni = crowdgen(night("vfx/crowd1.png"),night("vfx/crowd2.png"),night("vfx/crowd3.png"))
    image crowd_fb = crowdgen(past("vfx/crowd1.png"),past("vfx/crowd2.png"),past("vfx/crowd3.png"))
    image crowd_ni_fb = crowdgen(past_night("vfx/crowd1.png"),past_night("vfx/crowd2.png"),past_night("vfx/crowd3.png"))



init 5:
    image wallodrugs = drugsDisp(1600,800)

init python:



    def night(img_in):
        return im.MatrixColor(img_in, im.matrix.tint(0.6, 0.6, 0.7) * im.matrix.saturation(0.6))

    def sp_night(img_in):
        return im.MatrixColor(img_in, im.matrix.tint(0.9, 0.92, 1.0) * im.matrix.brightness(-0.05))

    def sunset(img_in):
        return im.MatrixColor(img_in, im.matrix.tint(1.1, 0.95, 0.85) * im.matrix.brightness(0.1) * im.matrix.saturation(1.2))

    def sp_sunset(img_in):
        return im.MatrixColor(img_in, im.matrix.tint(1.02, 0.95, 0.9) * im.matrix.brightness(0.05) * im.matrix.saturation(1.1))

    def past(img_in):
        return im.MatrixColor(img_in, im.matrix.saturation(0.15) * im.matrix.tint(1.0, .94, .76))

    def rain(img_in):
        return im.MatrixColor(img_in, im.matrix.saturation(0.4) * im.matrix.tint(0.95, 0.95, 1.0) * im.matrix.brightness(-0.1))

    def sp_rain(img_in):
        return im.MatrixColor(img_in, im.matrix.saturation(0.6) * im.matrix.tint(0.96, 0.96, 1.0) * im.matrix.brightness(-0.05))

    def past_night(img_in):
        return im.MatrixColor(img_in, im.matrix.tint(0.6, 0.6, 0.7) * im.matrix.saturation(0.6) * im.matrix.saturation(0.15) * im.matrix.tint(1.0, .94, .76))


    bg_filters = ((sunset,'ss'),
                  (night,'ni'),
                  (rain,'rn'),
                  )

    sp_filters = ((sp_sunset,'ss'),
                  (sp_night,'ni'),
                  (sp_rain,'rn'),
                  )





    letterbox = LiveComposite((800,600),
                              (0,0), Solid("#000", ymaximum=75),
                              (0,525), Solid("#000", ymaximum=75))
    renpy.image("letterbox",letterbox)



    flashback = ImageDissolve("ui/tr-flashback.png", 2.0, 32, reverse=True)
    flashforward = ImageDissolve("ui/tr-flashback.png", 2.0, 32)
    flashforward_fast = ImageDissolve("ui/tr-flashback.png", 0.5, 32)

    letter_in = ImageDissolve(im.Tile("ui/tr-letter.png"), 1.0, 8, reverse=True)
    letter_out = ImageDissolve(im.Tile("ui/tr-letter.png"), 1.0, 8)

    hands_in = ImageDissolve("vfx/handsdissolve.png", 0.2, ramplen=256, reverse=True)
    hands_out = ImageDissolve("vfx/handsdissolve.png", 0.2, ramplen=256)

    softwipedown = ImageDissolve(im.Tile("vfx/tr-wipeh.png"), 1.5, 16)
    softwipeup = ImageDissolve(im.Tile("vfx/tr-wipeh.png"), 1.5, 16, reverse=True)


    snowfg = SnowBlossom("vfx/snowflake.png", start=3.0, count=30, border=50, xspeed=(20, 50), yspeed=(120, 180), fast=True)
    snowbg = SnowBlossom(im.Scale("vfx/snowflake.png",5,5), count=60, yspeed=(80, 120), start=3.0, border=50, xspeed=(20, 50), fast=True)
    renpy.image("snow",LiveComposite((800,600),
                                     (0,0),snowbg,
                                     (0,0),snowfg))

    def GenericWhiteout(rise,hold,fall):
        return transition_attach_sound(Fade(rise, hold, fall, color="#FFF"), "sfx/whiteout.ogg")

    def SilentWhiteout(rise,hold,fall):
        return Fade(rise, hold, fall, color="#FFF")

    silentflash = Fade(0.25, 0,.75, color="#FFFFFF")
    flash = transition_attach_sound(silentflash, "sfx/flash.ogg")
    whiteout = GenericWhiteout(1.0,0.0,1.0)
    silentwhiteout = SilentWhiteout(1.0,0.0,1.0)

    cameraflash = Fade(0.05, 0.1 ,.75, color="#FFFFFF")
    cameraflashlong = Fade(0.05, 0.1 ,4.0, color="#FFFFFF")


    sakura = SnowBlossom(anim.Filmstrip("vfx/sakura.png", (10, 10), (2, 1), .25), xspeed=(150, 100), yspeed=(75, 150), count=80, fast=True)
    renpy.image("sakura", sakura)
    renpy.image("hospitalmask", "vfx/hospitalroommask_new.png")


    dandeliontfg = SnowBlossom("vfx/dandelion.png", count=10, border=25, xspeed=(100, 200), yspeed=(-40, -15), start=8.0, fast=False, horizontal=True)
    dandeliontbg = SnowBlossom(im.Scale("vfx/dandelion.png",13,16), count=20, border=25, xspeed=(50, 100), yspeed=(-30, -10), start=8.0, fast=False, horizontal=True)
    renpy.image("dandelions thin",LiveComposite((800,600),
                                    (0,0),dandeliontbg,
                                    (0,0),dandeliontfg))

    renpy.image("dandelionsfg thin",dandeliontfg)
    renpy.image("dandelionsbg thin",dandeliontbg)


    dandeliondfg = SnowBlossom("vfx/dandelion.png", count=20, border=25, xspeed=(100, 200), yspeed=(-40, -15), start=8.0, fast=True, horizontal=True)
    dandeliondbg = SnowBlossom(im.Scale("vfx/dandelion.png",13,16), count=40, border=25, xspeed=(50, 100), yspeed=(-30, -10), start=8.0, fast=True, horizontal=True)
    renpy.image("dandelions dense",LiveComposite((800,600),
                                    (0,0),dandeliondbg,
                                    (0,0),dandeliondfg))

    renpy.image("dandelionsfg dense",dandeliondfg)
    renpy.image("dandelionsbg dense",dandeliondbg)

    dandelionbg_blur = SnowBlossom(im.Scale("vfx/dandelion_blur.png",13,16), count=40, border=25, xspeed=(50, 100), yspeed=(-30, -10), start=8.0, fast=True, horizontal=True)
    renpy.image("dandelions_blurbg",dandelionbg_blur)

    dandelionfg_blur= SnowBlossom("vfx/dandelion_blur.png", count=20, border=25, xspeed=(100, 200), yspeed=(-40, -15), start=8.0, fast=True, horizontal=True)
    renpy.image("dandelions_blurfg",dandelionfg_blur)


    trans_dandelion = CropMove(5.0, "wipeleft")





    steam = anim.TransitionAnimation("vfx/steam1.png", 1.5, Dissolve(0.5, alpha=True),
                                     "vfx/steam2.png", 1.5, Dissolve(0.5, alpha=True),
                                     "vfx/steam3.png", 1.5, Dissolve(0.5, alpha=True))
    steam2 = anim.TransitionAnimation("vfx/steam3.png", 0.75, Dissolve(0.5, alpha=True),
                                     "vfx/steam1.png", 1.5, Dissolve(0.5, alpha=True),
                                     "vfx/steam2.png", 1.5, Dissolve(0.5, alpha=True),
                                     "vfx/steam3.png", 0.75, None)

    renpy.image("steam", steam)
    renpy.image("steam2", steam2)


    flashback = ImageDissolve(im.Tile("ui/tr-flashback.png"), 2.0, 32, alpha=True)
    clockwipe = ImageDissolve(im.Tile("ui/tr-clockwipe.png"), 2.0, 8)
    renpy.image("kslogo heart", "ui/bt-logolarge-heartonly.png")
    renpy.image("kslogo words", "ui/bt-logolarge.png")

    renpy.image("credits mask", "ui/roll_mask.png")

    runningspline = SplineMotion([
        ((0.470, 0.485,),),
        ((0.508, 0.525,), (0.484, 0.464,), (0.482, 0.541,),),
        ((0.518, 0.483,), (0.534, 0.512,), (0.532, 0.488,),),
        ((0.480, 0.528,), (0.506, 0.464,), (0.500, 0.544,),),
        ((0.470, 0.485,), (0.466, 0.520,), (0.452, 0.507,),),
        ], 1.1, anchors=(0.5, 0.5), repeat=True)

    fastrunningspline = SplineMotion([
        ((0.470, 0.485,),),
        ((0.508, 0.525,), (0.484, 0.464,), (0.482, 0.541,),),
        ((0.518, 0.483,), (0.534, 0.512,), (0.532, 0.488,),),
        ((0.480, 0.528,), (0.506, 0.464,), (0.500, 0.544,),),
        ((0.470, 0.485,), (0.466, 0.520,), (0.452, 0.507,),),
        ], 0.8, anchors=(0.5, 0.5), repeat=True)











    config.nvl_page_ctc = anim.Filmstrip("ui/ctc_strip.png", (16,16), (8,8), 0.03, ypos=560, xpos=772) 
    config.nvl_page_ctc_position = "fixed"


    def say_wrapper(who, what, **kwargs):
        store_current_line(who, what)
        return renpy.show_display_say(who, what, **kwargs)


    def change_quotes(what):
        innerwhat = what [1:-1]
        innerwhat = innerwhat.replace(displayStrings.quote_outer_open,displayStrings.quote_inner_open)
        innerwhat = innerwhat.replace(displayStrings.quote_outer_close,displayStrings.quote_inner_close)
        what = what[0] + innerwhat + what[-1]
        return what


    def quotefixer(who, what, **kwargs):
        return say_wrapper(who, change_quotes(what), **kwargs)

    def define_characters(): 
        
        add_styles = prefix_dict(displayStrings.styleoverrides, prefix="what_", combine=True)
        
        
        
        store.adv = ReadbackADVCharacter(name=None,
                                         ctc=config.nvl_page_ctc,
                                         ctc_position = "fixed",
                                         show_function=quotefixer,
                                         what_prefix=displayStrings.quote_outer_open,
                                         what_suffix=displayStrings.quote_outer_close,
                                         **add_styles)
        
        store.name_only = Character(None, kind=adv)
        
        
        
        store.hi = Character(displayStrings.name_hi, color="#629276")
        
        store.ha = Character(displayStrings.name_ha, color="#897CBF")
        store.emi = Character(displayStrings.name_emi, color = "#FF8D7C")
        store.rin = Character(displayStrings.name_rin, color = "#b14343")
        store.li = Character(displayStrings.name_li, color="#F9EAA0")
        store.shi = Character(displayStrings.name_shi, color="#72ADEE")
        store.mi = Character(displayStrings.name_mi, color="#FF809F")
        
        store.mi_shi = Character(displayStrings.name_shi, color="#FF809F")
        store.mi_not_shi = Character("{s}"+displayStrings.name_shi+"{/s} "+displayStrings.name_mi, color="#FF809F")
        
        store.ke = Character(displayStrings.name_ke, color="#CC7C2A")
        store.mu = Character(displayStrings.name_mu, color = "#FFFFFF")
        store.nk = Character(displayStrings.name_nk, color = "#FFFFFF")
        store.no = Character(displayStrings.name_no, color="#E0E0E0")
        store.yu = Character(displayStrings.name_yu, color="#2c9e31")
        store.sa = Character(displayStrings.name_sa, color="#D4D4FF")
        store.aki = Character(displayStrings.name_aki, color="#eb243b")
        store.hh = Character(displayStrings.name_hh, color="#6299FF")
        store.hx = Character(displayStrings.name_hx, color="#99AACC")
        store.emm = Character(displayStrings.name_emm, color="#995050")
        store.sk = Character(displayStrings.name_sk, color="#7187A8")
        store.mk = Character(displayStrings.name_mk, color="#AD735E")
        
        store.mystery = Character(displayStrings.name_mystery)
        
        
        
        store.ssh = Character(displayStrings.name_shi, kind=shi, what_prefix=u"[ ", what_suffix=u" ]")
        store.his = Character(displayStrings.name_hi, kind=hi, what_prefix=u"[ ", what_suffix=u" ]")
        
        
        store.ha_ = Character(displayStrings.name_ha_, kind=ha)
        store.emi_ = Character(displayStrings.name_emi_, kind=emi)
        store.rin_ = Character(displayStrings.name_rin_, kind=rin)
        store.li_ = Character(displayStrings.name_li_, kind=li)
        store.mi_ = Character(displayStrings.name_mi_, kind=mi)
        store.ke_ = Character(displayStrings.name_ke_, kind=ke)
        store.mu_ = Character(displayStrings.name_mu_, kind=mu)
        store.yu_ = Character(displayStrings.name_yu_, kind=yu)
        store.no_ = Character(displayStrings.name_no_, kind=no)
        store.sa_ = Character(displayStrings.name_sa_, kind=sa)
        store.aki_ = Character(displayStrings.name_aki_, kind=aki)
        store.nk_ = Character(displayStrings.name_nk_, kind=nk)
        store.hx_ = Character(displayStrings.name_hx_, kind=hx)
        store.hh_ = Character(displayStrings.name_hh_, kind=hh)
        store.emm_ = Character(displayStrings.name_emm_, kind=emm)
        
        
        
        
        store.n = ReadbackNVLCharacter(None,
                                       kind=nvl,
                                       ctc=anim.Blink(im.Rotozoom("ui/ctc.png", 270, 1.0),
                                       offset=1.0, ypos=560, xpos=772),
                                       ctc_position = "fixed",
                                       **add_styles)
        
        store.nb = Character(None,
                               kind=adv,
                               ctc=None,
                               what_color="#666666",
                               what_line_spacing=8,
                               what_prefix="",
                               what_suffix="",
                               show_function=say_wrapper,
                               window_style="b_nvl_window")
        
        store.rinbabble = Character(None,
                                    kind=n,
                                    what_prefix=u"{color=#FF8D7C}{b}"+displayStrings.name_rin+"{/b}{/color}\n" + displayStrings.quote_outer_open,
                                    what_suffix=displayStrings.quote_outer_close)
        
        
        
        
        
        
        store.narrator = Character(NARRATOR_NAME, what_prefix="", what_suffix="", show_function=say_wrapper)
        store.centered = Character(None, what_style="centered_text", window_style="centered_window", what_prefix="", what_suffix="", show_function=say_wrapper)
        store.centered_b = Character(None, kind=centered, what_color="#666666", what_drop_shadow=None, what_style="alive_text")
        store.centered_alive = Character(None, kind=centered_b, window_xpos=130, window_xanchor=0, window_xpadding=0)
        store.centered_alive_j = Character(None, kind=centered_b, window_xpos=70, window_xanchor=0, window_xpadding=0)




    dotwipe_down = ImageDissolve(im.Tile("ui/tr-dots_col.png"), 0.5, 32, ramptype="mcube")
    dotwipe_up = ImageDissolve(im.Tile("ui/tr-dots_col.png"), 0.5, 32, ramptype="mcube", reverse = True)
    slowfade = Fade(1.0, 0.5, 1.0)


    openeye = ImageDissolve("vfx/tr_eyes.png", 2.0, 64, ramptype="cube")
    shuteye = ImageDissolve("vfx/tr_eyes.png", 2.0, 64, ramptype="mcube", reverse=True)

    openeyefast = ImageDissolve("vfx/tr_eyes.png", 0.5, 64, ramptype="cube")
    shuteyefast = ImageDissolve("vfx/tr_eyes.png", 0.2, 64, ramptype="mcube", reverse=True)

    openeye_shock = ImageDissolve("vfx/tr-openshock.png", 0.8, 64, ramptype="cube")

    whip_right = ImageDissolve(im.Tile("vfx/tr-softwipe.png"), 0.3, 256, ramptype="mcube")
    whip_left = ImageDissolve(im.Tile("vfx/tr-softwipe.png"), 0.3, 256, ramptype="mcube", reverse = True)


    define.move_transitions("charamove", 1.0, _ease_time_warp, _ease_in_time_warp, _ease_out_time_warp)
    define.move_transitions("charamove_slow", 2.0, _ease_time_warp, _ease_in_time_warp, _ease_out_time_warp)
    define.move_transitions("charamove_old", 1.0, _ease_time_warp, _ease_in_time_warp, _ease_out_time_warp, old=True)

    define.move_transitions("ease_accel", 0.5, _ease_out_time_warp)
    define.move_transitions("ease_decel", 0.5, _ease_in_time_warp)

    define.move_transitions("slice_in", 0.2, _ease_in_time_warp)

    define.move_transitions("charamove_accel", 1.0, _ease_out_time_warp)
    define.move_transitions("charamove_decel", 1.0, _ease_in_time_warp)

    define.move_transitions("charafast", 0.2, _ease_time_warp, _ease_in_time_warp, _ease_out_time_warp)

    def Dissolvemove(time, time_warp=_ease_time_warp):
        top = Dissolve(time)
        before = MoveTransition(time, factory=MoveFactory(time_warp=time_warp), old=True)
        after = MoveTransition(time, factory=MoveFactory(time_warp=time_warp))
        return ComposeTransition(top, before=before, after=after)

    dissolvecharamove = Dissolvemove(1.0)

    delayed_dissolve = MultipleTransition([False,Dissolve(0.5),False,Dissolve(0.5),True])
    shownote = ComposeTransition(delayed_dissolve, None, charamoveinbottom)
    hidenote = ComposeTransition(Dissolve(0.5, alpha=True), charamoveoutbottom, None)

    delayblinds = ImageDissolve("vfx/tr-delayblinds.png", 1.0)

    delayblindsfade = MultipleTransition([False,SoundTransition("sfx/time.ogg"),False,delayblinds,Solid("#000"),delayblinds,True])
    delayblindsfadesilent = MultipleTransition([False,delayblinds,Solid("#000"),delayblinds,True])



    menueffect = None 
    charaenter = dissolve
    charaexit = dissolve
    charachange = dissolve
    characlose = dissolve
    charadistant = dissolve
    locationchange = dissolve
    locationskip = Fade(0.5, 0, 0.5)
    locationskip_in = Fade(0.5, 0, 0.0)
    locationskip_out = Dissolve(0.5)

    shorttimeskip = delayblindsfade
    shorttimeskipsilent = delayblindsfadesilent

    ex_m_tracks = []
    def ks_music(filename, alias):
        fullpath = "bgm/" + filename + ".ogg"
        setattr(store, "music_" + alias, fullpath)
        store.ex_m_tracks.append((filename.replace("_", " "), fullpath))





    ks_music("Afternoon", "tranquil")
    ks_music("Ah_Eh_I_Oh_You", "nurse")
    ks_music("Air_Guitar", "soothing")
    ks_music("Aria_de_l'Etoile", "twinkle")
    ks_music("Breathlessly", "moonlight")
    ks_music("Caged_Heart", "rain")
    ks_music("Cold_Iron", "tragic")
    ks_music("Comfort", "comfort")
    ks_music("Concord", "lilly")
    ks_music("Daylight", "daily")
    ks_music("Ease", "ease")
    ks_music("Everyday_Fantasy", "another")
    ks_music("Friendship", "friendship") 
    ks_music("Fripperies", "happiness")
    ks_music("Generic_Happy_Music", "comedy")
    ks_music("High_Tension", "tension")
    ks_music("Hokabi", "running")
    ks_music("Innocence", "innocence")
    ks_music("Letting_my_Heart_Speak", "heart")
    ks_music("Lullaby_of_Open_Eyes", "serene")
    ks_music("Moment_of_Decision", "drama")
    ks_music("Nocturne", "night")
    ks_music("Out_of_the_Loop", "kenji")
    ks_music("Painful_History", "hanako")
    ks_music("Parity", "rin")
    ks_music("Passing_of_Time", "timeskip")
    ks_music("Raindrops_and_Puddles", "dreamy")
    ks_music("Red_Velvet", "jazz")
    ks_music("Romance_in_Andante_II", "romance")
    ks_music("Romance_in_Andante", "credits")
    ks_music("Sarabande_from_BWV1010", "musicbox")
    ks_music("School_Days", "normal")
    ks_music("Shadow_of_the_Truth", "sadness")
    ks_music("Standing_Tall", "emi")
    ks_music("Stride", "pearly")
    ks_music("The_Student_Council", "shizune")
    ks_music("To_Become_One", "one")
    ks_music("Wiosna", "menus")




    config.main_menu_music = None
    config.enter_sound = None






    sfx_tcard = "sfx/tcard.ogg"
    sfx_4lslogo = "sfx/4lsaudiologo.ogg"
    sfx_alarmclock = "sfx/alarm.ogg"
    sfx_normalbell = "sfx/carillon.ogg"
    sfx_warningbell = "sfx/chaimu.ogg"
    sfx_crunchydeath = "sfx/crunch.ogg"
    sfx_fireworks = "sfx/fireworks.ogg"
    sfx_rain = "sfx/rain.ogg"
    sfx_rustling = "sfx/rustling.ogg"
    sfx_impact = "sfx/wumph.ogg"
    sfx_impact2 = "sfx/wumph_2.ogg"
    sfx_heartfast = "sfx/heart_single_fast.ogg"
    sfx_heartslow = "sfx/heart_single_slow.ogg"
    sfx_heartstop = "sfx/heart_stop.ogg"

    sfx_emijogging = "sfx/emijogging.ogg"
    sfx_emirunning = "sfx/emirunning.ogg"
    sfx_emipacing = "sfx/emipacing.ogg"
    sfx_emisprinting = "sfx/emisprinting.ogg"

    sfx_startpistol = "sfx/startpistol.ogg"
    sfx_crowd_indoors = "sfx/crowd_indoors.ogg"
    sfx_crowd_outdoors = "sfx/crowd_outdoors.ogg"
    sfx_crowd_cheer = "sfx/crowd_cheer.ogg"
    sfx_doorknock = "sfx/doorknock.ogg"
    sfx_doorknock2 = "sfx/doorknock2.ogg"
    sfx_doorslam = "sfx/doorslam.ogg"
    sfx_doorclose = "sfx/doorclose.ogg"

    sfx_cicadas = "sfx/cicadas.ogg"
    sfx_scratch = "sfx/scratch.ogg"
    sfx_traffic = "sfx/traffic.ogg"
    sfx_rumble = "sfx/rumble.ogg"
    sfx_skid = "sfx/skid2.ogg"
    sfx_gymbounce = "sfx/emibounce.ogg"
    sfx_hammer = "sfx/hammer.ogg"
    sfx_paper = "sfx/paperruffling.ogg"
    sfx_birdstakeoff = "sfx/birdstakeoff.ogg"
    sfx_storebell = "sfx/storebell.ogg"
    sfx_thunder = "sfx/thunder.ogg"
    sfx_slide = "sfx/slide.ogg"
    sfx_slide2 = "sfx/slide2.ogg"
    sfx_draw = "sfx/sword_draw.ogg"
    sfx_shower = "sfx/shower.ogg"
    sfx_switch = "sfx/switch.ogg"
    sfx_pillow = "sfx/pillow.ogg"
    sfx_cellphone = "sfx/cellphone.ogg"
    sfx_door_creak = "sfx/door_creak.ogg"
    sfx_dooropen = "sfx/dooropen.ogg"
    sfx_dropglasses = "sfx/dropglasses.ogg"
    sfx_can = "sfx/can.ogg"
    sfx_stallbuilding = "sfx/stallbuilding.ogg"
    sfx_parkambience = "sfx/parkambience.ogg"
    sfx_trainint = "sfx/trainint.ogg"

    sfx_footsteps_hard = "sfx/footsteps_hard.ogg"
    sfx_footsteps_soft = "sfx/footsteps_soft.ogg"
    sfx_paper = "sfx/paper.ogg"
    sfx_paperruffling = "sfx/paperruffling.ogg"
    sfx_rooftop = "sfx/rooftop.ogg"
    sfx_lighter = "sfx/lighter.ogg"
    sfx_phone = "sfx/phone.ogg"
    sfx_hollowclick = "sfx/hollowclick.ogg"
    sfx_businterior = "sfx/businterior.ogg"
    sfx_teacup = "sfx/teacup.ogg"
    sfx_can_clatter = "sfx/can_clatter.ogg"
    sfx_snap = "sfx/snap.ogg"

    sfx_billiards_break = "sfx/billiards_break.ogg"
    sfx_billiards = "sfx/billiards.ogg"
    sfx_lock = "sfx/lock.ogg"
    sfx_dropstuff = "sfx/dropstuff.ogg"
    sfx_camera = "sfx/camera.ogg"



    sfx_time = "sfx/time.ogg"
    sfx_flash = "sfx/flash.ogg"
    sfx_whiteout = "sfx/whiteout.ogg"

    vid_op = "base_op_1.mp4"
    vid_4ls = "video/base_4ls.mp4"

    ##If the platform is iOS, we override the vid_op and vid_4ls variables with the correct file name
    if (renpy.ios):
        vid_op = "ios_op_1.mp4"
        vid_4ls = "video/ios_4ls.mp4"

    config.screen_width = 800
    config.screen_height = 600

    ##Using software video decoding on Android, to allow for proper letterboxing
    config.hw_video = False
    ##Specific mobile port settings to reduce crashes, especially on low specs devices
    if (renpy.ios or renpy.android):
        config.cache_surfaces = False
        config.image_cache_size = 1
        config.hard_rollback_limit = 100
        ##Garbage Collector related stuff, pretty aggressive settings
        config.manage_gc = True
        config.gc_thresholds = (100, 5, 5)
        config.idle_gc_count = 100


    config.default_afm_enable = None

    _preferences.afm_time = 0
    if not persistent.afm_time:
        persistent.afm_time = 5

    config.default_fullscreen = False
    config.default_text_cps = 70
    config.has_sound = True
    config.has_music = True
    config.has_voice = False

    config.skip_indicator = False 

    config.window_icon = "ui/icon.png"

    config.enter_transition = dotwipe_down
    config.exit_transition = dotwipe_up
    config.intra_transition = dissolve
    config.main_game_transition = dotwipe_down
    config.game_main_transition = dotwipe_up
    config.end_splash_transition = None 
    config.end_game_transition = dotwipe_up
    config.after_load_transition = dotwipe_up

    config.window_show_transition = Dissolve(0.2)
    config.window_hide_transition = Dissolve(0.2)

    def wdt_hide(trans=dissolve):
        wdt_off()
        narrator("", interact=False)
        renpy.with_statement(None)
        renpy.with_statement(trans)

    def wdt_show(trans=dissolve):
        narrator("", interact=False)
        renpy.with_statement(trans)
        wdt_on()






    config.label_overrides = {"_noisy_return": "custom_noisy_return",
                              "_return": "custom_return",
                              "_confirm_quit": "quit_from_os",
                              "_game_menu": "_custom_game_menu"}




    def ib_base(image, **options): 
        return im.MatrixColor(image, im.matrix.opacity(0.4), **options)
    def ib_disabled(image, **options): 
        return im.MatrixColor(image, im.matrix.opacity(0.1), **options)


    style.default.font = mainfont


    def main_menu_composer(is_animated):
        
        if is_animated and store.animate_mm:
            is_animated = True
        else:
            is_animated = False
        
        
        is_animated = False
        
        widget_map = [('tc_act4_shizune', (677, 308), '16_tc4-shizune.png'),
                      ('tc_act3_shizune', (681, 383), '15_tc3-shizune.png'),
                      ('tc_act2_shizune', (620, 476), '14_tc2-shizune.png'),
                      ('tc_act4_rin', (526, 190), '13_tc4-rin.png'),
                      ('tc_act3_rin', (590, 232), '12_tc3-rin-rin.png'),
                      ('tc_act3_rin', (637, 295), '11_tc3-rin-hisao.png'),
                      ('tc_act2_rin', (629, 402), '10_tc2-rin.png'),
                      ('tc_act4_lilly', (464, 201), '09_tc4-lilly.png'),
                      ('tc_act3_lilly', (529, 279), '08_tc3-lilly.png'),
                      ('tc_act2_lilly', (582, 375), '07_tc2-lilly.png'),
                      ('tc_act4_hanako', (382, 279), '06_tc4-hanako.png'),
                      ('tc_act4_emi', (375, 370), '05_tc4-emi.png'),
                      ('tc_act3_emi', (429, 453), '04_tc3-emi.png'),
                      ('tc_act2_emi', (463, 498), '03_tc2-emi.png'),
                      ('tc_act3_hanako', (469, 312), '02_tc3-hanako.png'),
                      ('tc_act2_hanako', (493, 380), '01_tc2-hanako.png'),
                      ('tc_act1', (552, 473), '00_tc1-hisao.png')]
        
        basedelay = 0.07
        delay = basedelay * len (widget_map)
        widget_list = [(800,600), (0,0), "ui/main/bg-main.png", (720,568),Text(game_version+"\n"+renpy.version(),color="#00000080", size=9, font="font/playtime.ttf")]
        for trigger, offset, widget in widget_map:
            if persistent_seen(trigger) or has_devlvl():
                widget_list.append(offset)
                if is_animated:
                    widget_list.append(Fixed(mm_widget_in("ui/main/"+widget,delay), xmaximum=220, ymaximum=200))
                else:
                    widget_list.append("ui/main/"+widget)
                delay -= basedelay
        return LiveComposite(*widget_list), None

    def mm_live_bg(st,at):
        return main_menu_composer(True)

    def mm_static_bg(st,at):
        return main_menu_composer(False)

    renpy.image("mmcache",DynamicDisplayable(mm_static_bg))

    style.mm_root.background = DynamicDisplayable(mm_live_bg)
    style.create("mm_static", "mm_root")
    style.mm_static.background = DynamicDisplayable(mm_static_bg)

    style.mm_menu_frame.background = None

    style.mm_menu_frame.xanchor = 0.0
    style.mm_menu_frame.yanchor = 1.0 
    style.mm_menu_frame.xpos = 65

    style.mm_menu_frame.ypos = 540
    style.mm_button.background = None
    style.mm_button.xminimum = 0
    style.mm_button_text.xalign = 0

    style.mm_button_text.color = "#00000066"
    style.mm_button_text.insensitive_color = "#00000019"
    style.mm_button_text.hover_color = "#000000"

    style.prompt_text.color = "#00000066"


    style.create("rpa_button", "button")
    style.rpa_button.background = None
    style.create("rpa_button_text", "mm_button_text")

    style.create("rpa_active_button", "rpa_button")
    style.create("rpa_active_button_text", "rpa_button_text")
    style.rpa_active_button_text.insensitive_color = "#000000"



    style.say_window.background = "ui/bg-say.png"
    style.say_window.left_padding = 14
    style.say_window.right_padding = 30

    style.say_window.top_padding = 10
    style.say_window.xmargin = 0
    style.say_window.ymargin = 0
    style.say_window.yminimum = 160

    style.say_vbox.spacing = 15


    style.say_dialogue.first_indent = 14
    style.say_dialogue.rest_indent = 14

    style.say_dialogue['rollback'].color="#CCCCCC"


    style.centered_text.size = 26
    style.centered_text.outlines = [ (1,"#000C") ]

    style.create("alive_text", "centered_text")
    style.alive_text.outlines = []


    style.create("note_window", "centered_window")
    style.note_window.background=Frame("ui/bg-note.png", 0, 16, tile=True)
    style.note_window.xalign=0.5
    style.note_window.yalign=0.5
    style.note_window.top_padding=14
    style.note_window.left_padding=35
    style.note_window.right_padding=25
    style.note_window.xmaximum=402
    style.note_window.yfill = False
    style.note_window.xminimum=402

    style.create("note_text", "centered_text")
    style.note_text.size = 25
    style.note_text.outlines = []
    style.note_text.color = "#000244"
    style.note_text.text_align=0.0
    style.note_text.xalign=0.0
    style.note_text.yalign=0.0
    style.note_text.slow_cps = False
    style.note_text.layout = "greedy"

    style.nvl_window.background = "ui/bg-nvl.png"
    style.nvl_window.top_padding = 25


    style.say_window.left_padding = 14
    style.say_window.right_padding = 30

    style.create("b_nvl_window", "nvl_window")
    style.b_nvl_window.background = None
    style.b_nvl_window.top_padding = 140
    style.b_nvl_window.left_padding = 80

    style.menu_choice_button.background = "ui/bg-choice.png"
    style.menu_choice.take(style.mm_button_text)
    style.menu_choice.xalign = 0.5
    style.menu_choice.size = 20
    style.menu_choice_button.top_padding = 5

    style.hyperlink_text.color = "#F99"
    style.hyperlink_text.underline = False

    style.create("readback_text", "say_dialogue")
    style.readback_text.size= 16
    style.readback_text.color = "#00000066"
    style.create("readback_label", "readback_text")
    style.readback_label.bold = True

    style.create("comment_frame", "default")
    style.comment_frame.background = Frame("ui/bg-comment.png", 8,8,tile=True)
    style.comment_frame.xmargin = 4
    style.comment_frame.ymargin = 4
    style.comment_frame.xpadding = 16
    style.comment_frame.top_padding = 12
    style.comment_frame.bottom_padding = 18
    style.comment_frame.xminimum = 800

    style.create("comment_label", "say_label")

    style.create("comment_text", "say_dialogue")
    style.comment_text.first_indent = 0
    style.comment_text.rest_indent = 0



    style.gm_root.background = Solid("#0000007F") ##TODO: remove legacy dead code for gamemenu
    style.gm_root[None].background = None 
    style.gm_nav_frame.xalign = 0.5
    style.gm_nav_frame.yalign = 0.4
    style.gm_nav_frame.xminimum= 200
    style.gm_nav_frame.yminimum = 306
    style.gm_nav_frame.background = "ui/bg-gm.png"
    style.gm_nav_frame.top_padding = 62
    style.gm_nav_box.xalign = 0.5
    style.gm_nav_box.yalign = 0.5
    style.gm_nav_box.spacing = -1
    style.gm_nav_button.take(style.mm_button)
    style.gm_nav_button_text.take(style.mm_button_text)
    style.gm_nav_button.xalign = 0.5
    style.gm_nav_button_text.xalign = 0.5




    style.yesno_frame = Style(style.menu_frame, help="frame containing a yes/no prompt and yes/no buttons")
    style.yesno_frame_vbox = Style(style.vbox, help="box separating yes/no prompt from yes/no buttons")

    style.yesno_prompt = Style(style.prompt, help="a yes/no prompt")
    style.yesno_prompt_text = Style(style.prompt_text, help="a yes/no prompt (text)")

    style.yesno_button_hbox = Style(style.hbox, help="the box separating yes and no buttons")
    style.yesno_button = Style(style.button, help="a yes or no button")
    style.yesno_button_text = Style(style.button_text, help="a yes or no button (text)")


    style.yesno_frame.xfill = True
    style.yesno_frame.ypadding = .05

    style.yesno_frame_vbox.xalign = 0.5
    style.yesno_frame_vbox.yalign = 0.5
    style.yesno_frame_vbox.box_spacing = 30

    style.yesno_button_hbox.xalign = 0.5
    style.yesno_button_hbox.spacing = 100

    style.yesno_button.size_group = "yesno"

    style.yesno_frame.xalign = 0.5
    style.yesno_frame.yalign = 0.5
    style.yesno_frame.xmaximum = 331 

    style.yesno_frame.xmargin = 0
    style.yesno_frame.background = "ui/bg-popup.png"
    style.yesno_prompt.yminimum = 60
    style.yesno_prompt.color = "#00000066"
    style.yesno_button_hbox.box_spacing = 20
    style.yesno_button.background = None
    style.yesno_button_text.take(style.mm_button_text)
    style.yesno_button_text.xalign = 0.5



    style.file_picker_entry = Style(style.large_button, help="used to select a file to load or save")
    style.file_picker_entry_box = Style(style.hbox, help="the box inside a file picker entry")

    style.file_picker_text = Style(style.large_button_text, help="text inside a file picker entry")
    style.file_picker_empty_slot = Style(style.file_picker_text, help="text inside an empty file picker entry slot")
    style.file_picker_extra_info = Style(style.file_picker_text)
    style.file_picker_new = Style(style.file_picker_text)
    style.file_picker_old = Style(style.file_picker_text)

    style.file_picker_frame = Style(style.menu_frame, help="the frame enclosing the entire file picker")
    style.file_picker_frame_box = Style(style.vbox, help="the box containing the navbox and the grid of file picker entries")

    style.file_picker_navbox = Style(style.hbox, help="the box containing navigation buttons")

    style.file_picker_nav_button = Style(style.small_button, help="a file picker navigation button")
    style.file_picker_nav_button_text = Style(style.small_button_text, help="file picker navigation button text")

    style.file_picker_grid = Style(style.default, help="a grid containing file picker navigation buttons")


    style.file_picker_entry.xminimum = 0.5

    style.file_picker_frame.xmargin = 6
    style.file_picker_frame.ymargin = 6

    style.file_picker_frame_box.box_spacing = 4
    style.file_picker_entry_box.box_spacing = 4

    style.file_picker_frame.background = None
    style.file_picker_frame.xalign = 0.5
    style.file_picker_frame.yalign = 0.42
    style.file_picker_frame.xmaximum = 480
    style.file_picker_navbox.xalign = 0.5
    style.file_picker_new.bold = True
    style.file_picker_new.color = "#00000066"
    style.file_picker_new.hover_color = "#000000"
    style.file_picker_old.color = "#00000066"
    style.file_picker_old.hover_color = "#000000"
    style.file_picker_extra_info.color = "#00000066"
    style.file_picker_extra_info.line_spacing = 5
    style.file_picker_extra_info.hover_color = "#000000"
    style.file_picker_empty_slot.color = "#00000066"
    style.file_picker_empty_slot.hover_color = "#000000"
    style.file_picker_entry.xfill=False
    style.file_picker_entry.xminimum=380
    style.file_picker_entry.background = ib_base("ui/bt-scribble.png")
    style.file_picker_entry.hover_background = "ui/bt-scribble.png"
    style.file_picker_entry.top_padding = 3

    style.vscrollbar.thumb_offset = -10
    style.vscrollbar.ymaximum = 250
    style.vscrollbar.xmaximum = 24
    style.vscrollbar.top_gutter = 15
    style.vscrollbar.bottom_gutter = 14
    style.vscrollbar.top_bar = ib_base("ui/bt-vscrollbar.png")
    style.vscrollbar.hover_top_bar = "ui/bt-vscrollbar.png"
    style.vscrollbar.bottom_bar = ib_base("ui/bt-vscrollbar.png")
    style.vscrollbar.hover_bottom_bar = "ui/bt-vscrollbar.png"
    style.vscrollbar.thumb = ib_base("ui/bt-vscrollthumb.png")
    style.vscrollbar.hover_thumb = "ui/bt-vscrollthumb.png"

    style.create("vscrollbar_disabled", "vscrollbar")
    style.vscrollbar_disabled.top_gutter = 0
    style.vscrollbar_disabled.top_bar = ib_disabled("ui/bt-vscrollbar.png")
    style.vscrollbar_disabled.hover_top_bar = ib_disabled("ui/bt-vscrollbar.png")
    style.vscrollbar_disabled.bottom_bar = ib_disabled("ui/bt-vscrollbar.png")
    style.vscrollbar_disabled.hover_bottom_bar = ib_disabled("ui/bt-vscrollbar.png")
    style.vscrollbar_disabled.thumb = None
    style.vscrollbar_disabled.hover_thumb = None

    style.create("vscrollbar2", "vscrollbar")
    style.vscrollbar2.ymaximum = 224
    style.vscrollbar2.top_bar = ib_base("ui/bt-vscrollbar2.png")
    style.vscrollbar2.hover_top_bar = "ui/bt-vscrollbar2.png"
    style.vscrollbar2.bottom_bar = ib_base("ui/bt-vscrollbar2.png")
    style.vscrollbar2.hover_bottom_bar = "ui/bt-vscrollbar2.png"

    style.create("vscrollbar2_disabled", "vscrollbar2")
    style.vscrollbar2_disabled.top_gutter = 0
    style.vscrollbar2_disabled.top_bar = ib_disabled("ui/bt-vscrollbar2.png")
    style.vscrollbar2_disabled.hover_top_bar = ib_disabled("ui/bt-vscrollbar2.png")
    style.vscrollbar2_disabled.bottom_bar = ib_disabled("ui/bt-vscrollbar2.png")
    style.vscrollbar2_disabled.hover_bottom_bar = ib_disabled("ui/bt-vscrollbar2.png")
    style.vscrollbar2_disabled.thumb = None
    style.vscrollbar2_disabled.hover_thumb = None



    style.prefs_frame = Style(style.default, help="the frame containing all of the preferences")
    style.prefs_frame_box = Style(style.default, help="the box inside the frame containing all of the preferences")

    style.prefs_pref_frame = Style(style.menu_frame, help="a frame containing a single preference")
    style.prefs_pref_box = Style(style.vbox, help="the box separating the preference label from the preference choices")
    style.prefs_pref_choicebox = Style(style.vbox, help="the box containing the preference choices")

    style.prefs_label = Style(style.label, help="a preference label (window)")
    style.prefs_label_text = Style(style.label_text, help="a preference label (text)")

    style.prefs_button = Style(style.radio_button, help="preference value button")
    style.prefs_button_text = Style(style.radio_button_text, help="preference value button (text)")

    style.prefs_slider = Style(style.slider, help="preference value slider bar")

    style.prefs_volume_box = Style(style.vbox, help="box containing a volume slider and soundtest button")
    style.prefs_volume_slider = Style(style.prefs_slider, help="volume slider bar")

    style.soundtest_button = Style(style.small_button, help="soundtest button")
    style.soundtest_button_text = Style(style.small_button_text, help="soundtest button (text)")

    style.prefs_jump = Style(style.prefs_pref_frame, help="jump preference frame")
    style.prefs_jump_button = Style(style.button, help="jump preference button")
    style.prefs_jump_button_text = Style(style.button_text, help="jump preference button (text)")



    style.create('gallery_nav_vbox', 'vbox')
    style.create('gallery_nav_button', 'mm_button')
    style.create('gallery_nav_button_text', 'mm_button_text')

    style.gallery_nav_button_text.selected_color = "#000"
    style.gallery_nav_button.xmargin = 2
    style.gallery_nav_button.xpadding = 4


    style.create('gallery_pager_desc', 'gallery_nav_button_text')
    style.gallery_pager_desc.color = "#00000066"



    style.prefs_column = Style(style.vbox, help="preference columns")
    style.prefs_left = Style(style.prefs_column, help="the left preference column")
    style.prefs_center = Style(style.prefs_column, help="the center preference column")
    style.prefs_right = Style(style.prefs_column, help="the right preference column")


    style.prefs_pref_frame.xfill = True
    style.prefs_column.xanchor = 0.5

    style.prefs_pref_box.box_spacing = 12

    style.prefs_column.xmaximum = 250
    style.prefs_column.box_spacing = 10
    style.prefs_frame.top_margin = 10

    style.prefs_left.xpos = 137
    style.prefs_center.xpos = 400
    style.prefs_right.xpos = 663

    style.prefs_slider.xmaximum = 200

    style.prefs_pref_box.xfill = True
    style.prefs_volume_box.xfill = True
    style.prefs_pref_choicebox.xfill = True
    style.prefs_button.xalign = 1.0
    style.prefs_jump_button.xalign = 1.0
    style.prefs_slider.xalign = 1.0
    style.soundtest_button.xalign = 1.0

    style.prefs_button.size_group = "prefs"
    style.prefs_jump_button.size_group = "prefs"

    style.prefs_pref_frame.background = None
    style.prefs_pref_frame.bottom_margin = 0
    style.prefs_button.take(style.mm_button)
    style.prefs_button_text.take(style.mm_button_text)
    style.prefs_label.take(style.yesno_prompt)
    style.prefs_label.yminimum = None
    style.prefs_label.xalign = 0.0
    style.prefs_label_text.take(style.prompt_text)

    style.prefs_slider.clear()
    style.prefs_slider.left_bar = ib_base("ui/bt-cf-bar-left.png")
    style.prefs_slider.hover_left_bar = "ui/bt-cf-bar-left.png"
    style.prefs_slider.right_bar = ib_base("ui/bt-cf-bar-right.png")
    style.prefs_slider.hover_right_bar = "ui/bt-cf-bar-right.png"
    style.prefs_slider.thumb = ib_base("ui/bt-cf-thumb.png")
    style.prefs_slider.hover_thumb = "ui/bt-cf-thumb.png"
    style.prefs_slider.left_gutter = 12
    style.prefs_slider.right_gutter = 12
    style.prefs_slider.xmaximum = 200
    style.prefs_slider.thumb_offset = -3

    style.create("page_caption", "prefs_label")
    style.page_caption.bold = True




    if not persistent.hdisabled:
        persistent.hdisabled = False

    if not persistent.emi:
        persistent.emi = 0
    if not persistent.emibad:
        persistent.emibad = 0

    if not persistent.hanako:
        persistent.hanako = 0
    if not persistent.hanakosad:
        persistent.hanakosad = 0
    if not persistent.hanakorage:
        persistent.hanakorage = 0

    if not persistent.lilly:
        persistent.lilly = 0
    if not persistent.lillybad:
        persistent.lillybad = 0

    if not persistent.shizune:
        persistent.shizune = 0
    if not persistent.shizunebad:
        persistent.shizunebad = 0

    if not persistent.rin:
        persistent.rin = 0
    if not persistent.rinbad:
        persistent.rinbad = 0
    if not persistent.rintrue:
        persistent.rintrue = 0

    if not persistent.bad:
        persistent.bad = 0

    if (not persistent.seen_videos) or not ('video/base_4ls.mp4' or 'video/ios_4ls.mp4') in persistent.seen_videos:
        if not renpy.ios:
            persistent.seen_videos = ['video/base_4ls.mp4']
        else:
            persistent.seen_videos = ['video/ios_4ls.mp4']


    def init_vars():
        
        store.attraction_fail = 0
        store.attraction_sc = 0
        store.attraction_lilly = 0
        store.attraction_hanako = 0
        store.attraction_rin = 0
        store.attraction_emi = 0
        store.attraction_shizune = 0
        store.attraction_kenji = 0
        store.seen_labels = []
        store.current_line = None
        store.breadcrumbs = []
        persistent.breadcrumbs = []

    init_vars()
    NARRATOR_NAME = "{color=#0000}#{/color} "
    _game_menu_screen = "gm_bare"
    suppress_window_after_timeskip = False
    suppress_window_before_timeskip = False
    prefs_looped = False
    playthroughflag = True
    devlvl = 0
    entered_from_game = False
    coming_from_prefs_sub = False
    gm_active = False
    quit_from_os_flag = False
    ask_to_quit = False
    last_visited_label = None
    last_scene_label = None
    gm_exit_to = None
    previous_language = None
    np_current_language = None
    may_afm = True
    animate_mm = True
    statechangesincesave = True
    from_splash = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
