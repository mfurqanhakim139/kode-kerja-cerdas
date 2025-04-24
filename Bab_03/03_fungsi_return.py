def kuadrat(angka):
    hasil = angka * angka
    return hasil # Mengembalikan nilai hasil

def sapa_formal(nama):
    if nama == "Presiden":
        return "Salam hormat!" # Mengembalikan string
    # Jika tidak return di atas, fungsi akan selesai dan return None secara implisit

# Menggunakan nilai kembali
nilai_kuadrat_5 = kuadrat(5) # Panggil fungsi, simpan hasilnya di variabel
print(f"Kuadrat dari 5 adalah: {nilai_kuadrat_5}")
print(f"Kuadrat dari 10 adalah: {kuadrat(10)}") # Langsung digunakan di print

salam_presiden = sapa_formal("Presiden")
print(salam_presiden)

salam_biasa = sapa_formal("Budi")
print(salam_biasa) # Akan mencetak None
