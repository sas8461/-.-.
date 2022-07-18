from graph import*
N = 8
x1 = 100
x2 = 200
polygon([(150, 100), (x1, 200), (x2, 200), (150, 100)])
h = (x2-x1)/N
x = x1 + h
while x < x2:
    line(150, 100, round(x), 200)
    x = x + h
run()