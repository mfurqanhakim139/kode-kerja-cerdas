import re

# Contoh IGNORECASE
pola_i = re.compile(r'python', re.IGNORECASE)
print(pola_i.findall("Saya suka Python dan PYTHON."))

# Contoh VERBOSE (membuat pola kompleks lebih mudah dibaca)
# Pola ini mencoba mencocokkan format nomor telepon yang lebih fleksibel
pola_telp_verbose = re.compile(r'''
    (                 # Awal grup kode area (opsional)
        (\d{3}|\(\d{3}\))? # Grup 2: Kode area (3 digit) ATAU (3 digit) - opsional
    )                 # Akhir grup kode area
    (\s|-|\.)?        # Grup 3: Pemisah pertama opsional (spasi, -, .)
    \d{3}             # 3 digit pertama nomor utama
    (\s|-|\.)         # Grup 4: Pemisah kedua (wajib)
    \d{4}             # 4 digit terakhir nomor utama
    ''', re.VERBOSE | re.IGNORECASE) # Bisa gabungkan flag dengan |

print(pola_telp_verbose.search("Hubungi (123)-456-7890").group())
print(pola_telp_verbose.search("nomor saya 555.1234").group())
