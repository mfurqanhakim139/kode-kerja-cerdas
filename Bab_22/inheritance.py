# Definisi Class PengelolaGambar yang mewarisi dari FilePengelola
# dan contoh penggunaannya.

# Perlu install: pip install Pillow
# Pastikan juga class FilePengelola sudah didefinisikan di file yang benar.

from pathlib import Path
from PIL import Image, ImageDraw # Diperlukan untuk membuat dummy image & proses gambar
import sys
import os

# --- Asumsi Definisi FilePengelola ---
# Agar skrip ini bisa berjalan mandiri untuk demonstrasi,
# kita bisa sertakan definisi FilePengelola di sini atau mengimpornya.
# Untuk struktur buku yang benar, impor lebih disarankan.

try:
    # Mengasumsikan struktur folder dan file dari Bab 22
    # Pastikan ada Bab_22/__init__.py (kosong)
    # dan Bab_22/01_definisi_class_filepengelola.py berisi class FilePengelola
    from definisi_class_filepengelola import FilePengelola
    print("INFO: Berhasil mengimpor FilePengelola.")
except ImportError:
    print("="*50)
    print("PERINGATAN: Gagal mengimpor 'FilePengelola'.")
    print("Membuat definisi dummy FilePengelola agar skrip bisa lanjut.")
    print("Pastikan definisi asli ada di 'Bab_22/01_definisi_class_filepengelola.py'.")
    print("="*50)
    # Definisi dummy jika import gagal
    class FilePengelola:
        def __init__(self, path_folder_target):
            self.folder_target = Path(path_folder_target).resolve()
            self.folder_target.mkdir(parents=True, exist_ok=True)
            print(f"(Dummy) FilePengelola untuk folder '{self.folder_target}' siap.")
        def daftar_file(self, hanya_file=True):
            print("(Dummy) daftar_file dipanggil")
            # Kembalikan list kosong agar tidak error di loop PengelolaGambar
            return []
# ------------------------------------

class PengelolaGambar(FilePengelola): # Mewarisi dari FilePengelola
    """Class khusus untuk mengelola file gambar di folder target."""

    def __init__(self, path_folder_target):
        """
        Inisialisasi PengelolaGambar.

        Args:
            path_folder_target (str atau Path): Path ke folder gambar yang akan dikelola.
        """
        # Panggil __init__ dari class induk (FilePengelola) untuk setup folder
        super().__init__(path_folder_target)
        print("PengelolaGambar siap.")

    def daftar_file_gambar(self):
        """
        Mengembalikan list nama file gambar yang didukung Pillow di folder target.
        """
        gambar = []
        # Daftar ekstensi umum yang didukung Pillow (bisa ditambah)
        ekstensi_gambar = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']
        try:
            # Gunakan metode daftar_file dari class induk
            for nama_file in self.daftar_file(hanya_file=True):
                # Dapatkan ekstensi file (suffix) dan ubah ke lowercase
                ekstensi = Path(nama_file).suffix.lower()
                if ekstensi in ekstensi_gambar:
                    gambar.append(nama_file)
            return gambar
        except Exception as e:
             print(f"Error saat mendaftar file gambar: {e}")
             return []

    def ubah_ukuran_semua(self, lebar_baru, folder_output_relatif):
        """
        Mengubah ukuran semua gambar di folder target dan simpan ke subfolder output.

        Args:
            lebar_baru (int): Lebar baru gambar dalam piksel. Tinggi akan disesuaikan proporsional.
            folder_output_relatif (str): Nama subfolder di dalam folder target untuk menyimpan hasil resize.
        """
        # Buat path absolut untuk folder output di dalam folder target
        path_output = self.folder_target / folder_output_relatif
        try:
            path_output.mkdir(exist_ok=True) # Buat folder output jika belum ada
            print(f"\nMengubah ukuran gambar ke lebar {lebar_baru}px, simpan ke '{path_output}'...")

            file_gambar_list = self.daftar_file_gambar()
            if not file_gambar_list:
                print("Tidak ada file gambar yang ditemukan untuk diubah ukurannya.")
                return

            processed_count = 0
            for nama_file in file_gambar_list:
                img_path = self.folder_target / nama_file
                path_simpan = path_output / f"resized_{nama_file}" # Nama file output

                try:
                    # Buka gambar menggunakan 'with' agar file tertutup otomatis
                    with Image.open(img_path) as img:
                        # Pastikan gambar bisa dibaca (beberapa file mungkin rusak)
                        img.verify()
                    # Perlu dibuka lagi setelah verify
                    with Image.open(img_path) as img:
                        if img.width == 0 or img.height == 0:
                             print(f" -> Melewati {nama_file}: Ukuran tidak valid (0).")
                             continue
                        # Hitung tinggi baru agar rasio aspek terjaga
                        rasio = lebar_baru / img.width
                        tinggi_baru = int(img.height * rasio)

                        # Lakukan resize
                        print(f" -> Memproses {nama_file} ({img.width}x{img.height}) -> ({lebar_baru}x{tinggi_baru})")
                        img_resized = img.resize((lebar_baru, tinggi_baru))

                        # Simpan gambar hasil resize
                        # Pillow otomatis deteksi format dari ekstensi path_simpan
                        img_resized.save(path_simpan)
                        processed_count += 1
                except FileNotFoundError:
                     print(f" -> Gagal: File {nama_file} tidak ditemukan saat diproses.")
                except Exception as e:
                    # Tangkap error spesifik saat memproses satu gambar
                    print(f" -> Gagal memproses {nama_file}: {e}")

            print(f"\nProses ubah ukuran selesai. {processed_count} gambar diproses.")

        except Exception as e:
            print(f"Error saat proses ubah ukuran semua: {e}")

# --- Contoh Penggunaan ---
if __name__ == "__main__":
    print("\nMenjalankan contoh penggunaan PengelolaGambar...")
    folder_liburan = 'Gambar_Liburan_Tes' # Gunakan folder tes terpisah

    try:
        # Buat objek PengelolaGambar
        pengelola_foto = PengelolaGambar(folder_liburan)

        # --- Persiapan: Buat file gambar dummy untuk tes ---
        print("\nMembuat file gambar dummy untuk tes...")
        dummy_files_created = 0
        for i, ext in enumerate(['.jpg', '.png', '.gif', '.txt']): # Tambah .txt untuk non-gambar
             nama_dummy = f"foto_dummy_{i+1}{ext}"
             path_dummy = pengelola_foto.folder_target / nama_dummy
             if not path_dummy.exists():
                 if ext != '.txt':
                     # Buat gambar berwarna sederhana
                     try:
                         img_dummy = Image.new('RGB', (50, 50), color = f'hsl({i*60}, 80%, 60%)')
                         d = ImageDraw.Draw(img_dummy)
                         d.text((5,5), f"Dummy {i+1}", fill=(255,255,255))
                         img_dummy.save(path_dummy)
                         print(f" - Membuat gambar dummy: {nama_dummy}")
                         dummy_files_created += 1
                     except Exception as e_dummy:
                          print(f" - Gagal membuat gambar dummy {nama_dummy}: {e_dummy}")
                 else:
                      # Buat file teks biasa
                      path_dummy.write_text(f"Ini file teks dummy {i+1}")
                      print(f" - Membuat file teks dummy: {nama_dummy}")
                      dummy_files_created += 1
             else:
                  print(f" - File dummy '{nama_dummy}' sudah ada.")
        if dummy_files_created > 0:
             print("File dummy selesai dibuat.")
        # ----------------------------------------------------

        # Gunakan metode dari PengelolaGambar
        print("\n--- Operasi pada Folder Gambar ---")
        daftar_gambar = pengelola_foto.daftar_file_gambar() # Hanya ambil file gambar
        print(f"Daftar file gambar ditemukan: {daftar_gambar if daftar_gambar else '(Tidak ada)'}")

        # Ubah ukuran semua gambar yang ditemukan
        if daftar_gambar:
            pengelola_foto.ubah_ukuran_semua(lebar_baru=100, folder_output_relatif='Hasil_Resize')
        else:
             print("\nTidak ada gambar untuk diubah ukurannya.")

    except ValueError as ve:
         print(f"Gagal membuat objek PengelolaGambar: {ve}")
    except ImportError:
         print("Error: Gagal menjalankan karena Pillow tidak terinstal. Silakan install: pip install Pillow")
    except Exception as e:
         print(f"Terjadi error saat menjalankan contoh PengelolaGambar: {e}")

    print("\nContoh PengelolaGambar selesai.")
