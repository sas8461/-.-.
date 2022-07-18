from random import randint
a = int(input())
perv = a // 100
vtor = (a // 10) % 10
tret = a % 10
if not(perv == vtor or perv == tret or vtor == tret):
    print('da')
else:
    print('net')