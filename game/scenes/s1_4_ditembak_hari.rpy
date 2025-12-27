label s1_4_ditembak_hari:
    scene malam_depan_kost

    show bulan normal at pos_far_left
    show hari normal at pos_far_right
    with default_chara_transition

    call setExpr (['bulan'], 'shock')
    call talk ('hari', 'mau ga jadi pacarku?', 'happy')

    call talk ('bulan', '(LOHHHH)', 'shock')
    call talk ('bulan', 'eh, maksudmu gimana nih?', 'shock')

    call talk ('hari', 'aku pengen menjalani hubungan denganmu, bukan lagi sekedar teman, tapi pacar.')
    call talk ('hari', 'aku pengen mengisi hari-hariku dengan kita berdua.')

    call talk ('bulan', '(waduh, aku gamau pacaran sama Hari)')
    call talk ('bulan', ' emangnya kamu yakin kalo kita pacaran, kita akan selalu bahagia?')

    call talk ('hari', 'justru sebaliknya, buatku pacaran bukan tentang bahagianya doang')

    call talk ('bulan', 'maksudnya tuh gimana?')

    call talk ('hari', 'dalam hubungan, ada yang namanya komitmen. Komitmen ini lah yang tetap meyatukan kita, bukan cuma rasa bahagia dan senang.')
    call talk ('hari', 'pasti akan ada hari dimana kita merasa jenuh, sedih, dan kecewa. Buatku justru disana ujiannya, gimana kita tetap bisa menghadapi semuanya bersama, dalam suka maupun duka')

    call talk ('bulan', 'hmm, emang kita gabisa tetep seperti ini aja?')

    call talk ('hari', 'satu-satunya yang mengikat kita saat ini adalah game, dan gamenya pun baru aja kita beresin tadi...')
    call talk ('hari', 'Selain itu, menurutmu apa yang masih mengikat kita berdua?')

    call talk ('bulan', '...')

    call talk ('hari', 'Kamu sama Bumi, kalian sekelas, satu organisasi, bahkan satu kerjaan, banyak ikatan yang memberikan alasan kenapa kalian tetap bisa bareng.')
    call talk ('hari', 'Tapi kamu denganku, ga ada ikatan lagi yang tersisa.')
    call talk ('hari', 'Aku mau kita tetap seperti sekarang, tapi sepertinya gabisa, aku punya banyak hal lain yang harus kuurus. Aku mau fokus dengan apa yang memang terikat denganku, yang sudah menjadi kewajibanku juga.')
    call talk ('hari', 'Makannya, aku mau kita terikat bukan lagi hanya sebagai teman, supaya aku tetap punya alasan yang konkrit untuk tetap menyediakan ruang di kepalaku yang semuanya diisi oleh kamu.')

    menu:
        "(duhh, gimana nih?)":
            jump s1_4_alesan_01
        "(yaudah kita pacaran aja)":
            jump s1_4_terima

label s1_4_alesan_01:
    call talk ('bulan', 'Aku gapapa ko kalo misalnya kita jaga jarak, tapi aku gamau kehilangan kamu')

    call talk ('hari', 'opsimu cuman ada dua')
    call talk ('hari', 'Berpacaran denganku, atau ga kenal lagi sama aku')

    menu:
        "(alesan apa lagi ya?)":
            jump s1_4_alesan_02
        "(yaudah kita pacaran aja)":
            jump s1_4_terima
    
label s1_4_alesan_02:

    call talk ('bulan', 'Aku boros loh, emang kamu yakin bisa menuhi apa yang aku mau?')

    call talk ('hari', 'aku bakal usaha semaksimal mungkin buat itu, itu juga tujuan aku kerja sambilan')

    menu:
        "(hmm)":
            jump s1_4_alesan_03
        "(yaudah kita pacaran aja)":
            jump s1_4_terima

label s1_4_alesan_03:

    call talk ('bulan', 'tapi kamu beneran yakin mau sama aku?')

    call talk ('hari', 'iya, aku yakin')
    
label s1_4_terima:

    call talk ('bulan', '(yaudah, semoga ini emang jalan yang tepat)')
    call talk ('bulan', 'yaudah, aku mau pacaran sama kamu')

    call talk ('hari', 'loh', 'shock')
    call talk ('hari', 'beneran??', 'shock')

    call talk ('bulan', 'iya..', 'angry')

    call talk ('hari', 'jadi.. kita pacaran nih??')

    call talk ('bulan', 'iya, aku terima kamu')

    call setExpr ('bulan', 'happy')
    call talk ('hari', 'o-oh, makasih ya bulan, tolong temani aku ya Bulan, kita hadapi semua nya bareng-bareng')

    jump s2_1_gombal