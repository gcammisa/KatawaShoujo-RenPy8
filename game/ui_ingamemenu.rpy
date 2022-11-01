init python:

    def menu(items, **add_input): 
        
        is_narrator = False
        newitems = []
        for label, val in items:
            if val == None:
                narrator(label, interact=False)
                is_narrator=True
            else:
                newitems.append((label, val))
        rv = custom_menu(newitems, is_narrator, **add_input)
        for label, val in items:
            if rv == val:
                store_say(None, ">> " + label)
        return rv

    def custom_menu(items, is_narrator, window_style='menu_window', interact=True, with_none=None, **kwargs):
        """
        Displays a menu containing the given items, returning the value of
        the item the user selects.
    
        @param items: A list of tuples that are the items to be added to
        this menu. The first element of a tuple is a string that is used
        for this menuitem. The second element is the value to be returned
        if this item is selected, or None if this item is a non-selectable
        caption.
    
        @param interact: If True, then an interaction occurs. If False, no suc
        interaction occurs, and the user should call ui.interact() manually.
    
        @param with_none: If True, performs a with None after the input. If None,
        takes the value from config.implicit_with_none.
        """
        
        renpy.choice_for_skipping()
        
        location = renpy.game.context().current
        
        
        choices = [ val for label, val in items ]
        while None in choices:
            choices.remove(None)
        
        
        roll_forward = renpy.exports.roll_forward_info()
        
        if roll_forward not in choices:
            roll_forward = None
        
        
        
        for choice in persistent.breadcrumbs:
            if choice[0] == location:
                rval = choice[1]                
                renpy.ui.window(style=window_style, ypadding=40)
                show_menu(items, location=location, focus="choices", default=True, active=rval, **kwargs)
                ui.saybehavior(afm=generate_string(200))
                ui.interact(mouse='say', type="say", roll_forward=True)
                return rval
        
        if renpy.config.auto_choice_delay:    
            renpy.ui.pausebehavior(renpy.config.auto_choice_delay,
                                   random.choice(choices))
        
        
        renpy.ui.window(style=window_style, ypadding=40)
        show_menu(items, location=renpy.game.context().current, focus="choices", default=True, **kwargs)
        
        
        renpy.exports.shown_window()
        
        if interact:
            
            rv = renpy.ui.interact(mouse='menu', type="menu", roll_forward=roll_forward)
            
            renpy.checkpoint(rv)
            
            if with_none is None:
                with_none = renpy.config.implicit_with_none
            
            if with_none:
                renpy.game.interface.do_with(None, None)
            
            return rv
        
        return None

    def show_menu(menuitems,
             style = 'menu',
             caption_style='menu_caption',
             choice_style='menu_choice',
             choice_chosen_style='menu_choice_chosen',
             choice_button_style='menu_choice_button',
             choice_chosen_button_style='menu_choice_chosen_button',
             location=None,
             focus=None,
             default=False,
             active=None,
             **properties):
        
        
        
        renpy.random.shuffle(menuitems)
        
        ui.vbox(style=style, **properties)
        
        
        
        
        for label, val in menuitems:
            chosenbefore = False
            if val is None:
                pass
            
            else:
                
                text = choice_style
                button = choice_button_style
                
                if location:
                    chosen = renpy.game.persistent._chosen.setdefault(location, set())
                    if label in chosen:
                        chosenbefore = True
                    
                    def clicked(chosen=chosen, label=label, val=val):
                        chosen.add(label)
                        persistent.breadcrumbs.append((location,val))
                        return val
                else:
                    clicked = renpy.ui.returns(val)
                
                if active is not None:
                    ingamebutton_dead(label, val == active)
                else:
                    ingamebutton(label, clicked, chosenbefore)
        
        
        ui.close()


    def ingamebutton(text, clicked, previously=None):
        
        img = Fixed(Text(text, xalign=0.5, yalign=0.5, color="#000"), xmaximum=608)
        if previously:
            bgim = im.Composite(None,
                                (0,0), "ui/bg-choice.png",
                                (577,2), im.Alpha("ui/bt-cf-checked.png",0.5))
        elif previously is not None:
            bgim = im.Composite(None,
                                (0,0), "ui/bg-choice.png",
                                (577,2), im.Alpha("ui/bt-cf-unchecked.png",0.5))
        else:
            bgim = "ui/bg-choice.png"
        
        bg = Fixed(bgim, xmaximum=608)
        
        this_idle = LiveComposite((608,35),
                                  (0,0), ingm_bg(bg),
                                  (0,0), ingm_btn(img)
                                  )
        this_hover = LiveComposite((608,35),
                                  (0,0), ingm_bg(bg),
                                  (0,0), ingm_btn_hover(img)
                                  )
        
        ui.fixed(xpos=0.5, ymaximum=35, xmaximum=800)
        ui.imagebutton(this_idle, this_hover, clicked=clicked, style="default", xanchor=0.5, yanchor=0.5)
        ui.close()

    def ingamebutton_dead(text, is_active=False):
        
        clicked = None
        if is_active:
            img = Fixed(Text(text, xalign=0.5, yalign=0.5, color="#ccc"), xmaximum=608)
            bg = Fixed("ui/bg-choice_nochoice.png", xmaximum=608)
        else:
            img = Fixed(Text(text, xalign=0.5, yalign=0.5, color="#00000080"), xmaximum=608)
            bg = Fixed(im.MatrixColor("ui/bg-choice.png",im.matrix.desaturate()*im.matrix.brightness(-0.2)*im.matrix.opacity(0.3)), xmaximum=608)
        
        ui.fixed(xpos=0.5, ymaximum=35, xmaximum=800)
        ui.button(clicked=clicked, style="default", xanchor=0.5, yanchor=0.5)
        ui.image(ingm_bg(bg))
        ui.button(clicked=clicked, style="default", xanchor=0.5, yanchor=0.5)
        ui.image(ingm_bg(img))
        ui.close()

init:

    transform ingm_bg(disp):
        disp
        yalign 0.5 xalign 0.5 alpha 0.0 zoom 1.0 subpixel True
        0.5
        linear 0.5 alpha 1.0

    transform ingm_btn(disp):
        disp
        yalign 0.5 xalign 0.5 alpha 0.0 zoom 1.0 subpixel True
        0.5
        linear 0.5 alpha 0.4

    transform ingm_btn_hover(disp):
        disp
        yalign 0.5 xalign 0.5 alpha 0.0 zoom 1.0 subpixel True
        0.5
        linear 0.5 alpha 1.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
