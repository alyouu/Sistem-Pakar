# Sistem Pakar
|Deteksi Potensi Bencana Hidrogeologi Tanah Longsor|

## 1. Nama dan NIM
- Nama: ALYA ZULFADILA
- NIM: F1D02510102

## 2. Topik dan Cara Menjalankan Program
**Topik:** Deteksi potensi bencana hidrogeologi berupa tanah longsor. Program bertanya beberapa gejala/fakta
di lapangan (dijawab `y`/`t`), lalu menarik kesimpulan kewaspadaan longsor dengan metode Forward Chaining.

- **Bahasa:** Python 3 (tanpa library eksternal)
- **File:** `kb.json` (basis pengetahuan) dan `main.py` (mesin inferensi)

**Cara menjalankan:**
```bash
python main.py
```
Program akan membaca `kb.json`, menanyakan 7 fakta dasar satu per satu, lalu mencetak
siklus inferensi, kesimpulan, alasan, dan catatan batas keberlakuan.

## 3. Daftar Sumber & Tabel Aturan
   
| Kode | Sumber |
|------|--------|

| S1 | 
Badan Nasional Penanggulangan Bencana (BNPB), *Pengenalan Karakteristik Bencana dan Upaya Mitigasinya*, https://bnpb.go.id/storage/app/media/uploads/migration/pubs/470.pdf, diakses 12 Nov 2026 |

| S2 | Kementerian Energi dan Sumber Daya Mineral (ESDM), *Pengenalan Gerakan Tanah*, https://www.esdm.go.id/assets/media/content/Pengenalan_Gerakan_Tanah.pdf, diakses 12 Nov 2026 |

| S3 | Suprapto, Ratih Nurmasari, Ainun Rosyida, "Analisis Penyebab Tanah Longsor di Kabupaten Ponorogo", *Jurnal Dialog Penanggulangan Bencana* Vol. 8 No. 2 (2017), BNPB, https://jdpb.bnpb.go.id/index.php/jurnal/article/download/121/121, diakses 12 Nov 2026 |

**Tabel aturan IF-THEN:**

| Aturan | IF | THEN | Sumber |
|--------|----|------|--------|
| R1 | IF hujan lebat berkepanjangan **ATAU** genangan air di lereng | THEN tanah jenuh air | S1, S2 |
| R2 | IF tanah jenuh air **DAN** tanah lempung tebal | THEN daya dukung tanah menurun | S1 |
| R3 | IF lereng curam **DAN** vegetasi jarang | THEN gaya penahan lereng lemah | S2 |
| R4 | IF daya dukung tanah menurun **ATAU** gaya penahan lereng lemah | THEN lereng tidak stabil | S1 |
| R5 | IF lereng tidak stabil **DAN** muncul retakan di permukaan tanah | THEN potensi tanah longsor tinggi | S3 |
| R6 | IF potensi tanah longsor tinggi **DAN** ada permukiman di kaki lereng | THEN evakuasi dini warga diperlukan | S3 |

*Catatan chaining:* hasil R1 dipakai R2, hasil R2 dan R3 dipakai R4, hasil R4 dipakai R5, hasil R5 dipakai R6.

## 4. Metode: Forward Chaining
Saya memilih **Forward Chaining (FC)** karena kasus longsor bersifat *data-driven* yakni petugas/diagnosis
dimulai dari gejala yang terlihat (hujan, retakan, genangan) menuju penyebab dan kesimpulan,
sesuai cara kerja FC dari fakta menuju kesimpulan.

Cara kerjanya:
1. Program mengumpulkan **fakta dasar** (fakta yang tidak pernah menjadi hasil aturan) dan menanyakannya ke user.
2. Fakta yang dijawab `y` disimpan ke memori (dalam bentuk list/array).
3. Setiap **siklus**, program mencari aturan yang syaratnya terpenuhi oleh memori **dan** hasilnya belum ada di memori.
   - `mode "dan"`: semua syarat harus ada di memori.
   - `mode "atau"`: salah satu syarat cukup.
4. Hasil aturan ditambahkan ke memori, lalu siklus diulang sampai tidak ada aturan baru yang cocok.
5. Kesimpulan akhir = hasil aturan yang tidak lagi menjadi syarat aturan lain yang dijalankan.
   Program juga menelusuri **alasan** secara mundur dari riwayat aturan.

## 5. Tiga Kasus Uji

| # | Jawaban "y" | Kesimpulan yang diharapkan |
|---|-------------|----------------------------|
| 1 | hujan lebat berkepanjangan, genangan air di lereng (t), tanah lempung tebal, lereng curam, vegetasi jarang, muncul retakan, ada permukiman | evakuasi dini warga diperlukan |
| 2 | muncul retakan di permukaan tanah saja | **tidak ada** (kasus negatif) |
| 3 | hujan lebat berkepanjangan, tanah lempung tebal, muncul retakan (tanpa lereng curam/vegetasi) | potensi tanah longsor tinggi |

[Kasus 1]
<img width="1915" height="739" alt="Screenshot 1" src="https://github.com/user-attachments/assets/35a145e1-c2b1-428e-98d5-87f034c2ca14" />
[Kasus 2 - kasus negatif]
<img width="1920" height="661" alt="Screenshot 2" src="https://github.com/user-attachments/assets/956a76ac-eb40-41f3-bab8-05616eb47171" />
[Kasus 3]
<img width="1920" height="673" alt="Screenshot 3" src="https://github.com/user-attachments/assets/8ffa8092-883a-40e2-b41d-c9ec02a64e0b" />

## 6. Batas Keberlakuan
Catatan: Aturan berasal dari S1 (Badan Nasional Penanggulangan Bencana (BNPB)); S2 (Kementerian Energi
dan Sumber Daya Mineral (ESDM)); S3 (Jurnal Dialog Penanggulangan Bencana Vol. 8 No. 2) dan hanya mencakup
faktor hidrogeologi dasar. Hasil ini adalah saran kewaspadaan, bukan keputusan ahli mitigasi bencana pasti.

## 7. Penggunaan AI
Selama pengerjaan tugas ini saya dibantu alat bantu AI (Kimi) untuk mengoreksi struktur program yang saya buat ini.
