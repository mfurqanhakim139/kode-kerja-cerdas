import PyPDF2
from pathlib import Path

# Buat file PDF contoh sederhana jika Anda tidak punya
# (membutuhkan library lain seperti reportlab, atau gunakan PDF yang sudah ada)
# Untuk demo ini, asumsikan Anda sudah punya file bernama 'contoh.pdf'

nama_file_pdf = 'contoh.pdf' # Ganti dengan nama file PDF Anda
path_pdf = Path(nama_file_pdf)

if path_pdf.exists() and path_pdf.is_file():
    print(f"Mencoba membaca file PDF: {nama_file_pdf}")
    try:
        # 1. Buka file dalam mode 'rb'
        with open(path_pdf, 'rb') as file_pdf:
            # 2. Buat objek reader
            reader = PyPDF2.PdfReader(file_pdf)

            # 3. Dapatkan jumlah halaman
            jumlah_halaman = len(reader.pages)
            print(f"Jumlah halaman: {jumlah_halaman}")

            # 4. & 5. Ekstrak teks dari halaman pertama (indeks 0)
            if jumlah_halaman > 0:
                halaman_pertama = reader.pages[0]
                try:
                    teks_halaman_1 = halaman_pertama.extract_text()
                    if teks_halaman_1:
                        print("\nTeks dari Halaman 1 (beberapa baris pertama):")
                        # Cetak beberapa baris awal saja
                        for i, baris in enumerate(teks_halaman_1.splitlines()):
                            if i < 5: # Batasi 5 baris
                                print(baris)
                            else:
                                print("...")
                                break
                    else:
                        print("\nTidak ada teks yang bisa diekstrak dari halaman 1 (mungkin gambar?).")
                except Exception as e_extract:
                     print(f"\nError saat ekstraksi teks: {e_extract}")

            # Contoh loop untuk semua halaman (hati-hati bisa lambat untuk PDF besar)
            # print("\nMengekstrak semua halaman:")
            # for i in range(jumlah_halaman):
            #     halaman = reader.pages[i]
            #     teks = halaman.extract_text()
            #     print(f"--- Halaman {i+1} ---")
            #     print(teks[:100] + '...' if teks else '[Tidak ada teks]') # Cetak 100 char pertama

    except Exception as e:
        print(f"Gagal memproses PDF: {e}")
else:
    print(f"File PDF '{nama_file_pdf}' tidak ditemukan atau bukan file.")

