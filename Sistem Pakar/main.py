import json

# baca file basis pengetahuan
file_kb = open("kb.json", "r", encoding="utf-8")
kb = json.load(file_kb)
file_kb.close()

aturan_aturan = kb["aturan"]

# cari daftar pertanyaan (syarat yang tidak pernah menjadi hasil)
semua_hasil = []
for aturan in aturan_aturan:
    semua_hasil.append(aturan["maka"])

pertanyaan = []
for aturan in aturan_aturan:
    for syarat in aturan["syarat"]:
        if syarat not in semua_hasil and syarat not in pertanyaan:
            pertanyaan.append(syarat)

print(f"=== {kb['judul']} ===")
print("Jawab dengan y (ya) atau t (tidak).\n")

# mulai tanya ke user
fakta_terkumpul = []
nomor = 1

for p in pertanyaan:
    jawaban = input(f"{nomor}. Apakah {p}? (y/t) > ")
    if jawaban.lower() == "y":
        fakta_terkumpul.append(p)
    nomor += 1

print("\nFakta di lapangan:", fakta_terkumpul)
print("-" * 50)

# proses penalaran (forward chaining)
print("Mulai proses penalaran...\n")
riwayat_alasan = []
siklus = 1

while True:
    ada_aturan_baru = False
    
    for aturan in aturan_aturan:
        hasil = aturan["maka"]
        
        # lewati kalau hasilnya sudah ada di fakta terkumpul
        if hasil in fakta_terkumpul:
            continue
            
        syarat_terpenuhi = False
        
        # cek kecocokan syarat berdasarkan mode
        if aturan["mode"] == "dan":
            syarat_terpenuhi = True
            for s in aturan["syarat"]:
                if s not in fakta_terkumpul:
                    syarat_terpenuhi = False
                    
        elif aturan["mode"] == "atau":
            syarat_terpenuhi = False
            for s in aturan["syarat"]:
                if s in fakta_terkumpul:
                    syarat_terpenuhi = True
        
        # jika syarat cocok, simpan hasil dan alasannya
        if syarat_terpenuhi == True:
            fakta_terkumpul.append(hasil)
            riwayat_alasan.append(aturan)
            print(f"Siklus {siklus}: Aturan {aturan['id']} cocok -> Disimpulkan: {hasil}")
            
            ada_aturan_baru = True
            siklus += 1
            break 
            
    if ada_aturan_baru == False:
        break

print("-" * 50)

# penentuan kesimpulan akhir (hasil yang tidak dipakai lagi untuk syarat)
syarat_yang_dipakai = []
for alasan in riwayat_alasan:
    for s in alasan["syarat"]:
        syarat_yang_dipakai.append(s)

kesimpulan_akhir = []
for alasan in riwayat_alasan:
    hasil = alasan["maka"]
    if hasil not in syarat_yang_dipakai:
        kesimpulan_akhir.append(hasil)

# cetak hasil akhir beserta alasannya
if len(kesimpulan_akhir) > 0:
    print("KESIMPULAN AKHIR:")
    for k in kesimpulan_akhir:
        print(f"=> {k.upper()}")
        
    print("\nALASAN (Jejak Forward Chaining):")
    for alasan in riwayat_alasan:
        kata_hubung = f" {alasan['mode'].upper()} "
        syarat_gabungan = kata_hubung.join(alasan["syarat"])
        print(f"- Karena [{syarat_gabungan}], maka disimpulkan [{alasan['maka']}] (Sumber: {alasan['sumber']})")
else:
    print("KESIMPULAN AKHIR: Tidak Cukup Fakta Untuk Menyimpulkan Potensi Longsor.")

print("\nCATATAN:")
print(kb["batas"])

#baris ini untuk menahan CMD agar tidak langsung tertutup
input("\n[Tekan Enter untuk menutup program...]")