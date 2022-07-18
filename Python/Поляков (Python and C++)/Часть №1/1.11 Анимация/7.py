from graph import *

brushColor("blue")
rectangle(0, 0, 400, 400)

x2lev = 20
brushColor("red")
lev = rectangle(0, 190, x2lev, 210)

x1prav = 380
brushColor("red")
prav = rectangle(x1prav, 190, 400, 210)

def update():
    global x2lev
    x2lev = x2lev + 5
    moveObjectBy(lev, 5, 0)
    if x2lev == 200:
        while x2lev != 20:
            if x2lev <= 200:
                x2lev = x2lev - 5
            moveObjectBy(lev, -5, 0)

onTimer(update, 20)

run()
