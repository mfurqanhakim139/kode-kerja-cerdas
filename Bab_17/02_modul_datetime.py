import datetime
import time

# Waktu saat ini
sekarang = datetime.datetime.now()
print(f"Waktu saat ini: {sekarang}")
print(f"Tahun: {sekarang.year}, Bulan: {sekarang.month}, Tanggal: {sekarang.day}")
print(f"Jam: {sekarang.hour}, Menit: {sekarang.minute}, Detik: {sekarang.second}")

# Membuat timedelta (durasi 10 hari, 3 jam)
delta = datetime.timedelta(days=10, hours=3)
print(f"\nDurasi: {delta}")

# Aritmetika tanggal
tanggal_mendatang = sekarang + delta
print(f"10 hari 3 jam dari sekarang: {tanggal_mendatang}")
tanggal_lalu = sekarang - datetime.timedelta(days=7) # 7 hari lalu
print(f"7 hari yang lalu: {tanggal_lalu}")

# Format ke string (strftime)
format_umum = "%Y-%m-%d %H:%M:%S"
format_indo = "%d %B %Y, pukul %H:%M" # Contoh format lain
string_waktu_umum = sekarang.strftime(format_umum)
# Perlu locale Indonesia ter-setting di sistem untuk nama hari/bulan Bhs Indonesia
# Jika tidak, gunakan library external seperti 'babel' atau terjemahkan manual
string_waktu_indo = sekarang.strftime(format_indo)
print(f"\nFormat YYYY-MM-DD HH:MM:SS: {string_waktu_umum}")
print(f"Format Indonesia (contoh): {string_waktu_indo}")

# Parsing string ke datetime (strptime)
string_tgl = "2024-12-25 10:30:00"
format_tgl = "%Y-%m-%d %H:%M:%S"
try:
    datetime_obj = datetime.datetime.strptime(string_tgl, format_tgl)
    print(f"\nObjek datetime dari string '{string_tgl}': {datetime_obj}")
    print(f"Tahun dari objek: {datetime_obj.year}")
except ValueError as e:
    print(f"Gagal parsing string tanggal: {e}") # Error jika format tidak cocok

