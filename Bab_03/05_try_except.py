# Contoh penanganan kesalahan dengan try...except

print("Program pembagian dua angka.")
angka1_str = input("Masukkan angka pertama: ")
angka2_str = input("Masukkan angka kedua: ")

try:
    # Blok kode yang berpotensi error
    print("Mencoba melakukan konversi dan pembagian...")
    angka1 = int(angka1_str) # Potensi ValueError
    angka2 = int(angka2_str) # Potensi ValueError
    hasil = angka1 / angka2  # Potensi ZeroDivisionError
    print(f"Hasil {angka1} / {angka2} = {hasil}")

except ValueError:
    # Kode ini dijalankan jika terjadi ValueError di blok try
    print("Error: Input tidak valid. Pastikan Anda memasukkan angka saja.")

except ZeroDivisionError:
    # Kode ini dijalankan jika terjadi ZeroDivisionError di blok try
    print("Error: Tidak bisa membagi dengan nol!")

except Exception as e: 
    # Menangkap semua jenis error lain yang tidak terduga
    print(f"Terjadi error tak terduga: {e}")
    print(f"Tipe error: {type(e)}")

finally:
     # Blok finally (opsional) selalu dijalankan, baik ada error maupun tidak
     print("Blok finally dieksekusi.")

print("\nProgram selesai.") # Program tetap lanjut setelah except/finally
