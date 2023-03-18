# Bir öğrenci kayıt sistemi yazdığımızı düşünelim. 
# Sistemizmizdeki öğrenciler bir listede sadece ad soyad olacak şekilde tutalım
# Bu öğrenci kayıt sistemine:

# Aldığı isim soy isim ile listeye öğrenci ekleyen

students = ["Aykut Coşkun", "İlhan Coşkun"]
print(students)

print("******************")

def studentAdd():
    name = input("Öğrenci adı giriniz: ")
    surname = input("Öğrenci soyadı giriniz: ")
    students.append(name + " " + surname)
    print("Öğrenci listeye eklendi")
    print(students)
studentAdd()

print("*******************")


# Aldığı isim soyisim ile eşleşen değeri listeden kaldıran

def studentRemove():
    name = input("Silinecek öğrenci adını giriniz: ")
    surname = input("Silinecek öğrenci soyadını giriniz: ")
    students.remove(name + " " + surname)
    print("Öğrenci listeden silindi")
    print(students)
studentRemove()

print("*******************")

# Listeye birden fazla öğrenci eklemeyi mümkün kılan

def studentsAdd():
    number = int(input("Kaç tane yeni öğrenci kaydı eklenecek: "))
    for i in range(number):
        addStudent = input("Yeni öğrencinin adı soyadı: ")
        students.append(addStudent)
        i +=1
        print("Öğrenciler listeye eklendi")
        print(students)
studentsAdd()

print("*******************")

# Listedeki tüm öğrencileri tek tek ekrana yazdıran

def studentList():
    student = 0
    for student in range(len(students)):
        print(students[student])
        student +=1
print("Öğrenciler listelendi")
studentList()

print("*******************")

# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul
# edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan

def studentNumberFind():
   student = input("Numarası öğreneilecek öğrencinin adı soyadı: ")
   i=0
   while i < len(students):
    if students[i] == student:
        print("Öğrenci numarası: ")
        print(i)
        break
    i +=1
studentNumberFind() 


print("*******************")

# Listede birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)

def studentsDelete():
    deleteNumber = int(input("Silinecek öğrenci sayısı: "))
    for i in range(deleteNumber):
        studentDelete = input("Silinecek öğrencinin adı soyadı: ")
        students.remove(studentDelete)
        i +=1
        print("Öğrenciler silindi")
        print(students)
studentsDelete()
    