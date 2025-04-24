# Definisi Class FilePengelola untuk mengelola file dalam folder
from pathlib import Path
import glob # Untuk pencarian pola sederhana
import os # Diperlukan jika ingin menggunakan os.rename atau fitur os lain

class FilePengelola:
    """Class untuk mengelola operasi file dasar dalam sebuah folder target."""

    def __init__(self, path_folder_target):
        """
        Inisialisasi FilePengelola.

        Args:
            path_folder_target (str atau Path): Path ke folder yang akan dikelola.
        """
        try:
            # Simpan path absolut dan pastikan valid
            self.folder_target = Path(path_folder_target).resolve()

            # Pastikan folder target ada saat objek dibuat
            if not self.folder_target.is_dir():
                # Opsi 1: Buat jika belum ada
                print(f"Folder '{self.folder_target}' tidak ditemukan, mencoba membuat...")
                self.folder_target.mkdir(parents=True, exist_ok=True)
                print(f"Folder '{self.folder_target}' berhasil dibuat.")
                # Opsi 2: Raise error jika harus sudah ada
                # raise FileNotFoundError(f"Folder target '{self.folder_target}' tidak ditemukan atau bukan direktori.")

            print(f"FilePengelola untuk folder '{self.folder_target}' siap.")

        except TypeError as e:
             print(f"Error inisialisasi: Path folder tidak valid - {e}")
             # Mungkin raise error agar objek tidak dibuat dalam keadaan tidak valid
             raise ValueError(f"Path folder tidak valid: {path_folder_target}") from e
        except OSError as e:
             print(f"Error sistem file saat inisialisasi untuk '{path_folder_target}': {e}")
             raise # Re-raise OS error

    def daftar_file(self, hanya_file=True):
        """
        Mengembalikan list nama file (dan/atau folder) di folder target.

        Args:
            hanya_file (bool): Jika True, hanya kembalikan nama file.
                               Jika False, kembalikan nama file dan folder.

        Returns:
            list: List berisi nama item (string). Kosong jika error.
        """
        items = []
        try:
            # iterdir() menghasilkan objek Path untuk setiap item
            for item_path in self.folder_target.iterdir():
                if hanya_file:
                    if item_path.is_file():
                        items.append(item_path.name)
                else: # Jika tidak hanya_file, tambahkan semua (file dan folder)
                    items.append(item_path.name)
            return items
        except FileNotFoundError:
            print(f"Error: Folder target '{self.folder_target}' tidak ditemukan saat mendaftar file.")
            return []
        except PermissionError:
            print(f"Error: Tidak ada izin untuk membaca isi folder '{self.folder_target}'.")
            return []
        except Exception as e:
            print(f"Error tak terduga saat membaca isi folder: {e}")
            return []

    def hitung_item(self, hanya_file=True):
        """
        Menghitung jumlah file (atau semua item) di folder target.

        Args:
            hanya_file (bool): Sama seperti di daftar_file.

        Returns:
            int: Jumlah item yang ditemukan.
        """
        # Langsung panggil daftar_file dan hitung hasilnya
        return len(self.daftar_file(hanya_file=hanya_file))

    def cari_file_pola(self, pola):
        """
        Mencari file yang cocok dengan pola glob sederhana (misal: '*.txt', 'data_*.csv').

        Args:
            pola (str): Pola glob untuk pencarian.

        Returns:
            list: List berisi nama file yang cocok (string). Kosong jika error.
        """
        hasil_cocok = []
        try:
            # Path.glob() menghasilkan generator objek Path
            for item_path in self.folder_target.glob(pola):
                # Pastikan hanya file yang dimasukkan (glob bisa cocok dengan folder juga)
                if item_path.is_file():
                    hasil_cocok.append(item_path.name)
            return hasil_cocok
        except Exception as e:
            print(f"Error saat mencari pola '{pola}': {e}")
            return []

    def buat_subfolder(self, nama_subfolder):
        """
        Membuat subfolder baru di dalam folder target.

        Args:
            nama_subfolder (str): Nama subfolder yang ingin dibuat.

        Returns:
            bool: True jika berhasil dibuat atau sudah ada, False jika gagal.
        """
        # Validasi nama subfolder sederhana (opsional)
        if not nama_subfolder or '/' in nama_subfolder or '\\' in nama_subfolder:
             print(f"Error: Nama subfolder '{nama_subfolder}' tidak valid.")
             return False

        path_subfolder = self.folder_target / nama_subfolder
        try:
            # exist_ok=True agar tidak error jika folder sudah ada
            path_subfolder.mkdir(exist_ok=True)
            print(f"Subfolder '{nama_subfolder}' berhasil dibuat/sudah ada di '{self.folder_target}'.")
            return True
        except OSError as e:
            print(f"Gagal membuat subfolder '{nama_subfolder}': {e}")
            return False
        except Exception as e:
             print(f"Error tak terduga saat membuat subfolder: {e}")
             return False

    # --- Contoh Metode Tambahan (bisa ditambahkan nanti) ---

    # def pindahkan_file(self, nama_file_sumber, tujuan):
    #     """Memindahkan file dari folder target ke tujuan (bisa folder lain atau nama baru)."""
    #     sumber_path = self.folder_target / nama_file_sumber
    #     tujuan_path = Path(tujuan) # Bisa path absolut atau relatif
    #     # ... (tambahkan logika cek file ada, handle error, gunakan shutil.move) ...
    #     pass

    # def hapus_file(self, nama_file, ke_trash=True):
    #     """Menghapus file di folder target (opsional ke trash)."""
    #     file_path = self.folder_target / nama_file
    #     # ... (tambahkan logika cek file ada, handle error, gunakan file_path.unlink() atau send2trash) ...
    #     pass

# --- Contoh Penggunaan (biasanya di file terpisah) ---
if __name__ == "__main__":
    print("Contoh penggunaan FilePengelola:")

    # Buat objek untuk folder 'Dokumen_Tes' (akan dibuat jika belum ada)
    try:
        pengelola_docs = FilePengelola('Dokumen_Tes')

        # Buat beberapa file dummy untuk tes
        (pengelola_docs.folder_target / 'laporan_q1.txt').touch()
        (pengelola_docs.folder_target / 'gambar.jpg').touch()
        (pengelola_docs.folder_target / 'data_penting.csv').touch()
        (pengelola_docs.folder_target / 'subfolder_lama').mkdir(exist_ok=True)

        print("\n--- Operasi pada Dokumen_Tes ---")
        print(f"Jumlah file: {pengelola_docs.hitung_item(hanya_file=True)}")
        print(f"Jumlah semua item: {pengelola_docs.hitung_item(hanya_file=False)}")
        print(f"Daftar file: {pengelola_docs.daftar_file()}")
        print(f"Daftar semua item: {pengelola_docs.daftar_file(hanya_file=False)}")
        print(f"Cari file *.txt: {pengelola_docs.cari_file_pola('*.txt')}")
        print(f"Cari file data*: {pengelola_docs.cari_file_pola('data_*')}")
        pengelola_docs.buat_subfolder('Arsip_2025')
        pengelola_docs.buat_subfolder('Gambar_Cadangan')

    except ValueError as ve:
         print(f"Gagal membuat objek FilePengelola: {ve}")
    except Exception as e:
         print(f"Terjadi error saat menjalankan contoh: {e}")

