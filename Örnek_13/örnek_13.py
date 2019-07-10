"""
Girilen 5 sayidan negatif olanların toplamını yazdıran program

"""
negatifToplam = 0

for i in range(0, 5):
    girilenSayi = int(input("{}. Sayiyi Giriniz: ".format(i+1)))

    if girilenSayi < 0:
        negatifToplam += girilenSayi

print("Negatif toplam = ", negatifToplam)
print("Mutlak Degeri = ", abs(negatifToplam))