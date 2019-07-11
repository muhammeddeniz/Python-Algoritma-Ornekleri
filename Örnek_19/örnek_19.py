"""
Herhangi bir sayinin herhangibir dereceden kuvvetini hesaplayan program

"""

import  random

sayi = random.randint(1, 100)
ustDegeri = random.randint(1, 50)
sonuc = 1

print("Sayi = ", sayi)
print("Ust = ", ustDegeri)

for i in range(1, ustDegeri):
    sonuc *= sayi

print("Sonuc = ", sonuc)