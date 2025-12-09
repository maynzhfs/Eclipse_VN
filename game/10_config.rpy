## ----------------------------------------------------
## 10_CONFIG.RPY: LOGIKA UTAMA (FIX STABIL + OPTIMIZED)
## ----------------------------------------------------

# [WARNA DIM]
# Kita tidak pakai kode Hex lagi di logic, tapi pakai MatrixColor
define DIM_MATRIX = TintMatrix("#999999") 
define NORMAL_MATRIX = IdentityMatrix()

# [TRANSISI & POSISI]
define default_chara_transition = Dissolve(0.3)
define pos_center = Position(xalign=0.5, yalign=1.0)
define pos_left = Position(xalign=0.25, yalign=1.0)
define pos_right = Position(xalign=0.75, yalign=1.0)

# [DAFTAR EKSPRESI]
define standard_expressions = [
    "normal", "happy", "laugh", "blush", "shock", "angry",
    "sad", "anxious", "ponder", "bored", "eyes_closed", "smile", 
    "cry", "scared", "surprise_p", "disappoint"
]

# [TRANSFORM DEFINITION]
# Ini triknya! Kita buat "efek" visual terpisah.
# Ini aman banget dan gak bakal bikin error texture.
transform trans_dim:
    matrixcolor DIM_MATRIX

transform trans_normal:
    matrixcolor NORMAL_MATRIX

# ====================================================================
# INIT -1 PYTHON: LOGIKA UTAMA
# ====================================================================
init -1 python:
    import os 

    # --- 1. INDEXING FILE (OPTIMIZED) ---
    sprite_map = {}
    for file_path in renpy.list_files():
        if file_path.lower().endswith(('.png', '.webp')):
            filename = os.path.basename(file_path)
            sprite_map[filename] = file_path

    # --- 2. FUNGSI LOGIKA SET_EXPR (FIXED: PAKE TRANSFORM) ---
    def setExpr_logic(characters, expression, isListen=False):
        
        # Tentukan efek apa yang mau dipake (Redup atau Normal)
        active_transform = trans_dim if isListen else trans_normal
        
        char_list = characters if isinstance(characters, list) else [characters] 

        for char_tag in char_list:
            # Gabungkan nama + ekspresi (Contoh: "bulan happy")
            full_image_tag = char_tag + " " + expression
            
            # Kita TIDAK melakukan renpy.hide() biar posisinya gak ilang/reset.
            # Kita langsung timpa (show) dengan transform baru.
            
            renpy.show(
                full_image_tag,
                at_list=[active_transform], # Efek redup diterapkan di sini
                layer='master'
            )
            
            # Catatan: Kita biarkan Ren'Py menangani transisi visual secara natural 
            # atau lewat config default biar gak bentrok argumen lagi.

        return True

    # ----------------------------------------------------------------
    # 3. SETUP KARAKTER OTOMATIS
    # ----------------------------------------------------------------
    def SetupCharacter(char_data):
        short_name = char_data['tag'].lower()
        full_name = char_data['name']
        color = char_data.get('color', '#ffffff') 
        
        # a) Definisi Karakter
        char_object = renpy.store.Character(
            full_name, 
            color=color, 
            image=short_name,
            what_with=None,
            default_display=pos_center,
            type='chara',
            what_args={'default_expr': 'normal'}
        )
        setattr(renpy.store, short_name, char_object)
        
        # b) Daftarkan Gambar dari Index
        found_any = False
        for tag in standard_expressions:
            image_tag = short_name + " " + tag            
            target_filename = short_name + "_" + tag + ".png" 
            
            if target_filename in sprite_map:
                renpy.image(image_tag, sprite_map[target_filename])
                found_any = True
        
        # Cek Normal
        if not found_any:
            print(f"WARNING: Tidak ada sprite ditemukan untuk '{short_name}'. Cek nama file!")

    def SetupAllCharacters(character_list):
        for data in character_list:
            SetupCharacter(data)

# ====================================================================
# LABEL WRAPPER
# ====================================================================
label setExpr(characters=[], expression="normal", isListen=False):
    $ setExpr_logic(characters, expression, isListen)
    return

label talk(character_tag, dialogue_text, expression="normal"):
    # 1. Ubah ekspresi & Matikan Redup
    call setExpr([character_tag], expression, False)
    
    # 2. Jalankan Dialog
    $ renpy.say(getattr(renpy.store, character_tag), dialogue_text) 

    # 3. Nyalakan Redup lagi setelah ngomong
    call setExpr([character_tag], expression, True)
    return