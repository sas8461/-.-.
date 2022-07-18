print("Определить четное число или нет")
a = int(input("Введите число"))
if (a % 2) > 0:
    if a == 0:
        print("Ноль")
    elif a != 0:
        print("Не четное")
else:
    print("Четное")