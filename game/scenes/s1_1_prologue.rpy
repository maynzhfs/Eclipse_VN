label s1_1_prologue:
    scene sore_belakang_kampus with default_bg_transition

    show bulan normal at pos_left_f
    show bumi normal at pos_right 
    with default_chara_transition

    call talk ('bulan', 'Bumi..')

    call talk ('bumi', 'ya?', 'normal')

    call talk ('bulan', 'a-aku, aku mau nanya sesuatu', 'blush')

    call talk ('bumi', 'nanya sesuatu? nanya apa emang?')

    call talk ('bulan', 'kita kan udah sering bareng, tugas bareng, main bareng, semuanya bareng...')
    call talk ('bulan', 'Menurutmu, kita ini apa?')

    call talk ('bumi', 'yaa...')
    call setExpr (['bulan'],'shock')
    call talk ('bumi', 'kita cuma temen')

    call talk ('bulan', 'ga bisa kah lebih dari itu?', 'sad')

    call talk ('bumi', 'maaf Bulan, tapi aku gabisa, aku cuma mau kita jadi temen aja', 'sad')

    call talk ('bulan', 'tapi, kita kan udah lebih dari deket', 'sad')


    call talk ('bumi', 'maaf Bulan, maaf, aku gabisa...', 'sad')

    call talk ('bulan', '...', 'sad')
    call talk ('bumi', '...', 'sad')
    
    show bumi sad at pos_far_right_f with chara_move_transition

    call talk ('bumi', 'sebaiknya kita jaga jarak aja ya, Bulan.', 'sad')
    call talk ('bumi', 'aku gamau kamu kecewa dan berharap lebih dari ini, maaf...', 'sad')

    call talk ('bulan', '...', 'sad')

    jump s1_2_narasi
