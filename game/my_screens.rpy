init:
    
    

    screen say(who, what):
        
        style_prefix "say"
        vbox:
            xalign 0.5
            yalign 1.0
            if who != " " and who is not None:
                vbox:
                    python:
                        t = Text(what)
                        t.render(1920,1080,1,1)
                        vl = t.get_virtual_layout()
                        tw = vl.size[0]
                        if tw < 1136:
                            tw = 1136
                        th = vl.size[1]
                        if th < 100:
                            th = 100
                        th = th*2
                        if th > 228:
                            th = 228
                    frame:
                        style "nameBox"
                        xsize int(tw/2.7)
                        ysize int(th)
                        xpadding int(tw*0.03)
                        text who id "who"
                            
                            
            vbox:
                
                frame:

                    id "window"
                    text what id "what"

    style centered_window:
        xalign 0.5
        xfill True
        xpadding 10
        yalign 0.5
        yfill True
    
    style centered_text:
        layout "subtitle"
        outlines [(1, "#000C")]
        text_align 0.5
        xalign 0.5
        yalign 0.5 



    style say_window:
        xminimum 1136
        xmaximum 1890
        yminimum 155
        xmargin 0
        ymargin 0
        left_padding 30
        right_padding 65
        top_padding 10 #22
        xfill False
        background Frame("ui/bg-saybox.png")
    
    style nameBox:
        xminimum 300
        yminimum 100
        xpos -0.055
        ypos 0.6
        background Frame("ui/bg-namebox.png")
    


    screen nvl(dialogue, items=None):

        window:
            style "nvl_window"

            has vbox:
                style "nvl_vbox"

            # Display dialogue.
            for d in dialogue:
                window:
                    id d.window_id

                    has hbox:
                        spacing 10

                    if d.who is not None:
                        text d.who id d.who_id

                    text d.what id d.what_id

    style nvl_window:
        background "ui/bg-nvl.png"
        top_padding 59
        left_padding 55
        right_padding 70

    style b_nvl_window:
        background None
        top_padding 140
        left_padding 100
        right_padding 100


    screen dspeak(char0, char1, msg0, msg1=False):
        python:
                global current_line
                speaker=dict()
                ctc=dict()
                for (n, char) in enumerate((char0,char1)):
                    if hasattr(char,"name"):
                        if hasattr(char,"dynamic") and char.dynamic == True:
                            myname = eval(char.name)
                        else:
                            myname = char.name
                        if hasattr(char,"who_args") and "color" in char.who_args:
                            speaker[n] = "{color="+char.who_args["color"]+"}"+myname+"{/color}"
                        else:
                            speaker[n] = myname
                    else:
                        speaker[n] = str(char)
                    if hasattr(char,"display_args") and "ctc" in char.display_args:
                        ctc[n] = char.display_args["ctc"]
                    else:
                        ctc[n] = config.nvl_page_ctc
                
                msg0 = char0.what_prefix + msg0 + char0.what_suffix
                if not msg1:
                    msg1 = msg0
                else:
                    msg1 = char1.what_prefix + msg1 + char1.what_suffix
                
                current_line = None
                if msg0 == msg1:
                    store_say(speaker[0] + " & " + speaker[1], msg0)
                else:
                    store_say(speaker[0], msg0)
                    store_say(speaker[1], msg1)
        $ui.textbutton("aaa", clicked=Function(Return), xsize=1920, ysize=1080)

            
                  
              
        window:
            style "dwrapper"
            # background "black"
            # # background None
            # # xfill True
    
            
            
            grid 2 1:
                xspacing 20
                # background None
                xalign 0.5
                yalign 1.0
                # xsize 1890
                vbox:
                    # xsize 1890
                    frame:
                        xsize int(925*0.6)
                        yminimum 228
                        text speaker[0]:
                            style "say_label"
                            
                            # **displayStrings.styleoverrides
                    frame:
                        # xsize 0.5
                        xsize 925
                        yminimum 155
                        text msg0:
                            slow True
                            style "say_dialogue"
                            # **displayStrings.styleoverrides
                vbox:
                    # xsize 1890
                    # xalign 0.6
                    frame:
                        xsize int(925*0.6)
                        yminimum 228
                        text speaker[1]:
                            style "say_label"
                            # **displayStrings.styleoverrides
                    frame:
                        xsize 925
                        yminimum 155
                        text msg1:
                            slow True
                            style "say_dialogue"
                            # **displayStrings.styleoverrides
        # image (ctc[1]):
        #     ypos 0.5
    style dwrapper:
        xfill True
        yfill True
        # background "black"
                
                
            

                    




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

                label _(displayStrings.yesno_quit):
                    style "confirm_prompt"
                    # xalign 0.5

                hbox:
                    xalign 0.5
                    spacing 40

                    textbutton _(displayStrings.yesno_yes) action yes_action
                    textbutton _(displayStrings.yesno_no) action no_action
        
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

            $ui.textbutton (displayStrings.XstringClose, clicked = Function(hideTextOptions), xalign = 1.0, yalign = 1.0)
                
            
            vbox:
                python:
                    if not persistent.sayXsize:
                        checkboximage = "ui/bt-cf-unchecked.png"
                    else:
                        checkboximage = "ui/bt-cf-checked.png"
                    
                    ui.text(displayStrings.config_fontsize_label, style='prefs_label')

                    ui.hbox()
                    textsize_p.render_preference()

                    ui.text(str(persistent.fontsize), style='prefs_label')
                    ui.close()
                    stringXFill= displayStrings.Xfill_label
                    widget_button(stringXFill, checkboximage, enableXfill, xsize=600, ysize=30, widgetyoffset=-8, textxoffset=40)
            


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
