
import os
import json

# Lokasi folder gambar di laptop
folder_gambar = r"D:\PERKULIAHAN\SEMESTER 5\PEMROGRAMAN MOBILE\JSON\Tokyo卍Revengers 1 - Chapter 1"

# URL dasar folder gambar di GitHub
url_dasar = "https://raw.githubusercontent.com/AisyaUTondu/komik_kelompok3_komu/0b49b2a04cf1021a8e478ed8c9e5f5b464945ff4/Tokyo%E5%8D%8DRevengers%201%20-%20Chapter%201"

# Ekstensi gambar
ekstensi = (".jpg", ".jpeg", ".png", ".webp")

# Periksa apakah folder tersedia
if not os.path.isdir(folder_gambar):
    print("Folder gambar tidak ditemukan!")
else:
    # Ambil semua file gambar dan urutkan
    daftar_file = sorted([
        file for file in os.listdir(folder_gambar)
        if file.lower().endswith(ekstensi)
    ])

    # Buat URL gambar otomatis
    daftar_url = [
        f"{url_dasar}/{file}"
        for file in daftar_file
    ]

    # Susun data JSON
    data = {
        "chapter": "Tokyo Revengers - Chapter 1",
        "halaman": daftar_url
    }

    # Simpan JSON
    with open("chapter1.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("JSON berhasil dibuat!")
    print(f"Jumlah gambar: {len(daftar_file)}")
