from graph import*
N = 8
x1 = 50
y1 = 50
x2 = 50
y2 = 100
x3 = 100
y3 = 70
x4 = 100
y4 = 120
x5 = 150
y5 = 50
x6 = 150
y6 = 100
x7 = 100
y7 = 30
polygon([(x1, y1), (x2, y2), (x4, y4), (x3, y3), (x1, y1)])
polygon([(x3, y3), (x4, y4), (x6, y6), (x5, y5), (x3, y3)])
polygon([(x1, y1), (x3, y3), (x5, y5), (x7, y7), (x1, y1)])
h1 = (y2-y1)/N
h2 = ((y7-y3)/2)/N
ytr11 = y1 + h1
ytr12 = y3 + h1
xtr21 = x3 + h1
ytr21 = y3 + h2
ytr22 = y4 + h2
xtr31 = x1 + h1
xtr32 = x7 + h1
ytr31 = y1 + (-h2)
ytr32 = y7 + (-h2)
while ytr11 < y2:
    line(x1, round(ytr11), x3, round(ytr12))
    line(round(xtr21), round(ytr21), round(xtr21), round(ytr22))
    line(round(xtr31), round(ytr31), round(xtr32), round(ytr32))
    ytr11 = ytr11 + h1
    ytr12 = ytr12 + h1
    xtr21 = xtr21 + h1
    ytr21 = ytr21 + h2
    ytr22 = ytr22 + h2
    xtr31 = xtr31 + h1
    xtr32 = xtr32 + h1
    ytr31 = ytr31 + (-h2)
    ytr32 = ytr32 + (-h2)
run()