# Contoh Konseptual Menggunakan Twilio (Memerlukan Akun & Kredensial Twilio)
from twilio.rest import Client

# --- Konfigurasi Twilio (AMBIL DARI AKUN TWILIO ANDA & SIMPAN SECARA AMAN!) ---
account_sid = '' # Ganti
auth_token = '' # Ganti
nomor_twilio = '+' # Ganti dengan nomor Twilio Anda
nomor_tujuan = '+' # Ganti dengan nomor tujuan Anda

try:
    # Buat client Twilio
    client = Client(account_sid, auth_token)

    # Kirim pesan
    pesan_sms = client.messages.create(
                              body="Halo dari script Python via Twilio!",
                              from_=nomor_twilio,
                              to=nomor_tujuan
                          )

    print(f"Pesan dikirim! SID Pesan: {pesan_sms.sid}")

except Exception as e:
    print(f"Gagal mengirim SMS via Twilio: {e}")

