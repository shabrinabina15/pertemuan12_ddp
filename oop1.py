class person:
    nama = ""
    gender = ""
    umur = ""
    
    def __init__(self, nama, gender, umur):
        self.nama = nama
        self.gender = gender
        self.umur = umur
        
    def cetak(self):
        print("nama \t\t :", self.nama, "gender \t\t :", self.gender, "umur \t\t :", self.umur)
        
class person:
    def _init_(self, nama, umur, jenis_kelamin):
        self.jenis_kelamin = jenis_kelamin
        
    def jalan(self):
        print(f"")
        
    def ngomong(self):
        print(f"dia berbicara karena dia {self.jenis_kelamin}")
        
    def jenis_kelamin(self):
        print(f"")
        
        
class supir(person):
    def _init_(self, nama, umur, jenis_kelamin, sim):
        super()._init_(nama, umur, jenis_kelamin)
        self.sim = sim
        
    def nyupir(self):
        print(f"{self.nama} bisa nyupir karena memilki SIM A {self.sim}")
    
    
class mahasiswa(person):
    def _init_(self, nama, umur, jenis_kelamin):
        super()._init_(nama, umur, jenis_kelamin)
    
    
bayu = person("bayu", 20, "laki-laki")
bayu.jalan()
bayu.ngomong()
bayu.nyupir()

andi = supir("andi", 30, "laki-laki") 
andi.nyupir()    

bunga = mahasiswa("bunga", 20, "perempuan", "0121131")