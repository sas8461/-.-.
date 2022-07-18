a = int(input())
b = int(input())
g = 0
while a != b:
    if a > b:
        a = a - b
        g = g + 1
    elif a < b:
        b = b - a
        g = g + 1
print(a, g)