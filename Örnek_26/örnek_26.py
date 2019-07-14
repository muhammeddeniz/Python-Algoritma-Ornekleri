"""
10 ile 50 arasındaki asal sayilari ekrana yazdıran program

"""


for i in range(11, 50):
    for j in range(2, 10):
        if i % j == 0:
            break
        elif(j==9):
            print(i)