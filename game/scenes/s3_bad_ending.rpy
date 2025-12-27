label s3_bad_ending:
    scene black

    show senja normal at pos_left
    show bulan normal at pos_right
    with default_chara_transition

    call talk ('senja', 'Kamu yakin mau ngomong ke mereka berdua sekaligus?')
    call talk ('bulan', 'Kalau aku jujur… semuanya pasti baik-baik aja, kan?')

    call talk ('senja', '…Aku harap kamu benar.')

    hide senja bulan with default_chara_transition

    'akhirnya, Bulan menghubungi Bumi dan Hari dan mereka bertemu di koridor kampus. suasana ruangan terasa tegang'

    show bulan at pos_center
    show hari at pos_left
    show bumi at pos_far_right

    call talk ('bulan', 'Hari, Bumi, aku pengen bilang sesuatu')
    call talk ('bulan', 'Aku mau kalian tahu. Hari, kamu pacarku, dan Bumi, kamu tetep temenku. Aku nggak mau kehilangan kalian. Bisakah kita berteman baik saja?')

    call talk ('bumi', 'Berteman? Setelah semua ini? Bulan, kamu ga dengerin ya apa yang aku bilang kemarin?', 'angry')
    call talk ('hari', 'Bul, kamu nyuruh kita dateng tuh buat apa?')

    call talk ('bulan', 'Aku cuma mau kalian akur. Aku mau semuanya baik-baik aja.')

    call talk ('hari','Bul, Kamu sadar nggak sih, kamu lagi minta aku buat nerima semuanya sendirian?')

    call talk ('bulan', 'Aku cuma minta kamu ngerti, buat paham kalau keadaan nya tuh begini')

    call talk ('hari', 'Ngerti apa? Bahwa aku harus terus sakit demi ketenangan kalian? (Hari menghela napas panjang.)')

    call talk ('hari', 'kalau maumu begitu, Aku nggak sanggup, Bul, maaf.')

    hide hari with default_chara_transition

    call talk ('bulan', 'Hari… tunggu—!', 'sad')

    call talk ('bumi', 'harusnya dari awal kamu dengerin aku,dan ini ga bakal berakhir kayak gini')

    call talk ('bulan', ' Kenapa kamu harus ngomong gitu?!', 'sad')

    call talk ('bumi', 'Aku cuman bilang jujur')

    call talk ('bulan', 'Jujur? Sejak kapan perkataan kamu bikin keadaan jadi lebih baik?!')

    show bumi at pos_right
    with default_chara_transition

    call talk ('bumi', 'Kamu nggak baik-baik aja, Bulan.')

    call talk ('bulan', 'IYA! AKU MEMANG NGGAK BAIK-BAIK AJA!')
    call talk ('bulan', 'Dan kamu cuma bikin semuanya makin berat!')

    call talk ('bulan', 'Kalau kamu masih mau ngatur hidupku—')
    call talk ('bulan', 'PERGI AJA—')

    '(Bumi tersentak, dan akhirnya dia memutuskan untuk meninggalkan Bulan di tengah tangisannya yang mulai pecah)'

    hide bumi with default_chara_transition

    show bulan sad at pos_center

    jump badEnd