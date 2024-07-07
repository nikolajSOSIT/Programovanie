"""
Na prednáške sa pomocou farebných bodiek kreslil červený mesiac 
na modrom pozadí. Využívala sa pritom funkcia vzd. 
Napíš funkciu farebne_bodky(r, x1, y1, x2, y2, x3, y3), ktorá 
na podobnom princípe grafickú plochu vybodkuje podľa týchto pravidiel: 
ak by sme nakreslili tri rovnako veľké kruhy s polomerom r 
ale s rôznymi stredmi (x1, y1), (x2, y2), (x3, y3), tieto by sa mohli 
čiastočne prekrývať. Bodky budeš farbiť tak, že tie oblasti, v ktorých 
nie je žiaden kruh alebo sa prekrývajú práve 2 kruhy zafarbíš na modro, 
ostatné oblasti budú žlté. Napríklad pre volanie:
"""


import tkinter
import random
import math

def vzd(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def kresli_bodku(x, y, farba):
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=farba, width=0)

def farebne_bodky(x1, y1, x2, y2, x3, y3, pocet = 7500, r = 100):
    global width, height
    for i in range(pocet):
        randX = random.randint(5, width-5)
        randY = random.randint(5, height-5)
        if vzd(randX, randY, x1, y1) > r and vzd(randX, randY, x2, y2) > r and vzd(randX, randY, x3, y3) > r:
            kresli_bodku(randX, randY, 'navy')
        elif (vzd(randX, randY, x1, y1) < r and vzd(randX, randY, x2, y2) < r and vzd(randX, randY, x3, y3) > r) or (vzd(randX, randY, x1, y1) < r and vzd(randX, randY, x2, y2) > r and vzd(randX, randY, x3, y3) < r) or (vzd(randX, randY, x1, y1) > r and vzd(randX, randY, x2, y2) < r and vzd(randX, randY, x3, y3) < r):
            kresli_bodku(randX, randY, 'navy')
        else:
            kresli_bodku(randX, randY, 'yellow')
width = 400
height = 400
canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()

farebne_bodky(120, 120, 200, 120, 160, 180)

tkinter.mainloop()