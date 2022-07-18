from math import*
from graph import*
N = 8
y1 = 100
y2 = 200
x1 = 100
x2 = 150
polygon([(x1, y1), (x1, y2), (x2, y2), (x1, y1)])
h1 = (y2-y1)/N
h2 = (x2-x1)/N
y = y1 + h1
x = x1 + h2
while y2 > y:
    line(x1, round(y), round(x), round(y))
    y = y + h1
    x = x + h2
run()