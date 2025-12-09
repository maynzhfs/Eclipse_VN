## ----------------------------------------------------
## SCRIPT.RPY: CONTOH PENGGUNAAN
## ----------------------------------------------------

# Catatan: Pastikan 11_characters.rpy sudah mendefinisikan 'hari', 'senja', dan 'bulan'.
# Pastikan ada gambar BG bernama 'kafe_siang' di folder backgrounds/.

label start:

    scene kafe_siang 
    
    # SETUP AWAL SCENE
    show bulan normal at left
    show hari normal at center
    show senja normal at right
    
    # Semua karakter yang tidak bicara, berstatus mendengarkan (redup)
    call setExpr(['hari', 'senja', 'bulan'], 'normal', True) 
    
    # Bulan bicara (otomatis tidak redup saat bicara, lalu kembali redup)
    call talk('bulan', 'Hello everyone! I have great news!', 'happy')
    
    # Hari & Senja ikut senang (mereka tetap redup)
    call setExpr(['hari', 'senja'], 'happy', True) 
    
    # Hari bicara
    call talk('hari', 'Oh really? That sounds great!', 'shock')

    # Senja bicara, mengubah mood
    call talk('senja', 'Wait, what if the news is bad?', 'sad')
    
    # Hari & Bulan menjadi cemas (mereka tetap redup)
    call setExpr(['hari', 'bulan'], 'angry', True)

    # Akhir adegan, hapus semua karakter
    hide all with default_chara_transition
    
    scene hutan_malam
    
    return