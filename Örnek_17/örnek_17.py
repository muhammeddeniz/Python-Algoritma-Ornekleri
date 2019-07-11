"""
Klavyeden girilen sayinin mükemmel sayi olup olmadığını söyleyen program

Not: Kendisi hariç bütün pozitif bölenlerinin toplamı kendisine eşit olan sayılara mükemmel sayı denir.
"""

girilenSayi = int(input("Sayi giriniz: "))

bolenToplami = 0

for i in range(1, girilenSayi):
    if (girilenSayi % i == 0):
        bolenToplami += i

if (bolenToplami == girilenSayi):
    print("Bu sayi bir mükemmel sayidir.")
else:
    print("Bu sayi bir mükemmel sayi değildir.")