from graph import*
N = 8
y1 = 100
y2 = 200
polygon([(100, y1), (100, y2), (150, 150), (100, y1)])
polygon([(200, y1), (200, y2), (150, 150), (200, y1)])
h = (y2-y1)/N
y = y1 + h
while y < y2:
    line(150, 150, 100, round(y))
    line(150, 150, 200, round(y))
    y = y + h
run()