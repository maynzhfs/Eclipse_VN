label s2_4_ngobrol_di_kafe:
    scene black

    call narator ("keesokannya...")

    scene kafe_siang

    show bulan sad at pos_left_f
    show senja normal at pos_right

    call talk('senja', 'Gimana kamu? udah ngerasa lebih baik?')
    call talk('bulan', 'Senja, aku masih bingung banget. Bumi terus-terusan ngejar aku, sepertinya dia pengen aku ninggalin Hari.')
    call talk('senja', 'Lalu kamu gimana? ', 'confuse')
    call talk('bulan', 'Aku... aku nggak tahu karena ga mungkin aku tinggalin Hari, dia pacarku')
    call talk('senja', 'Itu artinya dia egois, Bulan. Dia nggak mau kamu bahagia sama orang lain. Kamu harus tegas.')
    call talk('bulan', 'Tapi Bumi juga temenku Ja, dia udah banyak bantu aku', 'sad')
    call talk('senja', 'Coba kamu tenang dulu, pikirin baik-baik. Siapa yang benar-benar bikin kamu nyaman? Siapa yang selalu bikin kamu tersenyum tulus? Siapa yang nggak pernah membuatmu ragu?')
    call talk('bulan', '...', 'sad')
    call talk('senja', 'Pilihan ada di tanganmu, Bulan. Kamu yang tahu yang terbaik untuk dirimu sendiri. Aku ada disini buat bantu kamu dan aku bakal dukung semua pilihanmu.')
    
    'Bulan memejamkan mata, mencoba menemukan jawabannya.'

    jump s3_1_hari_khawatir