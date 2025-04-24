import threading
import time
import datetime

def tugas_terjadwal(pesan, jeda_detik):
    print(f"{datetime.datetime.now()}: Thread dimulai, akan mencetak '{pesan}' setelah {jeda_detik} detik.")
    time.sleep(jeda_detik)
    print(f"\n{datetime.datetime.now()}: Waktunya tugas! Pesan: {pesan}")

print(f"{datetime.datetime.now()}: Program Utama: Menjadwalkan tugas...")

# Buat thread untuk menjalankan 'tugas_terjadwal' dengan argumen 'Halo!' dan jeda 5 detik
# Target adalah nama fungsi (tanpa ()), args adalah list/tuple argumennya
thread1 = threading.Thread(target=tugas_terjadwal, args=['Halo dari Thread!', 5])
thread1.start() # Mulai thread, fungsi tugas_terjadwal berjalan di latar

print(f"{datetime.datetime.now()}: Program Utama: Tetap berjalan sambil menunggu thread...")
# Program utama bisa melakukan hal lain di sini

# Biarkan program utama menunggu sebentar agar output thread terlihat
# time.sleep(6)
print(f"{datetime.datetime.now()}: Program Utama: Selesai.")
# Catatan: Program utama mungkin selesai sebelum thread selesai jika tidak ditunggu.
# Untuk menunggu thread selesai, gunakan: thread1.join()
