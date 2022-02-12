init -500:

    style default:
        properties gui.text_properties()
    
    

    screen say(who, what):
        style_prefix "say"

        window:
            id "window"
            text what id "what"
            $ t = Text(what)
            # $ tw = int((t.size()[0]))
            # $ th = int((t.size()[1]))
            # $ print(str(tw) + ' ' + str(th))
            $ t.render(1920,1080,1,1)
            $ vl = t.get_virtual_layout()
            $ tw = vl.size[0]
            $ th = vl.size[1]
            $ print("width: " + str(tw)+ " h: "+ str(th))
            
        if who is not None:

                window:
                    # xpos 1920tw
                    # ypos th
                    
                    style "namebox"
                    text who id "who"


        ## If there's a side image, display it above the text. Do not display on the
        ## phone variant - there's no room.
        if not renpy.variant("small"):
            add SideImage() xalign 0.0 yalign 1.0

    style namebox is default

    style window:
        xminimum 1136
        xfill False
        yfill False
    
        # background 'ui/bg-saybox.png'

        
    # style namebox:
        # fixed
        # xpos tw
        # ypos th

    

    style say_label:
        properties gui.text_properties("name")
        # xalign 0.5
        # yalign 0.5
        

    style say_dialogue:
        properties gui.text_properties("dialogue")
    style say_dialogue:
        background 'ui/bg-saybox.png'



    screen confirm(message, yes_action, no_action):
        

        ## Ensure other screens do not get input while this screen is displayed.
        modal True

        zorder 200

        style_prefix "confirm"

        

        frame:
            background Frame("ui/bg-popup.png")
            xalign 0.5
            yalign 0.5
            xminimum 530
            yminimum 277

            vbox:
                xalign 0.5
                yalign 0.5
                xminimum 337
                yminimum 83
                # spacing 30

                label _("Are You Sure to \nquit Katawa Shoujo?"):
                    style "confirm_prompt"
                    # xalign 0.5

                hbox:
                    xalign 0.5
                    spacing 40

                    textbutton _("Yes") action yes_action
                    textbutton _("No") action no_action
        
        image ("ui/sd-hanako.png"):
            xpos 638
            ypos 492

        ## Right-click and escape answer "no".
        key "game_menu" action no_action


    style confirm_prompt:
        xminimum 337

    

    style confirm_prompt_text:
        # text_align 0.5
        size 35
        layout "tex"
    
    style confirm_button:
        background None

    style confirm_button_text:
        color "#00000066"
        hover_color "#000"
        insensitive_color "#00000019"
        size 42


    screen text_options:
        
        

        frame:
            xsize 908
            ysize 400
            background "#00000066"
            
            hbox:
                    python:
                        textsize_p.render_preference()

style bar:
    yminimum 200

style button:
    background None
style button_text:
    color "#00000066"
    hover_color "#000"
    insensitive_color "#00000019"



        

    
style opt_btn:
    background None
style opt_btn_text:
    color "#00000066"
    hover_color "#000"
    insensitive_color "#00000019"

style opt_imagebtn:
    xalign 0.2
    yalign 0.5
