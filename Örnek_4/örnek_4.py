"""
hem üst değeri hem tabanı girilen sayiyi buulan program

"""

taban = input("Sayiyi giriniz: ")
üstDegeri = input("Üst değerini giriniz: ")
sonuc = 1

for i in range(1, int(üstDegeri)+1):
    sonuc *= int(taban)

print("Sonuc: ", sonuc)