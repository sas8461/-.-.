print("Введите число")
b = int(input())
if b//100 == 0 or b%10 == 0 or (b//10)%10 == 0:
    print("Есть цифра 0")
else:
    print("Нету цифры 0")