a = int(input())
b = int(input())
r = a
t = b
g = 0
h = 0
while a != b:
    if a > b:
        a = a - b
        g = g + 1
    elif a < b:
        b = b - a
        g = g + 1
while r != 0 and t != 0:
    if r > t:
        r = r % t
        h = h + 1
    elif r < t:
        t = t % r
        h = h + 1
if g > h:
    print("Простое больше")
elif g < h:
    print("Модифицированное больше")
else:
    print('Равно')