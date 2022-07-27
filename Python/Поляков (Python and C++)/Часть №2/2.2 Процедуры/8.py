def elka(n):
    b = 1
    for i in range(n, 0, -1):
        print(" " * i, "0" * b)
        b = b + 2
elka(4)