a = int(input())
b = 1
for i in range(a):
    if (b * b) % 10 == b or (b * b) % 100 == b or (b * b) % 1000 == b:
        print(b)
    b = b + 1