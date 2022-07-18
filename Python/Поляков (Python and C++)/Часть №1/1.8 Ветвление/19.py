a = int(input("Введите 3-х значное число"))
b = (a // 100) + ((a // 10) % 10)
g = ((a // 10) % 10) + (a % 10)
if b > g:
    print(b, g, sep='')
else:
    print(g, b, sep='')