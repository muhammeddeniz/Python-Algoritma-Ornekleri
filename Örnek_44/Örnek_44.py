"""
00001
00011
00111
01111

şeklini oluşturan kod
"""

degisken0 = 4;
degisken1 = 1;
yazdir = "";

for i in range(0,4):
    yazdir ="";

    for j in range (0,degisken0):
        yazdir+="0";
    degisken0-=1;

    for f in range(0, degisken1):
        yazdir += "1";
    degisken1+=1;
    print(yazdir);