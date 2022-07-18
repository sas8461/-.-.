x = int(input())
s = 0
while x != 0:
    if x % 10 == 5:
        s = s + 1
    x = int(input())
print(s)