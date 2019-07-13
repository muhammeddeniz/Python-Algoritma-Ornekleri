"""
Kullanıcıdan iki sayi alan ve bu iki sayi da 20 den büyükse toplama işlemi yapan, küçük
veya eşitse çarpma işlemi yapan program

"""

sayi1 = int(input("Birinci sayi: "))
sayi2 = int(input("İkinci sayi: "))

sonuc = 0

if(sayi1 > 20) & (sayi2 > 20):
    sonuc =\
        sayi2 + sayi1
else:
    sonuc = sayi1 * sayi2

print("Sonuc = ", sonuc)