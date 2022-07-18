from graph import*
N = 8
x1 = 50
y1 = 50
x2 = 50
y2 = 100
x3 = 100
y3 = 75
polygon([(x1, y1), (x2, y2), (x3, y3), (x1, y1)])
hx = (x3 - x1)/N
hy = ((y2 - y1)/2)/N
x = x1 + hx
y11 = y1 + hy
y12 = y2 - hy
while x < x3:
    line(x, y11, x, y12)
    x = x + hx
    y11 = y11 + hy
    y12 = y12 - hy
run()