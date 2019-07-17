"""
Girilen bir kelimenin uzunluğunu bulan program

"""

kelime = input("Kelime giriniz: ")
uzunluk = 0

for i in kelime:
    uzunluk += 1

print("Girdiğiniz kelimenin {} tane harfi var.".format(uzunluk))