label s2_1_gombal:
    scene black

    call narator ("Hari dan Bulan sedang mengerjakan tugas bersama. Bulan tampak fokus, sementara Hari sesekali mencuri pandang ke arah Bulan sambil tersenyum tipis.")

    scene pagi_depan_kost

    show bulan normal at pos_far_left
    show hari normal at pos_far_right

    call talk ('hari', '(pelan) Bul..')

    call talk ('bulan', 'hmm ya?..')

    show hari normal at pos_center with chara_move_transition
    
    call talk ('hari', 'diliat-liat, kamu lucu juga ya kalau lagi mode serius kayak gini')

    call talk ('bulan', 'HAH? apaan sih, Ri.', 'shock')
    call talk ('bulan', 'udah fokus aja ngerjain tugasmu sana')

    call talk ('hari', 'iya iyaa', 'happy')
    call talk ('hari', 'eh tapi beneran loh, aku suka liat kamu kalau lagi serius kayak gini')

    call talk ('bulan', 'Gombal! udah sana, jangan ganggu')

    call talk ('hari', 'yahh, padahal kan niat aku mau nyemangatin kamu')

    call talk ('bulan', 'ish!')

    call setExpr (['bulan', 'hari'], 'happy')
    "Mereka saling melempar senyun dan tertawa kecil, kemudian kembali fokus melanjutkan tugas masing-masing"

    jump s2_2_bumi_ribut