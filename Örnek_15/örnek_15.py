"""
Fibonacci serisinin ilk 10 terimini ekrana yazdıran program

"""

terim1 = 0
terim2 = 1


print(terim1)
print(terim2)

for i in range(0, 8):
    terim3 =terim2 + terim1
    terim1 = terim2
    terim2 = terim3
    print(terim3)