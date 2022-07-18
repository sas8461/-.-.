a = int(input())
b = int(input())
c = int(input())
g = (a+b+c)/3
print(a, "+", b, "+", c, "=", a+b+c, ", ", a, "*", b, "*", c, "=", a*b*c, ", ", sep='', end='')
print("(", a, "+", b, "+", c, ")/3=", "{:8}".format(g), sep='')