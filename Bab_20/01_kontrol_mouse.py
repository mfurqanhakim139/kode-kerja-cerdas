import pyautogui
import time

# --- Pengamanan WAJIB ---
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5 # Jeda 0.5 detik antar aksi

print("Script akan dimulai dalam 3 detik... Siapkan failsafe (gerakkan mouse ke kiri atas)!")
time.sleep(3)

try:
    # Dapatkan ukuran layar
    lebar_layar, tinggi_layar = pyautogui.size()
    print(f"Ukuran layar: {lebar_layar}x{tinggi_layar}")

    # Dapatkan posisi mouse saat ini
    x_awal, y_awal = pyautogui.position()
    print(f"Posisi mouse awal: ({x_awal}, {y_awal})")

    # Gerakkan mouse ke tengah layar selama 1 detik
    x_tengah, y_tengah = lebar_layar // 2, tinggi_layar // 2
    print(f"Menggerakkan ke tengah ({x_tengah}, {y_tengah})...")
    pyautogui.moveTo(x_tengah, y_tengah, duration=1)

    # Klik kiri di tengah layar
    print("Klik kiri...")
    pyautogui.click(x_tengah, y_tengah) # atau pyautogui.click() saja

    # Gerakkan relatif ke kanan bawah
    print("Gerak relatif...")
    pyautogui.moveRel(100, 50, duration=0.5)

    # Klik kanan di posisi baru
    print("Klik kanan...")
    pyautogui.rightClick()

    # Contoh scroll ke bawah (misal di text editor/browser)
    # print("Scroll ke bawah...")
    # pyautogui.scroll(-300) # Angka negatif = ke bawah
    # time.sleep(1)
    # print("Scroll ke atas...")
    # pyautogui.scroll(300) # Angka positif = ke atas

    # Kembali ke posisi awal
    print("Kembali ke posisi awal...")
    pyautogui.moveTo(x_awal, y_awal, duration=1)

    print("\nDemo kontrol mouse selesai.")

except pyautogui.FailSafeException:
    print("FAILSAFE terpicu! Script dihentikan.")
except Exception as e:
    print(f"Terjadi error: {e}")
