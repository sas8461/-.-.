from graph import *
#Крыша
penSize(1)
brushColor("blue")
polygon([(100, 200), (50, 230), (150, 230), (100, 200)])
#Основание
penSize(1)
brushColor("green")
rectangle(70, 230, 130, 290)
#Окно
penSize(1)
brushColor("white")
rectangle(75, 235, 100, 265)
#Верхнее окно
penSize(1)
brushColor("black")
rectangle(78, 238, 97, 243)
#Левое окно
penSize(1)
brushColor("black")
rectangle(78, 246, 86, 262)
#Правое окно
penSize(1)
brushColor("black")
rectangle(89, 246, 97, 262)
run()