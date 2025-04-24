import ezsheets
import datetime

ID_atau_URL_atau_Judul =  "1GNokDQToXnEmcd8PZ6LJxEb5CbOL5s6ALVHAmaTXpX8"

try:
    ss = ezsheets.Spreadsheet(ID_atau_URL_atau_Judul)
    sheet = ss[0] # Ambil sheet pertama
    print(f"Menulis ke sheet: {sheet.title}")

    # Tulis ke cell A1
    timestamp = datetime.datetime.now().isoformat()
    sheet['A1'] = f"Update Terakhir: {timestamp}"
    print("Menulis timestamp ke A1.")

    # Update baris ke-5 (misalnya)
    data_baris_5 = ['Data', 'Untuk', 'Baris', 'Lima']
    sheet.updateRow(5, data_baris_5)
    print("Memperbarui baris 5.")

    # Update kolom F (misalnya)
    data_kolom_f = ['Header F', 'Data F1', 'Data F2', 'Data F3']
    sheet.updateColumn('F', data_kolom_f) # atau updateColumn(6, ...)
    print("Memperbarui kolom F.")

    print("\nPenulisan selesai. Cek Google Sheet Anda.")

except Exception as e:
    print(f"Gagal menulis data. Error: {e}")

