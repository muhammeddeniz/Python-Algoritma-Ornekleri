"""
10 elemanlı bir sayı dizisinde en küçük  elemanın bu dizinin kaçıncı elemanı
olduğunu bulan program

"""
kucukSayi = 99999999999999
sayiSirasi = 0

for i in range(1, 11):
    sayiGir = int(input("{}. Sayiyi giriniz: ".format(i)))

    if sayiGir < kucukSayi:
        kucukSayi = sayiGir
        sayiSirasi = i

print("{}. siradaki sayi en küçük sayidir.".format(sayiSirasi))