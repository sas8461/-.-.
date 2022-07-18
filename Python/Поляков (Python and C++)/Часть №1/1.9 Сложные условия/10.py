from random import randint
a = randint(100, 999)
if (a % 10) % 2 == 0 and ((a // 10) % 10) % 2 == 0 and (a // 100) % 2 == 0:
    print(a, 'da')
else:
    print(a, 'net')