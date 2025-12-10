label s06_bumi_ribut
    scene black

    call narator ("Bulan dan Hari sedang berjalan berdua di koridor kampus, tertawa dan bercanda. Tanpa sadar, ternyata dari kejauhan, Bumi memperhatikan mereka dengan tatapan tidak suka.")

    call narator ("Sementara itu, Bumi mempercepat langkahnya, berniat menghampiri Hari dan Bulan. Namun, Senja tiba-tiba saja datang dan menahannya")

    show bumi angry at pos_left
    show senja normal at pos_right

    call talk ('senja', 'Bumi, kamu mau kemana?')

    call talk ('bumi', ' bukan urusanmu, Senja')

    call talk ('senja', 'Aku tahu kamu cemburu. Tapi tololng jangan ganggu Bulan lagi, dia juga udah bukan urusanmu')

    "Bumi hanya menghiraukan perkataan Senja dan tetap melangkah"

    call talk ('senja', 'Bumi dengar, dulu kamu yang dulu nyuruh dia untuk jaga jarak, kamu yang udah buat dia kecewa. Sekarang dia udah move on, buat apa kamu datang lagi?')

    call talk ('bumi', 'aku cuman mau dia tau dan sadar siapa yang terbaik buat dia')

    call talk ('senja', 'yang terbaik buat dia itu yang ga pernah nyakitin perasaan dia')

    show bumi angry at pos_far_left with chara_move_transition
    "Bumi tetap tak menghiraukan Senja dan terus melangkah menuju Bulan dan Hari. Senja hanya bisa menghela napas pasrah."

    hide senja with defaul_
