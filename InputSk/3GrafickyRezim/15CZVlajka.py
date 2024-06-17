"""
Napíš program, ktorý nakresli vlajku Českej republiky (vlajku bývalého Československa). V premenných:

sirka, vyska = 300, 200

má zadané rozmery vlajky. Modrý klin ide do polovice šírky vlajky. Mal by si dostať takýto výstup:
"""

import tkinter
import math
canvas = tkinter.Canvas()
canvas.pack()

sirka, vyska = 300, 200

canvas.create_rectangle(10, 10, sirka, vyska, fill="white")
canvas.create_rectangle(10, vyska/2, sirka, vyska, fill="red")
#va=round(math.sqrt(vyska*vyska-(vyska/2)**2))
canvas.create_polygon(11, 11, sirka/2, vyska/2, 11, vyska, fill="blue")


tkinter.mainloop()