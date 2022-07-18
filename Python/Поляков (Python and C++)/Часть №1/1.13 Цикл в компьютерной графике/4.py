from graph import*
def Kva(x, y):
    rectangle(x, y, x + 10, y + 10)
for x in range (10, 81, 10):
    for y in range(10, 81, 10):
        Kva(x, y)
run()