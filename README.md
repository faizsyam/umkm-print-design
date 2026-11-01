# Jago Desain Apa Aja

> Skill untuk Claude yang mengubah kebutuhan desain apa pun, lewat percakapan singkat yang menyesuaikan diri dengan kamu, menjadi **prompt gambar lengkap dan siap pakai** untuk visual statis: poster, banner, menu, kemasan, kartu, undangan, grafis media sosial, slide, infografis, mockup layar, identitas merek, logo, dan sejenisnya.

**Isi:** [Apa Ini](#apa-ini) · [Kenapa Dibuat](#kenapa-dibuat) · [Cara Pakai](#cara-pakai) · [Cara Kerja](#cara-kerja) · [Prinsip Kualitas](#prinsip-kualitas) · [Balasan Akhir](#balasan-akhir) · [Struktur File](#struktur-file) · [Batasan](#batasan)

---

## Apa Ini

Skill yang membuat Claude bekerja sebagai satu tim desain dengan tujuh peran: *brand strategist*, *audience researcher*, *senior art director*, *graphic designer*, *production specialist*, *visual communication specialist*, dan *image-generation prompt specialist*. Peran-peran ini memegang keputusan dan mengajukan keberatan di setiap *gate*; mereka bukan pekerjaan tambahan.

| Input | Output |
|---|---|
| Kebutuhan desain, dari satu kalimat singkat sampai brief profesional | **Satu atau lebih prompt berbahasa Inggris**, masing-masing dalam code block sendiri, plus label, langkah pakai singkat, dan catatan seperlunya |

### Cakupan

| Termasuk | Tidak termasuk |
|---|---|
| Visual **statis** di medium apa pun, fisik maupun layar: poster, spanduk, banner, signage, menu, kemasan dan label, kartu, undangan, sampul, grafis sosial dan iklan, slide, infografis, tampilan layar sebagai gambar statis, identitas merek, logo | Kode, model 3D, motion, animasi, dan hasil interaktif |

Bila permintaan butuh lebih dari gambar statis, skill menyebutkan sekali bagian yang bisa dikerjakan (bingkai statisnya) dan baru lanjut setelah kamu setuju.

### Menyesuaikan diri dengan kamu

Skill membaca **bahasa**, **tingkat literasi desain**, dan **kelengkapan brief** sejak pesan pertama, lalu menyesuaikan cara bicaranya, bukan kedalaman berpikirnya.

| Kamu | Yang terjadi |
|---|---|
| Baru di dunia desain | Kata-kata sehari-hari, pertanyaan tentang tujuan, orang, tempat, dan perasaan (bukan font atau palet), pilihan jawaban singkat dengan default |
| Fasih istilah desain | Istilah tepat, pertanyaan langsung tentang batasan dan keputusan; setiap keputusan desain yang kamu sebut dicatat sebagai keputusan tetap |
| Brief sudah lengkap | Tahap tanya-jawab diperpendek, paling banyak satu putaran |

Percakapan memakai bahasamu. Prompt akhir berbahasa Inggris (kecuali kamu minta lain atau menyebut generator yang lebih baik dalam bahasa lain), dengan teks di gambar tetap persis dalam bahasa aslinya.

## Kenapa Dibuat

Prompt singkat ke AI ("bikinin poster kopi yang bagus") hampir selalu menghasilkan desain yang generik, tulisannya salah, hierarkinya berantakan, terlalu padat, dan tidak mencerminkan keunikan subjeknya.

Skill ini memindahkan cara kerja tim desain profesional ke proses terstruktur, sehingga generator gambar tinggal merender prompt yang **spesifik, beralasan, dan lengkap keputusannya**.

Empat tujuan: **(1)** bebas AI slop, **(2)** dibangun dari prinsip desain, **(3)** kreatif dan berkesan, **(4)** setiap prompt bisa dijalankan sendiri tanpa bergantung pada prompt lain.

---

## Cara Pakai

Jalankan skill di **Claude**, render gambar di **generator gambar pilihanmu** (misalnya ChatGPT). Sebutkan generatornya bila kamu mau prompt disesuaikan.

### 1. Pasang skill

| Platform | Langkah |
|---|---|
| Claude.ai / app | Settings → **Skills** (di *Capabilities*; nama menu bisa berbeda) → unggah `jago-desain-apa-aja.skill` → aktifkan |
| Claude Code | Ekstrak file `.skill` (arsip zip) → salin folder `jago-desain-apa-aja/` ke direktori skills, misalnya `~/.claude/skills/` |

### 2. Jalankan di Claude

1. Sebutkan kebutuhanmu: *"bikin poster pameran"*, *"desain menu"*, *"prompt gambar kemasan"*, *"buatkan logo"*.
2. Jawab pertanyaan singkat (paling banyak 3 per pesan; jawaban pendek atau "terserah" diterima). Hal penting yang tetap belum terjawab dicatat sebagai asumsi di ringkasan untuk kamu setujui atau koreksi.
3. Cek **ringkasan** (satu tabel), lalu pilih:
   - **Guided:** kamu menyetujui setelah Phase 3 dan Phase 4. Temuan Phase 2 tampil di awal Phase 3, dan Phase 5 tampil tanpa jeda sebelum hasil akhir.
   - **Auto:** semua dikerjakan diam-diam; kamu langsung menerima hasil akhir beserta keputusan pentingnya.
   - Tidak memilih atau jawabannya tidak jelas: guided. Kamu boleh berpindah mode kapan saja.
4. Terima prompt akhir.

### 3. Render di generator gambar

1. Salin **seluruh** isi satu code block dan tempel **tanpa diubah atau diterjemahkan**. Tiap prompt lengkap dengan sendirinya.
2. Lampirkan aset yang disebut di catatan (logo, foto, kode) bila generator menerimanya.
3. **Periksa semua tulisan** di hasil (nama, harga, nomor, alamat). Generator masih bisa salah eja; minta ia memperbaikinya.
4. Untuk cetakan fisik, tanyakan ke percetakan soal ukuran dan resolusi file akhir.

Urutan prompt hanya penting bila kamu ingin konsistensi dengan memakai hasil yang sudah jadi sebagai referensi visual; itu opsional.

### 4. Revisi

Minta perubahan kapan saja. Skill kembali ke keputusan paling awal yang terpengaruh, mengerjakan ulang **hanya keputusan yang bergantung padanya**, menampilkan tabel singkat *Sebelum | Sesudah*, lalu memberi prompt baru yang lengkap untuk setiap gambar yang isinya berubah (dan menyebut yang tidak berubah).

| Perubahan | Kembali ke |
|---|---|
| Isi, daftar gambar, ukuran, atau rasio | Phase 1 |
| Konsep, suasana | Phase 3 |
| Warna, tingkat terang-gelap, huruf, perlakuan teks, logo, hiasan pendukung | Phase 4 |
| Susunan, penekanan | Phase 5 |
| Redaksi prompt | Phase 6 |

---

## Cara Kerja

### Enam phase

Berurutan, tidak ada yang dilewati, digabung, atau ditunda. Brief sederhana memperpendek kerja, tidak menghapusnya.

| # | Phase | Hasil utama |
|---|---|---|
| 1 | **Brief** | *Brief Ledger*: daftar gambar yang dibutuhkan (tujuan, format, rasio), tiap item dengan status dan asalnya, tulisan wajib dikunci persis, kata kualitatif (suasana, nada, gaya, warna) diterjemahkan menjadi target visual yang bisa diperiksa (*quality translation*). Setelah kamu konfirmasi, menjadi *standing block* yang dibaca semua phase |
| 2 | **Analysis** | *Communication Problem* beserta **pesan satu kalimat**, *Environment Profile* (tempat bertemu penonton, tahap lihat, cara medium membentuk gambar, apa yang harus menyatu dan apa yang boleh berbeda dari sekelilingnya), *audience encounter*, strategi pembeda, *Visual source inventory* |
| 3 | **Design Plan** | *Brand design* dan tema, *core idea*, gaya (tujuh dimensi), *hero*, prinsip pengatur (ruang kosong, sikap integrasi, peran logo, dan lainnya), peta pembawa tiap kualitas (*quality carrier map*), *seed bank* |
| 4 | **Design Elements** | Warna dengan *value key*, tipografi dan perlakuan teks, *identity unit* (logo + nama), *supporters* (hiasan dan visual pendukung), wadah dan bahasa bentuk, latar |
| 5 | **Design Execution** | Per gambar: tahap lihat, *space plan*, strategi tata letak, peringkat dan hierarki, penempatan semua item, keseimbangan, *capacity check* |
| 6 | **Prompt Synthesis** | Prompt akhir yang sudah diaudit, tiap gambar satu prompt, plus label, langkah pakai, dan catatan |

Setiap phase ditutup oleh *gate*: pemeriksaan standar, pemeriksaan khusus phase, dan satu keberatan substantif dari peran pemilik keputusan paling berisiko (dua keberatan pada kedalaman Full).

### Daftar gambar dan beberapa konsep

- **Satu gambar, satu prompt.** Phase 1 mencatat setiap gambar yang perlu ada: format atau rasio berbeda, sisi, panel, atau layar berbeda, atau varian yang kamu minta. Apa yang sebenarnya satu gambar tetap satu; ukuran berbeda dengan rasio dan situasi lihat yang sama dianggap gambar yang sama.
- **Tidak ada gambar yang diturunkan dengan memperbesar, memperkecil, atau memotong gambar lain.** Format memengaruhi jangkauan baca, area yang tersedia, alur mata, dan keseimbangan, sehingga tata letak diputuskan untuk tiap format. Yang berpindah antargambar adalah keputusan (identitas, gaya, warna, huruf), bukan tata letak.
- **Beberapa konsep:** Phase 1-2 dikerjakan sekali; Phase 3-5 dijalankan untuk semua konsep. Tiap konsep berangkat dari *core idea* yang berbeda secara struktural (bukan sekadar beda warna atau hiasan). Jumlah prompt = jumlah gambar × jumlah konsep.

### Kedalaman: Full dan Focused

Kedalaman mengatur seberapa luas kerja di dalam setiap phase; tidak pernah menghapus phase, keputusan, langkah protokol, atau gate.

- **Full:** identitas atau logo baru harus dibuat, ada gambar yang harus menang perhatian di tengah pesaing, daftar gambar lebih dari satu, atau isi terlalu padat untuk formatnya.
- **Focused:** selain itu. Naik ke Full begitu salah satu syarat Full muncul di phase mana pun.

### Design Log

Satu-satunya pembawa *state* antarphase dan antarpesan, berisi tiga bagian:

| Bagian | Isi |
|---|---|
| **S** (*standing block*) | Brief dan batasan: daftar gambar, tulisan wajib persis, aset tetap, pengecualian, batas produksi atau tampilan, kualitas yang diminta beserta pembawanya, kedalaman, mode. Dibaca semua phase |
| **Forward block** | Satu per phase: keputusan sebagai spesifikasi dengan sumbernya, kewajiban yang harus diwujudkan phase berikutnya, dan *open flags* (asumsi dan hal belum pasti, dipisahkan dari keputusan) |
| **Record** | Kandidat, alasan, keberatan, arah yang ditolak, catatan riset. Tidak pernah menjadi masukan keputusan berikutnya dan tidak pernah sampai ke Phase 6 |

Dengan akses file, log disimpan sebagai `/home/claude/design_log.md` dan tidak ditampilkan ke kamu kecuali diminta. Tiap keputusan hanya punya satu phase pemilik; phase berikutnya menerapkannya dan tidak memutuskan ulang, kecuali lewat aturan *return* karena pemeriksaan yang gagal.

---

## Prinsip Kualitas

Semuanya dibangun sebagai **kriteria keputusan di dalam phase**, bukan pemeriksaan tambahan di akhir.

### 1. Bebas AI slop

**Masalah.** Arah yang samar membuat generator mengisi sendiri semua yang tidak ditentukan, dengan nilai paling umum secara statistik.
**Strategi.** Buat arah dan bahasa prompt sespesifik mungkin untuk satu subjek, sampai tidak ada atribut penting yang dibiarkan kosong.

| Tahap | Solusi |
|---|---|
| **Hulu** (Phase 1-2) | Gali cerita dan keunggulan subjek. Uji pembeda dengan empat saringan (*true, relevant, distinctive, visualizable*). Kenali tempat nyata gambar bertemu penonton. Catat asosiasi umum sebagai *baseline*, lalu gali *true specifics* di *Visual source inventory* |
| **Tengah** (Phase 3-4) | Tiap keputusan penting dimulai dengan menamai ***apparent option*** sebagai patokan yang harus dikalahkan, lalu minimal tiga kandidat berbeda struktur, ditantang sebelum dipilih, dengan *runner-up* dan *decisive criterion* tercatat. Kandidat harus lolos tiga uji *originality* (*predictable, specific, ambitious*). Rencana akhir diuji dengan stress test: *swap/category, context-swap, distance and attention, contradiction, ambition, brief-quality*. Gaya disebut lewat *lineage* dan ciri khasnya, bukan kata suasana |
| **Hilir** (Phase 5-6) | Prinsip ***decided, not defaulted***: setiap atribut yang membentuk tampilan (sumbu komposisi, bentuk wadah, finish, cahaya, latar, proporsi warna, proporsi huruf, cara subjek digambarkan) harus bisa ditelusuri ke satu keputusan. Benda dideskripsikan lewat *true specifics*, **bukan nama kategorinya**. Atribut yang belum diputuskan dikembalikan ke phase pemiliknya, tidak diimprovisasi |
| **Pengaman** | *Apparent option* mencakup juga nilai bawaan model gambar (*apparent value*). *Decided-attribute test* berjalan di Phase 5 dan 6 |

### 2. Dibangun dari prinsip desain

| Aspek | Solusi |
|---|---|
| **Disiplin keputusan** | Setiap keputusan menyebut sumbernya (item brief atau temuan → implikasi → rencana → elemen → penempatan → kalimat prompt); yang tanpa sumber dianggap kebiasaan dan gagal. Mitigasi dan biaya yang diterima dibawa maju sebagai kewajiban. Cacat dikembalikan ke akarnya, tidak ditambal di prompt |
| **Kualitas yang diminta mengikat** | Kata seperti "hangat", "premium", "ceria", atau gaya, warna, dan teknik yang kamu sebut diterjemahkan menjadi ciri visual yang bisa diperiksa, dicarikan pembawa, dan dikawal sampai ke kalimat prompt. Tidak ada keputusan yang boleh bertentangan dengannya |
| **Konteks dulu, konvensi kemudian** | Tahap lihat, jarak, cahaya, dan kebiasaan baca diturunkan dari gambar yang sebenarnya dan tempat pasangnya, bukan dari nama mediumnya. Konvensi yang diandalkan penonton dipertahankan; pembeda dibelanjakan pada ekspresi dan identitas |
| **Hierarki** | Satu pemimpin jelas saat *glance*; tiap elemen punya peringkat dengan jenjang yang tegas pada minimal dua tuas, satu di antaranya tuas utama (ukuran, kontras nilai, isolasi, posisi) |
| **Keterbacaan** | *Legibility minimum* per tingkat diturunkan dari jarak lihat tahapnya dikali rasio yang ditentukan kondisi (bahan atau layar, cahaya, kontras, waktu lihat); *capacity check* memastikan teks muat di wadahnya sebelum ukuran dinyatakan |
| **Keseimbangan** | Bobot visual diperkirakan dan titik beratnya diukur setelah penempatan; perbaikan dimulai dari yang paling sedikit menambah bobot, dengan *counterweight* disiapkan sejak Phase 4 |
| **Identitas** | *Identity unit* (logo + nama sebagai satu objek). Logo baru lewat pengembangan bertahap: *concept mining*, tiga kandidat, *scrutiny*, revisi, lima tes. Logo yang kamu berikan dipakai apa adanya |
| **Renderability** | Apa yang bisa digambar generator dengan akurat dinilai dengan satu prinsip di semua phase. Keandalan turun saat hasil harus persis (huruf, angka, kode), saat banyak detail harus benar sekaligus, atau saat harus identik antargenerasi. Dikurangi lewat desain dulu; sisanya dicatat sebagai *rendering risk* |

### 3. Lima fokus yang diperkuat

Lima masalah yang paling sering merusak hasil ditangani di akarnya, di phase tempat keputusannya dibuat.

| Fokus | Prinsipnya | Di mana |
|---|---|---|
| **Ruang lega dan skala** | Ruang adalah sumber daya yang dialokasikan **sebelum** isi ditempatkan, di dua tingkat: porsi kosong keseluruhan format dan ruang napas di dalam tiap zona (padding wadah, jarak antaritem, spasi baris), keduanya disesuaikan dengan ukuran format dan jarak lihat. Format besar memberi ruang dan elemen utama lebih longgar; teks pendukung boleh lebih kecil relatif terhadap format selama tetap terbaca. Isi yang terlalu banyak diatasi dengan triage, pengelompokan, dan bentuk susunan yang lebih ringkas; ruang kosong baru dikurangi sebagai upaya terakhir, tidak pernah dengan mengecilkan teks di bawah batas terbaca | Phase 3 *space intent*; Phase 5 *space plan*, *zone test*, triage |
| **Hero dan informasi pendukung** | *Hero* dipertimbangkan bersama konten dan visual pendukung yang menguatkan pesannya, memperjelas nilainya, atau memberi konteks, disusun dalam satu zona (*hero group*), hanya dari bahan yang kamu berikan atau yang benar adanya. Itu praduga yang diuji, bukan pola wajib: hero yang berdiri sendiri dipertahankan bila memang lebih efektif, dengan alasan yang dicatat | Phase 3 hero dan *integration stance*; Phase 5 *relationship map* |
| **Susunan informasi dan visual pendukung** | Bentuk susunan dipilih per kelompok informasi dari fungsi, hubungan isi (urutan, perbandingan, item paralel, label dan nilai), panjang, tetangga, dan area yang tersedia: bertumpuk, sebaris, kolom, tabel, atau mengelompok di sekitar acuannya. Satu bentuk yang diulang pada kelompok yang fungsinya berbeda adalah kebiasaan, bukan keputusan; konsistensi datang dari sistem bersama. Ikon, pemisah, penanda, thumbnail, dan ilustrasi kecil dipilih berdasarkan tugasnya (mengenali, mengelompokkan, menguatkan, membantu menafsirkan). Hiasan tanpa tugas dan penyajian teks saja saat informasi punya tugas yang tak terpenuhi sama-sama dianggap cacat | Phase 4 *supporters*; Phase 5 *arrangement form per group* |
| **Arahan ilustrasi dan foto** | Ilustrasi, fotografi, dan media campuran adalah bahasa visual yang beragam, bukan satu gaya. Phase 3 menetapkan bahasa pembuatan gambar yang spesifik untuk subjek (ilustrasi: *lineage*, proporsi, goresan, teknik render, tekstur, tingkat detail, perlakuan warna, tingkat stilisasi; foto: framing, cahaya, grading, finish), bukan sekadar nama medium. Hiasan dan karakter mengikuti bahasa itu, dan Phase 6 mendeskripsikannya konkret | Phase 3 gaya dimensi (5); Phase 4; Phase 6 |
| **Keputusan menyeluruh** | Setiap keputusan, besar atau kecil, dinilai terhadap seluruh desain: perannya, hubungannya dengan elemen dan informasi lain, dampaknya pada hierarki, ruang, dan pesan, serta apa yang dibatasinya di hilir. Keputusan yang dioptimalkan sendirian atau diambil dari templat dan pola kebiasaan dianggap belum selesai | Prinsip 1; *realization trace*, *contradiction scan*, *composition review* |

### 4. Sepuluh prinsip pengatur

| # | Prinsip | Intinya |
|---|---|---|
| 1 | Whole-system thinking | Tiap keputusan dinilai terhadap keseluruhan desain |
| 2 | Structured exploration | Keputusan penting melewati protokol eksplorasi; solusi yang familiar hanya masuk setelah mengalahkan alternatif yang diturunkan dari masalah ini |
| 3 | Evidence-informed judgment | Isi dari kamu, hasil riset, kesimpulan, dan pilihan kreatif dipisah dengan tag asal |
| 4 | Contextual specificity | Arah yang berfungsi sama untuk pesaing belum selesai |
| 5 | Functional creativity and restraint | Setiap elemen punya *purpose line* (fungsi, kerugian bila hilang, efek pada penonton); minimalis dan maksimalis bukan default, polos pun keputusan; pengurangan tidak boleh menghilangkan karakter |
| 6 | Explicit rank and allocated space | Perhatian diarahkan, ruang dialokasikan lebih dulu |
| 7 | Internal consistency | Merek, tema, gaya, warna, huruf, logo, citra, dan komposisi saling menguatkan; teks dikelompokkan menurut apa yang dirujuknya |
| 8 | Fidelity to the brief | Isi wajib, teks, pengecualian, aset tetap, kualitas, dan prioritas tidak diubah diam-diam; batasan adalah bahan, dicari pembedanya di dalamnya |
| 9 | Effort follows impact | Pertimbangan terpanjang untuk logo, ide inti, hero, dan rencana ruang |
| 10 | Context before convention | Prinsip universal berlaku di semua medium; apa yang dikenakan dan diandalkan medium diturunkan di Phase 2 |

### 5. Prioritas saat persyaratan bertabrakan

1. Kebenaran fakta; isi wajib, pengecualian, dan aset tetap dari kamu
2. Persepsi dan pemahaman dalam kondisi nyata, untuk seluruh rentang penonton (termasuk penglihatan rendah dan perbedaan penglihatan warna)
3. Kualitas dan prioritas yang kamu nyatakan
4. Tujuan komunikasi dan strategi pembeda
5. Identitas merek yang sudah mapan tetapi tidak diberikan sebagai aset
6. Ambisi kreatif

Pilihan yang kamu tetapkan tetap dipakai walau melemahkan tujuan; skill memitigasinya di dalam pilihan itu dan menyampaikan kekhawatirannya sekali sebagai saran berlabel.

---

## Balasan Akhir

Singkat, berurutan:

1. **Pengantar** satu baris.
2. **Prompt:** tiap prompt didahului label (nomor, tujuan gambar dan tempatnya dalam keseluruhan permintaan, format dan rasio), lalu prompt-nya sendiri di code block.
3. **Keputusan utama** (mode auto saja): tiga sampai lima poin satu baris.
4. **Cara pakai:** maksimal tiga langkah.
5. **Catatan:** hanya bila perlu, maksimal tiga poin: dugaan salah ketik (sebagai pertanyaan), tulisan yang dibuatkan skill, aset yang harus dilampirkan, panel cadangan yang harus diganti, atau risiko volume dan render.
6. **Penutup:** satu baris undangan revisi, menyebut prompt mana yang terpengaruh.

Rasionale desain tidak pernah masuk ke prompt, catatan, atau balasan kecuali kamu memintanya.

---

## Struktur File

```
jago-desain-apa-aja/
├── SKILL.md                         # Misi, tim, workflow, peta kepemilikan keputusan, aturan eksekusi, Design Log,
│                                    # prinsip, kedalaman, prioritas konflik, non-negotiables, revisi, kontrak output
└── references/
    ├── 00_conversation_ux.md        # Aturan semua pesan ke pengguna
    ├── terms.md                     # Istilah bersama, termasuk renderability dan legibility minimum
    ├── protocol.md                  # Protokol eksplorasi tiga tingkat, terminologi spesialis
    ├── 01_brief_and_requirements.md
    ├── 02_research_and_analysis.md
    ├── 03_design_plan.md
    ├── 04_design_elements.md
    ├── 05_design_execution.md
    ├── 06_prompt_synthesis.md
    └── quality_control.md           # Gate, uji lintas-phase, audit, triage, release checklist
```

Berkas dibaca bertahap: `00_conversation_ux.md` dan `terms.md` sebelum pesan pertama, file tiap phase saat memasukinya, `protocol.md` saat masuk Phase 2, dan `quality_control.md` di gate pertama.

---

## Batasan

- **Hanya visual statis.** Hasil akhirnya prompt, bukan gambar; kualitas render bergantung pada generator. Kode, 3D, motion, animasi, dan hasil interaktif di luar cakupan.
- **Periksa tulisan di gambar.** Skill menekan risikonya, tidak menghilangkannya. Teks panjang, angka (harga, nomor), dan aksara non-Latin paling rawan; bila risikonya tidak bisa dikurangi lewat desain, skill menyebutkannya di catatan agar kamu periksa.
- **Tidak mengarang fakta.** Angka, klaim, testimoni, sertifikasi, tanda kepercayaan resmi, kontak, kredensial, tanggal, dan spesifikasi hanya muncul bila kamu berikan. Tidak ada tokoh, maskot, atau wajah orang sungguhan yang dimasukkan tanpa diminta.
- **Teks dari kamu dipakai persis.** Dugaan salah ketik dijaga apa adanya dan ditanyakan, tidak diperbaiki diam-diam.
- **Logo dan karakter dari kamu dipakai apa adanya**, tidak didesain ulang, disederhanakan, atau diwarnai ulang. Identitas yang baru tidak pernah sekadar nama dengan huruf menarik.
- **QR/QRIS, barcode, foto, dan logo yang tidak bisa dilampirkan** diberi panel cadangan yang dirancang menyatu dengan komposisi; ganti dengan aset aslimu. Tidak ada tiruan.
- **Tidak menyalin** pesaing atau desain yang sudah ada.
- **Rasio dipertahankan.** Tiap prompt dibuat untuk rasio yang kamu maksud (atau yang diturunkan dari ukuran atau kebiasaan jenis gambarnya, ditandai sebagai asumsi), tanpa mengganti rasio atau meminta *crop*. Hasil render tetap bergantung pada generator, jadi periksa hasilnya.
- **Saran tidak masuk tanpa persetujuan.** Apa pun yang diusulkan skill diberi label dan baru dipakai setelah kamu setuju.
