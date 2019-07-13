"""
İki kenari girilen dikdörtgenin alanını ve çevresini bulan program

"""

kisaKenar = int(input("Kısa kenar : "))
uzunKenar = int(input("Uzun kenar : "))

print("Alan = ", kisaKenar * uzunKenar)
print("Çevre = ", 2 * (uzunKenar + kisaKenar))