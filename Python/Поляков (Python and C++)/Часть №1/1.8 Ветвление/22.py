a, b, c = map(int, input().split())
r = False
if a % 2 == 0:
    r = True
if b % 2 == 0:
    r = True
if c % 2 == 0:
    r = True
print(r)