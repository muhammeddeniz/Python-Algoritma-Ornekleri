"""
Klavyeden girilen sayinin pozitif negatif veya 0 olduğunu söyleyen program

"""
girilenSayi = int(input("Sayi giriniz: "))

if girilenSayi > 0:
    print("Girdiğiniz sayi pozitiftir.")
elif girilenSayi < 0:
    print("Girdiğiniz sayi negatiftir.")
else:
    print("Girdiğiniz sayi 0'dır.")
