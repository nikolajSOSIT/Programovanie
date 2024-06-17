"""
Podobná úloha ako v predchádzajúcom príklade, 
len v tomto sa využívajú uhlopriečky štvorca. 
Asi tu budeš vedieť využiť podmienky x < y alebo 300 - x < y:
"""

import tkinter
import random

canvas = tkinter.Canvas(bg='white', width=300, height=300)
canvas.pack()

for i in range(4000):
    x = random.randint(1, 300)
    y = random.randint(1, 300)
    if x < y and 300 - x < y:
        farba ='green'
    elif 300 - x > y and y > x:
        farba = 'red'
    elif 300 - y > x:
        farba = "blue"
    else: 
        farba = 'yellow'
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=farba, width=0)

tkinter.mainloop()
