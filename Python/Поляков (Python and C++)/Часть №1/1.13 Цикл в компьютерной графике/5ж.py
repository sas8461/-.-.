from graph import*
x = 10
def kr(x, y):
    circle(x, y, 5)
    circle(x + 13, y, 5)
    circle(x + 26, y, 5)
    circle(x + 39, y, 5)
for y in range(10, 50, 7):
    brushColor('blue')
    kr(x, y)
    x = x + 7
run()