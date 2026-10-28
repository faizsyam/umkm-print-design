# UMKM Print Design

> Skill untuk Claude yang memandu pemilik UMKM Indonesia, lewat percakapan santai, dari cerita bisnis sampai **prompt gambar siap pakai** untuk desain cetak (spanduk, banner, menu, poster, stiker, kemasan, kartu nama, logo, dan sejenisnya).

---

## Daftar Isi

1. [Apa Ini?](#1-apa-ini)
2. [Kenapa Dibuat?](#2-kenapa-dibuat)
3. [Cara Implementasi dan Penggunaan](#3-cara-implementasi-dan-penggunaan)
4. [Cara Kerja Singkat: Enam Phase](#4-cara-kerja-singkat-enam-phase)
5. [Tiga Tantangan Utama dan Solusinya](#5-tiga-tantangan-utama-dan-solusinya)
   - [Tantangan 1: Menghindari AI Slop](#tantangan-1-menghindari-ai-slop)
   - [Tantangan 2: Membangun dari Prinsip Desain Berkualitas](#tantangan-2-membangun-dari-prinsip-desain-berkualitas)
   - [Tantangan 3: Kreatif, Menonjol, dan Berkesan](#tantangan-3-kreatif-menonjol-dan-berkesan)
6. [Struktur File](#6-struktur-file)
7. [Batasan dan Catatan](#7-batasan-dan-catatan)

---

## 1. Apa Ini?

**UMKM Print Design** adalah sebuah *skill* (paket instruksi) untuk Claude. Setelah dipasang, Claude bertindak sebagai satu tim desain lengkap: brand strategist, art director, graphic designer, print designer, dan image-generation prompt specialist.

Alurnya sederhana dari sisi pengguna:

| Yang pengguna lakukan | Yang skill lakukan |
|---|---|
| Bercerita tentang usahanya dan butuh cetakan apa | Bertanya singkat dalam bahasa Indonesia santai, lalu merangkum |
| Memilih mode: konfirmasi tiap tahap, atau serahkan semua | Menganalisis, merancang konsep, memilih elemen, menyusun layout |
| Menerima hasil akhir | Menyerahkan **satu prompt berbahasa Inggris** dalam code block, plus langkah pakai singkat |

Hasil akhirnya adalah prompt yang berdiri sendiri (*standalone*), siap ditempel ke generator gambar. Semua yang dibaca pengguna memakai bahasa Indonesia yang santai dan tanpa jargon. Catatan kerja, Design Log, dan prompt akhir memakai bahasa Inggris.

**Cakupan:** desain cetak fisik untuk usaha kecil. Permintaan khusus-digital akan ditandai dulu, lalu dijalankan hanya jika pengguna setuju.

---

## 2. Kenapa Dibuat?

Pemilik UMKM umumnya tidak punya latar desain, waktu, atau anggaran untuk agensi. Kalau mereka langsung meminta gambar ke AI dengan prompt singkat ("bikinin spanduk warung bakso yang bagus"), hasilnya hampir selalu:

- terlihat generik dan mirip dengan ribuan desain lain,
- tulisan salah, terpotong, atau diubah,
- hierarki tidak jelas, terlalu penuh, atau terlalu ramai,
- tidak mencerminkan keunikan usahanya.

Skill ini dibuat untuk menutup celah itu. Ia memindahkan pekerjaan berpikir seorang desainer profesional ke dalam proses yang terstruktur, sehingga prompt yang sampai ke generator gambar sudah **spesifik, beralasan, dan lengkap keputusannya**. Generator hanya tinggal merender.

Tiga tujuan inti, dibahas rinci di [Bagian 5](#5-tiga-tantangan-utama-dan-solusinya):

1. Menghindari **AI slop**.
2. Membangun desain dari **prinsip desain berkualitas**, bukan lompat ke kesimpulan.
3. Menghasilkan desain yang **kreatif**: menonjol, menyampaikan pesan dengan kuat, dan berkesan.

---

## 3. Cara Implementasi dan Penggunaan

**Rekomendasi:** gunakan **Claude** untuk menjalankan skill ini, lalu gunakan **ChatGPT (fitur buat gambar)** untuk merender prompt yang dihasilkan.

### 3.1 Prasyarat

- Akun Claude dengan fitur **Skills** aktif (di Claude.ai, atau Claude Code).
- Akun ChatGPT dengan akses fitur pembuatan gambar.
- File `umkm-print-design.skill`.

### 3.2 Instalasi

**Di Claude.ai atau aplikasi Claude**

1. Buka pengaturan, lalu menu **Skills** (biasanya di bagian *Capabilities*; nama menu dapat berbeda antarversi).
2. Unggah file `umkm-print-design.skill`.
3. Pastikan skill dalam keadaan aktif.

**Di Claude Code**

1. File `.skill` adalah arsip zip. Ekstrak sehingga terbentuk folder `umkm-print-design/`.
2. Salin folder itu ke direktori skills milik Claude Code (misalnya `~/.claude/skills/` untuk skill personal).

### 3.3 Cara memakai

1. **Mulai percakapan** di Claude dengan permintaan cetakan, misalnya: *"Aku mau bikin spanduk untuk warung bakso"*, *"bikin menu"*, *"desain logo"*, atau *"prompt gambar untuk X-banner"*.
2. **Jawab pertanyaan singkat.** Skill bertanya paling banyak tiga pertanyaan per pesan, masing-masing disertai contoh jawaban dan nilai bawaan jika kamu lewati. Jawaban pendek atau "terserah" diterima.
3. **Konfirmasi ringkasan** (tabel singkat berisi usaha, jenis cetakan, tulisan yang harus tercetak persis, kesan yang diinginkan, dan asumsi), lalu **pilih mode**:
   - **Guided:** kamu menyetujui setelah Phase 2, 3, dan 4, dengan satu tabel ringkas per tahap.
   - **Auto:** semua dikerjakan senyap, lalu kamu menerima hasil akhir dengan daftar keputusan penting.
4. **Terima hasil akhir:** satu prompt dalam code block, langkah pakai, dan catatan jika perlu.

### 3.4 Merender di ChatGPT

1. **Salin seluruh isi** code block prompt.
2. **Tempel di ChatGPT** lewat fitur buat gambar, **tanpa diubah atau diterjemahkan**. Tulisan di dalam desain sudah dijaga persis (verbatim) dalam bahasa aslinya.
3. **Periksa semua tulisan** pada gambar (nama, harga, nomor, alamat). Generator gambar masih bisa salah mengeja. Minta ChatGPT membetulkan bagian yang keliru.
4. **Lampirkan aset milikmu** bila diminta di catatan (misalnya file logo). Untuk QR/QRIS, foto, atau barcode, skill menyediakan *panel kosong* yang sengaja dirancang. Ganti panel itu dengan aset aslimu, karena kode tidak pernah ditiru.
5. **Tanyakan ke percetakan** soal ukuran dan resolusi file akhir.

Generator lain mungkin juga bisa dipakai, tetapi prompt ini disusun dan disarankan untuk ChatGPT.

### 3.5 Revisi

Minta perubahan kapan saja. Skill menelusuri keputusan paling awal yang terpengaruh, mengerjakan ulang tahap-tahap setelahnya, menunjukkan hanya bagian yang berubah (tabel *Sebelum | Sesudah*), lalu menyerahkan prompt baru yang lengkap.

| Jenis perubahan | Kembali ke |
|---|---|
| Isi tulisan | Phase 1 |
| Konsep atau suasana | Phase 3 |
| Warna, huruf, logo, hiasan | Phase 4 |
| Susunan atau penekanan | Phase 5 |
| Redaksi prompt | Phase 6 |

---

## 4. Cara Kerja Singkat: Enam Phase

Skill menjalankan **enam phase secara berurutan**. Tidak ada phase yang boleh dilewati, digabung, atau ditunda, sesederhana apa pun brief-nya. Brief sederhana memperpendek kerja, tidak menghapusnya.

| Phase | Fokus | Hasil utama |
|---|---|---|
| **1. Brief** | Mencatat dan memverifikasi semua yang diketahui | *Brief Ledger*: tiap item diberi status (wajib/opsional/dikecualikan) dan asal (diberikan, disimpulkan, diteliti, pilihan kreatif); tulisan wajib dikunci persis; kata kualitatif seperti "mewah" atau "hangat" diterjemahkan jadi target visual |
| **2. Analysis** | Memahami masalah, tempat, dan sumber visual | *Communication Problem*, *Environment Profile*, *differentiation strategy*, *Visual source inventory* |
| **3. Design Plan** | Memilih satu ide yang menjadi dasar seluruh desain | *Core idea*, *style direction*, *hero*, dan *governing principles* |
| **4. Design Elements** | Membangun sistem visual yang koheren | Warna dengan *value key*, tipografi, *identity unit* (logo + nama), *supporters*, latar |
| **5. Design Execution** | Menyusun komposisi sesuai cara karya benar-benar dilihat | *Execution Specification*: *viewing stages*, *space plan*, *spatial strategy*, hierarki |
| **6. Prompt Synthesis** | Menerjemahkan spesifikasi jadi instruksi visual | Prompt akhir yang diaudit |

Mekanisme pendukung yang berlaku di semua phase:

- **Design Log:** satu-satunya pembawa *state* antar phase dan antar giliran.
- **Gate:** setiap phase ditutup dengan pemeriksaan wajib dan satu keberatan substantif dari peran yang bertanggung jawab.
- **Depth:** *Full* untuk karya besar, padat, atau butuh logo baru; *Focused* untuk kasus lain. Depth mengatur kedalaman kerja, tidak pernah menghapus langkah.
- **Conflict priority:** urutan prioritas jika syarat berbenturan: fakta dan isi wajib, lalu keterbacaan, lalu syarat pengguna, lalu strategi, lalu identitas brand, dan terakhir ambisi kreatif.
- **Non-negotiables:** tidak mengarang fakta bisnis (harga, klaim, sertifikasi), tidak mengubah tulisan pengguna, tidak mengubah logo yang diberikan, tidak menyalin kompetitor.

---

## 5. Tiga Tantangan Utama dan Solusinya

Ketiga tantangan ini saling mengunci. Menghindari *slop* tanpa dasar desain menghasilkan sesuatu yang aneh. Dasar desain tanpa kreativitas menghasilkan sesuatu yang rapi tapi mudah dilupakan. Karena itu, ketiganya dibangun sebagai **kriteria keputusan di dalam phase**, bukan sebagai langkah tambahan di akhir.

---

### Tantangan 1: Menghindari AI Slop

#### Masalah

*AI slop* adalah hasil generik yang terasa seperti rata-rata dari semua gambar yang pernah dilihat model. Akar masalahnya: **arah yang samar membuat generator gambar mengisi sendiri semua yang tidak ditentukan**, dan ia selalu memilih nilai yang paling mungkin secara statistik. Semakin banyak atribut yang tidak diputuskan, semakin generik hasilnya.

Strategi skill ini: **buat arah desain dan bahasa prompt sespesifik dan setailor-made mungkin untuk satu bisnis**, sampai tidak ada atribut penting yang dibiarkan kosong.

#### Cara skill menyelesaikannya

| Tahap | Mekanisme | Efeknya terhadap slop |
|---|---|---|
| **Phase 1** | Menggali cerita bisnis dan keunggulannya sebagai prioritas pertanyaan teratas; kata kualitatif samar diterjemahkan menjadi *quality translation* (target visual, *quality carriers*, sinyal yang bertentangan) | Bahan baku yang spesifik sejak awal, dan kata samar tidak dibiarkan menjadi "suasana" yang diisi model |
| **Phase 2** | *Differentiation* diuji dengan empat saringan: *True, Relevant, Distinctive, Visualizable*; posisi yang cocok untuk puluhan kompetitor ditolak | Pembeda yang benar-benar milik bisnis ini |
| **Phase 2** | *Environment Profile* menggambarkan tempat pasang nyata (tetangga visual, cahaya, jarak, perilaku orang) dan menentukan dimensi *departure* dan *fit* | Desain dibuat untuk satu tempat, bukan untuk "mana saja" |
| **Phase 2** | *Visual source inventory* mencatat asosiasi yang jelas sebagai *baseline*, lalu menggali *true specifics* bisnis (praktik, bahan, proses, tempat, bahasa, sejarah); inventaris yang hanya berisi emblem umum dinyatakan gagal | Sumber ide yang tidak akan dipilih model secara otomatis |
| **Phase 3** | Setiap keputusan penting dimulai dengan menamai ***apparent option*** (jawaban pertama yang diberikan kebanyakan orang) sebagai patokan yang harus dikalahkan | Menutup jalur "ambil yang paling umum" |
| **Phase 3** | *Design territory survey* lintas sumber (sejarah desain, tradisi visual lokal, kriya dan produksi, lintas kategori, dunia bisnis itu sendiri) sebelum kandidat ditulis | Opsi tidak lagi hanya berasal dari asosiasi pertama model |
| **Phase 3** | Kandidat harus berupa *candidate card* dengan semua field terisi memakai istilah spesialis; gaya harus disebut lewat *lineage* dan ciri pembentuknya, bukan kata suasana; lulus *originality tests*; lulus empat stress test (*Swap, Category, Apparent-choice, Context-swap*) | Label kosong dan daftar kata sifat ditolak |
| **Phase 3** | *Hero* dideskripsikan sampai ke *true specifics* yang membuatnya milik bisnis ini (bentuk, bahan, konstruksi, susunan) | Subjek bukan "rata-rata kategori" |
| **Phase 3** | *Boundaries* diturunkan dari *apparent options* dan tampilan tetangga (termasuk kecenderungan bawaan model), lalu diwujudkan sebagai sifat positif yang diputuskan, bukan sekadar larangan | Anti-referensi yang konkret |
| **Phase 4** | Identifier baru tidak boleh sekadar nama yang diberi huruf bagus; wajib punya *personality device*; pengembangan logo melewati *concept mining*, tiga kandidat, delapan pertanyaan *scrutiny* (termasuk uji *Generic* dan *Cliché*), revisi, dan lima tes | Logo bukan hasil satu kali coba |
| **Phase 4** | *Supporters* hanya boleh ada bila menjawab *deficit* nyata dari *text-only baseline*; tanda dekoratif yang lazim di kategori itu dijadikan patokan yang harus dikalahkan; nama font tidak dipakai sebagai arahan, diganti ciri huruf | Tidak ada hiasan pengisi dan tidak ada pilihan huruf "bawaan" |
| **Phase 5** | Tinjauan akhir memeriksa prinsip ***decided, not defaulted***: setiap atribut yang membentuk tampilan (sumbu komposisi dan simetri, *finish* rendering, cahaya, latar, proporsi warna, lettering, cara subjek digambarkan) harus bisa ditelusuri ke satu keputusan; tata letak stok ditolak tanpa alasan kuat | Atribut yang belum diputuskan ditemukan sebelum menjadi prompt |
| **Phase 6** | Benda yang digambar dideskripsikan lewat *true specifics*, **bukan nama kategorinya** (nama kategori saja memanggil "contoh rata-rata" milik model); setiap atribut pembentuk tampilan harus dinyatakan; kalau belum pernah diputuskan, kembali ke phase pemiliknya, bukan diimprovisasi di sini | Tidak ada celah yang diisi default model |
| **Phase 6** | *Visual-effect test* pada setiap kalimat; tanpa rasionale, tanpa kata sifat pengisi, tanpa penekanan massal; tulisan wajib dikunci persis dan satu kali | Prompt padat keputusan, bukan padat adjektiva |
| **Lintas phase** | Istilah *apparent option* diperluas: model gambar punya "apparent value" sendiri, yaitu nilai yang ia isi untuk atribut yang tidak ditentukan; ada *Decided-attribute test* di quality control dan *Attribute left to the model* di failure modes | Kebiasaan slop punya nama, tes, dan jalur perbaikan |

**Ringkasnya:** spesifisitas dibangun dari hulu (cerita dan *true specifics* bisnis), dijaga di tengah (kandidat harus mengalahkan *apparent option*), dan dikunci di hilir (tidak ada atribut pembentuk tampilan yang tersisa untuk diisi model).

---

### Tantangan 2: Membangun dari Prinsip Desain Berkualitas

#### Masalah

Desain yang baik tidak lahir dari lompatan ke kesimpulan. Desainer berpengalaman mengikuti urutan yang tetap: memahami masalah, meneliti konteks, menjelajahi beberapa arah, memilih dengan kriteria, lalu mengeksekusi dengan disiplin. Tanpa urutan itu, hasilnya cantik di permukaan tetapi gagal dibaca dari jauh, terlalu padat, atau tidak cocok dengan tempatnya.

Strategi skill ini: **meniru cara kerja studio profesional**, dengan peran yang jelas, langkah yang tidak boleh dilompati, dan pemeriksaan di setiap gerbang.

#### Cara skill menyelesaikannya

**a. Proses yang meniru studio profesional**

| Mekanisme | Isi |
|---|---|
| **Enam phase berurutan** | Brief, analisis, konsep, elemen, eksekusi, lalu penerjemahan; tiap phase hanya dimulai setelah *exit artifact* dan *gate* phase sebelumnya lulus |
| **Tujuh peran tim** | Brand strategist, consumer-behavior researcher, senior art director, graphic designer, print designer, visual communication specialist, image-generation prompt specialist; masing-masing memiliki keputusan tertentu dan bisa mengajukan keberatan di gate |
| **Exploration protocol** | Keputusan penting: nama *apparent option* dulu, minimal tiga kandidat yang berbeda pada *structural axis*, evaluasi dalam urutan berbeda dari urutan pembuatan, tantangan sebelum memilih, *runner-up* dan *decisive criterion*, lalu *decision record*; hibrida diperbolehkan, kompromi ("dan juga...") ditolak |
| **Decision quality standard** | *Context matrix* (kandidat dinilai terhadap seluruh parameter, bukan satu alasan saja), *interaction check*, *strength-weakness engineering*, *originality tests*, *realization trace*, dan *specialist terminology* |
| **Gate di setiap phase** | Enam pemeriksaan sama (keputusan wajib, protokol, satu keberatan substantif, kriteria selesai, keterlacakan, *Design Log*) ditambah pemeriksaan khusus phase |
| **Traceability** | Setiap keputusan harus menyebut sumbernya, dari item *Brief Ledger* sampai klausa prompt; keputusan tanpa sumber dianggap lahir dari kebiasaan dan gagal |
| **Iterate at the root** | Cacat dikembalikan ke keputusan paling awal yang bertanggung jawab, lalu phase berikutnya dijalankan ulang; menambal prompt tidak diizinkan |

**b. Prinsip desain yang dijadikan keputusan eksplisit**

| Prinsip | Di mana diterapkan |
|---|---|
| **Memahami konteks sebelum merancang** | *Environment Profile*, *audience encounter*, *Communication Problem* dengan *weakest link* (attention, comprehension, credibility, action) di Phase 2 |
| **Hierarki dan urutan baca** | *Dominance by several means* (skala, kontras, warna, isolasi, posisi, bobot); satu pemimpin yang jelas pada tahap *glance*; jenjang antartingkat harus tegas; elemen dihitung bersama teks (Phase 3 dan 5) |
| **Pengalaman penonton bertahap** | *Viewing stages* (glance, approach, close inspection); hanya konten tahap *glance* yang diukur untuk jarak terjauh; item ditempatkan menurut kapan penonton membutuhkannya, bukan menurut betapa pentingnya bagi pemilik (Phase 5) |
| **Ruang sebagai elemen desain** | *Space intent* diputuskan di Phase 3 dan diuji dengan estimasi kapasitas; *space plan* (margin luar, *isolation zones*, *separations*, *resting fields*) diputuskan sebelum penempatan; setiap area kosong harus punya tugas (*fill test*) |
| **Keterbacaan sebagai batas minimum** | *Legibility minimum* per tingkat dari jarak, bahan, cahaya, dan kontras; *capacity check* memastikan setiap string muat di kontainernya sebelum ukuran final dicetak |
| **Pengelompokan menurut makna** | *Relationship map* dan *coupling modes* (*integrated, attached, separate*) agar teks yang menjelaskan sebuah benda disusun bersama benda itu, bukan sekadar "gambar dengan keterangan" |
| **Warna dan nilai terang-gelap** | *Value key* dihitung dari proporsi area (termasuk latar dan pita besar) agar sesuai dengan setiap kualitas yang diminta |
| **Tipografi menurut peran** | Teks diperlakukan menurut *content role*; teks yang membawa suara (slogan, klaim, harga) *designed*, teks informasi *set*; huruf dijelaskan lewat klasifikasi, kontras goresan, proporsi, dan spasi |
| **Identitas yang utuh** | *Identity unit* (logo + nama sebagai satu objek) dengan logika konstruksi bersama, spasi terukur, dan enam mekanisme pembeda dari teks di sekitarnya |
| **Kondisi cetak nyata** | *Bleed*, *safe margin*, bahan, finishing, pencahayaan, jarak lihat, dan lipatan atau panel |
| **Kejujuran dan keselamatan** | Tidak ada fakta karangan, tanda sertifikasi palsu, atau wajah orang sungguhan; konten pengguna dikunci persis |

**c. Pengendalian kualitas berlapis**

- **Tiga level tinjauan:** keputusan, komposisi, prompt.
- **Delapan *stress test* di Phase 3** dan lebih dari dua puluh *diagnostic tests* (misalnya *Removal, Subtraction, Fill, Unit and disconnection, Capacity, Referent, Caption, Value-key*).
- ***Compliance audit*** pada prompt dan balasan, serta *release checklist* sebelum pengiriman.
- ***Issue triage:*** pelanggaran *critical/major/minor* dengan jalur ke phase penyebabnya.

**Ringkasnya:** setiap keputusan lahir dari urutan berpikir yang bisa ditelusuri, diuji terhadap alternatif nyata, dan diperiksa pada gate. Itulah yang membedakan "proses desainer" dari "tebakan yang kebetulan bagus".

---

### Tantangan 3: Kreatif, Menonjol, dan Berkesan

#### Masalah

Tidak generik dan mengikuti praktik desain yang baik belum cukup. Hasilnya bisa saja benar, rapi, dan tetap tidak diingat siapa pun. Kreativitas di sini bukan hiasan di atas keputusan, melainkan **sifat dari cara keputusan diambil**: unsur yang tidak terduga sebelum dilihat, tetapi terasa tak terelakkan sesudahnya.

Strategi skill ini: **menanamkan dua belas prinsip kreatif sebagai kriteria keputusan** di phase tempat keputusannya benar-benar dibuat. Masing-masing punya batas penerapan agar tidak berubah menjadi aturan mekanis baru.

#### Pemetaan prinsip kreatif ke implementasi

| # | Prinsip | Implementasi di skill | Batas |
|---|---|---|---|
| 1 | **Integrate, don't allocate** | Phase 3: *integration stance*. Phase 5: *relationship map* dan *coupling modes*; *Referent test* (jika dua item yang digabung bisa bertukar posisi tanpa mengubah makna, itu baru dialokasikan, belum terintegrasi) dan *Caption test* | Jika *hero* sudah membawa pesan sendirian, atau penggabungan akan melemahkannya, yang berlaku adalah pemisahan dengan isolasi, karena dominasi *hero* adalah aset dan tiap penggabungan menghabiskannya. Tema, gaya, dan audiens menentukan seberapa jauh penggabungan boleh |
| 2 | **Reject the first answer** | *Exploration protocol*: *apparent option* dinamai dulu, minimal tiga kandidat dengan sedikitnya satu dari luar yang jelas, *challenge* sebelum memilih; *Distinctness test*: kandidat yang sekadar kompeten harus mengalahkan yang ambisius lewat kriteria yang dinyatakan | Keputusan sepele diputuskan langsung; *Depth* mengatur detail kartu, bukan langkahnya |
| 3 | **Every element does more than one job** | *Distinct job* dan *removal test*: sebelum elemen dibuang, ditanyakan apakah satu tugas kedua dapat membuatnya layak. *Space does double duty*; teks yang dirancang (*designed copy*) menjadi gambar sekaligus pesan | Tugas tambahan tidak boleh menaikkan biaya ruang atau melewati *weight ceiling*, dan tidak boleh ditambahkan hanya untuk membenarkan elemen |
| 4 | **Derive form from content** | *Visual source inventory*, *design territory survey*, *concept mining* logo dari nama, produk, proses, asal, dan ritual pelanggan; *supporters* digambar dari inventaris itu | Sumber harus benar, workable secara visual, dan dihormati (tanpa tokenisme) |
| 5 | **Find the core message, then serve it** | *Core idea* satu kalimat yang harus *specific, visual, generative, truthful, functional*; Phase 5 diawali pernyataan pesan satu kalimat; *decision commitments* dicek sebelum Phase 6 | Ide yang hanya kata suasana ditolak |
| 6 | **Ground decisions in the viewer's experience** | *Audience encounter* per *viewing stage*; sifat *functional* pada *core idea* kini mencakup dapat dibaca pada tahap *glance* tanpa harus diterjemahkan | Kejutan harus menurunkan usaha membaca atau menambah kesenangan, bukan menambah kebingungan |
| 7 | **Treat constraints as material** | *Conflict priority*; kualitas yang diminta pengguna adalah syarat mengikat; *departure* hanya dipilih di antara opsi yang menjaga semua kualitas; prinsip 8 kini menegaskan bahwa pembeda dicari **di dalam** batasan dengan berkomitmen penuh, bukan mengencerkan atau menghindarinya | Pilihan yang dinamai pengguna tetap, kelemahannya dimitigasi dari dalam |
| 8 | **Commit to a hierarchy of emphasis** | *Dominant and supporting relationships*: peringkat dengan kontras antartingkat yang dinyatakan, satu pemimpin pada *glance*; Phase 5: jenjang antartingkat harus tegas, tingkat yang nyaris sama digabung atau dipisahkan jelas | Tetap di dalam batas keterbacaan, dan tidak boleh menaikkan semua tingkat sekaligus |
| 9 | **Restraint as an active choice** | *Space intent*, *space plan*, *fill test*, *subtraction pass*; minimalisme maupun maksimalisme bukan default | Restraint menghapus yang tak punya tugas, bukan melarang menambah apa yang memang kurang (minat, bukti penawaran, suasana, penuntun baca) |
| 10 | **Prefer specificity over generality** | *Swap test*, *Category test*, prinsip *contextual specificity* (kini mencakup setiap atribut pembentuk tampilan), deskripsi lewat *true specifics* | Spesifik berarti benar dan dapat dirender |
| 11 | **Introduce one point of tension** | Phase 3: *point of tension*, satu patahan sengaja dari sistem yang koheren (skala, kontras, penempatan, atau konsep) beserta elemen pembawanya; Phase 5: diperiksa terbaca pada tahap *glance* dan didukung semua yang lain | Paling banyak satu; hanya elemen yang boleh memimpin yang boleh membawanya; harus sesuai semua kualitas; "tidak ada" adalah jawaban sah; dipilih, bukan tambahan bawaan |
| 12 | **Verify before finalizing** | *Gate*, *stress tests*, *realization trace*, *compliance audit*, *release checklist* | Dijalankan di setiap phase, bukan hanya di akhir |

**Pelengkap kreatif lain di skill:**

- ***Functional creativity*:** kebaruan harus menyebut tugasnya, yaitu membaca lebih cepat, pesan lebih benar, atau kesan lebih tahan lama.
- ***Designed copy*:** slogan, klaim, dan harga dirancang sebagai lettering grafis dengan sedikitnya satu perangkat yang disengaja (ritme baris, kontras skala, wadah berbentuk, mengikuti kontur *hero*), bukan diketik datar.
- ***Hero* yang menunjukkan pesan lewat skala, *crop*, dan perilaku tepi**, bukan sekadar muat di ruang. *Hero* yang tidak layak dipaksakan boleh digantikan dengan "tanpa *hero*" atau satu set setara.
- **Beberapa konsep sekaligus:** tiap konsep berangkat dari *core idea* berbeda pada *structural axis*, bukan hanya beda warna atau hiasan.

**Ringkasnya:** kreativitas tidak ditempel di akhir. Ia hadir sebagai pertanyaan yang harus dijawab di tempat keputusan dibuat: apakah ini jawaban pertama, apakah elemen ini bekerja lebih dari satu tugas, di mana letak satu kejutannya, dan apakah semuanya melayani pesan inti.

---

## 6. Struktur File

```
umkm-print-design/
├── SKILL.md                              # Misi, tim, workflow, prinsip operasi, prioritas konflik,
│                                         # non-negotiables, kontrak output
└── references/
    ├── 00_conversation_ux.md             # Aturan semua pesan ke pengguna (bahasa, pertanyaan,
    │                                     # wait note, entri phase, balasan akhir)
    ├── terms.md                          # Istilah bersama (satu arti di semua file)
    ├── protocol.md                       # Exploration protocol dan decision quality standard
    ├── 01_brief_and_requirements.md      # Phase 1: Brief
    ├── 02_research_and_analysis.md       # Phase 2: Analysis
    ├── 03_design_plan.md                 # Phase 3: Design Plan
    ├── 04_design_elements.md             # Phase 4: Design Elements
    ├── 05_design_execution.md            # Phase 5: Design Execution
    ├── 06_prompt_synthesis.md            # Phase 6: Prompt Synthesis
    └── quality_control.md                # Gate, diagnostic tests, audit, triage, release checklist
```

Setiap file phase diawali *phase card* (analog profesional, tujuan, input, prinsip yang berlaku, keputusan wajib, dan pemeriksaan "Before leaving"). File dibaca saat dibutuhkan, tidak sekaligus.

---

## 7. Batasan dan Catatan

- **Hanya untuk desain cetak.** Permintaan khusus-digital akan ditandai, dan skill hanya lanjut bila pengguna setuju.
- **Hasil akhir adalah prompt, bukan gambar.** Kualitas render bergantung pada generator gambar.
- **Tulisan pada gambar perlu diperiksa.** Generator gambar masih bisa salah mengeja atau mengubah teks. Skill mengurangi risikonya (tulisan dikunci persis dan satu kali, volume teks dikelola), tetapi tidak menghilangkannya.
- **Skill tidak mengarang fakta bisnis.** Harga, klaim, testimoni, sertifikasi, kontak, dan angka hanya muncul bila diberikan pengguna. Saran dari skill selalu diberi label dan baru masuk setelah pengguna setuju.
- **QR/QRIS, barcode, dan foto yang tidak bisa direproduksi dengan setia** diberi *reserved asset panel*. Ganti dengan aset aslimu.
- **Logo yang kamu berikan dipakai apa adanya**, tidak didesain ulang, disederhanakan, atau diubah warnanya, kecuali kamu memintanya.
- **Ukuran ekstrem** dapat membuat rasio disesuaikan ke rasio terdekat yang didukung generator, dengan catatan untuk di-*crop*.