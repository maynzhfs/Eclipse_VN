label:
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

    hide hari with chara_move_transition

    call talk ('bulan', 'Hari… tunggu—!')

    call