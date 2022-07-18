from graph import*
N = 8
x1 = 200
y1 = 100
x2 = 200
y2 = 300
polygon([(100, 300), (x1, y1), (x2, y2), (100, 300)])
h = (y2-y1)/N
y = y1 + h
while y < y2:
    line(100, 300, x1, round(y))
    y = y + h
run()