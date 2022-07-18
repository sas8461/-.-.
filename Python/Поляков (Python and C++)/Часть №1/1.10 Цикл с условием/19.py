a = int(input())
b = 2
g = 0
while b != 1000:
    if a % b == 0:
        g = g + 1
    b = b + 1
if g > 1:
    print("Сложное")
else:
    print("Простое")