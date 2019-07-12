"""
Girilen sayinin Güçlü sayi olup olmadığını söyleyen program

Not: rakamları çarpımı ile rakamları toplamının toplamı kendine
eşit olan iki basamaklı sayılara denir.

"""

girilenSayi = int(input("Sayiyi giriniz: "))

if (girilenSayi > 99) & (girilenSayi < 10):
    print("İki basamaklı bir sayi girmelisiniz.")

birlerBasamagi = girilenSayi % 10
onlarBasamagi = (girilenSayi - birlerBasamagi)/ 10

rakamlarToplami = birlerBasamagi + onlarBasamagi
rakamlarCarpimi = birlerBasamagi * onlarBasamagi

if (girilenSayi == rakamlarCarpimi + rakamlarToplami):
    print("Bu sayi bir Güçlü Sayidir.")
else:
    print("Bu sayi bir Güçlü Sayi değildir.")