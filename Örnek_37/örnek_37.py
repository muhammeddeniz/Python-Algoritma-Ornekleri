"""
Dışardan girilen vize ve final notuna göre öğrencinin harf notunu hesaplayıp ekrena yazdıran program

"""

vize = int(input("Vize Notu : "))
final = int(input("Final : "))

puan = (vize * 40/100) + (final * 60/100)
print("YIL SONU NOTU : ", puan)

if (puan > 0) & (puan < 60):
    print("HARF NOTU: F")
elif (puan > 59) & (puan < 70):
    print("HARF NOTU: D")
elif (puan > 69) & (puan < 80):
    print("HARF NOTU: C")
elif (puan > 79) & (puan < 90):
    print("HARF NOTU: B")
elif (puan > 89) & (puan <= 100):
    print("HARF NOTU: A")