# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)
# buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method  
# buat minimal 2 objek dari masing2 class child
print("Membuat 4 Class Animal, Minimal 3 Class Child Memiliki ; 2 Properti & Method & Memiliki 2 Objek :")
class Animal:
    def __init__(self, Nama, Makanan, Hidup, Berkembang_biak):
        self.Nama = Nama
        self.Makanan = Makanan
        self.Hidup = Hidup
        self.Berkembang_biak = Berkembang_biak
        
    def cetak(self):
        print("Nama\t\t\t\t: ", self.Nama,
              "\nMakanan\t\t\t\t: ", self.Makanan,
              "\nHidup\t\t\t\t: ", self.Hidup,
              "\nBerkembang_biak\t\t\t: ", self.Berkembang_biak
              )    
        