a = int(input())
b = 0
while a > 9 and b == 0:
    if a % 10 != (a % 100) // 10:
        b = b + 1
    a = a // 10
if b > 0:
    print("Не верно")
else:
    print("Верно")