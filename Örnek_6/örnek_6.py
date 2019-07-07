"""
girilen sayinin faktoriyelini hesaplayan program

"""

girilenSayi = int(input("Sayiyi giriniz: "))
fatoriyel = 1

for i in range(1, girilenSayi + 1):
    fatoriyel *= i

print("Girdiğiniz sayinin faktoriyeli: ", fatoriyel)