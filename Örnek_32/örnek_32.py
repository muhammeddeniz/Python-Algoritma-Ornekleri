"""
Girilen 5 adet sayidan en büyük olanını ekrana yazan program

"""

buyukSayi = 0

for i in range(0, 5):
    girilenSayi = int(input("Sayi giriniz: "))
    if (girilenSayi > buyukSayi):
        buyukSayi = girilenSayi

print("En büyük sayi = ", buyukSayi)