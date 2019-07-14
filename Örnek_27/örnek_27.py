"""
1 ile 100 arasında kaç tane asal sayi olduğunu gösteren program

"""
toplam = 0

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            break
        elif(j == 9):
            toplam += i
print(toplam)