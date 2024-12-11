from Animal import *
print("===================== Jenis Hewan Ular =====================")
class Ular(Animal):
    def __init__(self, Nama, Makanan, Hidup, Berkembang_biak, Design, Racun):
        super().__init__(Nama, Makanan, Hidup, Berkembang_biak)
        self.Design = Design
        self.Racun = Racun
        
    def cetak_ular(self):
        super().cetak()
        print("Design \t\t\t\t: ", self.Design,
              "\nRacun \t\t\t\t: ", self.Racun)
        
print("===================== Ular Sawah =====================")
Sawah = Ular("Sawah/Welang-weling", "Ayam", "Persawahan", "Bertelur", "Loreng-loreng", "Tidak Berbisa")
Sawah.cetak_ular()

print("===================== Ular Piton =====================")
Piton = Ular("Piton", "Tikus", "Darat", "Bertelur", "Corak Hitam-Coklat", "Berbisa")
Piton.cetak_ular()

print("==================== Ular Anaconda ===================")
Anaconda = Ular("Anaconda", "Hewan Kecil/Reptilia", "Amazon", "Bertelur", "Anaconda Hijau", "Berbisa")
Anaconda.cetak_ular()
