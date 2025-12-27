label s3_4:
    scene black

    show bulan sad at pos_left_f
    show senja normal at pos_right
    with default_chara_transition

    call talk ('bulan', 'Ja...', 'sad')
    call talk ('senja', 'kenapa lagi Bul?', 'normal')

    call talk ('bulan', 'aku bingung, aku kesel, Bumi kenapa sih makin hari makin gangguin terus. kemaren dia ngajak aku ngobrol, tapi rasanya kayak aku yang di ceramahin', 'sad')
    call talk ('senja', 'gini Bul, sekarang-sekarang perkataan yang lagi sering keluar itu lewat perasaan nya, wajar aja karena dia sedang cemburu denganmu', 'normal')

    call talk ('bulan', 'tapi kan kenapa loh harus sampai kayak begini', 'sad')
    call talk ('senja', 'itu kan sesuatu diluar kendali kamu, sekarang aku mau tanya, kamu merasa terganggu ga dengan dia yang seperti itu?', 'normal')

    call talk ('bulan', 'iya Ja...', 'sad')

    call talk ('senja', 'kalau saran aku, kamu perlu cut-off sama dia. supaya dia sadar dan belajar', 'normal')
    call talk ('bulan', 'tapi Ja, kayak.. dia juga temen aku dan udah banyak bantu aku juga, emng ga ada ya jalan lain?', 'sad')

    call talk ('senja', 'menurutku agak susah Bul, karena kamu mau tetep sama Hari dengan keadaan Bumi begitu', 'normal')
    call talk ('bulan', 'tapi aku sebenarnya masih pengen temenan sama Bumi, gimanapun dia tetep temen aku', 'sad')

    call talk ('senja', 'kalau kamu pengennya seperti itu yaudah gapapa coba aja, tapi ya, kalau saran aku di cut-off aja, karena itu yang baik buat kamu dan buat dia juga')
    call talk ('senja', 'Tapi Bul, kalau kamu maksa semuanya baik-baik aja… ')
    call talk ('senja', 'Biasanya… yang paling capek itu kamu sendiri.')

    jump s3_5
