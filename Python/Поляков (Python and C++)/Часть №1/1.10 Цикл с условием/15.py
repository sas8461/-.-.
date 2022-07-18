a = int(input())
b = 0
while a > 0 and b == 0:
    if a % 10 == (a % 100) // 10:
        b = b + 1
    else:
        a = a // 10
if b > 0:
    print('Есть')
else:
    print("Нету")