# Contoh fitur dan metode berguna pada Dictionary

data_mahasiswa = {'nama': 'Citra', 'nim': '789012', 'jurusan': 'Sistem Informasi'}
print(f"Data mahasiswa: {data_mahasiswa}")

# 1. len(): Jumlah pasangan kunci-nilai
jumlah_data = len(data_mahasiswa)
print(f"Jumlah data: {jumlah_data}") # -> 3

print("-" * 20)

# 2. in / not in: Cek keberadaan KUNCI
print(f"Apakah 'nama' ada sebagai kunci? {'nama' in data_mahasiswa}") # -> True
print(f"Apakah 'alamat' ada sebagai kunci? {'alamat' in data_mahasiswa}") # -> False
print(f"Apakah 'Citra' ada sebagai kunci? {'Citra' in data_mahasiswa}") # -> False (cek kunci, bukan nilai)

print("-" * 20)

# 3. keys(), values(), items()
kunci = data_mahasiswa.keys()
nilai = data_mahasiswa.values()
pasangan = data_mahasiswa.items()

# Objek view ini dinamis, berubah jika dict berubah
print(f"Objek view keys(): {kunci}") 
print(f"Objek view values(): {nilai}")
print(f"Objek view items(): {pasangan}")

# Konversi ke list jika perlu snapshot statis
print(f"List Kunci: {list(kunci)}")
print(f"List Nilai: {list(nilai)}")
print(f"List Pasangan: {list(pasangan)}")

print("-" * 20)

# 4. Iterasi menggunakan items() (paling umum)
print("Detail Mahasiswa (dari items()):")
for k, v in data_mahasiswa.items():
    print(f"- {k.capitalize()}: {v}")

print("-" * 20)

# 5. get(kunci, default=None)
alamat = data_mahasiswa.get('alamat') # Kunci tidak ada, return None
print(f"Alamat (get): {alamat}") 
nama = data_mahasiswa.get('nama', 'Anonim') # Kunci ada, return nilai asli
print(f"Nama (get): {nama}") 
status = data_mahasiswa.get('status', 'Aktif') # Kunci tidak ada, return default 'Aktif'
print(f"Status (get dg default): {status}")

print("-" * 20)

# 6. setdefault(kunci, default)
# Coba set 'angkatan' jika belum ada, beri default 2024
angkatan = data_mahasiswa.setdefault('angkatan', 2024)
print(f"Hasil setdefault 'angkatan': {angkatan}") # -> 2024 (karena belum ada)
print(f"Data setelah setdefault 'angkatan': {data_mahasiswa}") # 'angkatan' ditambahkan

# Coba set 'nama' lagi (sudah ada), beri default 'Nama Baru'
nama_lagi = data_mahasiswa.setdefault('nama', 'Nama Baru')
print(f"Hasil setdefault 'nama' (lagi): {nama_lagi}") # -> Citra (nilai lama dikembalikan)
print(f"Data tidak berubah: {data_mahasiswa}") # Nilai 'nama' tidak diubah
