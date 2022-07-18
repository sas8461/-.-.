n = int(input())

a = 0
for i in range(1, n + 1):
    a = a + i
print(a)

b = 1
g = 0
while b != n + 1:
    g = g + b
    b = b + 1
print(g)