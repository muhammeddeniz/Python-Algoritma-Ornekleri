"""
Grilen 8 sayidan çift olanların teklere bölümünü veren program

"""

ciftToplam = 0
tekToplam = 0

for i in range(0, 8):
    girilenSayi = int(input("{}. sayiyi giriniz: ".format(i+1)))
    if (girilenSayi % 2 == 0):
        ciftToplam += girilenSayi
    elif (girilenSayi % 2 != 0):
        tekToplam += girilenSayi

print("tek toplam = ", tekToplam)
print("cift toplam = ", ciftToplam)

oran = ciftToplam / tekToplam
print("Sonuc: ", oran)