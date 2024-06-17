"""
Nakresli n sústredných štvorcov (štvorce majú spoločný stred), 
v ktorých sa striedajú tri dané farby ('red', 'blue', 'yellow'). 
Veľkosti štvorcov nech sú 10, 20, 30, … 
Napríklad pre n = 20 dostaneš:
"""

import tkinter

x,y = 120, 30
farba1, farba2, farba3 = "red", "blue", "yellow"
a = 10
n = 20

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

x2, y2 = x + a*n, y + a*n

for i in range(n):
    canvas.create_rectangle(x, y, x2, y2, fill=farba1)
    x,y = x+a/2, y+a/2
    x2, y2 = x2-a/2, y2-a/2
    farba1, farba2, farba3 = farba2, farba3, farba1

tkinter.mainloop()