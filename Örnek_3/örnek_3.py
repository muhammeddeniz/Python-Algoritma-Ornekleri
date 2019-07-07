"""
birden ona kadar sayilarin küplerini toplayan program

"""

carpim = 0

for i in range(1, 11):
    print(i)
    carpim += i*i*i

print(carpim)