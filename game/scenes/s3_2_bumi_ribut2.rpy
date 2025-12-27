label s3_2_bumi_ribut2:

    scene black
    call narator ('sesampainya Bulan di taman belaang kampus. Bulan melihat Bumi sedang duduk sendiri di sebuah bangku taman, dan Bulan langsung datang menghampirinya')

    scene sore_belakang_kampus
    show bulan normal at pos_right
    show bumi normal at pos_far_left_f

    call talk ('bulan', 'Jadi kamu mau ngomong apa?', 'sad')

    '(Bumi menatap Bulan cukup lama sebelum bicara.)'

    call talk ('bumi', 'Aku bakal bilang ini berkali-kali, Bul.')
    call talk ('bumi', 'Kamu harus hati-hati sama Hari.')

    call talk ('bulan', 'Hati-hati kenapa?!', 'angry')

    call talk ('bumi', 'Karena dia bukan orang yang baik buat kamu!', 'angry')
    call talk ('bumi', 'Dan kamu harusnya tau itu!', 'angry')

    call talk ('bulan', 'Bukannya kamu aja ga begitu deket sama Hari? Terus kamu kenal dia darimana?', 'angry')

    '(Bumi menarik napas, lalu mulai bicara panjang.)'

    call talk ('bumi', 'Aku nggak perlu deket sama dia.')
    call talk ('bumi', 'Karena aku kenal kamu', 'sad')
    call talk ('bumi', 'Aku tau kamu yang gampang percaya sama orang', 'sad')
    call talk ('bumi', 'Aku tau kamu yang selalu berusaha ngertiin orang lain', 'sad')
    call talk ('bumi', 'Bahkan sampai kamu lupa sama diri kamu sendiri', 'sad')


    call talk ('bumi', 'Makanya aku ngomong kayak gini supaya kamu tau dan kamu sadar', 'sad')
    call talk ('bumi', 'Supaya kamu ga salah ambil ambil jalan', 'sad')

    '(Bulan terdiam, tidak menjawab)'

    call setExpr('bulan', 'sad')

    call talk ('bumi', 'Aku temen kamu Bul..', 'sad')
    call talk ('bumi', 'Aku peduli sama kamu', 'sad')

    call talk ('bumi', 'Kamu nggak perlu deket sama dia.', 'sad')
    call talk ('bumi', 'Aku nggak mau kamu ngulang kekecewaan yang sama.', 'sad')

    call talk ('bumi', 'Bul, kalau kamu terus sama dia, kamu bakal nyesel', 'sad')

    'hening sejenak'
    '(Bulan menunduk. Tangannya mengepal, lalu mengendur. Ia tidak berkata apa-apa.)'

    call talk ('bumi', '...', 'sad')
    call talk ('bumi', 'Kamu dengerin aku, kan?', 'sad')

    '(Bulan tetap diam)'

    call talk ('bulan', '(Kepalaku penuh.)', 'sad')
    call talk ('bulan', '(Bukan karena aku nggak ngerti…)', 'sad')
    call talk ('bulan', '(tapi karena aku terlalu capek buat merespons.)', 'sad')

    call talk ('bumi', 'Kamu tau kan aku ngomong gini karena aku peduli', 'sad')

    call talk ('bulan', 'Bisa tolong tinggalin aku disini? kepalaku pusing.', 'sad')

    call talk ('bumi', 'baiklah, tapi aku harap kamu dengerin semua perkataanku dari awal', 'sad')

    hide bumi normal with default_chara_transition

    '(Bumi pergi meninggalkan taman.)'
    '(Bulan masih berdiri di tempat. Sendiri.)'

    jump s3_3_hari_khawatir2