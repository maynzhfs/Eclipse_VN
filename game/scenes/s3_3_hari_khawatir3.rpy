label s3_3_hari_khawatir3:
    scene black 

    call narator ("Bulan masih terdiam di tempat duduknya itu, kemudian Hari menghampirinya")

    scene pagi_belakang_kampus

    show bulan sad at pos_left
    show hari sad at pos_right

    call talk ('hari', 'Bul, gimana tadi?')
    show bulan sad at pos_left_f
    call talk ('bulan', 'Ri.. aku...', 'sad')

    call talk ('hari', 'sini coba cerita gimana aja tadi', 'sad')
    
    scene black

    call narator ("Bulan menghela nafasnya panjang, dan mulai menceritakan satu persatu apa yang baru saja terjadi antara dia dengan Bumi.")

    scene pagi_belakang_kampus

    show hari normal at pos_right
    show bulan sad at pos_left_f

    call talk ('bulan', 'katanya yang dia bilang itu semua nya demi aku', 'sad')
    call talk ('hari', 'tapi aku ga terima cara dia nyampein itu ke kamu', 'sad')
    call talk ('hari', 'dan dia ga berhak buat ngatur hidup kamu', 'sad')

    call talk ('bulan', 'terus gimana?', 'sad')
    call talk ('bulan', 'aku bingung, aku capek, tapi aku...', 'sad')

    call talk ('hari', 'Bul, sini dengerin aku sebentar', 'sad')
    call talk ('hari', 'aku bakal disini, dan aku ga bakal ninggalin kamu cuman karena kamu bingung', 'sad')
    call talk ('hari', 'Tapi aku juga ga bisa liat kamu nyakitin diri kamu sendiri, dan jujur aja, aku juga sakit liat kamu kayak gitu', 'sad')

    '(Bulan menoleh)'

    call talk ('bulan', 'maksud kamuu gimana?')

    call talk ('hari', 'kamu ga bisa terus maksa buat nyenengin semua orang')
    call talk ('hari', 'dan jangan sampai kamu menyia-nyiakan itu, Bul')
    call talk ('hari', 'karena akupun belum tentu kuat')

    '(Hari menarik nafas panjang)'

    call talk ('hari', 'aku ada disini disamping kamu, buat nemenin kamu')
    call talk ('hari', 'bukan buat jadi korban')
    
    call talk ('hari', 'kalau kamu butuh diam, aku temenin')
    call talk ('hari', 'kalau kamu butuh waktu, aku tungguin')
    call talk ('hari', 'tapi tolong, jangan sampai kamu bikin aku terpaksa untuk pergi')

    'untuk pertama kalinya, Bulan sadar'
    'bahkan orang yang paling peduli pun punya batas'
    'dan batas itu sekarang ada di tanganku'

    hide bulan hari
    with default_chara_transition

    jump s3_4
