from graph import*
N = 9
x1 = 100
y1 = 100
x2 = 300
y2 = 200
rectangle(x1, y1, x2, y2)
h = round((y2-y1)/N)
line(x1, y1+h, x2, y1+h)
for y in range(100 + h, 198, h):
    line(x1, y, x2, y)
run()