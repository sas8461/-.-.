a = input()
b = 0
while b == 0:
    if a != "Sas223":
        a = input("Повторите пароль")
    elif a == "Sas223":
        b = b + 1
        g = input("Введите Имя")
        h = input("Введите Фамилию")
print(g, h)