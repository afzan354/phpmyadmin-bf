

---

# 🔐 phpMyAdmin Brute Forcer (`phpmyadmin_bf.py`)

Script ini digunakan untuk melakukan brute-force login pada halaman login **phpMyAdmin** menggunakan kombinasi username dan password dari file. Dirancang untuk tujuan **pengujian keamanan lokal** atau sistem milik sendiri.

⚠️ **PERINGATAN: Script ini hanya boleh digunakan untuk keperluan edukasi dan pengujian sistem yang sah. Penyalahgunaan terhadap sistem tanpa izin adalah tindakan ilegal.**

---

## 🧩 Fitur

* Membaca username dan password dari file (`user.txt` dan `pass.txt`)
* Menangani CSRF token (`token`) dan parameter session (`set_session`) dari halaman login
* Menggunakan sesi (`requests.Session`) untuk menjaga cookies
* Mendeteksi login sukses berdasarkan kemunculan string `Logout`

---

## 📁 Struktur File

Pastikan kamu menyiapkan file berikut:

```
phpmyadmin_bf.py
user.txt     # Daftar username, satu per baris
pass.txt     # Daftar password, satu per baris
```

Contoh `user.txt`:

```
root
admin
test
```

Contoh `pass.txt`:

```
root
123456
admin123
```

---

## ⚙️ Instalasi

1. **Clone repo ini**:

   ```bash
   git clone https://github.com/username/phpmyadmin-bf.git
   cd phpmyadmin-bf
   ```

2. **Install dependencies Python**:
   Script ini memerlukan `requests` dan `beautifulsoup4`.

   ```bash
   pip install requests beautifulsoup4
   ```

---

## 🧪 Target Default

Script ini secara default menargetkan:

```
http://localhost/phpmyadmin/index.php
```

Jika kamu ingin menguji pada target yang berbeda (misalnya server lokal atau di jaringan lain), edit baris berikut dalam script:

```python
url = 'http://localhost/phpmyadmin/index.php'
```

---

## ▶️ Cara Menjalankan

```bash
python phpmyadmin_bf.py
```

Output akan menampilkan hasil setiap percobaan:

```
Failed: root - 123456
Failed: root - admin123
Success! Username: root, Password: root
```

Jika login berhasil, percobaan akan berhenti dan mencetak kombinasi yang valid.

---

## ⚠️ Disclaimer

* Script ini **tidak boleh digunakan** untuk menyerang situs phpMyAdmin yang bukan milikmu atau tanpa izin eksplisit.
* Penggunaan ilegal dapat dikenakan sanksi hukum sesuai peraturan yang berlaku di wilayahmu.

---

## 📄 Lisensi

Distribusi bebas untuk **edukasi dan audit keamanan sistem sendiri**. Gunakan dengan etika dan tanggung jawab penuh.

---


