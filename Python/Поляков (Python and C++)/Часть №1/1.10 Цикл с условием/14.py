a = int(input())
b = a % 10
while a > 0:
    if b < (a % 100) // 10:
        b = (a % 100) // 10
        a = a // 10
    else:
        a = a // 10
print(b)