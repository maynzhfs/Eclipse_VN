label s3_netral_ending:
    scene pagi_depan_kost

    show bulan normal at pos_left_f
    show senja normal at pos_right
    with default_chara_transition

    call change_music("audio/Hopeful Happy Ending Music - Dawn of Life.mp3",fade_time = 2.0)

    call talk ('senja', 'Kamu keliatan beda hari ini.')

    call talk ('bulan', 'Aku cuman ngerasa…')
    call talk ('bulan', 'kalau aku terus maksa buat nyelesain semuanya sekarang,')
    call talk ('bulan', 'yang ada cuman bikin aku makin berantakan.')

    call talk ('senja', ' jadinya kamu mau gimana sekarang?')

    call talk ('bulan', 'aku kayaknya mau diem aja dulu', 'happy')
    call talk ('bulan', 'bukan buat apa-apa', 'happy')
    call talk ('bulan', 'cuman buat nunggu aja', 'happy')

    call talk ('senja', 'nunggu buat apa, Bul?')

    call talk ('bulan', 'nunggu buat diri aku sendiri')
    call talk ('bulan', 'aku cuman pengen biarkan ini berlalu aja karena waktu')
    call talk ('bulan', 'sampai pada waktu itu tiba, mungkin aku lebih siap buat memilih')

    '(mereka terdiam sejenak, membiarkan angin berhembus melewati mereka)'

    call talk ('senja', 'memang kadang, kita butuh waktu untuk diri sendiri')
    call talk ('senja', 'dan membiarkan sampai waktnya lewat sendiri')

    call talk ('bulan', '...')

    call talk ('bulan', 'Iya Ja..')
    call talk ('bulan', 'Aku masih terlalu berat buat milih sekarang, jadi yaa, biarkan waktu berlalu aja')

    jump neutralEnd