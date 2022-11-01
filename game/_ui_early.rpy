define multipersistent = MultiPersistent("com.fls.katawashoujo") #Defining multipersistence to fix the ending not playing bug


python early:
    import copy
    config.save_directory = "katawashoujo_actual_1.3" 
    game_version = "Katawa Shoujo v1.3.1"




    def parse_jump_in(l):
        is_expr = False
        firstword = l.word()
        if firstword == "expression":
            label = l.simple_expression()
            is_expr = True
        else:
            label = firstword
        if not label:
            renpy.error("parse error when evaluating custom jump")
        if l.rest():
            renpy.error("custom jump statement includes superfluous syntax: " + l.rest())
        return dict(label=label,is_expr=is_expr)

    def execute_jump_in(p):
        global save_name, last_scene_label
        if p["is_expr"]:
            label = eval(p["label"])
        else:
            label = p["label"]
        last_scene_label = label
        save_name = label
        scene_register(label)
        renpy.jump(label)

    def predict_jump_in(p):
        return []

    def next_jump_in(p):
        return p["label"]

    def lint_jump_in(p):
        label = p["label"]
        if not label:
            renpy.error("no target given to custom jump statement.")
        if not renpy.has_label(label) and not p["is_expr"]:
            renpy.error("custom jump to nonexistent label.")

    def execute_jump_out(p):
        global playthroughflag, mycontext, ss_desc
        nvl_clear()
        if not playthroughflag:
            replay_end()
        execute_jump_in(p)

    renpy.statements.register('jump_in',
                              parse=parse_jump_in,
                              execute=execute_jump_in,
                              predict=predict_jump_in,
                              lint=lint_jump_in,
                              next=next_jump_in)

    renpy.statements.register('jump_out',
                              parse=parse_jump_in,
                              execute=execute_jump_out,
                              predict=predict_jump_in,
                              lint=lint_jump_in,
                              next=next_jump_in)

    def replay_end():
        config.skipping = None
        renpy.scene()
        renpy.transition(config.main_game_transition)
        mycontext = "mm"
        ss_desc = ""
        wdt_off()
        renpy.music.stop(fadeout=0.5)
        renpy.music.play(music_menus, fadein=5.0, fadeout=0.5, if_changed=True)
        renpy.full_restart(label="invoke_scene_select")
        return



    m1, m2, m3, m4, m5, m6, m7, m8 = "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"
    rp_actmark = "##separator##"

    def replay_has_seen(label):
        
        global playthroughflag
        return not playthroughflag and persistent_seen(label)

    def persistent_seen(label):
        return label in persistent.seen_labels

    def name_from_label(label):
        for (name, mylabel, display, path) in s_scenes:
            if mylabel == label:
                return name
        return False

    def wrap_label(label):
        
        desired_target = persistent.current_language+"_"+label
        if renpy.has_label(desired_target):
            return desired_target
        else:
            return master_language+"_"+label

    def scene_register(inlabel, persistent_only=False):
        
        global seen_labels
        if not inlabel in persistent.seen_labels:
            persistent.seen_labels.append(inlabel)
        if not persistent_only:
            seen_labels.append(inlabel)

    def seen_scene(label): 
        
        return label in seen_labels

    def made_choice(label, choice):
        
        return seen_scene((label, choice))


    @renpy.atl_warper
    def acdc_warp_simple(x):
        n = 10.0 
        masterscale = n/(n-1)
        
        if (x < (1.0/n)):
            xmod = x*(n/2.0)
            res = (((2.0/n) * _ease_time_warp(xmod)) / 2.0) * masterscale
        
        elif (x > (1.0 - (1.0/n))):
            xmod = 1.0-(((x-1)*n)/2.0)
            res = (((2.0/n) * _ease_time_warp(xmod) / 2.0) + (1 - (2.0/n))) * masterscale
        
        else:
            res = (x - (0.5/n)) * masterscale
        
        return res

    def acdc_generic(x,n):
        import math
        if (x < (1.0 / n)):
            res = (((2.0 / n) * (0.5 - math.cos(math.pi * (x * (n / 2.0))) / 2.0)) / 2.0) * (n / (n - 1.0))
        elif (x > (1.0 - (1.0 / n))):
            res = (((2.0 / n) * (0.5 - math.cos(math.pi * (1.0 - (((x - 1.0) * n) / 2.0))) / 2.0) / 2.0) + (1.0 - (2.0 / n))) * (n / (n - 1.0))
        else:
            res = (x - (0.5 / n)) * (n / (n - 1.0))
        return res

    @renpy.atl_warper
    def acdc_warp(x):
        return acdc_generic(x,10)

    @renpy.atl_warper
    def acdc20_warp(x):
        return acdc_generic(x,20)

init python:
    if not persistent.seen_labels:
        persistent.seen_labels = []
    seen_labels = []


label iscene(target, is_h=False, is_end=False):

    window show None
    if playthroughflag:
        $ scene_register(target)
    $ last_visited_label = target
    if not notextmode:
        if is_h and persistent.hdisabled:
            call scene_deleted (is_end) from _call_scene_deleted
        else:
            call expression wrap_label(target) from _call_expression
    window hide None
    return

label imenu(target):

    python:
        scene_register(target)
        last_visited_label = target
        renpy.music.set_volume(0.3, 1.0, "music")
        renpy.music.set_volume(0.3, 1.0, "ambient")
    call expression wrap_label(target) from _call_expression_1
    python:
        renpy.music.set_volume(1.0, 1.0, "music")
        renpy.music.set_volume(1.0, 1.0, "ambient")
        scene_register((target,_return))

    return _return

label invoke_scene_select:
    $ renpy.call_in_new_context("_main_menu", "scene_select")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
