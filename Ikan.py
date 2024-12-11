from Animal import *

print("====================== Hewan Ikan ========================")
class Ikan(Animal):
    def __init__(self, Nama, Makanan, Hidup, Berkembang_biak, Jenis, Motif):
        super().__init__(Nama, Makanan, Hidup, Berkembang_biak)
        self.Jenis = Jenis
        self.Motif = Motif
        
    def cetak_ikan(self):
        super().cetak()
        print("Jenis \t\t\t\t: ", self.Jenis,
              "\nMotif \t\t\t\t: ", self.Motif)
        
print("===================== Ikan Koi ======================")        
Koi = Ikan("Koi", "Cacing", "Air Tawar", "Bertelur", "Asagi", "Oren Putih")
Koi.cetak_ikan()  

print("===================== Ikan Hiu ======================")
Hiu = Ikan("Hiu", "Hewan Kecil", "Perairan Laut Dalam", "Melahirkan", "Hiu Tutul", "Tutul")
Hiu.cetak_ikan()  

print("==================== Ikan Cupang ====================")
Cupang = Ikan("Cupang", "Jentik Nyamuk", "Air tawar/Sungai", "Bertelur", "Plakat/Ekor Pendek", "Warna-Warni")
Cupang.cetak_ikan()