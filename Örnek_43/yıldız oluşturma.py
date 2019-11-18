"""
***
**
*
gibi şekilleri oluşturan kod
"""

girilenSayi = int(input("kaç yıldızdan başlamasını istiyorsunuz : "));
temp = girilenSayi;
yazdir = "";

for i in range(0,girilenSayi):
    yazdir ="";
    for j in range(0,temp):
        yazdir += "*";
    print(yazdir);
    temp -= 1;