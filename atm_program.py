import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("Masukan pin anda: "))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input("Pin anda salah. Silahkan coba lagi: "))

        trial += 1

        if trial == 3:
            print("Error. Silahkan ambil kartu dan coba lagi..")
            exit()

    while True:
        print("Selamat datang di ATM Console Python")
        print("\n1 - Cek Saldo \t 2 - Debat \t 3 - Simpan \t 4 - Gannti Pin \t 5 - Keluar")

        selectmenu = int(input("\nSilakan pilih menu: "))
        if selectmenu == 1:
            print("\nSaldo anda sekarang: Rp. " +
                  str(atm.checkBalance()) + "\n")

        elif selectmenu == 2:
            nominal = float(input("Masukan nominal saldo: "))
            verify_withdraw = input(
                "Konfirmasi:\nAnda akan melakukan debet dengan nominal berikut ?\n" + str(nominal) + "\nSilahkan pilih: y/n" + "\n")

            if verify_withdraw == "y":
                print("Saldo awal anda adalah: Rp. " +
                      str(atm.checkBalance()) + "")
            else:
                break
            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi debet berhasil!")
                print("Saldo sekarang:Rp. " + str(atm.checkBalance()) + "")
            else:
                print("Maaf. Saldo tidak cukup untuk melakukan debet!")
                print("Silahkan lakukan penambahan nominal saldo")

        elif selectmenu == 3:
            nominal = float(input("Masukan nominal saldo: "))
            verify_deposit = input(
                "Konfirmasi:\nAnda akan melakukan penyimpanan dengan nominal berikut ? y/n \n" + str(nominal) + " ")

            if verify_deposit == "y":
                atm.depositBalance(nominal)
                print("Saldo anda sekarang adalah: Rp. " +
                      str(atm.checkBalance()) + "\n")
            else:
                break

        elif selectmenu == 4:
            verify_pin = int(input("Masukan pin anda: "))

            while verify_pin != int(atm.checkPin()):
                print("Pin anda salah, silahkan coba lagi:")

            update_pin = int(input("Silahkan masukan pin baru: "))
            print("Pin anda berhasil diganti!")

            verify_newpin = int(input("Silahkan masukan pin baru: "))

            if verify_newpin == update_pin:
                print("Pin baru berhasil di verifikasi!")
            else:
                print("Maaf, pin anda salah!!")

        elif selectmenu == 5:
            print("Resi tercetak otomatis saat anda keluar.\nHarap simpan tanda terima ini sebagai bukti transaksi anda.")
            print("=" * 50)
            print("No. Rekord: ", random.randint(100000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("=" * 50)
            print("Terimakasih telah setia mengunakan ATM Console Python!")
            exit()

        else:
            print("Error. Maaf, nampaknya menu yang kamu pilih tidak tersedia")
