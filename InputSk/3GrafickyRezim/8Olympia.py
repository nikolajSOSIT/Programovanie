"""
Napíš program, ktorý nakreslí olympijské kruhy. V premenných:

x, y = 70, 100
r = 50
dx, dy = 120, 60

má zadané: súradnice stredu horného najľavejšieho kruhu (x, y),
polomer kruhov (r) a vzdialenosť medzi kruhmi v jednom rade (dx)
a vzdialenosť medzi radmi (dy). Hrúbka čiar kružníc nech je 15. 
Pre takto zadané hodnoty by si mal dostať takýto výstup:
"""

import tkinter

x, y = 70, 100
r = 50
dx, dy = 120, 60
farba1, farba2, farba3, farba4, farba5 = "blue", "yellow", "black", "lime", "red"

canvas = tkinter.Canvas(width=1920,height=1080)
canvas.pack()

for i in range(5):
    canvas.create_oval(x-r, y-r, x+r, y+r, outline=farba1, width=15)
    x += dx / 2
    y += dy * (-1)**i
    farba1, farba2, farba3, farba4, farba5 = farba2, farba3, farba4, farba5, farba1

tkinter.mainloop()