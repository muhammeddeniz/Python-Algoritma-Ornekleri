"""
Girilen kelimeyi tersten yazdıran program

"""

kelime = input("Kelime giriniz : ")

harfler = list(kelime)
tersHarfler = ""

for i in range(1, len(harfler) + 1):
    index = len(harfler) - i
    tersHarfler +=str(harfler[index])

print(tersHarfler)