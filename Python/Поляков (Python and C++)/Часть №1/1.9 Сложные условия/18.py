a = int(input())
b = int(input())
if a == 1 and b <= 31:
    print(365 - b)
elif a == 2 and b <= 28:
    print(365 - 31 - b)
elif a == 3 and b <= 31:
    print(365 - 31 - 28 - b)
elif a == 4 and b <= 30:
    print(365 - 31 - 28 - 31 - b)
elif a == 5 and b <= 31:
    print(365 - 31 - 28 - 31 - 30 - b)
elif a == 6 and b <= 30:
    print(365 - 31 - 28 - 31 - 30 - 31 - b)
elif a == 7 and b <= 31:
    print(365 - 31 - 28 - 31 - 30 - 31 - 30 - b)
elif a == 8 and b <= 31:
    print(365 - 31 - 28 - 31 - 30 - 31 - 30 - 31 - b)
elif a == 9 and b <= 30:
    print(365 - 31 - 28 - 31 - 30 - 31 - 30 - 31 - 31 - b)
elif a == 10 and b <= 31:
    print(365 - 31 - 28 - 31 - 30 - 31 - 30 - 31 - 31 - 30 - b)
elif a == 11 and b <= 30:
    print(365 - 31 - 28 - 31 - 30 - 31 - 30 - 31 - 31 - 30 - 31 - b)
elif a == 12 and b <= 31:
    print(365 - 31 - 28 - 31 - 30 - 31 - 30 - 31 - 31 - 30 - 31 - 30 - b)
else:
    print("Неверный месяц")