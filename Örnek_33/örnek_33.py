"""
Klavyeden -1 sayısı girilene kadar ekrana sayı girişine izin veren program

"""

kontrol = True

while kontrol:
    sayi = int(input("Sayi giriniz : "))

    if sayi == -1:
        kontrol = False
