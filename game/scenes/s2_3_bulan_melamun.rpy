label s2_3_bulan_melamun:
    scene kamar_kost

    show bulan sad at pos_left_f with chara_move_transition
    'Bulan sedang melamun di kamarnya. Ponselnya bergetar, ada pesan masuk dari Bumi.'
    
    show bulan sad at pos_far_left_f with chara_move_transition
    show bumi normal at pos_far_right
    with default_chara_transition

    call talk('bumi', 'Bulan, aku cuma mau kamu tau. Aku peduli sama kamu.')
    hide bumi with default_chara_transition

    show bulan sad at pos_left_f with chara_move_transition
    'Bulan membaca pesan itu, lalu menghela napas. Tak lama, pesan lain masuk dari Hari.'
    
    show bulan sad at pos_far_left_f with chara_move_transition
    show hari normal at pos_far_right
    with default_chara_transition
    call talk('hari', 'Bul, kamu lagi apa? Jangan mikirin omongan Bumi, ya. Aku sayang sama kamu.')
    hide hari with default_chara_transition

    show bulan sad at pos_left_f with chara_move_transition
    'Bulan bingung harus membalas yang mana. Dia merasa terjebak di antara keduanya, dan akhirnya Bulan memutuskan untuk menelepon Senja'
    
    show bulan sad at pos_far_left_f with chara_move_transition
    show senja normal at pos_far_right
    with default_chara_transition

    call talk('bulan', 'Ja, aku bingung, ini kenapa Bumi jadi kayak begini? padahal aku udah nurutin apa yang dia mau', 'sad')
    
    call talk('senja', 'Dia itu cemburu karena kamu sekarang dengan Hari, Bul')
    
    call talk('bulan', 'Tapi kan itu ga ada hubungannya dengan dia, Ja', 'sad')
    
    call talk('senja', 'Sudah ga apa Bul, ga usah terlalu dipikirkan. tapi ngomong-ngomong kamu dengan Hari gimana?')
    
    call talk('bulan', 'Kalau aku dengan Hari mah aman-aman aja Ja, cuman aja Bumi agak..', 'sad')
    
    call talk('senja', 'Yang paling penting kamu bahagia Bul, jadi jangan pikirkan yang tidak perlu kamu pikirin, ok?', 'happy')
    
    call talk('bulan', 'Senja, kalau besok kita ketemuan di cafe gimana? aku butuh banget kamu sekarang', 'sad')
    
    call talk('senja', 'ok boleh ko Bul, kita ketemuan aja ya di cafe besok')
    
    jump s2_4_ngobrol_di_kafe