"""
Beden kitle endeksini hesaplayan program

"""

boy = float(input("Boy ( metre olarak )  : "))
kilo = int(input("Ağırlık ( kilo olarak ): "))

bedenIndexi = kilo / (boy * boy)

print("Beden İnkdeksi = ", bedenIndexi)