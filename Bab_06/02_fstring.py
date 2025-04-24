# Contoh memformat string menggunakan f-strings

nama = "Citra Amelia"
umur = 28
pekerjaan = "Data Analyst"
gaji = 12500000.50
hobi = ["membaca", "hiking", "koding"]

# Menggabungkan variabel ke dalam string
print(f"Nama: {nama}")
print(f"Usia: {umur} tahun")
print(f"Pekerjaan: {pekerjaan}")

# Melakukan format angka (misal: pemisah ribuan, desimal)
# :,.2f -> : mulai format, , pemisah ribuan, .2f dua angka desimal float
print(f"Gaji bulanan: Rp {gaji:,.2f}") 

# Menyisipkan ekspresi atau pemanggilan fungsi
print(f"Gaji tahunan (perkiraan): Rp {gaji * 12:,.0f}")
print(f"Nama dalam huruf kecil: {nama.lower()}")
print(f"Jumlah hobi: {len(hobi)}")

# Kondisional sederhana di dalam f-string
status_umur = 'Dewasa' if umur >= 18 else 'Remaja'
print(f"Status usia: {status_umur}")

# Menampilkan isi list (akan memanggil __str__ dari list)
print(f"Hobi: {hobi}")

# Debugging cepat (Python 3.8+)
# print(f"{nama=}, {umur=}") # Akan mencetak nama_var=nilai_var
