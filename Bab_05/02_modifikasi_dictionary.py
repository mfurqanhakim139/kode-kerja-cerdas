# Contoh menambah, mengubah, dan menghapus item di Dictionary

# 1. Menambah dan Mengubah
data_mahasiswa = {'nama': 'Budi', 'nim': '123456'}
print(f"Data awal: {data_mahasiswa}")

# Menambah pasangan kunci-nilai baru
data_mahasiswa['jurusan'] = 'Informatika' # Kunci 'jurusan' belum ada
data_mahasiswa['angkatan'] = 2023
print(f"Setelah tambah jurusan & angkatan: {data_mahasiswa}")

# Mengubah nilai dari kunci yang sudah ada
data_mahasiswa['nama'] = 'Budi Hartono' # Kunci 'nama' sudah ada, nilainya diupdate
print(f"Setelah ubah nama: {data_mahasiswa}")

print("-" * 20)

# 2. Menghapus (del)
nilai_ujian = {'matematika': 85, 'fisika': 78, 'kimia': 92}
print(f"Nilai ujian sebelum hapus: {nilai_ujian}")

try:
     del nilai_ujian['fisika'] # Hapus pasangan dengan kunci 'fisika'
     print(f"Setelah hapus fisika: {nilai_ujian}")

     # Mencoba hapus kunci yang tidak ada akan error
     # del nilai_ujian['biologi']

except KeyError as e:
     print(f"Error saat menghapus! Kunci tidak ditemukan: {e}")
