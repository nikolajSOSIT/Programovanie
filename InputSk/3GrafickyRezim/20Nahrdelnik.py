"""
Program pre dané n nakreslí n dotýkajúcich sa kruhov,
ktorých stredy ležia na obvode kružnice. 
Tieto kruhy zafarbi náhodnými farbami.
"""

import tkinter
import math
import random

n = int(input('Zadaj n: '))
r = 100
o = 2*math.pi*r
_r = o/n/2
x, y = 150, 150 
canvas = tkinter.Canvas()
canvas.pack()

for i in range(n):
    x1 = x + r * math.sin(math.radians(i * 360 / n))
    y1 = y + r * math.cos(math.radians(i * 360 / n))
    canvas.create_oval(x1-_r, y1-_r, x1+_r, y1+_r, fill=f'#{random.randrange(256**3):06x}')

tkinter.mainloop()