"""
Girilen sayinin mutlak değerini bulan program

"""

girilenSayi = int(input("Sayi : "))


if girilenSayi < 0:
    girilenSayi *= -1

print("Girdiğiniz sayinin mutlak değeri : ", girilenSayi)