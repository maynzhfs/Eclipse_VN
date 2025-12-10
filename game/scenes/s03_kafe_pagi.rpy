label s03_kafe_pagi:
    call play_ambience("audio/restaurant_ambience.mp3", volume=0.1, fade_time = 3.0)
    call play_music("audio/find your cafein_bgm.mp3", fade_time = 2.0)

    scene kafe_siang 
    
    # SETUP AWAL SCENE
    show bulan normal at pos_left
    show senja normal at pos_right
    
    call setExpr(['senja', 'bulan'], 'normal') 
    
    call talk('senja', 'Bulan, kulihat2 belakangan ini kamu dekat dengan Hari ya? ', 'happy')

    call talk('bulan', 'Hari? oh iya, dia menemaniku belakangan ini, dia juga ternyata baik orangnya, lagipula kami juga selalu nyambung ketika ngobrol', 'shock')

    call talk('senja', 'Trus, Bumi bagaimana?')

    call setExpr(['senja'], 'shock')
    call talk('bulan', 'yaa begitu, kami sudah tidak sedekat dulu. Dia minta aku buat jaga jarak, jadi kuturuti saja.')
    
    call talk('senja', 'tapi kulihat kalian tetap dekat tuh')

    call talk ('bulan', 'dekat sih iya, cuma perasaanku udah hilang untuknya.')
    call talk ('bulan', 'Tapi memang kelakuan dia berubah jadi aneh sekarang...')

    call talk ('senja', 'Aneh? mungkin dia cuman cemburu sama Hari...')

    call talk ('bulan', 'hmm, bisa jadi sih, tapi ya sudah lah, lagipula Hari juga sepertinya cuma mau berteman')

    call talk ('senja', 'eh? Kamu yakin Hari cuma mau berteman?', 'shock')

    call setExpr(['senja'], 'shock')
    call talk ('bulan', 'yakin ko, kenapa emang?')

    call tal ('senja', 'e-engga sih, cuma sepertinya dia suka sama kamu')

    call talk ('bulan', 'yaudah, itu kan perasaannya dia, lagipula kita ga bisa atur perasaaan orang lain kan?')

    call talk ('senja', 'i-iya sih... cuma kan...')

    call talk ('bulan', 'Aku juga kan gapunya perasaan apapun sama Hari')

    call talk ('senja', '...')

    call talk ('bulan', 'Sudahlah, kalopun dia suka padaku, aku yakin dia ga bakal nembak juga')

    jump s04_ditembak_hari

