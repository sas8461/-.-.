a = int(input())
b = -1
g = a + 0
while g > 0:
    g = g // 10
    b = b + 1
while b > -1:
    print(a // 10**b)
    a = a % 10**b
    b = b - 1