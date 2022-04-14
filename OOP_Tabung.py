import os
os.system("clear")

class Volume:

    def __init__(self, phi, r, T) -> None:
        self.phi = phi
        self.r = r
        self.T = T

    def get_volume(self):
        return self.phi * self.r * self.r * self.T


class luas(Volume):

    def __init__(self, phi, r, T) -> None:
        super(luas, self).__init__(phi, r, T)
  
    def get_luasSelimut(self):
        return 2 * self.phi * self.r * self.T

    def get_luasPermukaan(self):
        return (2 * self.phi * self.r * self.T) + (2 * self.phi * self.r * self.r)


class main:
    a = ("PROGRAM MATEMATIKA TABUNG")
    b = ("by : Hilmy Adrizul Rifqi Hidayat")
    print("\n","="*80)
    print(a.center(80," "))
    print(b.center(80," "))
    print("="*80)

    print("1. Hitung Volume ")
    print("2. Hitung Luas Selimut")
    print("3. Hitung Luas Permukaan\n")

    pilih = int(input("Masukan Pilihan      : "))

    if pilih == 1:
        print("Rumus Luas Volume    : phi * r * r * T")
        phi = 3.14 #Sesuai Ketentuan Matematika
        r = float(input("\nMasukan Jari - Jari Tabung : "))
        T = float(input("Masukan Tinggi Tabung      : "))

        Volume1 = Volume(phi, r, T)
        hasil = Volume1.get_volume()
        print("Luas Volume Tabung adalah  :", hasil, "\n")


    elif pilih == 2:
        print("Rumus Luas Selimut   : 2 * phi * r * T")
        phi = 3.14 #Sesuai Ketentuan Matematika
        r = float(input("\nMasukan Jari - Jari Tabung : "))
        T = float(input("Masukkan Tinggi Tabung     : "))

        luas1 = luas(phi, r, T)
        hasil = luas1.get_luasSelimut()
        print("Luas Selimut Tabung adalah :", hasil, "\n")


    elif pilih == 3:
        print("Rumus Luas Permukaan : 2 * phi * r * T + 2 * phi * r * r")
        phi = 3.14 #Sesuai Ketentuan Matematika
        r = float(input("\nMasukan Jari - Jari Tabung  : "))
        T = float(input("Masukkan Tinggi Tabung      : "))  

        luasPerm = luas(phi, r, T)
        hasil = luasPerm.get_luasPermukaan()
        print("Luas Permukaan Tabung adalah :", hasil, "\n")