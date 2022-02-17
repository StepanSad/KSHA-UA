init:
    
    

    screen say(who, what):
        style_prefix "say"
        vbox:
            xalign 0.5
            yalign 1.0
            if who != " ":
                vbox:
                    # python:
                    #     t = Text(what)
                    #     t.render(1920,1080,1,1)
                    #     vl = t.get_virtual_layout()
                    #     tw = vl.size[0]
                    #     if tw < 1136:
                    #         tw = 1136
                    #     th = vl.size[1]
                    #     if th < 100:
                    #         th = 100
                    #     th = th*2
                    #     if th > 228:
                    #         th = 228
                    #     print(int(tw), int(th))
                    frame:
                        # xsize int(tw/2.7)
                        # ysize int(th)
                        text who id "who"
                        
                            
                            
            vbox:
                frame:

                    id "window"
                    text what id "what"


    #     ## If there's a side image, display it above the text. Do not display on the
    #     ## phone variant - there's no room.
    #     if not renpy.variant("small"):
    #         add SideImage() xalign 0.0 yalign 1.0


    style say_window:
        xminimum 1136
        yminimum 155
        xfill persistent.sayxfill
        background Frame("ui/bg-saybox.png")
    
    style say_frame:
        xminimum 300
        yminimum 100
        # ysize say_window.xsize
        # ypos 0.58
        # xpos -0.06
        
        # left_padding 0.1
        # yanchor -0.5
        background Frame("ui/bg-saybox.png")
    



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
            background Frame("ui/bg-config.png")
            xpadding 20
            ypadding 20

            $ ui.textbutton("Close", clicked=Function(hideTextOptions), xalign = 1.0, yalign = 1.0, style = "button")
            
            vbox:
                vbox:
                    python:
                        widgetysize = 30
                        if not persistent.sayxfill:
                            checkboximage = "ui/bt-cf-unchecked.png"
                        else:
                            checkboximage = "ui/bt-cf-checked.png"
                        ui.text(displayStrings.config_fontsize_label, style='prefs_label')
                        textsize_p.render_preference()
                        widget_button(displayStrings.config_sayXfill_label, checkboximage, enableXfill, xsize=600, ysize=widgetysize, widgetyoffset=-8, textxoffset=40)
                


style button:
    background None
    size 36
style button_text:
    size 36
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
