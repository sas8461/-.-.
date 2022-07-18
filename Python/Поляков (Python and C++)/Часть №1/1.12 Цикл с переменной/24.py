n = int(input())
a = 0
b = 0
c = 0
k = 0
for i in range(1, (n + 1) * (n + 1) * (n + 1)):
    if a == n and b == n:
        if n == c ** 2 + a ** 2 + b ** 2:
            k = k + 1
            print(n, '==', c ** 2, "+", a ** 2, "+", b ** 2, "(", k, ")")
        c = c + 1
        a = 0
        b = 0
    elif b == n and a != n:
        if n == c ** 2 + a ** 2 + b ** 2:
            k = k + 1
            print(n, '==', c ** 2, "+", a ** 2, "+", b ** 2, "(", k, ")")
        a = a + 1
        b = 0
    else:
        if n == c ** 2 + a ** 2 + b ** 2:
            k = k + 1
            print(n, '==', c ** 2, "+", a ** 2, "+", b ** 2, "(", k, ")")
        b = b + 1