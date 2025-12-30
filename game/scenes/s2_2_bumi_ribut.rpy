label s2_2_bumi_ribut:
    scene black

    call narator ("Bulan dan Hari sedang berjalan berdua di koridor kampus, tertawa dan bercanda. Tanpa sadar, ternyata dari kejauhan, Bumi memperhatikan mereka dengan tatapan tidak suka.")

    call stop_music()

    call narator ("Sementara itu, Bumi mempercepat langkahnya, berniat menghampiri Hari dan Bulan. Namun, Senja tiba-tiba saja datang dan menahannya")

    scene koridor_kampus
    show bumi angry at pos_left
    show senja normal at pos_right

    call play_music("audio/distant candle light.mp3", fade_time = 2.0)

    call setExpr ('bumi', 'angry')

    call talk ('senja', 'Bumi, kamu mau kemana?', 'sad')

    call talk ('bumi', ' bukan urusanmu, Senja', 'angry')

    call talk ('senja', 'Aku tahu kamu cemburu. Tapi tolong jangan ganggu Bulan lagi, dia juga udah bukan urusanmu', 'angry')

    "Bumi hanya menghiraukan perkataan Senja dan tetap melangkah"

    show bumi angry at pos_far_left with chara_move_transition

    call talk ('senja', 'Bumi dengar, dulu kamu yang dulu nyuruh dia untuk jaga jarak, kamu yang udah buat dia kecewa. Sekarang dia udah move on, buat apa kamu datang lagi?', 'angry')

    show bumi angry at pos_far_left with chara_move_transition
    call talk ('bumi', 'aku cuman mau dia tau dan sadar siapa yang terbaik buat dia', 'angry')

    call talk ('senja', 'yang terbaik buat dia itu yang ga pernah nyakitin perasaan dia', 'angry')

    hide bumi
    hide senja with default_chara_transition
    "Bumi tetap tak menghiraukan Senja dan terus melangkah menuju Bulan dan Hari. Senja hanya bisa menghela napas pasrah."

    "Bumi menghampiri Bulan dan Hari, senyum paksa terukir di wajahnya."
    
    show bumi normal at pos_far_right
    show bulan normal at pos_left
    show hari normal at pos_far_left

    call talk('bumi', 'Wah, diliat-liat kalian makin hari makin nempel aja. lagi ngapain nih?', 'angry') 

    show bulan at pos_left_f
    show hari at pos_far_left_f
    with chara_move_transition

    call talk('bulan', 'Eh, Bumi. Nggak ada apa-apa, kok. Cuma ngobrol biasa.', 'happy')

    call talk('hari', 'Iya, santai aja, Bumi.')

    call setExpr(['hari', 'bulan'], 'shock')
    call talk('bumi', 'Oh, gitu. Kirain lagi ngobrolin masa depan berdua~', 'angry')
    
    call setExpr(['hari', 'bumi'], 'angry')
    call talk('bulan', 'Apaan sih, Bumi. Ada apa kamu ke sini?', 'angry')
    
    call talk('bumi', 'Aku cuma mau ngingetin kamu, Bulan. Hati-hati sama orang baru. Belum tentu sebaik yang kamu kira.', 'angry')
    call talk('hari', 'Maksudmu apa, Bumi?', 'angry')
    call talk('bumi', 'Ya gada maksud apa-apa ko. intinya Bulan, jangan lupa sama yang pernah aku bilang dulu.', 'angry')
    call talk('bulan', 'Bumi, cukup! Jangan mulai.', 'angry')
    call talk('bumi', 'Aku cuma khawatir sama kamu, Bulan. Kamu itu gampang percaya sama orang.', 'angry')
    call talk('hari', 'Aku nggak akan bikin Bulan sakit hati. Kamu tenang aja.')
    call talk('bumi', 'Omongan doang gampang, bro. Buktiin nya gimana.', 'angry')

    call setExpr (['hari', 'bulan', 'bumi'], 'angry')
    'Suasana menjadi tegang. Bulan merasa tidak nyaman dengan situasi ini.'

    call talk('bulan', 'Udah, udah! Kenapa jadi gini sih? Bumi, kamu sebaiknya pergi.', 'angry')
    call talk('bumi', 'Aku pergi kalo kamu janji bakal mikirin omonganku.', 'angry')
    call talk('bulan', 'Aku udah punya keputusan sendiri.', 'angry')
    call talk('bumi', 'Oke. Aku bakal terus ingetin kamu sampai kamu sadar. Sampai ketemu, Bulan, Hari.', 'angry')


    hide bumi with default_chara_transition
    'Bumi pergi dengan tatapan penuh arti. Bulan menatap kepergian Bumi dengan perasaan campur aduk.'

    show hari at pos_left_f
    show bulan sad at pos_right_f
    with chara_move_transition

    show hari at pos_left_f
    show bulan sad at pos_right
    call talk('hari', 'Kamu gapapa Bulan?')
    call talk('bulan', 'Aku... aku nggak tahu, Ri. Kenapa Bumi jadi gini?', 'sad')
    call talk('hari', 'Dia cuma cemburu, Bul. Kamu jangan terlalu dipikirin. Aku ada di sini buat kamu.', 'happy')

    'Hari menggenggam tangan Bulan, mencoba menenangkannya. Bulan membalas genggaman tangan Hari, namun pikirannya masih kalut.'

    hide hari
    hide bulan

    with default_chara_transition

    jump s2_3_bulan_melamun