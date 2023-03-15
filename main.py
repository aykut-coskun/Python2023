# str -> string, metinsel ifade
kurs = "Python kursu"
print(kurs)

# int -> tam sayı
x = 20

# float -> ondalik sayı
x = 20.5

# complex -> a+bj şeklinde gerçek ve sanal kısımdan oluşan tip 
x = 5+5j

# list -> birbirinden farklı veri tipine sahip değiş. barındıran saıralı ve değiştirilebilir veri tipi
list = ["elma","ayva","kivi"]

# tuple -> sıralı ve değiştirilemez bir koleksiyondur
x = tuple("elma")

# boolean -> mantıksal veri tipi. True yada False olmak üzere iki değere sahiptir
x = 20
y = 25

print(x > y)
print(x < y)


# Kodlama.io sitesindeki kurslar, eğitmenler-> string 
kurs1 = "Java"
kurs2 = "C#"
egitmen1 = "Engin Demiroğ"

# Kodlama.io'daki Ödev tamamlama yüzdeleri -> int 
odevYuzdesi = 20


# Kodlama.io sitesinde giriş yap kısmı şart bloğuna örnek 

isim = "Aykut"
sifre = "12345"
durum1 = "Başarılı"
durum2 = "Başarısız"

if isim == durum1 and sifre == durum1:
    print("Siteye giriş yapıldı")
elif isim != durum2 and sifre == durum2:
    print("İsim hatalı")
elif isim == durum2 and sifre != durum2:
    print("Şifre hatalı")
else:
    print("isim ve şifre giriniz")


