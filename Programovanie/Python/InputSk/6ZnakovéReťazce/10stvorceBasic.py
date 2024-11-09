"""
Napíš funkciu stvorce(vel, retazec), ktorá dostáva dva parametre: 
veľkosť štvorca a znakový reťazec s menami farieb. 
Funkcia nakreslí rad farebných štvorcov veľkosti vel, 
ktoré budú zafarbené farbami z reťazca. 
Zrejme štvorcov bude toľko, koľko farieb je v reťazci.
"""

import tkinter

canvas = tkinter.Canvas()
canvas.pack()

def stvorce(vel, retazec):
    x = 0
    y = 0
    farby = retazec.split()
    for i in farby:
        canvas.create_rectangle(x, y, x + vel, y + vel, fill = i)
        x += vel + 5


stvorce(40, 'red blue purple red gold green yellow cyan indigo magenta')

tkinter.mainloop()