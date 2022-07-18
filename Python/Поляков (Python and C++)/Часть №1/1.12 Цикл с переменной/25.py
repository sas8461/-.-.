n = int(input())
a = 0
for i in range(n):
    b = int(input())
    if b % 6 == 0:
        a = a + 1
print(a)