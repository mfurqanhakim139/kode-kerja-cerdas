def fungsi_a(angka):
    hasil = 10 / angka # Potensi ZeroDivisionError
    return hasil

def fungsi_b(nilai):
    nilai_baru = nilai * 2
    return fungsi_a(nilai_baru - 4) # Panggil fungsi_a

# Panggil fungsi_b dengan nilai yang menyebabkan pembagian nol di fungsi_a
print("Mencoba memanggil fungsi...")
try:
   # Panggilan fungsi_b(2) akan menyebabkan fungsi_a dipanggil dengan angka = 0
   hasil_akhir = fungsi_b(2)
   print(f"Hasil: {hasil_akhir}")
except ZeroDivisionError as e:
   print(f"\nTerjadi Error: {e}")
   print("--- Contoh Traceback (jika tidak pakai try-except) ---")
   # Jika baris di bawah ini dijalankan tanpa try-except, traceback akan muncul:
   # Traceback (most recent call last):
   #   File "Bab_11/01_contoh_traceback.py", line 13, in <module>
   #     hasil_akhir = fungsi_b(2)
   #   File "Bab_11/01_contoh_traceback.py", line 7, in fungsi_b
   #     return fungsi_a(nilai_baru - 4)
   #   File "Bab_11/01_contoh_traceback.py", line 2, in fungsi_a
   #     hasil = 10 / angka
   # ZeroDivisionError: division by zero
