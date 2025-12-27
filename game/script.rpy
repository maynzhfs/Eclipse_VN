label start:

    call s1_1_prologue
    
    return

label endGame:

    call stop_music(fade_time=2.0)
    call stop_ambience(fade_time=2.0)
    
    hide screen narator_screen with None
    hide all with None

    scene black with Dissolve(2.0)
    call narator("— T A M A T —", duration=5.0)
    return

label trueEnd:
    
    call stop_music(fade_time=2.0)
    call stop_ambience(fade_time=2.0)
    
    hide screen narator_screen with None
    hide all with None

    scene black with Dissolve(2.0)
    call narator("— INI TRUE ENDING —", duration=5.0)
    return

label neutralEnd:
    call stop_music(fade_time=2.0)
    call stop_ambience(fade_time=2.0)
    
    hide screen narator_screen with None
    hide all with None

    scene black with Dissolve(2.0)
    call narator("— INI NEUTRAL ENDING —", duration=5.0)
    return

label badEnd:
    call stop_music(fade_time=2.0)
    call stop_ambience(fade_time=2.0)
    
    hide screen narator_screen with None
    hide all with None

    scene black with Dissolve(2.0)
    call narator("— INI BAD ENDING —", duration=5.0)
    return