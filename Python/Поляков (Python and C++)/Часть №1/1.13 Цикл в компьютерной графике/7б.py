from graph import*
N = 8
x1 = 100
y1 = 300
x2 = 200
y2 = 300
polygon([(100, 10), (x1, y1), (x2, y2), (100,10)])
h = (x2-x1)/N
x = x1 + h
while x < x2:
    line(100, 10, round(x), y1)
    x = x + h
run()