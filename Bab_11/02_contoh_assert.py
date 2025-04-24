def hitung_diskon(harga, persen_diskon):
    # Asumsi programmer: persen diskon harus antara 0 dan 100
    assert 0 <= persen_diskon <= 100, 'Persen diskon harus antara 0 dan 100!'
    diskon = harga * (persen_diskon / 100)
    harga_akhir = harga - diskon
    return harga_akhir

harga_baju = 200000
diskon_valid = 10
diskon_tidak_valid = 110 # Ini seharusnya tidak terjadi

harga_setelah_diskon_valid = hitung_diskon(harga_baju, diskon_valid)
print(f"Harga setelah diskon {diskon_valid}%: Rp {harga_setelah_diskon_valid:,.0f}")

# Baris berikut akan menyebabkan AssertionError jika dijalankan:
try:
    print("\nMencoba diskon tidak valid...")
    harga_setelah_diskon_tidak_valid = hitung_diskon(harga_baju, diskon_tidak_valid)
    print(f"Harga setelah diskon {diskon_tidak_valid}%: Rp {harga_setelah_diskon_tidak_valid:,.0f}")
except AssertionError as e:
    print(f"AssertionError terpicu: {e}")

print("\nProgram selesai.")
