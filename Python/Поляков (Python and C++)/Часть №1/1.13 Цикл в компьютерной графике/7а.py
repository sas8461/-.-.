from graph import*
N = 8
x1 = 100
y1 = 100
x2 = 150
y2 = 200
rectangle(x1, y1, x2, y2)
h = (y2-y1)/N
y = y1 + h
while y < y2:
    line(x1, round(y), x2, round(y))
    y = y + h
run()