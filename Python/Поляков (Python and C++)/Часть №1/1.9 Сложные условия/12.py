from random import randint
a = int(input())
if (a % 10) % 2 == ((a // 10) % 10) % 2 == 0 or (a % 10) % 2 == (a // 100) % 2 == 0 \
        or ((a // 10) % 10) % 2 == (a // 100) % 2 == 0:
    print(a, 'da')
else:
    print(a, 'net')