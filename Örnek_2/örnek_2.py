"""
kullanıcının girdiği sayının karesini alan program

"""

# kullanıcıdan alınan her input string olarak değerlendirilir
# eğer input ile işlem yapılacaksa tür dönüşümü yapılmalı


sayi = input("Bir sayi giriniz: ")
sayi = int(sayi)
sayi *= sayi

print("Girdiğiniz sayinin karesi = ", sayi)