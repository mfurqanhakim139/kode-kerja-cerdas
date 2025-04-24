# Menggunakan modul smtplib untuk mengirim email
import smtplib
import sys
from email.mime.text import MIMEText # Untuk format email yang lebih baik (opsional tapi disarankan)

# --- Konfigurasi Server (Berdasarkan Detail Anda) ---
EMAIL_SAYA = '#####' # Alamat email pengirim
# --- !!! GANTI DENGAN PASSWORD ASLI ANDA (TAPI JANGAN SIMPAN DI KODE!) !!! ---
PASSWORD_SAYA = '####' # Ganti dengan password asli atau metode aman
# --------------------------------------------------------------------------
SMTP_HOST = '####' # Server SMTP Anda
SMTP_PORT = 465 # Port 465 biasanya untuk SSL

# --- Tujuan & Pesan ---
EMAIL_TUJUAN = 'mfurqanhakim139@gmail.com' # Ganti dengan alamat email tujuan
subjek = 'Tes Kirim Email dari Python '
isi_body = """Halo,

Ini adalah email otomatis yang dikirim menggunakan Python dan smtplib
melalui server 

Salam,
Script Python Anda
"""

# --- Format Pesan (Lebih Baik Menggunakan MIMEText) ---
# Ini membantu email terformat dengan benar dan mengurangi kemungkinan dianggap spam
msg = MIMEText(isi_body)
msg['Subject'] = subjek
msg['From'] = EMAIL_SAYA
msg['To'] = EMAIL_TUJUAN
pesan_lengkap = msg.as_string() # Konversi objek MIME ke string

# --- Kirim Email ---
smtp_obj = None # Inisialisasi di luar try
print(f"Mencoba menghubungkan ke server SMTP: {SMTP_HOST} port {SMTP_PORT} (SSL)...")
try:
    # Gunakan SMTP_SSL untuk koneksi SSL langsung (port 465)
    smtp_obj = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT)
    # ehlo() tidak selalu diperlukan secara eksplisit dengan SMTP_SSL,
    # tapi tidak masalah jika ditambahkan
    # smtp_obj.ehlo()

    print("Mencoba login...")
    # Login menggunakan email dan password
    smtp_obj.login(EMAIL_SAYA, PASSWORD_SAYA)
    print("Login berhasil.")

    print(f"Mengirim email ke {EMAIL_TUJUAN}...")
    # Kirim email menggunakan objek MIME yang sudah di-string
    smtp_obj.sendmail(EMAIL_SAYA, EMAIL_TUJUAN, pesan_lengkap)
    print("Email berhasil dikirim.")

except smtplib.SMTPAuthenticationError:
    print("Gagal login. Periksa email/password dan pengaturan keamanan akun.")
    print("Pastikan juga server mengizinkan login jenis ini.")
except smtplib.SMTPConnectError:
     print(f"Gagal terhubung ke server {SMTP_HOST}:{SMTP_PORT}. Periksa host/port atau koneksi jaringan.")
except smtplib.SMTPServerDisconnected:
     print("Koneksi ke server terputus secara tak terduga.")
except TimeoutError: # Atau socket.timeout jika Anda set timeout
     print("Koneksi ke server timeout.")
except Exception as e:
    print(f"Gagal mengirim email. Terjadi error lain: {e}")
    print(f"Tipe error: {type(e)}")
finally:
    # Selalu coba putuskan koneksi jika objeknya berhasil dibuat
    if smtp_obj:
        try:
            print("Memutuskan koneksi...")
            smtp_obj.quit()
        except Exception:
            pass # Abaikan jika sudah error sebelumnya

print("\nSkrip selesai.")