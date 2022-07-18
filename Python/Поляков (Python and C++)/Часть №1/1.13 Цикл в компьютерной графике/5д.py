from graph import*

def romb(x, y):
    polygon([(x, y), (x+5, y-5), (x+10, y), (x+5, y+5), (x, y)])
for x in range(10, 55, 22):
    brushColor("blue")
    romb(x, 10)
for x in range(10, 55, 22):
    brushColor("blue")
    romb(x, 22)
for x in range(3, 65, 22):
    brushColor("blue")
    romb(x, 16)
for x in range(16, 65, 22):
    brushColor("blue")
    romb(x, 16)
run()