a = int(input("Введите 4-х значное число"))
b = (a // 1000) + ((a % 1000) // 100)
g = ((a % 1000) // 100) + ((a % 100) // 10)
h = ((a % 100) // 10) + (a % 10)
if min(b, g, h) == b:
    if g > h:
        print(h, g, sep='')
    else:
        print(g, h, sep='')
elif min(b, g, h) == g:
    if b > h:
        print(h, b, sep='')
    else:
        print(b, h, sep='')
elif min(b, g, h) == g:
    if b > g:
        print(g, b, sep='')
    else:
        print(b, g, sep='')