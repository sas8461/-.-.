from graph import *

def update():
    global xCenter #Будем изменять xCenter
    if xCenter < 390:
        xCenter = xCenter + 5  # новая х-координата центра
        moveObjectBy(obj, 5, 0)

    elif xCenter == 390:
        xCenter = xCenter - 380  # новая х-координата центра
        moveObjectBy(obj, - 380, 0)

    def keyPressed(event): #закрытие если нажмем на клавишу
        if event.keycode == VK_ESCAPE:
            close()

    onKey(keyPressed)

brushColor("blue")
rectangle(0, 0, 400, 400)

R = 10
xCenter = 10
yCenter = 200
penColor("yellow")
brushColor("yellow")
obj = circle(xCenter, yCenter, R)

onTimer(update, 20)

run()