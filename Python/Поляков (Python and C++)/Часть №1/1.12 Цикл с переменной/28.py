n = int(input())
a = 0
for i in range(n):
    b = int(input())
    if b % 10 == 1 and b % 7 == 0 and b >= 10 and b <= 99:
        a = a + 1
print(a)