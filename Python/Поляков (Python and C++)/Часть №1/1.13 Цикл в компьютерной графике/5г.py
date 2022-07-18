from graph import*

rectangle(0, 10, 60, 40)

def trio(x, y):
    polygon([(x, y), (x, y+10), (x-10, y+10), (x,y)])
for x in range(10, 61, 10):
    for y in range(10, 31, 10):
        brushColor("blue")
        trio(x,y)
run()