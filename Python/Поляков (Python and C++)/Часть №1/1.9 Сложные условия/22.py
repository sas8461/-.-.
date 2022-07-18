from random import randint
a = randint(1, 4)
b = randint(1, 4)
c = randint(1, 4)
d = randint(1, 4)
if a == c and b == d:
    print(a, b, c, d, "Не верные координаты")
elif (c == a + 1 and d == b + 2) or (c == a + 1 and d == b - 2):
    print(a, b, c, d, 'Бьет', 1)
elif (c == a - 1 and d == b + 2) or (c == a - 1 and d == b - 2):
    print(a, b, c, d, 'Бьет', 2)
elif (c == a + 2 and d == b + 1) or (c == a + 2 and d == b - 1):
    print(a, b, c, d, 'Бьет', 3)
elif (c == a - 2 and d == b + 1) or (c == a - 2 and d == b - 1):
    print(a, b, c, d, 'Бьет', 4)
else:
    print(a, b, c, d, "Не бьет")