"""
Napíš program, ktorý pomocou canvas.create_polygon nakreslí rovnostranný trojuholník. V premenných:

x, y = 50, 250
a = 280
má nastavené súradnice ľavého dolného vrcholu a veľkosť strany trojuholníka. Pre takto zadané premenné by si mal dostať takýto výstup:


Zrejme využiješ príkaz create_polygon(), do ktorého zadáš 3 vrcholy trojuholníka. Spomeň si, ako vypočítaš výšku rovnostranného trojuholníka.



"""

import tkinter
from math import sqrt
x, y = 50, 250
a = 280
va=round(sqrt(a*a-(a/2)**2))

canvas = tkinter.Canvas()
canvas.pack()

canvas.create_polygon(x, y, x+a, y, x+a/2, y-va, fill="blue")

tkinter.mainloop()