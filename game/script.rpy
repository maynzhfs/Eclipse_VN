label start:

    call s01_prologue
    
    return

label endGame:

    call stop_music(fade_time=2.0)
    call stop_ambience(fade_time=2.0)
    
    hide screen narator_screen with None
    hide all with None

    scene black with Dissolve(2.0)
    call narator("— T A M A T —", duration=5.0)
    return