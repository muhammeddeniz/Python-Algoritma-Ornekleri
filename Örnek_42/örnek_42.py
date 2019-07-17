"""
Rastgele  küçükten büyüğe 5 sayi üreten program

"""
import  random

sayi1 = random.randint(1, 50)
sayi2 = random.randint(sayi1, 100)
sayi3 = random.randint(sayi2, 150)
sayi4 = random.randint(sayi3, 200)
sayi5 = random.randint(sayi4, 300)

print(sayi1, sayi2, sayi3, sayi4, sayi5)
