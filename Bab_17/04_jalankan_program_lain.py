# Menggunakan modul subprocess untuk menjalankan program eksternal dan skrip Python lain
import subprocess
import sys
import time
import os # Untuk mendapatkan path sistem (Windows)
from pathlib import Path # Untuk membuat file dummy

nama_script_dummy = 'script_dummy.py'
konten_script_dummy = """
import time
import datetime

print(f"({datetime.datetime.now()}) Halo dari script dummy!")
print("Script dummy akan tidur selama 3 detik...")
time.sleep(3)
print(f"({datetime.datetime.now()}) Script dummy selesai.")
"""

def jalankan_kalkulator_windows():
    """Mencoba menjalankan Kalkulator Windows."""
    if sys.platform != 'win32':
        print("Info: Melewati Kalkulator (hanya untuk Windows).")
        return None # Kembalikan None jika bukan Windows

    system_root = os.environ.get('SystemRoot', 'C:\\Windows')
    calc_path = os.path.join(system_root, 'System32', 'calc1.exe')

    print(f"\nMencoba menjalankan Kalkulator dari: {calc_path}")
    try:
        proses_calc = subprocess.Popen(calc_path)
        print(f"Kalkulator seharusnya sudah berjalan (Proses ID: {proses_calc.pid}).")
        return proses_calc # Kembalikan objek proses
    except FileNotFoundError:
        print(f"ERROR: Tidak dapat menemukan '{calc_path}'. Kalkulator tidak dijalankan.")
    except Exception as e:
        print(f"ERROR: Gagal menjalankan Kalkulator: {e}")
    return None # Kembalikan None jika gagal

def buat_dan_jalankan_script_dummy():
    """Membuat dan menjalankan script_dummy.py."""
    # --- Membuat file script dummy ---
    try:
        print(f"\nMembuat file '{nama_script_dummy}'...")
        path_dummy = Path(nama_script_dummy)
        path_dummy.write_text(konten_script_dummy, encoding='utf-8')
        print("File script dummy berhasil dibuat.")
    except Exception as e:
        print(f"Gagal membuat file script dummy: {e}")
        return None, None # Kembalikan None jika gagal buat file

    # --- Menjalankan script Python lain menggunakan subprocess ---
    proses_py = None
    try:
        print(f"\nMencoba menjalankan '{nama_script_dummy}'...")
        proses_py = subprocess.Popen([sys.executable, nama_script_dummy])
        print(f"Script '{nama_script_dummy}' telah dimulai di latar belakang (PID: {proses_py.pid}).")
    except FileNotFoundError:
         print(f"Error: Interpreter Python '{sys.executable}' atau script '{nama_script_dummy}' tidak ditemukan.")
    except Exception as e:
        print(f"Gagal menjalankan script Python lain: {e}")

    return proses_py, path_dummy # Kembalikan objek proses dan path

# --- Main Execution Block ---
if __name__ == "__main__":
    print("Memulai skrip utama...")

    # 1. Jalankan Kalkulator (hanya di Windows)
    proses_kalkulator = jalankan_kalkulator_windows()

    # 2. Buat dan Jalankan Script Dummy
    proses_dummy, path_script_dummy = buat_dan_jalankan_script_dummy()

    # 3. (Opsional) Tunggu script dummy selesai
    if proses_dummy:
        print("\nMenunggu script dummy selesai (proses_py.wait())...")
        try:
            return_code = proses_dummy.wait(timeout=10) # Tambahkan timeout (misal 10 detik)
            print(f"Script dummy telah selesai dengan kode keluar: {return_code}")
        except subprocess.TimeoutExpired:
            print("Script dummy melebihi batas waktu tunggu, mungkin masih berjalan.")
        except Exception as e:
            print(f"Error saat menunggu script dummy: {e}")

    # Kalkulator (jika dijalankan) akan tetap berjalan di latar belakang
    if proses_kalkulator:
         print("\nKalkulator (jika berhasil dijalankan) mungkin masih terbuka.")
         # Anda bisa menambahkan logika untuk menutupnya jika perlu,
         # misalnya proses_kalkulator.terminate() setelah jeda waktu

    # Cleanup (opsional)
    if path_script_dummy and path_script_dummy.exists():
        try:
            print("\nMembersihkan file dummy...")
            path_script_dummy.unlink(missing_ok=True) # Hapus file dummy
            print(f"File '{nama_script_dummy}' dihapus.")
        except Exception as e:
            print(f"Gagal membersihkan file dummy: {e}")

    print("\nSkrip utama selesai.")