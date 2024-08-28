# Disable_Wifi_Monitor

Skrip sederhana meonaktifkan atau aktifkan jaringan wifi apa pun yang ditemukan dalam jangkauan perangkat PC atau router dengan mode monitor yang Terdiri dari subproses, optparse, dan kita juga dapat menggunakan modul waktu (untuk berapa lama Anda ingin menonaktifkan wifi Anda atau wifi lain yang ditemukan)

# Syarat

Sebelum anda menggunakan nya pastikan di system anda sudah memenuhi syarat yang di butuhkan:

- Python 3.x
- Aircrack-ng suite

- system kali linux
- adaptor eksternal nirkabel / adaptor usb wifi


Setelah persayaratan terpenuhi anda bisa menggunakanya

## installasi


1. **Clone repository ini**:

   ```bash
   git clone https://github.com/Yoga913/Disable_Wifi_Monitor.git
   cd Disable_Wifi_Monitor
   ```

## Cara Penggunaan

1. **Jalankan Skrip**:

   ```bash
   python3 Disable_Wifi_Monitor.py -i <interface>
   ```

   Ganti `<interface>` dengan antarmuka jaringan Anda, seperti `wlan0` atau `wlan0mon`.

2. **Ikuti Petunjuk**:

   - Skrip akan meminta antarmuka baru setelah mengaktifkan mode monitor.
   - Masukkan alamat MAC dan saluran WiFi target sesuai petunjuk.

## Contoh

```bash
python3 Disable_Wifi_Monitor.py -i wlan0
```

- Anda akan diminta untuk memasukkan antarmuka baru, alamat MAC, dan saluran target. Gunakan informasi ini untuk memulai serangan yang diinginkan.

## Catatan Penting

- Skrip ini dapat digunakan untuk pengujian penetrasi jaringan WiFi. Pastikan Anda memiliki izin eksplisit dari pemilik jaringan sebelum menggunakan skrip ini.
- Penulis tidak bertanggung jawab atas penyalahgunaan alat ini.

## Kontribusi

Silakan buat pull request atau buka issue untuk perbaikan atau tambahan fitur.

## Lisensi

Skrip ini dilisensikan di bawah [MIT Lisensi]. Lihat file `LICENSE` untuk detailnya.
