from graph import*
def romb(x, y):
    polygon([(x, y), (x+10, y-20), (x+20, y), (x+10, y+20), (x, y)])
for x in range(20, 71, 10):
    romb(x, 30)
run()