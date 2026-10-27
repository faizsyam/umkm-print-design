# UMKM Print Design

Skill untuk Claude yang membantu pemilik UMKM membuat desain cetak (spanduk, banner, menu, poster, stiker, kemasan, dan lainnya) lewat obrolan santai, tanpa perlu paham desain. Hasil akhirnya adalah satu **prompt gambar** siap pakai yang bisa ditempel ke ChatGPT atau alat pembuat gambar lain.

---

## 1. Apa ini?

UMKM Print Design adalah *skill*: paket instruksi yang membuat Claude bekerja seperti tim desain kecil (ahli strategi merek, art director, desainer grafis, ahli cetak, dan lainnya). Claude memandu pemilik usaha dari cerita bisnis sampai prompt akhir, dengan bahasa Indonesia yang santai dan mudah dipahami.

**Yang kamu berikan:** cerita singkat tentang usahamu dan jenis cetakan yang dibutuhkan.
**Yang kamu dapat:** satu prompt gambar (bahasa Inggris, di dalam kotak kode) beserta langkah pakainya.

---

## 2. Kenapa ini dibuat? (Masalah)

| Masalah | Akibatnya |
|---|---|
| Banyak pemilik UMKM belum terbiasa menjelaskan keinginan desain. Permintaan seperti "yang penting menarik dan segar" terlalu umum. | Hasil generik, mirip desain orang lain, dan tidak mencerminkan usahanya. |
| Pembuat gambar AI memerlukan prompt yang rinci dan terstruktur. | Prompt asal-asalan menghasilkan desain berantakan, tulisan salah, dan susunan yang sulit dibaca. |
| Desain cetak punya syarat khusus: dilihat dari jauh, di tempat ramai, dengan bahan dan ukuran tertentu. | Desain terlihat bagus di layar tetapi gagal saat dipasang di lapangan. |
| Jasa desainer profesional tidak selalu terjangkau atau cepat. | Pemilik usaha memakai template umum atau mengerjakan sendiri tanpa panduan. |
| Istilah desain membingungkan. | Pemilik usaha ragu bertanya dan tidak yakin dengan keputusannya. |

---

## 3. Tantangan yang dihadapi

1. **Menggali kebutuhan tanpa membebani.** Informasi bisnis harus lengkap, tetapi pengguna tidak boleh merasa diinterogasi.
2. **Menjaga keinginan pengguna tetap utuh.** Kata-kata seperti "cerah", "mewah", atau "ramah" harus benar-benar terlihat di hasil, bukan hilang di tengah proses.
3. **Tampil beda dari sekitar.** Desain harus menonjol di lingkungan nyata (jalan ramai, etalase, gerobak), bukan sekadar bagus di atas kertas.
4. **Tulisan harus terbaca.** Nama, harga, dan kontak wajib tertulis persis seperti dari pemilik usaha, dan mudah dibaca dari jarak yang tepat.
5. **Menghindari tampilan "AI generik".** Hasil harus punya ide yang jelas, logo yang dirancang dengan pertimbangan, dan ruang kosong yang disengaja.
6. **Bahasa yang bisa dipahami semua orang.** Keputusan desain harus dijelaskan dengan kata sehari-hari.
7. **Tidak mengarang fakta.** Harga, sertifikasi, atau klaim tidak boleh ditambahkan tanpa persetujuan pemilik usaha.

---

## 4. Solusi: kerangka kerja enam tahap

Claude bekerja berurutan dalam enam tahap. Tiap tahap punya pemeriksaan kualitas sebelum lanjut.

| Tahap | Apa yang dikerjakan | Yang kamu lihat |
|---|---|---|
| 1. Kenalan (Brief) | Menggali usaha, tempat pasang, isi tulisan, dan kesan yang diinginkan | Pertanyaan singkat (maksimal 3 per pesan), lalu ringkasan yang kamu konfirmasi |
| 2. Analisa | Memahami lingkungan, pesaing, dan bagian yang paling gampang gagal | Tabel temuan, lalu Claude meminta persetujuanmu |
| 3. Rencana desain | Memilih ide utama, gaya, dan fokus tampilan | Tabel pilihan, lalu Claude meminta persetujuanmu |
| 4. Elemen desain | Memilih warna, huruf, logo, dan hiasan pendukung | Tabel pilihan singkat |
| 5. Penataan | Mengatur urutan baca, ruang kosong, dan susunan | Tabel pilihan singkat |
| 6. Prompt akhir | Menulis prompt dan memeriksa semua tulisan | Prompt dalam kotak kode, cara pakai, dan catatan |

**Prinsip utama**

- **Keinginanmu mengikat.** Setiap kesan yang kamu sebut diterjemahkan menjadi ciri visual yang bisa dicek, lalu dipantau sampai prompt akhir.
- **Keputusan berbasis lingkungan.** Desain dirancang untuk tempat dan jarak pandang yang sebenarnya.
- **Selalu membandingkan pilihan.** Pilihan paling gampang tidak otomatis dipakai; alternatif ditimbang dulu.
- **Tulisan dikelompokkan menurut maknanya.** Tulisan yang menjelaskan gambar utama (misalnya bahan, slogan, atau harga) ditempatkan menyatu dengan gambar itu, bukan dipisah seperti keterangan di bawah foto.
- **Tulisanmu persis.** Teks wajib dipertahankan apa adanya; dugaan salah ketik hanya ditanyakan.
- **Tidak ada fakta karangan.** Saran dari Claude ditandai sebagai saran dan baru dipakai jika kamu setuju.
- **Ruang kosong disengaja.** Setiap area kosong punya fungsi, dan tiap hiasan punya alasan.
- **Alasan teknis tetap di belakang layar.** Penalaran internal dan prompt akhir memakai bahasa Inggris; semua yang kamu baca memakai bahasa Indonesia santai.

---

## 5. Cara pakai

### Langkah utama (disarankan): Claude + ChatGPT

1. **Pasang skill di Claude.**
   Buka Claude, masuk ke pengaturan, cari bagian *Skills* (di *Capabilities*), lalu unggah file `umkm-print-design.skill`. Nama menu dapat berbeda sesuai versi dan paket langganan; jika tidak menemukannya, cek dokumentasi bantuan Claude.
2. **Mulai obrolan baru dan ceritakan kebutuhanmu.**
   Contoh: *"Tolong buatkan prompt desain spanduk untuk warung bakso saya."* Makin lengkap ceritamu (jenis usaha, ukuran, tempat pasang, tulisan yang harus ada), makin cepat prosesnya.
3. **Jawab pertanyaan dan konfirmasi.**
   Claude akan bertanya singkat, merangkum, lalu meminta persetujuanmu di akhir tahap 1, 2, dan 3. Kamu boleh menjawab "lanjut" atau menulis bagian yang ingin diubah.
4. **Salin prompt akhir.**
   Di akhir, Claude memberi prompt dalam kotak kode. Salin seluruh isinya tanpa diubah atau diterjemahkan.
5. **Tempel di ChatGPT.**
   Buka ChatGPT, gunakan fitur pembuat gambar, tempel prompt, lalu kirim.
6. **Periksa hasilnya.**
   Cek nama, harga, nomor telepon, dan alamat satu per satu. Jika ada tulisan yang salah, minta ChatGPT memperbaiki tulisan itu saja, atau kembali ke Claude untuk merevisi.
7. **Siapkan untuk cetak.**
   Minta gambar dengan ukuran terbesar, lalu tanyakan ke percetakan soal ukuran dan resolusi file yang dibutuhkan.

### Alternatif

| Kebutuhan | Pilihan |
|---|---|
| Alat pembuat gambar selain ChatGPT | Gemini, Microsoft Copilot (Image Creator), Ideogram, Leonardo, Midjourney, dan sejenisnya. Hasil dan ketepatan tulisan berbeda-beda; coba beberapa dan bandingkan. |
| Memakai Claude Code | Salin folder `umkm-print-design` ke folder skill Claude Code (misalnya `~/.claude/skills/`), lalu jalankan seperti biasa. |
| Tidak bisa memasang skill | Mulai obrolan dengan menempelkan isi `SKILL.md` sebagai instruksi dan lampirkan isi folder `references`. Cara ini kurang praktis dan hasilnya mungkin kurang konsisten. |
| Sudah punya logo | Sebutkan di awal. Logo tidak akan diubah; jika alat gambar tidak mereproduksinya dengan tepat, lampirkan file logo saat memakai prompt. |
| Ingin revisi | Kembali ke obrolan yang sama, sebutkan bagian yang mau diubah, dan Claude akan mengulang hanya tahap yang terdampak. |

---

## 6. Contoh alur singkat

1. Kamu: "Aku jualan es teh di gerobak, mau bikin spanduk."
2. Claude menyapa, merangkum, lalu bertanya tiga hal singkat (tempat jualan, yang bikin usahamu beda, tulisan yang harus ada).
3. Claude menanyakan preferensi warna dan hal yang ingin dihindari, lalu menampilkan ringkasan untuk dikonfirmasi.
4. Claude meminta kamu menunggu, lalu menampilkan hasil analisa dan meminta persetujuan.
5. Setelah kamu setuju, Claude menampilkan ide utama dan gaya, lalu meminta persetujuan lagi.
6. Claude menyelesaikan elemen desain dan penataan, lalu memberikan prompt akhir dalam kotak kode beserta cara pakainya.

---

## 7. Isi paket

```
umkm-print-design/
├── SKILL.md                         Inti skill: alur, prinsip, aturan keluaran
├── README.md                        Dokumen ini
└── references/
    ├── 00_conversation_ux.md        Panduan percakapan dan bahasa ke pengguna
    ├── 01_brief_and_requirements.md Tahap 1: menggali kebutuhan
    ├── 02_research_and_analysis.md  Tahap 2: analisa
    ├── 03_design_plan.md            Tahap 3: rencana desain
    ├── 04_design_elements.md        Tahap 4: elemen desain
    ├── 05_design_execution.md       Tahap 5: penataan
    ├── 06_prompt_synthesis.md       Tahap 6: penulisan prompt
    └── quality_control.md           Pemeriksaan kualitas di setiap tahap
```

---

## 8. Batasan

- Skill ini hanya untuk **desain cetak**. Untuk desain khusus layar (misalnya konten media sosial), Claude akan memberi tahu dan menawarkan penyesuaian.
- Yang dihasilkan adalah **prompt**, bukan file desain jadi. Kualitas gambar dan ketepatan tulisan bergantung pada alat pembuat gambar yang dipakai.
- Pembuat gambar AI sering salah menulis teks kecil. Selalu periksa nama, harga, dan kontak sebelum dicetak.
- Rasio ukuran tertentu (misalnya 150 x 70 cm) mungkin tidak bisa dihasilkan persis; gunakan rasio terdekat lalu potong atau perluas.
- Logo, sertifikasi, dan klaim hanya dipakai jika kamu yang memberikannya.
- Hasil akhir sebaiknya dikonsultasikan dengan percetakan sebelum produksi.

---

## 9. Tanya jawab singkat

**Apakah harus paham desain?** Tidak. Semua penjelasan memakai kata sehari-hari.

**Berapa lama prosesnya?** Tergantung seberapa lengkap ceritamu dan kecepatan jawabanmu. Claude akan memberi tahu saat perlu menunggu.

**Bisa pakai bahasa Inggris?** Bisa. Claude menyesuaikan bahasa yang kamu pakai, sedangkan prompt akhir tetap berbahasa Inggris.

**Bisa untuk banyak jenis cetakan sekaligus?** Bisa. Sebutkan semuanya di awal; Claude membuat prompt terpisah untuk tiap media.