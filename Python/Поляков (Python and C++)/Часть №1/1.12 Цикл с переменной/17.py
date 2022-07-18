from random import randint
n = int(input())
g = randint(0, 1000)
for i in range(n):
    print(g)
    g = randint(0, 1000)