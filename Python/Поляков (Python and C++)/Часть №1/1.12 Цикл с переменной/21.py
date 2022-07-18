a = int(input())
b = 1
sum = 0
for i in range(1, a):
    if a % b == 0:
        sum = sum + b
    b = b + 1
print(sum)