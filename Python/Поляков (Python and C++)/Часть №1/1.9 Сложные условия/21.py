from random import randint
a = randint(1, 12)
b = randint(1, 12)
c = randint(1, 12)
d = randint(1, 12)
if a == c and b == d:
    print(a, b, c, d, "Не верные координаты")
elif a == c or b == d:
    print(a, b, c, d, 'Бьет', 1)
elif ((c == a + 1) and (d == b + 1)) or ((c == a + 1) and (d == b - 1)) or ((c == a - 1) and (d == b + 1)) or ((c == a - 1) and (d == b - 1)):
    print(a, b, c, d, 'Бьет', 2)
elif (c == a + 2) and (d == b + 2) or (c == a + 2) and (d == b - 2) or (c == a - 2) and (d == b + 2) or (c == a - 2) and (d == b - 2):
    print(a, b, c, d, 'Бьет', 3)
elif (c == a + 3) and (d == b + 3) or (c == a + 3) and (d == b - 3) or (c == a - 3) and (d == b + 3) or (c == a - 3) and (d == b - 3):
    print(a, b, c, d, 'Бьет', 4)
elif (c == a + 4) and (d == b + 4) or (c == a + 4) and (d == b - 4) or (c == a - 4) and (d == b + 4) or (c == a - 4) and (d == b - 4):
    print(a, b, c, d, 'Бьет', 5)
elif (c == a + 5) and (d == b + 5) or (c == a + 5) and (d == b - 5) or (c == a - 5) and (d == b + 5) or (c == a - 5) and (d == b - 5):
    print(a, b, c, d, 'Бьет', 6)
elif (c == a + 6) and (d == b + 6) or (c == a + 6) and (d == b - 6) or (c == a - 6) and (d == b + 6) or (c == a - 6) and (d == b - 6):
    print(a, b, c, d, 'Бьет', 7)
elif (c == a + 7) and (d == b + 7) or (c == a + 7) and (d == b - 7) or (c == a - 7) and (d == b + 7) or (c == a - 7) and (d == b - 7):
    print(a, b, c, d, 'Бьет', 8)
elif (c == a + 8) and (d == b + 8) or (c == a + 8) and (d == b - 8) or (c == a - 8) and (d == b + 8) or (c == a - 8) and (d == b - 8):
    print(a, b, c, d, 'Бьет', 9)
elif (c == a + 9) and (d == b + 9) or (c == a + 9) and (d == b - 9) or (c == a - 9) and (d == b + 9) or (c == a - 9) and (d == b - 9):
    print(a, b, c, d, 'Бьет', 10)
elif (c == a + 10) and (d == b + 10) or (c == a + 10) and (d == b - 10) or (c == a - 10) and (d == b + 10) or (c == a - 10) and (d == b - 10):
    print(a, b, c, d, 'Бьет', 11)
elif (c == a + 11) and (d == b + 11) or (c == a + 11) and (d == b - 11) or (c == a - 11) and (d == b + 11) or (c == a - 11) and (d == b - 11):
    print(a, b, c, d, 'Бьет', 12)
else:
    print(a, b, c, d, "Не бьет")