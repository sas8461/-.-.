from graph import*

rectangle(10, 10, 90, 30)

def trio1(x, y):
    polygon([(x, y), (x+10, y+10), (x, y+10), (x+10, y), (x, y)])
for x in range(10, 81, 20):
    brushColor("blue")
    trio1(x, 10)
for x in range(20, 81, 20):
    brushColor("blue")
    trio1(x, 20)

def trio2(x, y):
    polygon([(x, y), (x+10, y+10), (x+10, y), (x, y+10), (x, y)])
for x in range(20, 81, 20):
    brushColor("blue")
    trio2(x, 10)
for x in range(10, 81, 20):
    brushColor("blue")
    trio2(x, 20)
run()