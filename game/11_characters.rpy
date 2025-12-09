# Format Dictionary:
# { 'tag': '[Nama Pendek (untuk Skrip)]', 'name': '[Nama Lengkap Karakter]', 'color': '[Warna Hex]' }

define characters_data = [
    {
        'tag': 'narator',
        'name': None,
        'color': '#aaaaaa'
    },
    {
        'tag': 'bulan', 
        'name': 'Bulan', 
        'color': '#c8ffc8'
    },
    {
        'tag': 'hari', 
        'name': 'Hari', 
        'color': '#ffc8c8'
    },
    # TEMPAT TEMAN ANDA MENAMBAHKAN KARAKTER BARU
    {
        'tag': 'bumi', 
        'name': 'Bumi', 
        'color': '#c8c8ff'
    },
    # TEMPAT TEMAN ANDA MENAMBAHKAN KARAKTER BARU
    {
        'tag': 'senja', 
        'name': 'Senja', 
        'color': '#ffce85'
    }
]

## --- JANGAN DIUBAH ---
# Panggil fungsi setup untuk semua data di atas
init:
    $ SetupAllCharacters(characters_data)