"""
Girilen 10 sayidan pozitiflerin ve negatiflerin sayisini gösteren program

"""

pozitifSayisi = 0
negatifSayisi = 0

for i in range(0,10):
    girilenSayi = int(input("{}. sayiyi giriniz : ".format(i+1)))

    if girilenSayi > 0:
        pozitifSayisi += 1
    elif girilenSayi < 0:
        negatifSayisi += 1

print("{} tane pozitif sayi var".format(pozitifSayisi))
print("{} tane negatif sayi var".format(negatifSayisi))