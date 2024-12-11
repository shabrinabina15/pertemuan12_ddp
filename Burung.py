from Animal import *

print("===================== Jenis Hewan Burung =====================")
class Burung(Animal):
    def __init__(self, Nama, Makanan, Hidup, Berkembang_biak, Jenis, Umur):
        super().__init__(Nama, Makanan, Hidup, Berkembang_biak)
        self.Jenis = Jenis
        self.Umur = Umur
        
    def cetak_burung(self):
        super().cetak()
        print("Jenis \t\t\t\t: ", self.Jenis,
              "\nUmur \t\t\t\t: ", self.Umur)
        
print("===================== Burung Gereja ======================")
Gereja = Burung("Gereja", "Biji-bijian", "Udara", "Bertelur", "Betina", "4 Tahun")
Gereja.cetak_burung()

print("===================== Burung Merpati =====================")
Merpati = Burung("Merpati", "Biji-bijian", "Udara", "Bertelur", "Betina", "2 Tahun")
Merpati.cetak_burung()

print("===================== Burung Unta ========================")
Merpati = Burung("Unta", "Biji-bijian", "Gurun Savana", "Bertelur", "Betina", "8 Tahun")
Merpati.cetak_burung()