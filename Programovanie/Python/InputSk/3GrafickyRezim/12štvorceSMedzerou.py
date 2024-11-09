"""
Napíš program, ktorý si najprv zo vstupu (input) vypýta n a potom medzi šírku 10 a 380 vykreslí n čo najväčších rovnako veľkých štvorcov (s medzerou 5). 
Pre dané n teda najprv vypočítaš veľkosť štvorcov tak, aby boli čo najväčšie a zmestili sa do danej šírky. 
Štvorce vyplň náhodnými farbami. 
Napríklad pre n=7 môžeš dostať takýto výstup:
"""

import tkinter
import random

n = int(input("počet štvorcov: "))
a = (370/n) - 10 
x,y = 10, 10
canvas = tkinter.Canvas()
canvas.pack()

for i in range(n):
    canvas.create_rectangle(x, y, x+a, y+a, fill=f"#{random.randrange(256**3):06x}")
    x += a+5


tkinter.mainloop()
