# Contoh mengakses nilai dalam Dictionary

data_mahasiswa = {'nama': 'Budi', 'nim': '123456', 'jurusan': 'Informatika'}
print(f"Data awal: {data_mahasiswa}")

# Mengakses nilai menggunakan kunci
try:
    nama_mhs = data_mahasiswa['nama']
    jurusan_mhs = data_mahasiswa['jurusan']
    print(f"Nama: {nama_mhs}")      
    print(f"Jurusan: {jurusan_mhs}") 

    # Mencoba akses kunci yang tidak ada akan error
    # alamat_mhs = data_mahasiswa['alamat'] 
    # print(f"Alamat: {alamat_mhs}")

except KeyError as e:
    print(f"Error! Kunci tidak ditemukan: {e}")

# Cara aman mengakses (menggunakan .get())
alamat_mhs_aman = data_mahasiswa.get('alamat') # Mengembalikan None jika tidak ada
print(f"Alamat (get): {alamat_mhs_aman}") 

kota_mhs = data_mahasiswa.get('kota', 'Belum diisi') # Beri nilai default
print(f"Kota (get dg default): {kota_mhs}")
