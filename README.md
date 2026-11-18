# Rekod Program JAWHAR — Paparan Awam

Laman lihat sahaja untuk Rekod Program dan Aktiviti Bahagian Baitulmal, JAWHAR.
Pengguna boleh melihat Papan Pemuka, Senarai program dan menjana Laporan PDF **tanpa log masuk**. Alat pentadbiran (eksport CSV, sandaran dan sebagainya) tidak tersedia pada laman awam.

## Cara ia berfungsi

| Bahagian | Fungsi |
|---|---|
| **App Editor** (Claude, peribadi) | Sumber data utama. Editor memasukkan dan mengemas kini rekod di sini. |
| **`data.json`** (repositori ini) | Salinan data untuk paparan awam. Dijana daripada app Editor. |
| **`index.html`** (GitHub Pages) | Laman awam. Membaca `data.json` setiap kali dibuka. |

Laman awam tidak mempunyai pangkalan data, kata laluan atau fungsi menulis, jadi tiada apa yang boleh diubah oleh pengunjung.

## Pemasangan kali pertama (kira-kira 5 minit)

1. Di GitHub, cipta repositori baharu (contoh: `rekod-program-jawhar`).
2. Muat naik **semua fail dan folder** dalam pakej ini ke repositori (Add file, kemudian Upload files). Pastikan `.github`, `tools`, `.nojekyll`, `index.html`, `data.json` dan `robots.txt` turut dimuat naik.
3. Pergi ke **Settings, kemudian Pages**. Di bawah *Build and deployment*, pilih **Deploy from a branch**, cawangan **main** dan folder **/ (root)**, kemudian Save.
4. Selepas satu hingga dua minit, alamat laman awam dipaparkan di bahagian atas halaman Pages, biasanya `https://<nama-pengguna>.github.io/<nama-repositori>/`.

## Cara kemas kini data (sync)

1. Dalam app Editor, buka tab **Pentadbiran**, kemudian tekan kad **Terbit ke GitHub**.
2. Pilih pilihan privasi (lihat di bawah), kemudian tekan **Muat turun data.json**.
3. Di repositori, buka fail `data.json`, pilih ikon pensel atau Add file, kemudian Upload files, dan ganti dengan fail baharu. Tekan **Commit changes**.
4. GitHub menyemak fail secara automatik (format, tarikh dan **rekod pendua**). Jika semakan gagal, tanda silang merah muncul pada commit itu dan mesej ralat menyatakan baris yang bermasalah. Betulkan di app Editor dan muat naik semula.
5. Laman awam dikemas kini dalam kira-kira satu minit.

Sepanduk di bahagian atas laman awam menunjukkan tarikh dan masa data terakhir dikemas kini.

## Privasi: baca sebelum menerbitkan

- **Semua orang di internet yang mempunyai pautan boleh melihat data ini**, termasuk fail `data.json` yang boleh dimuat turun terus. Repositori mestilah *public* untuk GitHub Pages pada pelan percuma.
- Secara lalai app Editor **tidak menerbitkan nama pegawai**. Nama diganti "Pegawai A, B, C..." secara konsisten supaya statistik kekal tepat tanpa mendedahkan identiti.
- Catatan program dan nota KP/TKP **tidak diterbitkan** melainkan anda menandanya.
- Kehadiran KP/TKP (hadir, diwakili atau tidak hadir) dan bilangan kehadiran **diterbitkan** kerana ia diperlukan untuk statistik.
- Laman ini mempunyai tag `noindex` dan `robots.txt` supaya enjin carian tidak menyenaraikannya. Ini **bukan** kawalan akses; sesiapa yang tahu pautan masih boleh membukanya.
- Pastikan penerbitan ke awam telah mendapat kelulusan jabatan mengikut dasar ICT dan tadbir urus data yang berkuat kuasa.

## Keselamatan laman

- Tiada skrip dimuat dari pelayan luar. Pustaka penjana PDF disertakan dalam `index.html`. Hanya fon Google dimuat dari luar.
- Dasar keselamatan kandungan (CSP) dalam `index.html` menyekat sambungan ke laman lain.
- Semua teks daripada `data.json` dipaparkan secara selamat dan tidak boleh melaksanakan kod.
- Kawal siapa yang boleh menulis ke repositori: beri akses *Write* kepada penyelenggara yang dipercayai sahaja, dan aktifkan pengesahan dua faktor pada akaun GitHub.

## Fail dalam pakej

```
index.html                 laman awam (lihat sahaja)
data.json                  data program (dikemas kini daripada app Editor)
robots.txt, .nojekyll      tetapan laman
tools/validate_data.py     semakan format dan pendua
.github/workflows/validate.yml   menjalankan semakan setiap kali data.json diubah
```

## Perubahan reka bentuk laman

`index.html` dijana daripada app Editor. Jika reka bentuk atau fungsi app berubah, minta versi `index.html` baharu dan ganti fail ini. Kemas kini data biasa **tidak** memerlukan `index.html` baharu, hanya `data.json`.
