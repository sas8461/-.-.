from random import randint, uniform
n = int(input())
a = 0
b = 0
j = 0
s = 0
g = uniform(0, 1)
for i in range(n):
    if g >= 0 and g < 0.25:
        a = a + 1
    elif g >= 0.25 and g < 0.5:
        b = b + 1
    elif g >= 0.5 and g < 0.75:
        j = j + 1
    elif g >= 0.75 and g < 1:
        s = s + 1
    g = uniform(0, 1)
print(a + b + j + s)
print(a, b, j, s)