x = int(input())
max = x
min = x
while x != 0:
    if x != 0:
        x = int(input())
        if x > max:
            max = x
        elif x < min:
            if x != 0:
                min = x
print(min, max)