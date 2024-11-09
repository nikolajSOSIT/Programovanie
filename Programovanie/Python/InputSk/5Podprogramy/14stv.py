"""
Napíš funkciu stv(riadok, stlpec, farba='white'), 
ktorá nakreslí farebný štvorec do myslenej štvorcovej siete,
v ktorej je každé políčko veľké 30x30. 
Ľavý horný roh najľavejšieho horného štvorca má súradnice (5, 5). 
Napríklad pre volanie:

for i in range(8):
    for j in range(12):
        if i == j:
            stv(i, j)
        else:
            stv(i, j, nahodna_farba())

"""
import tkinter
import random
import time

canvas = tkinter.Canvas()
canvas.pack()

def nahodna_farba():
    return f"#{random.randrange(256**3):06x}"

def stv(riadok, stlpec, farba='white'):
    canvas.create_rectangle(stlpec * 30 + 5, riadok * 30 + 5, stlpec * 30 + 35, riadok * 30 + 35, fill=farba, outline="")

#rgb

def rgb(r, g , b ):
    return f"#{r:02x}{g:02x}{b:02x}"

r, g = 255, 0
for i in range(8):
    for j in range(12):
        g = 14*i+14*j
        if g > 255:
            g = 255
        stv(i, j, rgb(r, g, 0))

tkinter.mainloop()


tkinter.mainloop()
