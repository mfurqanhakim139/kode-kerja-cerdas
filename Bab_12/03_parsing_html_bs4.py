import requests
import bs4 # Nama modulnya bs4

# Contoh URL halaman sederhana (gunakan URL target Anda)
# url = 'https://contoh-halaman-scraping.com' # Ganti dengan URL asli
# Untuk demo, kita pakai HTML string sederhana:
html_contoh = """
<html><head><title>Halaman Contoh</title></head>
<body>
<div id="konten-utama">
    <h1>Judul Artikel Utama</h1>
    <p class="paragraf-pembuka">Ini adalah paragraf pembuka artikel.</p>
    <p>Ini paragraf kedua, berisi <a href="https://example.com">tautan penting</a>.</p>
    <div class="info-tambahan">
        <p>Info tidak relevan.</p>
        <a href="/halaman-lain">Tautan lain</a>
    </div>
</div>
<div id="sidebar">
    <h2>Sidebar</h2>
    <ul>
        <li><a href="/link1" class="link-sidebar">Link 1</a></li>
        <li><a href="/link2" class="link-sidebar">Link 2</a></li>
    </ul>
</div>
</body></html>
"""

# Buat objek Soup
soup = bs4.BeautifulSoup(html_contoh, 'html.parser')

# 1. Cari judul (tag <h1>)
judul_element = soup.select_one('h1') # select_one() untuk mengambil elemen pertama saja
if judul_element:
    judul_teks = judul_element.getText().strip()
    print(f"Judul Halaman: {judul_teks}")
else:
    print("Judul (h1) tidak ditemukan.")

# 2. Cari semua paragraf di dalam div utama (id=konten-utama)
paragraf_utama = soup.select('#konten-utama p')
print(f"\nParagraf di Konten Utama ({len(paragraf_utama)}):")
for p in paragraf_utama:
    print(f"- {p.getText().strip()}")

# 3. Cari semua link (tag <a> dengan atribut href) di dalam sidebar
link_sidebar = soup.select('#sidebar a[href]')
print(f"\nLink di Sidebar ({len(link_sidebar)}):")
for link in link_sidebar:
    teks_link = link.getText().strip()
    url_link = link.get('href') # Ambil nilai atribut href
    print(f"- Teks: {teks_link}, URL: {url_link}")

# 4. Cari paragraf dengan kelas spesifik
paragraf_pembuka = soup.select_one('p.paragraf-pembuka') # Tag p dengan class paragraf-pembuka
if paragraf_pembuka:
    print(f"\nParagraf Pembuka: {paragraf_pembuka.getText().strip()}")
