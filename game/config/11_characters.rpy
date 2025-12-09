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
        'color': '#8800ff'
    },
    {
        'tag': 'hari', 
        'name': 'Hari', 
        'color': '#0713ff'
    },
    {
        'tag': 'bumi', 
        'name': 'Bumi', 
        'color': '#158900'
    },
    {
        'tag': 'senja', 
        'name': 'Senja', 
        'color': '#ffaa00'
    },
    {
        'tag': 'all', 
        'name': 'SEMUA', 
        'color': '#ffffff'
    }
]

## --- JANGAN DIUBAH ---
# Panggil fungsi setup untuk semua data di atas
init:
    $ SetupAllCharacters(characters_data)