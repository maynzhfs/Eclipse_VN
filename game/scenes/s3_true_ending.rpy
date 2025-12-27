label s3_true_ending:
    scene black

    show bulan at pos_left
    show senja at pos_right
    with default_chara_transition

    call talk ('senja', 'Kamu kelihatan tenang, Bul')
    call talk ('senja', 'tapi aku tau, kamu lagi nahan banyak hal.')
    call talk ('bulan', 'Aku capek, Ja...', 'sad')
    call talk ('bulan', 'Rasanya apa pun yang aku lakuin, ada aja yang tersakiti.', 'sad')

    call talk ('senja', 'Terus kamu pengen apa sekarang?')

    call talk ('bulan', 'aku pengen coba ikutin saranmu')
    call talk ('bulan', 'meskipun aku tau, pasti ada yang tersakiti, dan aku harus bisa ninggalin itu')

    '(Senja terdiam sejenak)'

    call talk ('senja', 'kadang ya Bul,')
    call talk ('senja', 'ninggalin sesuatu itu bukan tanda kita menyerah')
    call talk ('senja', 'bisa jadi itu alasan kita bertahan agar tetap ngerasa hidup')

    hide bulan
    hide senja
    with default_chara_transition

    scene black

    call narator ('(Bulan menghubungi Bumi dan mengajaknya ketemuan di koridor.)')

    show bulan normal at pos_right
    show bumi normal at pos_left
    with default_chara_transition

    call talk ('bulan', 'Bumi, aku mau ngomong sesuatu')
    '(Bumi tak menjawab, hanya menatap Bulan)'

    call talk ('bulan', 'setelah aku pikir panjang, dan dengan saran Senja, sepertinya kita ga bisa lanjut, makasih buat kemarin, kamu udah banyak bantu aku. tapi maaf, sampai sini aja. buat kedepannya kita jalan masing-masing')
    call talk ('bumi', 'kamu udah yakin dengan keputusanmu itu?')

    call talk ('bulan', 'iya, aku udah berpikir berkali-kali dan aku udah memutuskan untuk lebih baik seperi ini saja')

    call talk ('bumi', 'kamu ga mau buat dicoba lagi? kalau dengan masalah aku yang terlalu ngatur, aku udah berubah ko')
    call talk ('bulan', ' engga Bumi, maaf, cukup sampai sini aja')

    call talk ('bumi', '...')

    call talk ('bulan', 'makasih buat yang kemarin')



    call talk ('bulan', '(pergi menghampiri hari)')

    call talk ('bulan', 'Hari, aku udah cutoff Bumi, jadi... temenin aku terus ya..')
    call talk ('hari', 'iya Bul, makasih udah memilih buat terus bareng aku')
    
    jump trueEnd

