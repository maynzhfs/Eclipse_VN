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
    call narator( 'Aku akhirnya mengerti. \n'
    'Meninggalkan bukan berarti kehilangan. \n'
    'Kadang, itu cuma caraku untuk tetap hidup… dan tetap mencintai. \n'
    , duration=5.0
    )
    return

label neutralEnd:
    call stop_music(fade_time=2.0)
    call stop_ambience(fade_time=2.0)
    
    hide screen narator_screen with None
    hide all with None

    scene black with Dissolve(2.0)
    call narator('Aku tidak memilih siapa pun. \n'
    'Aku memilih waktu. \n'
    '\n'
    'Bukan untuk menghilang. \n'
    'Tapi untuk bernapas. \n'
    , duration=5.0
    )
    return

label badEnd:
    call stop_music(fade_time=2.0)
    call stop_ambience(fade_time=2.0)
    
    hide screen narator_screen with None
    hide all with None

    scene black with Dissolve(2.0)
    call narator('Aku ingin menyatukan mereka.'
    'Tapi emosiku menghancurkan segalanya. \n'
    '\n'
    'Hari pergi karena hatinya patah. \n'
    'Bumi pergi karena aku yang mengusirnya. \n'
    '\n'
    'Dan untuk pertama kalinya… \n'
    'aku benar-benar sendirian. \n'
    , duration=5.0
    )
    return