label s3_5:
    scene black

    call narator ('Suara kota jauh. Angin pelan. Bulan sendirian.')

    show bulan sad at pos_center

    call talk ('bulan', 'Aku capek, \n' 
    'Dunia rasanya nyuruh aku memilih. \n'
    'Tapi aku malah ragu sama diri sendiri… aku masih kuat atau nggak.'
    , 'sad')
    
    hide bulan
    with default_chara_transition
    
    call narator ('Bulan menatap tangannya.')

    show bulan sad at pos_center

    call talk ('bulan', 'Setiap kali aku mendekat, ada yang terluka. \n' 
    'Setiap kali aku menjauh, ada yang merasa ditinggalkan. \n'
    , 'sad')
    
    hide bulan
    with default_chara_transition

    call narator ('(Notifikasi masuk — dari Hari. Tidak dibuka.)')
    call narator ('(Notifikasi masuk — dari Bumi. Tidak dibuka.)')

    show bulan normal at pos_center

    call talk ('bulan', 'Aku takut salah.', 'sad')
    call talk ('bulan', 'Jadi aku harus apa?...', 'sad')

    menu:
        "(aku ga mau milih siapa pun, aku cuma pengen semuanya baik-baik aja)":
            hide all with default_chara_transition
            jump s3_bad_ending
        "(apa aku ikutin aja ya nasihat senja? mungkin aku harus tegas, walaupun ada yang sakit?)":
            hide all with default_chara_transition
            jump s3_true_ending
        "(aku terlalu capek untuk milih, aku butuh waktu buat sendiri...)":
            hide all with default_chara_transition
            jump s3_netral_ending
    
