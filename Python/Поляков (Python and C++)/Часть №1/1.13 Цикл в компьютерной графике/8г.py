from graph import*
N = 5
x1, y1, x2, y2 = 50, 50, 100, 100
rectangle(x1, y1, x2, y2)
line(50, 50, 100, 100)
h = (x2 - x1)/N
x11 = x1 + h
y12 = y2 - h
x21 = x1 + h
y21 = y2 - h
while x2 > x11:
    line(x11, y2, x1, y12)
    line(x2, y21, x21, y1)
    x11 = x11 + h
    y12 = y12 - h
    x21 = x21 + h
    y21 = y21 - h
run()