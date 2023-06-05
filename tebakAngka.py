import random


def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    tebakan = 0
    jumlah_tebakan = 0

    print("Halo! Mari bermain tebak angka. ")
    print("Saya telah memilih angka antara 1 hingga 100. Coba tebak yaa")

    while tebakan != angka_rahasia:
        tebakan = int(input("Masukkan tebakan Anda :"))
        jumlah_tebakan += 1

        if tebakan < angka_rahasia:
            print("Tebakan anda terlalu rendah. Coba Lagi !")
        elif tebakan > angka_rahasia:
            print("Tebakan Anda terlalu tinggi. Coba lagi! ")

    print(
        f"Selamat ! Anda berhasil menebak angka {angka_rahasia} dengan {jumlah_tebakan} tebakan .")


tebak_angka()
