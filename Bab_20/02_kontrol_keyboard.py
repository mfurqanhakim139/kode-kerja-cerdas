import pyautogui
import time
import sys

# --- Pengamanan WAJIB ---
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2 # Jeda lebih singkat antar penekanan tombol

print("Script akan dimulai dalam 3 detik...")
print("Pastikan FOKUS ada di text editor KOSONG!")
time.sleep(3)

try:
    # Mengetik string
    print("Mengetik teks...")
    pyautogui.write('Halo dari PyAutoGUI!', interval=0.05)

    # Menekan Enter
    print("Menekan Enter...")
    pyautogui.press('enter')

    pyautogui.write('Ini baris kedua.', interval=0.05)
    pyautogui.press('enter')

    # Menekan tombol spesial
    print("Menekan beberapa tombol spesial...")
    pyautogui.press('f1') # Mungkin membuka help?
    time.sleep(0.5)
    pyautogui.press('esc') # Menutup help?
    time.sleep(0.5)

    # Mengetik angka
    pyautogui.press(['1', '2', '3', 'enter']) # Tekan tombol 1, 2, 3, lalu enter

    # Menahan Shift untuk mengetik huruf besar
    print("Mengetik huruf besar...")
    pyautogui.keyDown('shift') # Tahan Shift
    pyautogui.press('a')
    pyautogui.press('b')
    pyautogui.press('c')
    pyautogui.keyUp('shift') # Lepas Shift
    pyautogui.press('enter')

    # Menggunakan hotkey (Contoh: Select All -> Ctrl+A)
    print("Mencoba Ctrl+A (Select All)...")
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    # Contoh lain: Copy (Ctrl+C)
    # pyautogui.hotkey('ctrl', 'c')

    # Contoh: Membuka Run dialog (Win+R) di Windows
    # if sys.platform == 'win32':
    #     print("Mencoba Win+R...")
    #     pyautogui.hotkey('win', 'r')
    #     time.sleep(1)
    #     pyautogui.write('notepad') # Ketik notepad
    #     pyautogui.press('enter')

    print("\nDemo kontrol keyboard selesai.")

except pyautogui.FailSafeException:
    print("FAILSAFE terpicu! Script dihentikan.")
except Exception as e:
    print(f"Terjadi error: {e}")
