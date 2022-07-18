from random import randint
n = int(input())
k = randint(1000, 9999)
for i in range(n):
    r1 = (k // 1000) + ((k // 100) % 10)
    r2 = ((k // 100) % 10) + ((k % 100) // 10)
    r3 = ((k % 100) // 10) + (k % 10)
    if (r1 > r2 and r1 > r3) or (r1 == r2 and r1 > r3) or (r1 == r3 and r1 > r2):
        if r2 > r3:
            print(r2, r3, sep='')
        elif r2 < r3:
            print(r3, r2, sep='')
        elif r2 == r3:
            print(r3, r2, sep='')
    elif (r2 > r1 and r2 > r3) or (r2 == r3 and r2 > r1):
        if r1 > r3:
            print(r1, r3, sep='')
        elif r1 < r3:
            print(r3, r1, sep='')
        elif r1 == r3:
            print(r3, r1, sep='')
    elif (r3 > r1 and r3 > r2):
        if r2 > r1:
            print(r2, r1, sep='')
        elif r2 < r1:
            print(r1, r2, sep='')
        elif r2 == r1:
            print(r1, r2, sep='')
    elif r3 == r1 and r3 == r2:
        print(r2, r3, sep='')
    k = randint(1000, 9999)