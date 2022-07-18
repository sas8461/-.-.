from graph import*
def pr(x, y):
    polygon([(x,y), (x+5, y), (x+5, y+10), (x, y+10), (x,y)])
for x in range(10, 25, 7):
    for y in range(10, 40, 12):
        brushColor("blue")
        pr(x, y)
for x in range(35, 50, 7):
    for y in range(10, 40, 12):
        brushColor("blue")
        pr(x, y)
for x in range(60, 75, 7):
    for y in range(10, 40, 12):
        brushColor("blue")
        pr(x, y)
for x in range(85, 100, 7):
    for y in range(10, 40, 12):
        brushColor("blue")
        pr(x, y)
run()