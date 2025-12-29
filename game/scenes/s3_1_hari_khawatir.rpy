label s3_1_hari_khawatir:
    scene black

    call narator ('Beberapa hari telah berlalu, Bulan dan Hari semakin dekat, dan Bulan mulai melupakan apa yang kemarin-kemarin Bumi lakukan. Yaa, dia mencoba mengganggap itu cuman angin yang berlalu')
    call narator ('Dan seperti biasa, setelah kelas berakhir aku menemui Hari yang udah menunggu di koridor kampus')

    scene koridor_kampus

    show hari happy at pos_right
    show bulan normal at pos_left_f

    call talk ('hari', 'Udah beres kelas?', 'normal')
    call talk ('bulan', 'Udahh~', 'happy')

    call talk ('hari', 'Gimana tadi kelasnya?', 'normal')
    call talk ('bulan', 'Capekkk, aku pengen istirahat dulu, enaknya dimana ya', 'normal')

    call talk ('hari', 'Hmm, mau ke cafe?')
    call talk ('bulan','Mauuu')

    'Akhirnya mereka memutuskan untuk pergi ke cafe, tempat dimana mereka biasa menghabiskan harinya bersama'
    'Tapi, sesampainya mereka di parkiran...'

    show hari normal at pos_left
    show bulan normal at pos_far_left 
    with chara_move_transition
    show bumi normal at pos_far_right 
    with default_chara_transition

    call talk ('bumi', 'Bulan, sekarang lagi kosong? ada yang ingin aku bicarakan. Ini penting, bukan obrolan singkat.')

    menu:
        "(eh, mau ngomongin apa ya dia?)":
            jump s3_1_langsung
        "(aku kan mau ke cafe sama Hari)":
            jump s3_1_nantiaja

label s3_1_langsung:

    show bulan at pos_far_left_f
    call talk ('bulan', 'Mau ngomongin apa ya?')
    call talk ('bumi', 'Kita bicara di taman belakang kampus, aku tunggu disana')

    hide bumi normal with default_chara_transition

    call talk ('hari', 'Bul, kalau ada apa-apa aku ada disini, jadi jangan terlalu maksain diri ya')
    call talk ('bulan', 'Iya Hari, makasih ya')

    jump s3_2_bumi_ribut2

label s3_1_nantiaja:

    show bulan at pos_far_left_f
    call talk ('bulan', 'Kayaknya ga bisa sekarang deh, aku mau pergi dulu. Kalau besok aja gimana?')
    call talk ('bumi', 'Kalau gitu, besok pagi kita ketemu di taman belakang kampus', 'sad')

    hide bumi normal with default_chara_transition

    call talk ('hari', 'Kamu yakin besok mau dateng?','sad')
    call talk ('bulan', 'Iya Hari, kenapa emangnya?')

    call talk ('hari', 'Gapapa Bul, jangan maksain diri ya, kalau ada apa-apa aku disini')
    call talk ('bulan', 'Iya Hari, makasih ya')

    jump s3_2_bumi_ribut3