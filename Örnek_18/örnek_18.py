"""
1 ile 1000 arasındaki çift sayiların toplamını veren program

"""

ciftToplam = 0

for i in range(2, 1000):
    if (i % 2 == 0):
        ciftToplam += i

print("1 ile 1000 arasındaki çift sayiların toplamı = ", ciftToplam)