## ----------------------------------------------------
## 12_BACKGROUNDS.RPY: AUTOLOAD BACKGROUNDS (FINAL FIX)
## ----------------------------------------------------

# Transisi default untuk pergantian Latar Belakang
define default_bg_transition = Fade(0.5, 0.0, 0.5)

init python:
    import os
    
    BG_PATH_PREFIX = "images/backgrounds/"
    
    all_files = renpy.list_files()
    
    # Perulangan hanya pada file yang berada di folder backgrounds/
    for full_path in all_files:
        if full_path.startswith(BG_PATH_PREFIX):
            filename = os.path.basename(full_path) 
            
            if filename.lower().endswith(('.jpg', '.png', '.jpeg')):
                
                # 1. Mendapatkan tag
                tag = os.path.splitext(filename)[0].lower()
                
                # 2. Mendaftarkan image tag standar (image kafe_siang = "...")
                # Ini SANGAT penting agar 'scene kafe_siang' dikenali.
                renpy.image(tag, full_path)
                
                # 3. KITA HAPUS Bagian renpy.define yang Error
                # Kita akan mengandalkan config.default_transition atau panggilan 'with'

# ----------------------------------------------------
# WORKFLOW TRANSISI LATAR BELAKANG:
# Karena kita tidak bisa membuat 'scene kafe_siang' otomatis,
# teman Anda harus menggunakan: scene kafe_siang with default_bg_transition
# ----------------------------------------------------