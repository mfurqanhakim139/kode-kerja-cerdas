# Contoh otomatisasi clipboard menggunakan pyperclip
# Instal dulu: pip install pyperclip
import pyperclip
import time
import datetime

try:
    # 1. Menyalin teks ke clipboard
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    teks_untuk_disalin = f"Ini teks dari Python! Disalin pada {timestamp}"

    pyperclip.copy(teks_untuk_disalin)
    print("--- COPY ---")
    print(f"Teks berikut telah disalin ke clipboard:")
    print(f"'{teks_untuk_disalin}'")
    print("\nSilakan coba paste (Ctrl+V atau Cmd+V) di aplikasi lain (notepad, browser, dll).")
    input("Tekan Enter di sini setelah Anda mencoba paste...")

    # 2. Mengambil (paste) teks dari clipboard
    print("\n--- PASTE ---")
    teks_dari_clipboard = pyperclip.paste()
    print(f"Teks yang berhasil diambil dari clipboard:")
    print(f"'{teks_dari_clipboard}'")

    # Contoh modifikasi teks clipboard
    if teks_dari_clipboard:
         clipboard_modifikasi = "[PYTHON] " + teks_dari_clipboard.upper() + " [/PYTHON]"
         pyperclip.copy(clipboard_modifikasi)
         print("\nTeks di clipboard telah dimodifikasi dan disalin ulang.")
         print("Silakan coba paste lagi.")

except pyperclip.PyperclipException as e:
    # Error spesifik dari pyperclip (misal tidak bisa akses clipboard)
    print(f"\nError Pyperclip: Tidak bisa mengakses clipboard.")
    print(f"Detail: {e}")
    print("Pastikan Anda memiliki akses ke clipboard atau coba instal 'xclip'/'xsel' di Linux.")
except Exception as e:
    # Error umum lainnya
    print(f"\nTerjadi error tak terduga: {e}")
