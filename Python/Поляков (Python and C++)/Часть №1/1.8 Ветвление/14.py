a, b, c = map(int, input().split())
if a > b:
    if a > c:
        print(a)
if a < b:
    if b > c:
        print(b)
else:
    print(c)