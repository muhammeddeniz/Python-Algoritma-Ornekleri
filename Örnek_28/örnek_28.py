"""
1 ile 10 arasındakitsayilarin karelerinin toplamini bulan program

"""
toplam = 0

def kareAl(sayi):
    sayi *=sayi
    return sayi

for i in range(1,10):
    toplam += kareAl(i)

print(toplam)