"""
Napíš program, ktorý nakreslí n náhodných farebných domčekov. Každý domček sa skladá z rovnostranného trojuholníka (použi riešenie z predchádzajúcej úlohy) a štvorca. 
Polohu domčeka, veľkosť strany jeho štvorca a trojuholníka zvoľ náhodne (veľkosť bude náhodné číslo z <10, 50>). 
Tiež ich farby zvoľ náhodne. 
Pre 20 domčekov by si mohol dostať takýto výstup:
"""


from math import sqrt
import tkinter
import random

n = 20 
canvas = tkinter.Canvas()
canvas.pack()
for i in range(n):
    x,y = random.randrange(10, 380), random.randrange(10, 380)
    a = random.randrange(10, 50)
    va=round(sqrt(a*a-(a/2)**2))
    canvas.create_polygon(x, y, x+a, y, x+a/2, y-va, fill=f"#{random.randrange(256**3):06x}")
    canvas.create_rectangle(x, y, x+a, y+a, fill=f"#{random.randrange(256**3):06x}")
tkinter.mainloop()