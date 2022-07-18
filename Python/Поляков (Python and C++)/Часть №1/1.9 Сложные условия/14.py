a, b, c = map(int, input().split())
g = False
if a >= 100 and a <= 999 or b >= 100 and b <= 999 or c >= 100 and c <= 999:
    g = True
print(g)