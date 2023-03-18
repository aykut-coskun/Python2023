class Matematik:
    def __init__(self,sayi1,sayi2): # contructor- yapıcı blok
        self.s1 = sayi1
        self.s2 = sayi2
        print("Matematik başladı (referansı oluştu)")
    
    def topla(self):
        return self.s1 + self.s2
    
    def cikar(self):
        return self.s1 - self.s2
    
    def bol(self):
        return self.s1 / self.s2
    
    def carp(self):
        return self.s1 * self.s2


matematik = Matematik(14,7)
sonuc = matematik.bol()
print("Sonuç : " + str(sonuc))

class Istatistik(Matematik):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)
    def varyansHesapla(self):
        return self.s1 * self.s2

# inheritance - kalıtım

Istatistik = Istatistik(5,8)