"""
Girilen 6 tam sayinin ortalamasını ekrana yazdıran program

"""
toplam = 0
ort = 0

for i in range(1, 7):
    girilenSayi = int(input("Sayi giriniz : "))
    toplam += girilenSayi

ort = toplam / 6
print("Ortalama = ", ort)