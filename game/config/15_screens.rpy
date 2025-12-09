screen narator_screen(text_to_display, duration=5.0):
    modal True
    zorder 100 
    style_prefix "narator"

    default hide_action = [Hide('narator_screen', Dissolve(0.5)), Return()]

    timer duration action hide_action 
    
    textbutton "":
        area (0, 0, 1.0, 1.0) 
        background None
        hover_background None
        focus_mask None
        action hide_action 

    frame:
        xalign 0.5
        yalign 0.5
        xsize 0.8
        ysize 0.8
        background None 

        text text_to_display:
            xalign 0.5
            yalign 0.5
            text_align 0.5
            size 48
            color "#ffffff" 
            font gui.text_font

    key "K_RETURN" action hide_action 
    key "K_SPACE" action hide_action 