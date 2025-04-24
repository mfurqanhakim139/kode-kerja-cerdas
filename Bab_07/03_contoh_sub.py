import re

# Pola: sensor nama agen (tangkap huruf pertama di grup 1)
pola_sensor = re.compile(r'agen (\w)\w*')
teks_rahasia = "Info dari agen Alex: agen Cindy dalam bahaya."

# Ganti nama agen dengan inisial (dari grup 1 -> \1) diikuti ***
teks_tersensor = pola_sensor.sub(r'agen \1***', teks_rahasia)

print(f"Teks asli: {teks_rahasia}")
print(f"Teks tersensor: {teks_tersensor}")
