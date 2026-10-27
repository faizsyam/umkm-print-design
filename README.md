# UMKM Print Design

> Ceritakan usahamu secara santai. Dapatkan satu prompt yang dibuat khusus untuk usahamu, siap ditempel ke AI image generator untuk membuat spanduk, menu, banner, kemasan, dan cetakan lainnya.

---

## 1. Apa ini?

**UMKM Print Design** adalah *skill* untuk Claude yang bekerja seperti **tim graphic designer** untuk usaha kecil. Kamu tidak perlu bisa desain. Cukup ceritakan usahamu dengan bahasa sehari-hari, lalu skill ini akan bertanya, menyelidiki, menimbang beberapa ide, dan menyusun **satu prompt** yang siap kamu tempel ke AI image generator (paling disarankan: ChatGPT) untuk dibuatkan gambarnya.

**Bedanya dengan minta "buatkan spanduk yang menarik":**
permintaan asal biasanya menghasilkan gambar yang tampak bagus tapi *mirip semua warung lain*: mangkuk di tengah, api menyala, merah-kuning, penuh hiasan. Skill ini sebaliknya. Desain dibuat **khusus untuk usahamu, tempat pasangmu, dan pelangganmu**, dengan cara berpikir seorang desainer profesional, sehingga hasilnya sulit dipakai begitu saja oleh usaha lain.

**Bisa untuk cetakan fisik seperti:**
spanduk · banner · X-banner · roll-up · baliho · papan nama · neon box · menu · daftar harga · poster · flyer · brosur · stiker · label · kemasan · kartu nama · signage · gerobak · backdrop · umbul-umbul · logo

**Yang perlu kamu tahu sejak awal:**
- Skill ini menghasilkan **prompt**, bukan gambarnya. Gambar dibuat oleh AI image generator dari prompt itu.
- Percakapan memakai **bahasa Indonesia santai**. Prompt akhir berbahasa Inggris karena AI image generator bekerja lebih baik dengan bahasa itu, tapi tulisan yang akan tercetak (nama, harga, alamat) tetap persis seperti yang kamu tulis.
- Khusus untuk **cetakan fisik**, bukan desain layar seperti feed Instagram.

---

## 2. Cara pakai

### A. Pasang skill di Claude (sekali saja)

1. Buka Claude (claude.ai atau aplikasinya) dan masuk ke akunmu.
2. Buka **Settings → Capabilities**, lalu nyalakan **Code execution and file creation**. Skill membutuhkan ini untuk berjalan.
3. Di bagian **Skills**, klik **+**, pilih **Create skill**, lalu **Upload a skill**. (Di beberapa versi, menunya ada di **Customize → Skills**.)
4. Pilih file **`umkm-print-design.skill`**. File ini sebenarnya berformat ZIP, jadi kalau ditolak, ubah ekstensinya menjadi `.zip` lalu upload ulang.
5. Pastikan toggle skill **umkm-print-design** dalam keadaan menyala.

> **Catatan:** skill yang kamu upload bersifat pribadi untuk akunmu. Di paket Team atau Enterprise, admin organisasi perlu mengaktifkan Skills lebih dulu. Letak menu bisa sedikit berbeda antar versi aplikasi.

### B. Mulai di chat

Buka chat baru dan tulis kebutuhanmu seperti ngobrol biasa. Skill akan aktif otomatis ketika kamu menyebut cetakan seperti spanduk, menu, banner, atau logo. Kalau ingin memastikan, sebut saja namanya, misalnya *"Pakai skill umkm-print-design, aku butuh spanduk untuk warung soto."*

Setelah itu alurnya singkat:

1. **Claude bertanya**, maksimal tiga pertanyaan per pesan. Tiap pertanyaan ada contoh jawaban dan pilihan bawaan, dan jawaban "terserah" pun diterima.
2. **Claude menampilkan ringkasan** pemahamannya dalam satu tabel. Balas **1** jika benar dan kamu ingin konfirmasi tiap tahap, balas **2** jika benar dan kamu mau serahkan semuanya ke AI, atau tulis bagian yang perlu dikoreksi.
3. **Claude bekerja.** Di mode 1, kamu melihat satu tabel kecil per tahap (pilihan kita dan opsi lain yang dipertimbangkan) dan cukup membalas "lanjut" atau menulis yang mau diubah. Di mode 2, kamu langsung menerima hasil akhir.
4. **Claude memberikan prompt** dalam satu kotak kode, lengkap dengan langkah pakainya.

Jika punya logo, lampirkan ke chat Claude sejak awal supaya bisa dicatat dengan tepat.

### C. Setelah menerima prompt

1. **Salin seluruh isi kotak kode.**
2. **Tempel di ChatGPT** lewat fitur membuat gambar, tanpa diubah dan tanpa diterjemahkan. Kalau punya logo, lampirkan juga di sana.
3. **Periksa semua tulisan** di gambar (nama, harga, nomor, alamat). AI image generator masih sering salah menulis, dan kamu bisa meminta perbaikan.
4. **Tanyakan ke percetakan** soal ukuran dan resolusi file sebelum cetak.
5. **Mau revisi?** Kembali ke chat Claude yang sama dan bilang apa yang kurang pas, misalnya *"terlalu mewah"*, *"warnanya jangan gelap"*, atau *"harganya ganti"*. Skill memperbaiki dari akar masalahnya, bukan menambal prompt, dan memberimu prompt baru yang lengkap.

### Tips agar hasilnya maksimal

- **Ceritakan keunikan yang nyata.** "Kuah dimasak 12 jam sejak subuh" jauh lebih berguna daripada "enak dan murah".
- **Sebutkan tempat pasangnya.** "Pinggir jalan raya, dilihat dari motor" menghasilkan desain yang sangat berbeda dari "digantung di dalam kafe".
- **Berikan tulisan persis seperti yang mau dicetak.** Skill tidak akan memperbaiki ejaanmu diam-diam, tapi akan bertanya kalau curiga ada salah ketik.
- **QR, QRIS, atau barcode?** Skill menyiapkan area khusus di desain. Pasang kode aslimu di sana, karena kode tidak pernah ditiru.
- **Butuh beberapa pilihan konsep atau beberapa jenis cetakan?** Sebutkan saja. Tiap konsep atau cetakan mendapat prompt sendiri.

---
---

# Di Balik Layar

*Untuk yang ingin tahu kenapa, bagaimana, dan sampai di mana skill ini bekerja. Tidak perlu dibaca untuk memakainya.*

---

## 3. Kenapa ini dibuat

Pemilik UMKM sekarang punya akses ke AI image generator, tapi hasilnya sering mengecewakan, dan penyebabnya bukan kurangnya selera pemilik usaha.

**AI image generator pada dasarnya menggambar rata-rata dari apa yang pernah dilihatnya.** Diminta "spanduk warung bakso yang menarik", ia menjawab dengan versi rata-rata dari semua spanduk bakso. Hasilnya tampak jadi, tapi tidak bisa dibedakan dari milik tetangga sebelah. Kalau tiga warung di satu jalan memakai spanduk yang serupa, ketiganya saling menghapus keunikan.

Padahal pemilik usaha memegang *bahan baku* keunikan yang tidak dimiliki siapa pun: cerita, tempat, pelanggan, dan rasa yang ingin ditimbulkan. Yang tidak mereka punya adalah **cara berpikir seorang desainer** dan kosakata untuk menyampaikannya. Graphic designer profesional sering tak terjangkau, sementara template percetakan menyeragamkan semua orang.

Skill ini dibangun di atas satu keyakinan: **kecerdasan desain harus ada di dalam prompt, bukan diharapkan muncul dari AI image generator.** Generator hanyalah penerjemah ke piksel. Ide, penilaian, dan keputusan harus sudah selesai sebelum gambar dibuat. Karena itu skill ini meniru cara kerja studio desain yang baik (bertanya, menyelidiki, menimbang, menguji, lalu menulis arahan produksi) dan menyembunyikannya di balik percakapan yang bisa diikuti siapa pun.

---

## 4. Tantangan utama

Rancangan skill ini adalah jawaban atas enam pertanyaan. Dua yang pertama adalah inti persoalannya, dan empat sisanya memastikan jawaban itu benar-benar sampai ke hasil akhir.

### Pertanyaan 1: Bagaimana menghindari AI slop?

**Gejala.** Desain yang rapi tapi bisa dipasang di usaha mana pun: objek di tengah, ornamen berlebihan, palet klise sesuai kategori, ruang yang dijejali dekorasi, tulisan yang kacau.

**Akar masalah.** Bukan sekadar "AI kurang kreatif". Ada dua penyebab yang saling menguatkan:
1. **Ide pertama yang muncul, baik di kepala manusia maupun model, hampir selalu ide paling umum**, karena itulah yang paling sering terlihat.
2. **Tidak ada yang mengarahkan generator ke sesuatu yang spesifik** untuk usaha ini, tempat ini, dan orang-orang ini.

**Jawaban: arahan yang dibuat khusus (*tailor-made*) untuk setiap usaha.** Caranya:

1. **Kritis terhadap ide pertama.** Pilihan yang paling "tampak jelas" disebut lebih dulu sebagai *benchmark*. Ia boleh menang, tapi hanya jika bisa menyebut kriteria spesifik yang gagal dipenuhi alternatifnya. "Memang begitu biasanya" bukan alasan.
2. **Mengajukan minimal tiga opsi yang benar-benar berbeda.** Berbeda secara struktur, bukan sekadar warna. Sumbernya sengaja dilebarkan ke luar kategori: kebenaran produk, momen pelanggan, kondisi tempat, nama dan asal-usul, bahan dan teknik produksi, tradisi visual lokal, hingga praktik di industri lain. Sebuah *design territory survey* dilakukan sebelum kandidat ditulis.
3. **Menyelidiki kelebihan dan kekurangan tiap opsi terhadap konteks lengkap**, bukan satu sisi. Tiap kandidat diuji terhadap tujuan, kesan yang diminta, merek, jarak pandang, lingkungan, jumlah isi, bahan cetak, budaya, dan apakah AI image generator mampu menggambarkannya.
4. **Menantang pemenangnya.** Sebut runner-up, argumen terkuat melawan pemenang, lalu satu *decisive criterion*. Kalau kriteria itu tidak bisa disebut, pekerjaan belum selesai.
5. **Memperbaiki kelemahan pemenang.** Setiap kelemahan material harus punya langkah mitigasi, atau diterima sebagai biaya dengan alasan tertulis.
6. **Menguji keunikan.** Apakah orang asing bisa menebaknya dari kategori dan lokasi saja? Apakah masih berlaku kalau nama pesaing dipasang? Apakah akan sama benarnya di tempat lain? Kandidat yang gagal dibangun ulang, bukan dibela.

### Pertanyaan 2: Bagaimana menghasilkan karya yang terasa dibuat graphic designer sungguhan?

**Gejala.** Hasil AI sering terasa "belum selesai": semua elemen berukuran sama penting, huruf dipilih asal, warna menabrak, logo hanya nama dengan font bagus, teks menempel seperti keterangan foto.

**Akar masalah.** Karya seorang desainer bukan hasil gambar yang bagus, melainkan hasil **proses**: memahami masalah komunikasi, memilih satu konsep, menyusun sistem visual, mengatur untuk mata yang melihat, lalu dikritik sebelum dilepas. AI image generator hanya menerima instruksi, jadi kalau prosesnya tidak dijalankan sebelum prompt, hasilnya tidak akan punya kualitas itu.

**Jawaban: menjalankan kebiasaan kerja desainer secara eksplisit, lalu menuliskannya sebagai arahan produksi.**

| Kebiasaan desainer | Bagaimana skill menirunya |
|---|---|
| **Mulai dari masalah, bukan gambar.** | Fase 2 merumuskan *communication problem*, bagian yang paling mudah gagal, dan satu kalimat pesan yang harus tertangkap pada pandangan pertama. |
| **Satu konsep, bukan tumpukan elemen.** | Fase 3 memilih satu *core idea* dan satu *hero* (hal pertama yang dilihat). Setiap elemen di Fase 4 harus menyebut keputusan yang diwujudkannya (*realization trace*). Elemen tanpa tugas dibuang lewat *removal test* dan *subtraction test*. |
| **Menata perhatian lewat visual hierarchy.** | Dominasi dibangun dengan beberapa cara sekaligus (scale, contrast, color, isolation, position, weight). Isi dibagi menurut tahap baca: dari jauh, dekat, dan sangat dekat, sehingga hanya isi tahap pertama yang diukur untuk jarak terjauh. |
| **Typography dan warna sebagai sistem.** | Huruf ditentukan per peran (klasifikasi, kontras goresan, proporsi, spasi). Warna ditentukan dengan struktur harmoni, proporsi luas, dan *value key* yang dihitung dari area, bukan dari kesan. Tulisan yang berfungsi sebagai suara usaha (slogan, ajakan) diperlakukan sebagai *designed copy*, sedangkan info seperti harga diset rapi dan jelas. |
| **Negative space direncanakan.** | *Space plan* ditetapkan sebelum isi ditempatkan, dengan proporsi dan tugas untuk setiap area kosong (*fill test*). Di prompt, ruang kosong ditulis sebagai fitur desain yang positif. |
| **Logo adalah tanda yang dikembangkan, bukan nama yang dihias.** | Logo baru melalui pengembangan panjang: beberapa benih ide, perangkat kepribadian, kebenaran yang diekspresikan, uji penyatuan *logo mark* dengan *wordmark*, dan uji pembeda dari teks di sekitarnya. Logo yang sudah ada tidak disentuh. |
| **Teks berdampingan dengan yang dirujuknya.** | Teks yang melabeli, menjelaskan, atau memberi harga suatu objek disusun bersama objek itu. *Caption test*: kalau teks ditutup dan yang tersisa hanya "gambar dengan keterangan di bawahnya", susunannya diulang. |
| **Membahasakan keputusan dengan presisi seorang spesialis.** | Gaya disebut lewat lineage dan ciri pembentuknya, bukan mood. Warna, huruf, dan komposisi dideskripsikan dengan istilah yang bisa didefinisikan. Setiap kalimat prompt harus lolos *visual-effect test*: kalau dihapus, apakah gambar berubah? |
| **Dikritik sebelum dilepas.** | Skill bekerja sebagai tujuh peran (brand strategist, consumer-behavior researcher, senior art director, graphic designer, print designer, visual communication specialist, image-generation prompt specialist). Di setiap *gate*, minimal satu peran wajib mengajukan keberatan substantif terhadap keputusan paling lemah, dan keberatan itu harus diselesaikan atau diterima dengan alasan tertulis. |

### Pertanyaan 3: Bagaimana memastikan yang diminta pemilik usaha benar-benar terwujud?

**Masalah sebenarnya.** Kata seperti "ringan", "bersih", atau "ramah" tidak bisa diperiksa, jadi diam-diam kalah oleh default AI. Pemilik minta "lapang dan terang", hasilnya dominan gelap, dan tidak ada yang menyadarinya.

**Jawaban.** Setiap kesan, gaya, warna, atau prioritas yang diminta diperlakukan sebagai **binding requirement**. Ia diterjemahkan menjadi target visual yang bisa diperiksa (value key, chroma, temperature, density, formality), diberi beberapa *quality carrier* (ciri visual yang membawanya), dan dicatat sinyal apa yang akan bertentangan dengannya. Opsi yang bertentangan gugur otomatis, dan kualitas itu dilacak di setiap fase sampai klausa terakhir prompt.

### Pertanyaan 4: Bagaimana menggali bahan baku dari orang yang bukan desainer, tanpa membebani mereka?

**Masalah sebenarnya.** Keunikan desain bergantung pada informasi yang ada di kepala pemilik. Tetapi pemilik tidak punya bahasa desain, sibuk, dan memakai ponsel. Formulir panjang berisi istilah teknis membuat mereka mundur.

**Jawaban.** Skill bertanya soal *orang, tempat, dan perasaan*, tidak pernah soal font atau layout. Batasnya tiga pertanyaan per pesan dan tiga ronde, tiap pertanyaan ada contoh dan jawaban bawaan. Yang bisa disimpulkan atau diriset tidak ditanyakan. Seluruh kerja dalam disembunyikan di balik satu tabel kecil per tahap, dan kamu memilih sendiri apakah mau mengonfirmasi tiap tahap (*guided mode*) atau menyerahkan semuanya (*auto mode*).

### Pertanyaan 5: Bagaimana menjaga hasil tetap jujur dan benar-benar bisa dicetak?

**Masalah sebenarnya.** Dua risiko berbeda. Pertama, AI suka mengarang: harga, klaim, sertifikasi, nomor telepon, atau tahun berdiri yang tidak pernah diberikan bisa muncul di cetakan. Kedua, desain yang bagus di layar belum tentu bekerja di dunia fisik: dilihat dari motor yang melaju, di antara spanduk lain, dengan teks yang terlalu banyak untuk ruangnya.

**Jawaban.**
- **Integritas.** Tidak ada fakta bisnis yang diciptakan. Tulisan pengguna dipertahankan *verbatim* (dugaan typo ditanyakan, bukan dibetulkan diam-diam). Tanda halal, QR, dan QRIS tidak pernah ditiru, melainkan disediakan area khusus untuk dipasang aslinya. Saran selalu berlabel saran dan tidak masuk cetakan tanpa persetujuan.
- **Kenyataan fisik.** Skill merekonstruksi lingkungan pasang (tetangga, cahaya, jarak, perilaku orang lewat) lalu memutuskan secara sadar **dimensi mana yang sengaja berbeda** dan **dimensi mana yang harus tetap mirip sekitar** agar kredibel. *Capacity check* memastikan semua teks muat di ukuran akhir. Jika sesak, teks diturunkan prioritasnya atau dikelompokkan, **tidak pernah dibuang**.

### Pertanyaan 6: Bagaimana menjaga arah tetap konsisten di proses yang panjang?

**Masalah sebenarnya.** Ini tantangan yang lahir dari rancangan skill sendiri. Enam fase berarti banyak keputusan, dan ide yang kuat di Fase 3 mudah hilang di Fase 6.

**Jawaban.** Semua keputusan dicatat di satu *Design Log* yang dibaca ulang di awal tiap fase. Setiap keputusan harus bisa ditelusuri ke sumbernya (pernyataan pengguna atau temuan riset → implikasi → rencana → elemen → eksekusi → klausa prompt); keputusan yang tidak punya sumber dianggap lahir dari kebiasaan dan ditolak. Jika sebuah cacat ditemukan, skill kembali ke fase paling awal yang bertanggung jawab lalu menjalankan ulang fase sesudahnya, bukan menambal di prompt.

---

## 5. Cara kerja

Enam pertanyaan di atas dijawab oleh satu alur enam fase yang berjalan **berurutan dan tidak boleh dilewati**, seberapa pun sederhana permintaannya. Brief yang sederhana memperpendek pekerjaan, tapi tidak menghapusnya.

```
  CERITA KAMU                                                     PROMPT SIAP PAKAI
       │                                                                  ▲
       ▼                                                                  │
  [1 Brief] → [2 Analisis] → [3 Rencana] → [4 Elemen] → [5 Susunan] → [6 Prompt]
   catat &      pahami         pilih satu    bangun       atur         tulis arahan
   verifikasi   masalah &      ide utama     sistem       komposisi    untuk AI image
                tempatnya                    visualnya    untuk mata   generator
```

| Fase | Yang dikerjakan | Padanan di dunia kerja | Menjawab pertanyaan |
|---|---|---|---|
| **1. Brief** | Menggali cerita usaha, tempat pasang, isi cetakan (kata per kata), kesan yang diinginkan, dan batasan. Berakhir dengan ringkasan yang kamu konfirmasi. | Account lead yang menolak menebak fakta | 3, 4, 5 |
| **2. Analisis** | Mencari tahu apa yang sungguh membedakan usahamu, seperti apa tempat pasangnya, dan bagian mana yang paling mudah gagal. | Brand strategist dan consumer-behavior researcher | 1, 2, 5 |
| **3. Design plan** | Memilih **satu ide utama**, gaya, dan hero lewat perbandingan kandidat sungguhan. | Creative concepting oleh senior art director | 1, 2 |
| **4. Design elements** | Menyusun warna, huruf, logo dan nama, designed copy, dan hiasan pendukung. Tiap elemen punya tugas yang hanya ia yang bisa kerjakan. | Graphic designer yang membangun design system | 2, 3 |
| **5. Execution** | Mengatur ruang, ukuran, dan urutan baca sesuai cara cetakan itu benar-benar dilihat. | Print designer dan visual communication specialist | 2, 5 |
| **6. Prompt synthesis** | Menerjemahkan semua keputusan menjadi arahan visual yang bisa dikerjakan ilustrator yang tidak pernah melihat brief aslinya. | Production brief dari art director ke ilustrator | 2, 6 |

Pemeriksaan kualitas (*quality control*) berjalan di setiap fase sebagai **gate**, dan di akhir sebagai audit prompt.

### Urutan prioritas jika syarat bertabrakan

1. Kebenaran fakta, isi wajib, larangan, dan aset yang kamu berikan
2. Keterbacaan di kondisi nyata (diselesaikan dengan menyusun ulang, **tidak dengan membuang isi wajib**)
3. Kesan, gaya, warna, dan prioritas yang kamu minta
4. Tujuan komunikasi dan strategi pembeda
5. Identitas merek yang tidak kamu berikan sebagai file
6. Ambisi kreatif

Ambisi desainer sengaja di urutan terakhir. Desain yang indah tapi mengabaikan permintaanmu adalah desain yang gagal.

### Kedalaman kerja

- **Full:** untuk logo baru, cetakan besar atau yang harus terlihat dari jauh, banyak sisi, atau isi yang padat.
- **Focused:** untuk cetakan biasa dengan identitas sederhana atau yang sudah ada.

Kedalaman hanya mengatur *seberapa luas* pekerjaan di dalam tiap fase (jumlah territory yang disurvei, jumlah benih logo, jumlah keberatan di gate). Tidak ada langkah wajib yang dihapus.

### Revisi

Permintaan revisi kembali ke fase paling awal yang bertanggung jawab (isi → Fase 1; ide atau suasana → Fase 3; warna, huruf, logo → Fase 4; susunan → Fase 5; kata-kata → Fase 6), lalu semua fase sesudahnya dijalankan ulang. Batasnya dua putaran per masalah. Setelah itu skill memilih resolusi terbaik dan menyebutkannya terang-terangan.

---

## 6. Konten

```
umkm-print-design/
├── SKILL.md                          ← Inti skill: misi, tim, alur 6 fase, prinsip,
│                                       prioritas konflik, larangan keras, kontrak output
└── references/
    ├── 00_conversation_ux.md         ← Aturan bicara dengan pengguna: bahasa, pertanyaan,
    │                                   wait note, tabel per fase, balasan akhir, glosarium
    ├── 01_brief_and_requirements.md  ← Fase 1: mencatat dan memverifikasi isi, mengubah
    │                                   kesan samar menjadi target visual
    ├── 02_research_and_analysis.md   ← Fase 2: pembeda, Environment Profile, perilaku
    │                                   audiens, Visual source inventory
    ├── 03_design_plan.md             ← Fase 3: territory survey, core idea, style, hero,
    │                                   governing principles, space intent, peran logo
    ├── 04_design_elements.md         ← Fase 4: warna, huruf, logo dan nama, copy treatment,
    │                                   supporters, background
    ├── 05_design_execution.md        ← Fase 5: viewing stages, space plan, spatial
    │                                   strategy, capacity check, composition review
    ├── 06_prompt_synthesis.md        ← Fase 6: apa yang masuk dan tidak masuk prompt,
    │                                   struktur, penulisan teks, audit
    ├── protocol.md                   ← Exploration protocol dan decision quality standard
    ├── quality_control.md            ← Gate, diagnostic tests, compliance audit, issue
    │                                   triage, release checklist
    └── terms.md                      ← Istilah bersama, satu arti di semua file
```

Setiap file dibaca **sekali, tepat ketika dibutuhkan**. File tiap fase diawali *phase card* (tujuan, masukan, prinsip, keputusan wajib, dan daftar periksa sebelum keluar), sehingga kalau proses tersesat, jalan pulangnya jelas: phase card, lalu Design Log, lalu komitmen keputusan.

**Yang dikeluarkan skill:**
- Selama percakapan: pertanyaan singkat, satu ringkasan, tabel keputusan per fase
- Di akhir: satu prompt per konsep atau per sisi cetakan (masing-masing dalam kotak kode sendiri), maksimal tiga langkah pakai, dan maksimal tiga catatan penting
- Tidak pernah ditampilkan: analisis internal, alasan desain yang panjang, dan Design Log

---

## 7. Batasan

**Cakupan**
- **Hanya cetakan fisik.** Untuk desain murni digital, skill akan memberi tahu bahwa ini di luar cakupannya dan menawarkan adaptasi, lalu baru berjalan setelah kamu setuju. Untuk karya campuran, kondisi cetak dijadikan acuan utama.
- **Bukan pengganti desainer untuk brand identity yang besar.** Skill menggarap satu cetakan atau satu logo dengan matang, bukan sistem merek multi-tahun.

**Hasil akhir**
- **Skill menulis prompt, bukan menggambar.** Kualitas akhir bergantung pada AI image generator yang dipakai, dan hasilnya bisa berbeda dari satu percobaan ke percobaan lain.
- **AI image generator masih bisa salah menulis**, terutama teks panjang, harga, dan nomor. Pemeriksaan manual atas semua tulisan wajib dilakukan.
- **Bukan file siap cetak.** Ukuran, resolusi, margin potong (*bleed*), dan mode warna perlu dipastikan bersama percetakan.
- **Rasio yang sangat panjang** (misalnya spanduk 1:4) mungkin perlu dipotong atau disesuaikan. Skill mencatatnya bila relevan.
- **QR, QRIS, barcode, dan foto asli tidak bisa dibuat atau ditiru.** Skill menyiapkan area di dalam komposisi, dan kamu memasang file aslinya.

**Soal fakta**
- **Tidak menciptakan fakta usaha.** Harga, klaim, testimoni, sertifikasi, tanda halal atau tanda kepercayaan lain, kontak, bahan, dan tahun berdiri hanya muncul jika kamu yang memberikannya. Kalau cetakan butuh tagline dan kamu tidak punya, skill menulis yang faktual dan sederhana, lalu menandainya di catatan.
- **Riset bergantung pada alat yang tersedia.** Tanpa akses pencarian, skill bernalar dari ceritamu, menandai kesimpulannya sebagai sementara, dan menghindari pilihan yang bergantung pada detail yang belum terverifikasi.

**Soal proses**
- **Bukan jalan pintas satu klik.** Enam fase berjalan penuh, jadi butuh beberapa menit dan beberapa interaksi (di auto mode, hanya satu kali menunggu). Itu harga dari desain yang dipikirkan, bukan ditempelkan.
- **Kesan, gaya, dan warna yang kamu minta mengikat.** Jika sebuah permintaan melemahkan tujuan cetakan, skill tetap mengikutinya, mengurangi kelemahannya dari dalam, dan menyampaikan kekhawatirannya **sekali** sebagai saran.

---

## 8. Untuk reviewer dan praktisi desain

### Gagasan inti

**Desain adalah rantai keputusan yang bisa ditelusuri, bukan satu loncatan inspirasi.** Setiap klausa prompt dapat dilacak mundur:

> butir brief atau temuan riset → design implication → plan decision → element decision → execution decision → prompt clause

Cacat ditemukan dan diperbaiki di akarnya, lalu fase-fase sesudahnya dijalankan ulang (*return, then re-run forward*), bukan ditambal di prompt.

### Keputusan rancangan yang layak diperhatikan

| Keputusan | Alasannya |
|---|---|
| **Exploration protocol dengan "apparent option" sebagai benchmark** (≥3 kandidat, evaluasi dibalik urutan, runner-up, satu decisive criterion, strength-weakness engineering) | Melawan jawaban rata-rata pada sumbernya. Pilihan klise boleh menang, tapi harus membayar dengan alasan yang bisa disebut. |
| **Design territory survey lintas keluarga sumber** (gerakan sejarah, vernakular lokal, craft dan produksi, praktik lintas kategori, dunia si usaha) | Kandidat dangkal berasal dari asosiasi bawaan model terhadap kategori. Survei memperlebar medan sebelum evaluasi dimulai. |
| **Originality tests**: apparent-choice, lineage, synthesis, depth, distinctness | Gaya harus bisa disebut lewat lineage dan ciri pembentuknya, bukan mood. Kata bergengsi yang tidak bisa didefinisikan dianggap kekaburan dan dibuang. |
| **Kesan samar diperlakukan sebagai spesifikasi teknis** (*quality translation*: target visual, 2 sampai 4 quality carriers, contradicting signals) | Brief berisi kata sifat adalah sumber utama kegagalan. *Value key* dihitung dari proporsi luas, termasuk latar dan blok besar, karena massa gelap yang dominan membatalkan "ringan dan lapang" seberapa pun terang aksennya. |
| **Environment as parameter** (dimensi *departure* dan *fit*) | Pembeda hanya valid relatif terhadap tetangga. Prinsipnya: tahan kesan yang diinginkan tetap, biarkan tempat menentukan ekspresinya. |
| **Space plan sebelum placement; urutan tetap: viewing stages → space plan → sizes → placement** | Negative space adalah keputusan terencana dengan tugas yang jelas. Ukuran baru dicetak setelah capacity check, bukan dikoreksi sesudahnya. |
| **Grouping menurut referen** (integrated, attached, separate), bukan hanya urutan baca | Teks yang melabeli, menjelaskan, atau memberi harga sebuah objek disusun bersama objek itu. Pengelompokan murni menurut urutan perhatian menghasilkan "gambar dengan keterangan". |
| **Extended mark development** (seeds, personality device, truth expressed, distinction mechanisms, unit and disconnection tests) | Logo UMKM paling sering gagal sebagai "nama berfont bagus". Kesatuan mark dan wordmark dites dengan menutup salah satunya. |
| **Prompt boundary yang tegas** | Strategi, riset, dan alasan "karena" tidak masuk prompt. Hanya yang mengubah isi gambar yang masuk (*visual-effect test*). Ukuran dinyatakan sebagai proporsi, dan penekanan hanya untuk elemen yang memang dominan. |
| **Pemisahan bahasa** | Percakapan Indonesia untuk kenyamanan manusia, kerja internal dan prompt Inggris untuk performa AI image generator, teks cetak tetap dalam bahasa aslinya kata per kata. |
| **Non-negotiables yang tidak bisa dikalahkan strategi kreatif** | Fakta, teks pengguna, aset tetap, dan kesan yang diminta menang atas "keberanian" desain. Ini melindungi pemilik usaha dari hasil yang indah tapi tidak jujur. |

### Failure modes yang diantisipasi

Tiap fase mencatat failure mode dengan cara deteksi dan koreksinya, antara lain: menginterogasi pengguna, saran yang diperlakukan sebagai fakta, normalisasi teks diam-diam, referensi yang diperlakukan sebagai template, brief berisi kata sifat yang dianggap "tanpa syarat", hiasan yang tidak menjawab kekurangan apa pun, dan prompt yang bercampur komentar. Cacat diklasifikasikan menurut tingkat keparahan dan dirutekan ke fase paling awal yang bertanggung jawab.