"""
V ďalšej verzii bodkovacej úlohy vybodkuješ kruh. 
Program opäť nakreslí 4000 náhodných bodiek, ale tie z nich,
ktoré majú vzdialenosť od (x0, y0) menšiu ako r, zafarbí na červeno,
zvyšné na modro. Napríklad pre premenné:

x0, y0 = 180, 130
r = 110
by si mal dostať takýto obrázok:

Vzdialenosť dvoch bodov v rovine môžeš počítať podľa vzorca
sqrt((x1-x2)**2 + (y1-y2)**2).
"""

import math
import random
import tkinter

x0, y0 = 150, 150
r = 50

canvas = tkinter.Canvas(height="300", width="300")
canvas.pack()


for i in range(4000):
    x = random.randint(1, 300)
    y = random.randint(1, 300)
    if math.sqrt((x0 - x)**2 + (y0 - y)**2) < r:
        farba ='red'
    else: farba = 'blue'
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=farba, outline="")

tkinter.mainloop()
