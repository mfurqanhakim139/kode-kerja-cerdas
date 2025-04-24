import time

# Mendapatkan epoch timestamp saat ini
waktu_sekarang_epoch = time.time()
print(f"Epoch timestamp saat ini: {waktu_sekarang_epoch}")

# Mengukur durasi
waktu_mulai = time.time()
# Lakukan sesuatu yang butuh waktu (contoh: loop sederhana)
total = 0
for i in range(1000000):
    total += i
waktu_selesai = time.time()
durasi = waktu_selesai - waktu_mulai
print(f"\nLoop selesai dalam {durasi:.4f} detik.") # .4f format 4 angka desimal

# Memberi jeda
print("\nMenunggu 3 detik...")
time.sleep(3) # Program berhenti selama 3 detik
print("Selesai menunggu.")

