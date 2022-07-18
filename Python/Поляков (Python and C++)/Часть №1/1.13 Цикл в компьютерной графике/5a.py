from graph import*
def romb(x, y):
    polygon([(x, y), (x+5, y-5), (x+10, y), (x+5, y+5), (x, y)])
for x in range(10, 51, 10):
    for y in range(10, 21, 10):
        brushColor("blue")
        romb(x, y)
run()