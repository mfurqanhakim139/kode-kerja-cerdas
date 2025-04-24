import re

# Cari 'apel', 'mangga', atau 'jeruk' (Alternation |)
pola_buah = re.compile(r'apel|mangga|jeruk')
teks_buah = "Saya suka mangga dan apel."
print(f"Buah ditemukan: {pola_buah.findall(teks_buah)}")

# Cari kata yang diawali 'me' diikuti 1+ huruf kecil (Kelas Karakter [], Quantifier +)
pola_me = re.compile(r'me[a-z]+')
teks_me = "Dia membaca, menulis, dan menggambar."
print(f"Kata 'me': {pola_me.findall(teks_me)}")

# Ekstrak nama depan dan belakang (Grouping (), Kelas Karakter \w, \s)
pola_nama = re.compile(r'(\w+)\s(\w+)') # Grup 1: nama depan, Grup 2: nama belakang
hasil_nama = pola_nama.search("Budi Santoso")
if hasil_nama:
    print(f"Nama Lengkap: {hasil_nama.group()}")   # group() atau group(0) = seluruh match
    print(f"Nama Depan: {hasil_nama.group(1)}") # Grup 1
    print(f"Nama Belakang: {hasil_nama.group(2)}")# Grup 2

# Opsional 'bapak' atau 'ibu' (Grouping (), Alternation |, Quantifier ?)
pola_sapaan = re.compile(r'(bapak|ibu)?\s?\w+') # Membuat spasi menjadi opsional dengan ?
hasil_sapaan_bapak = pola_sapaan.search('bapak Budi')
if hasil_sapaan_bapak:
    print(f"Cocok 'bapak Budi': {hasil_sapaan_bapak.group()}")

hasil_sapaan_ibu = pola_sapaan.search('ibu Ani')
if hasil_sapaan_ibu:
    print(f"Cocok 'ibu Ani': {hasil_sapaan_ibu.group()}")

hasil_sapaan_dewi = pola_sapaan.search('Dewi')
if hasil_sapaan_dewi:
    print(f"Cocok 'Dewi': {hasil_sapaan_dewi.group()}")
else:
    print(f"Tidak cocok dengan pola 'Dewi'")