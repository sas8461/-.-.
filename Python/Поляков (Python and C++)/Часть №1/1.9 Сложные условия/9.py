from random import randint
a = randint(100, 999)
if a % 10 > (a // 10) % 10 and (a // 10) % 10 > a // 100:
    print(a, 'da')
else:
    print(a, 'net')