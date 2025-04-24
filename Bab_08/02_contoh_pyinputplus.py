import pyinputplus as pyip

# Contoh inputInt dengan batasan
usia = pyip.inputInt(prompt="Masukkan usia Anda (antara 1-100): ", min=1, max=100)
print(f"Usia valid: {usia}")

# Contoh inputChoice
pilihan_warna = pyip.inputChoice(['merah', 'kuning', 'hijau'], prompt="Pilih warna favorit: ")
print(f"Warna dipilih: {pilihan_warna}")

# Contoh inputYesNo
setuju = pyip.inputYesNo(prompt="Apakah Anda setuju? (yes/no): ")
print(f"Jawaban: {setuju}")

# Contoh inputEmail
email = pyip.inputEmail(prompt="Masukkan alamat email Anda: ")
print(f"Email valid: {email}")

# Contoh inputStr dengan blockRegexes
respons = pyip.inputStr(
    prompt="Masukkan komentar Anda (jangan pakai kata 'bodoh'): ",
    blockRegexes=[(r'bodoh', 'Kata-kata kasar tidak diizinkan!')]
)
print(f"Komentar diterima: {respons}")

# Contoh inputNum dengan limit dan default
nomor_keberuntungan = pyip.inputNum(
    prompt="Tebak angka keberuntungan (1-10, maks 3x coba): ",
    min=1, max=10, limit=3, default="Gagal Menebak"
)
print(f"Hasil tebakan: {nomor_keberuntungan}")

# Contoh inputPassword
password_rahasia = pyip.inputPassword(prompt="Masukkan password Anda: ")
print("Password diterima (tapi tidak ditampilkan di sini).")
