"""
Girilen 3 basamaklı bir sayının basamaklarının küpleri toplamı sayının
kendine eşit olup olmadığını bulan program (Armstrong sayı)

"""
def kupAl(sayi):
    sayi = sayi*sayi*sayi
    return sayi

girilenSayi = int(input("Sayiyi giriniz: "))

birlerBasamagi = int(girilenSayi % 10)
onlarBasamagi = int((girilenSayi - birlerBasamagi)/10%10)
yuzlerBasamagi = int(girilenSayi/100)

sayi1 = kupAl(birlerBasamagi)
sayi2 = kupAl(onlarBasamagi)
sayi3 = kupAl(yuzlerBasamagi)

if (sayi1 + sayi2 + sayi3 == girilenSayi):
    print("{} bir Armstrong sayıdir.".format(girilenSayi))
else:
    print("{} bir Armstrong sayı değildir.".format(girilenSayi))