from random import randint
a = randint(1, 12)
b = randint(1, 12)
c = randint(1, 12)
d = randint(1, 12)
if (a % 2 > 0 and c % 2 > 0 and b % 2 > 0 and d % 2 > 0) or (a % 2 == 0 and c % 2 == 0 and b % 2 == 0 and d % 2 == 0):
    print(a, b, c, d, 'da')
elif (a % 2 > 0 and c % 2 > 0 and b % 2 == 0 and d % 2 == 0) or (a % 2 == 0 and c % 2 == 0 and b % 2 > 0 and d % 2 > 0):
    print(a, b, c, d, 'da')
else:
    print(a, b, c, d, 'net')