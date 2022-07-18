a, b, c = map(int, input().split())
r = False
if a > 100:
    r = True
elif b > 100:
    r = True
elif c > 100:
    r = True
print(r)