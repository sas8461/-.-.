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
    global x2lev, x1prav
    if x2lev != 200 and x1prav != 200:
        x2lev = x2lev + 5
        x1prav = x1prav - 5
        moveObjectBy(lev, 5, 0)
        moveObjectBy(prav, -5, 0)
    elif x2lev == 200 and x1prav == 200:
        x2lev = x2lev - 180
        x1prav = x1prav + 180
        moveObjectBy(lev, -180, 0)
        moveObjectBy(prav, 180, 0)

onTimer(update, 20)

run()

