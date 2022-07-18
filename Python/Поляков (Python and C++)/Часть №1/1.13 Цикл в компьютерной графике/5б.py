from graph import*
def romb(x, y):
    polygon([(x, y), (x+5, y-5), (x+10, y), (x+5, y+5), (x, y)])
for x in range(10, 91, 10):
    brushColor("blue")
    romb(x, 20)
for x in range(20, 91, 30):
    brushColor("blue")
    romb(x, 10)
for x in range(20, 91, 30):
    brushColor("blue")
    romb(x, 30)
run()