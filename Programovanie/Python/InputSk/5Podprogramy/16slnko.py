"""
Napíš funkciu slnko(n, x, y), ktorá nakreslí slnko 
ako n lúčov (hrubšie žlté, resp. zlaté úsečky, ktoré
vychádzajú zo stredu (x, y) a majú dĺžku 70) a veľký 
žltý/zlatý kruh so stredom (x, y) a polomerom 40. 
Otestuj, napríklad:

slnko(10, 100, 80)
slnko(20, 250, 120)
"""

import tkinter
import math

def slnko(n,x,y):
    canvas.create_oval(x-40, y-40, x+40, y+40, fill="gold", outline="")
    for i in range(0, n):
        canvas.create_line(x, y, x + 70*math.cos(math.radians(i*(360/n))), y + 70*math.sin(math.radians(i*(360/n))), fill="gold", width=10)

canvas = tkinter.Canvas()
canvas.pack()

slnko(10, 100, 80)
slnko(20, 250, 120)

tkinter.mainloop()