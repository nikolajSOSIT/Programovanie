"""
Napíš program, ktorý v grafickej ploche najprv 
vygeneruje n náhodných bodiek (malé kruhy). 
Potom nakreslí čo najmenší obdĺžnik tak, 
aby sa v ňom nachádzali všetky nakreslené body. 
Napríklad, pre n=7 môžeš dostať takýto obrázok:
"""

import tkinter
import random

n = 7
x1, y1, x2, y2 = 0, 0, 0, 0

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

for i in range(n):
    
    _x = random.randint(1, 300)
    _y = random.randint(1, 300)
    canvas.create_oval(_x-2, _y-2, _x+2, _y+2, fill="red", outline="")

    if i == 0:
        x1, y1, x2, y2 = _x, _y, _x, _y

    if x1 > _x:
        x1 = _x
    if y1 > _y:
        y1 = _y
    if x2 < _x:
        x2 = _x
    if y2 < _y:
        y2 = _y

canvas.create_rectangle(x1, y1, x2, y2, outline="blue", width=2)

tkinter.mainloop()