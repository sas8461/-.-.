a = int(input())
b = int(input())
if b < 0:
    print("Ошибка 1")
elif a < 0:
    h = 0
    for i in range(b+1):
        print(h*h)
        h = h + 1
elif a >= 0:
    g = a
    for i in range(b-a+1):
        print(g*g)
        g = g + 1