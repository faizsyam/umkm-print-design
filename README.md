# UMKM Print Design

> Skill untuk Claude yang memandu pemilik UMKM, lewat percakapan santai, dari cerita bisnis sampai **prompt gambar siap pakai** untuk desain cetak: spanduk, banner, menu, poster, stiker, kemasan, kartu nama, logo, dan sejenisnya.

**Isi:** [Apa Ini](#apa-ini) · [Kenapa Dibuat](#kenapa-dibuat) · [Cara Pakai](#cara-pakai) · [Enam Phase](#enam-phase) · [3 Tantangan](#tiga-tantangan-dan-solusinya) · [Struktur File](#struktur-file) · [Batasan](#batasan)

---

## Apa Ini

Skill yang membuat Claude bekerja sebagai satu tim desain (brand strategist, art director, graphic designer, print designer, prompt specialist).

| Input | Output |
|---|---|
| Cerita usaha dan jenis cetakan yang dibutuhkan | **Satu prompt berbahasa Inggris** dalam code block, plus langkah pakai singkat |

- Percakapan dengan pengguna: Indonesia santai, tanpa jargon.
- Cakupan: **desain cetak** saja. Permintaan khusus digital ditandai dulu.

## Kenapa Dibuat

Prompt singkat ke AI ("bikinin spanduk bakso yang bagus") hampir selalu menghasilkan desain yang generik, teksnya salah, hierarkinya berantakan, dan tidak mencerminkan keunikan usaha.

Skill ini memindahkan cara berpikir desainer profesional ke proses terstruktur, sehingga generator gambar tinggal merender prompt yang **spesifik, beralasan, dan lengkap keputusannya**.

Tiga tujuan: **(1)** bebas AI slop, **(2)** dibangun dari prinsip desain, **(3)** kreatif dan berkesan.

---

## Cara Pakai

**Rekomendasi:** jalankan skill di **Claude**, render gambar di **ChatGPT**.

### 1. Pasang skill

| Platform | Langkah |
|---|---|
| Claude.ai / app | Settings → **Skills** (di *Capabilities*; nama menu bisa berbeda) → unggah `umkm-print-design.skill` → aktifkan |
| Claude Code | Ekstrak file `.skill` (arsip zip) → salin folder `umkm-print-design/` ke direktori skills, misalnya `~/.claude/skills/` |

### 2. Jalankan di Claude

1. Minta cetakan: *"bikin spanduk warung bakso"*, *"desain menu"*, *"prompt gambar X-banner"*.
2. Jawab pertanyaan singkat (maks. 3 per pesan; jawaban pendek atau "terserah" diterima).
3. Konfirmasi ringkasan, lalu pilih mode:
   - **Guided:** kamu menyetujui setelah Phase 2, 3, 4.
   - **Auto:** semua dikerjakan, kamu langsung menerima hasil akhir.
4. Terima prompt akhir.

### 3. Render di ChatGPT

1. Salin **seluruh** isi code block, tempel di fitur buat gambar **tanpa diubah atau diterjemahkan**.
2. **Periksa semua tulisan** (nama, harga, nomor). Generator masih bisa salah eja; minta ChatGPT memperbaikinya.
3. Ganti panel kosong (QR/QRIS, foto, barcode) dengan aset aslimu; lampirkan logo bila diminta.
4. Tanyakan ke percetakan soal ukuran dan resolusi file akhir.

### 4. Revisi

Minta perubahan kapan saja. Skill kembali ke keputusan paling awal yang terpengaruh, mengerjakan ulang tahap sesudahnya, menampilkan tabel *Sebelum | Sesudah*, lalu memberi prompt baru yang lengkap.

| Perubahan | Kembali ke |
|---|---|
| Isi tulisan | Phase 1 |
| Konsep, suasana | Phase 3 |
| Warna, huruf, logo, hiasan | Phase 4 |
| Susunan, penekanan | Phase 5 |
| Redaksi prompt | Phase 6 |

---

## Enam Phase

Berurutan, tidak ada yang dilewati. Brief sederhana memperpendek kerja, tidak menghapusnya.

| # | Phase | Hasil utama |
|---|---|---|
| 1 | **Brief** | *Brief Ledger*: status dan asal tiap item, tulisan wajib dikunci persis, kata kualitatif jadi target visual |
| 2 | **Analysis** | *Communication Problem*, *Environment Profile*, *differentiation*, *Visual source inventory* |
| 3 | **Design Plan** | *Core idea*, *style direction*, *hero*, *governing principles* |
| 4 | **Design Elements** | Warna (*value key*), tipografi, *identity unit*, *supporters*, latar |
| 5 | **Design Execution** | *Viewing stages*, *space plan*, *spatial strategy*, hierarki |
| 6 | **Prompt Synthesis** | Prompt akhir yang sudah diaudit |

**Berlaku di semua phase:** *Design Log* (satu-satunya pembawa state), *gate* di tiap phase, *depth* Full/Focused (mengatur kedalaman, tidak menghapus langkah), *conflict priority*, dan *non-negotiables* (tidak mengarang fakta, tidak mengubah tulisan atau logo pengguna, tidak menyalin kompetitor).

---

## Tiga Tantangan dan Solusinya

Ketiganya saling mengunci dan dibangun sebagai **kriteria keputusan di dalam phase**, bukan langkah tambahan di akhir.

### Tantangan 1: Menghindari AI Slop

**Masalah.** Arah yang samar membuat generator mengisi sendiri semua yang tidak ditentukan, dengan nilai paling umum secara statistik.
**Strategi.** Buat arah dan bahasa prompt sespesifik mungkin untuk satu bisnis, sampai tidak ada atribut penting yang dibiarkan kosong.

| Tahap | Solusi |
|---|---|
| **Hulu** (Phase 1-2) | Gali cerita dan keunggulan bisnis. Uji pembeda lewat empat saringan (*True, Relevant, Distinctive, Visualizable*). Kenali tempat pasang nyata (*Environment Profile*). Catat asosiasi umum sebagai *baseline*, lalu gali *true specifics* bisnis di *Visual source inventory* |
| **Tengah** (Phase 3-4) | Setiap keputusan mulai dari menamai ***apparent option*** sebagai patokan yang harus dikalahkan. Kandidat wajib spesifik, lulus *originality* dan stress test (*Swap, Category, Apparent-choice, Context-swap*), dan gaya disebut lewat *lineage*, bukan kata suasana. *Hero* dideskripsikan sampai *true specifics*-nya. *Boundaries* diturunkan dari *apparent options* dan jadi sifat positif. Logo dan *supporters* harus lolos uji *Generic* dan *Cliché*, atau tidak dipakai |
| **Hilir** (Phase 5-6) | Prinsip ***decided, not defaulted***: setiap atribut pembentuk tampilan (komposisi, *finish*, cahaya, latar, proporsi warna, lettering, cara subjek digambarkan) harus bisa ditelusuri ke satu keputusan. Benda dideskripsikan lewat *true specifics*, **bukan nama kategorinya**. Atribut yang belum diputuskan dikembalikan ke phase pemiliknya, tidak diimprovisasi |
| **Pengaman** | *Apparent option* juga mencakup nilai bawaan model gambar. Ada *Decided-attribute test* di quality control dan *Attribute left to the model* di failure modes |

### Tantangan 2: Dibangun dari Prinsip Desain Berkualitas

**Masalah.** Desain bagus tidak lahir dari lompatan ke kesimpulan. Tanpa urutan berpikir, hasilnya cantik tapi gagal dibaca dari jauh, terlalu padat, atau tidak cocok tempatnya.
**Strategi.** Tiru cara kerja studio profesional: peran jelas, langkah tidak boleh dilompati, ada pemeriksaan di tiap gerbang.

| Aspek | Solusi |
|---|---|
| **Proses** | Enam phase berurutan, tujuh peran tim (masing-masing bisa mengajukan keberatan di *gate*), *exploration protocol*: minimal tiga kandidat beda struktur, ditantang sebelum dipilih, dicatat *runner-up* dan *decisive criterion* |
| **Disiplin keputusan** | *Context matrix*, *interaction check*, *realization trace*. Tiap keputusan harus menyebut sumbernya; yang tanpa sumber dianggap kebiasaan dan gagal. Cacat dikembalikan ke akar, tidak ditambal di prompt |
| **Hierarki** | Dominasi lewat beberapa cara sekaligus (skala, kontras, warna, isolasi, posisi, bobot), satu pemimpin jelas saat *glance*, jenjang antartingkat tegas |
| **Cara orang melihat** | *Viewing stages* (glance, approach, close inspection); item ditempatkan menurut kapan penonton membutuhkannya |
| **Ruang** | *Space intent* dan *space plan* diputuskan sebelum penempatan; setiap area kosong harus punya tugas (*fill test*) |
| **Keterbacaan** | *Legibility minimum* per tingkat dari jarak, bahan, dan cahaya; *capacity check* memastikan teks muat di wadahnya |
| **Pengelompokan** | *Relationship map* dan *coupling modes* (*integrated, attached, separate*): teks disusun bersama benda yang dijelaskannya |
| **Warna dan huruf** | *Value key* dihitung dari proporsi area; teks diperlakukan menurut peran (*designed* untuk suara merek, *set* untuk informasi) |
| **Identitas** | *Identity unit* (logo + nama sebagai satu objek), pengembangan logo dengan *concept mining*, tiga kandidat, *scrutiny*, dan lima tes |
| **Kondisi cetak** | *Bleed*, *safe margin*, bahan, finishing, jarak lihat |
| **Kontrol kualitas** | Tiga level tinjauan (keputusan, komposisi, prompt), puluhan *diagnostic tests*, *compliance audit*, *release checklist*, *issue triage* |

### Tantangan 3: Kreatif, Menonjol, dan Berkesan

**Masalah.** Tidak generik dan benar secara desain belum cukup; hasil bisa rapi tapi tidak diingat.
**Strategi.** Kreativitas adalah sifat dari *cara keputusan diambil*, bukan hiasan di atasnya. Dua belas prinsip kreatif ditanam sebagai kriteria di phase tempat keputusannya dibuat, masing-masing dengan batas agar tidak jadi aturan mekanis.

| # | Prinsip | Di mana diterapkan |
|---|---|---|
| 1 | **Integrate, don't allocate** | Phase 3 *integration stance*; Phase 5 *relationship map*, *Referent test* dan *Caption test*. Jika *hero* sudah membawa pesan sendirian, berlaku pemisahan dengan isolasi |
| 2 | **Reject the first answer** | *Exploration protocol*, *Distinctness test* |
| 3 | **Satu elemen, lebih dari satu tugas** | *Distinct job*, *removal test* (cek tugas kedua sebelum membuang), *designed copy* |
| 4 | **Bentuk dari isi** | *Visual source inventory*, *territory survey*, *concept mining* logo, *supporters* diambil dari inventaris |
| 5 | **Pesan inti dulu** | *Core idea* satu kalimat (*specific, visual, generative, truthful, functional*); Phase 5 diawali pernyataan pesan |
| 6 | **Pengalaman penonton** | *Audience encounter* per *viewing stage*; ide harus terbaca saat *glance* tanpa perlu diterjemahkan |
| 7 | **Batasan sebagai material** | *Conflict priority*; pembeda dicari di dalam batasan dengan berkomitmen penuh |
| 8 | **Hierarki yang tegas** | Peringkat dengan kontras dinyatakan; tingkat yang nyaris sama digabung atau dipisah jelas |
| 9 | **Restraint sebagai pilihan** | *Space intent*, *fill test*, *subtraction pass*; minimalis maupun maksimalis bukan default |
| 10 | **Spesifik, bukan umum** | *Swap test*, *Category test*, prinsip *contextual specificity* |
| 11 | **Satu titik tegangan** | Phase 3 *point of tension*: satu patahan sengaja dari sistem yang koheren; maksimal satu, dipilih bukan default, "tidak ada" jawaban sah |
| 12 | **Verifikasi sebelum final** | *Gate*, stress test, *realization trace*, *compliance audit* di setiap phase |

**Pelengkap:** kebaruan harus menyebut tugasnya (baca lebih cepat, pesan lebih benar, kesan lebih lama); slogan, klaim, dan harga dirancang sebagai lettering grafis; beberapa konsep dibuat dari *core idea* yang berbeda, bukan sekadar beda warna.

---

## Struktur File

```
umkm-print-design/
├── SKILL.md                         # Misi, tim, workflow, prinsip, prioritas konflik, output
└── references/
    ├── 00_conversation_ux.md        # Aturan pesan ke pengguna
    ├── terms.md                     # Istilah bersama
    ├── protocol.md                  # Exploration protocol, decision quality standard
    ├── 01_brief_and_requirements.md
    ├── 02_research_and_analysis.md
    ├── 03_design_plan.md
    ├── 04_design_elements.md
    ├── 05_design_execution.md
    ├── 06_prompt_synthesis.md
    └── quality_control.md           # Gate, tests, audit, triage, release checklist
```

## Batasan

- **Hanya desain cetak.** Hasil akhirnya prompt, bukan gambar; kualitas render bergantung pada generator.
- **Periksa tulisan di gambar.** Skill menekan risikonya, tidak menghilangkannya.
- **Tidak mengarang fakta bisnis.** Harga, klaim, sertifikasi, dan kontak hanya muncul bila kamu berikan.
- **QR/QRIS, barcode, foto** diberi panel kosong; ganti dengan aset asli.
- **Logo dari kamu dipakai apa adanya.**
- **Ukuran ekstrem** disesuaikan ke rasio terdekat yang didukung generator, dengan catatan untuk di-*crop*.