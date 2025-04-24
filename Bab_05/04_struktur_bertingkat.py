# Contoh struktur data bertingkat (Nesting)

print("--- Dictionary berisi List ---")
data_kelas = {
    'nama_kelas': 'Python Dasar',
    'kode': 'PY101',
    'jadwal': ['Senin 10:00', 'Rabu 10:00', 'Jumat 13:00'],
    'peserta': ['Andi', 'Budi', 'Citra', 'Dewi']
}
print(f"Data Kelas: {data_kelas}")
print(f"Jadwal hari pertama: {data_kelas['jadwal'][0]}") # Akses list, lalu itemnya
print(f"Peserta kedua: {data_kelas['peserta'][1]}")

print("\n--- List berisi Dictionary ---")
semua_mahasiswa = [
    {'nama': 'Andi', 'nim': '111', 'ipk': 3.5},
    {'nama': 'Budi', 'nim': '222', 'ipk': 3.2},
    {'nama': 'Citra', 'nim': '333', 'ipk': 3.8}
]
print(f"Semua Mahasiswa: {semua_mahasiswa}")
# Akses mahasiswa kedua (indeks 1), lalu ambil nilai dari kunci 'nama'
print(f"Nama mahasiswa kedua: {semua_mahasiswa[1]['nama']}") 
# Hitung rata-rata IPK
total_ipk = 0
for mhs in semua_mahasiswa:
    total_ipk += mhs['ipk']
rata_ipk = total_ipk / len(semua_mahasiswa)
print(f"Rata-rata IPK: {rata_ipk:.2f}")

print("\n--- Dictionary berisi Dictionary ---")
keluarga = {
    'ayah': {'nama': 'Pak Joko', 'usia': 50, 'pekerjaan': 'PNS'},
    'ibu': {'nama': 'Bu Ani', 'usia': 48, 'pekerjaan': 'Ibu Rumah Tangga'},
    'anak1': {'nama': 'Dewi', 'usia': 20, 'status': 'Mahasiswa'},
    'anak2': {'nama': 'Eko', 'usia': 15, 'status': 'Pelajar'}
}
print(f"Data Keluarga: {keluarga}")
# Akses data 'ibu', lalu ambil nilai dari kunci 'usia'
print(f"Usia ibu: {keluarga['ibu']['usia']}") 
print(f"Status anak kedua: {keluarga['anak2']['status']}")
