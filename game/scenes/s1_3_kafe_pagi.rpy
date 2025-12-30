label s1_3_kafe_pagi:
    call play_ambience("audio/restaurant_ambience.mp3", volume=0.1, fade_time = 10.0)
    # call change_music("audio/find your cafein_bgm.mp3", fade_time = 10.0)
    call stop_music()

    scene kafe_siang 
    
    # SETUP AWAL SCENE
    show bulan normal at pos_right
    show senja normal at pos_left_f
    with default_chara_transition
    
    call setExpr(['senja', 'bulan'], 'normal') 
    
    call talk('senja', 'Bulan, kulihat2 belakangan ini kamu dekat dengan Hari ya? ', 'happy')

    call talk('bulan', 'Hari?', 'confuse')
    call talk('bulan', 'oh iya, dia menemaniku belakangan ini, dia juga ternyata baik orangnya, lagipula kami juga selalu nyambung ketika ngobrol')

    call talk('senja', 'Trus, Bumi bagaimana?')

    call setExpr(['senja'], 'shock')
    call talk('bulan', 'yaa begitu, kami sudah tidak sedekat dulu. Dia minta aku buat jaga jarak, jadi kuturuti saja.', 'sad')
    
    call talk('senja', 'tapi kulihat kalian tetap dekat tuh')

    call talk ('bulan', 'dekat sih iya, cuma perasaanku udah hilang untuknya.')
    call talk ('bulan', 'Tapi memang kelakuan dia berubah jadi aneh sekarang...')

    call talk ('senja', 'Aneh? mungkin dia cuman cemburu sama Hari...')

    call talk ('bulan', 'hmm, bisa jadi sih, tapi ya sudah lah, lagipula Hari juga sepertinya cuma mau berteman', 'sad')

    call talk ('senja', 'eh? Kamu yakin Hari cuma mau berteman?', 'shock')

    call setExpr(['senja'], 'shock')
    call talk ('bulan', 'yakin ko, kenapa emang?', 'happy')

    call talk ('senja', 'e-engga sih, cuma sepertinya dia suka sama kamu')

    call talk ('bulan', 'yaudah, itu kan perasaannya dia, lagipula kita ga bisa atur perasaaan orang lain kan?')

    call talk ('senja', 'i-iya sih... cuma kan...', 'sad')

    call talk ('bulan', 'Aku juga kan gapunya perasaan apapun sama Hari')

    call talk ('senja', '...')

    call talk ('bulan', 'Sudahlah, kalopun dia suka padaku, aku yakin dia ga bakal nembak juga', 'happy')

    jump s1_4_ditembak_hari

