"""
Nasledovný program vykresľuje farebné krúžky 
v štvorcovej sieti n x n a zafarbuje ich podľa 
podmienky v príkaze if:

A. Zmeň túto podmienku tak, aby sa nakreslil obrázok, 
v ktorom sa zafarbí stredný rad a stredný stĺpec 
(v programe nemeň iné príkazy, nepridávaj ďalšie):

B. Zmeň túto podmienku tak, aby sa nakreslil obrázok, 
v ktorom sa zafarbia obe uhlopriečky:
"""

import tkinter

canvas = tkinter.Canvas()
canvas.pack()

n = 13
for i in range(n):
    for j in range(n):
        x = j*20 + 100
        y = i*20 + 12
        #A) 
        #if i == n//2 or j == n//2:
        #B)
        if i + j == n-1 or j == i:
            farba = 'red'
        else:
            farba = 'white'
        canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill=farba)

tkinter.mainloop()