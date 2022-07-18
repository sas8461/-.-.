a = int(input())
b = a//1000 + (a//100)%10
c = (a//100)%10 + (a%100)//10
n = (a%100)//10 + a%10
m = b + c + n
print(b, c, n, m)