label s2_1_gombal:
    scene black

    call narator ("Hari dan Bulan sedang mengerjakan tugas bersama. Bulan tampak fokus, sementara Hari sesekali mencuri pandang ke arah Bulan sambil tersenyum tipis.")

    scene pagi_depan_kost

    show bulan normal at pos_far_right
    show hari normal at pos_far_left_f

    call talk ('hari', '(pelan) Bul..')

    call talk ('bulan', 'hmm ya?..')

    show hari normal at pos_right_f with chara_move_transition
    
    call setExpr('bulan', 'blush')
    call talk ('hari', 'diliat-liat, kamu lucu juga ya kalau lagi mode serius kayak gini')

    call talk ('bulan', 'HAH? apaan sih, Ri.', 'blush')
    call talk ('bulan', 'udah fokus aja ngerjain tugasmu sana', 'angry')

    call setExpr('bulan', 'blush')
    call talk ('hari', 'iya iyaa', 'happy')
    call talk ('hari', 'eh tapi beneran loh, aku suka liat kamu kalau lagi serius kayak gini')

    call setExpr('hari', 'happy')
    call talk ('bulan', 'Gombal! udah sana, jangan ganggu', 'angry')

    call talk ('hari', 'yahh, padahal kan niat aku mau nyemangatin kamu', 'happy')

    call talk ('bulan', 'ish!', 'happy')

    call setExpr (['bulan', 'hari'], 'happy')
    "Mereka saling melempar senyun dan tertawa kecil, kemudian kembali fokus melanjutkan tugas masing-masing"

    jump s2_2_bumi_ribut