from graph import*
N = 8
x1 = 100
x2 = 125
x3 = 175
x4 = 200
polygon([(x1, 100), (x2, 200), (x3, 200), (x4, 100), (x1, 100)])
h1 = (x4-x1)/N
h2 = (x3-x2)/N
xv = x1 + h1
xn = x2 + h2
while xn < x3:
    line(round(xv), 100, round(xn), 200)
    xv = xv + h1
    xn = xn + h2
run()