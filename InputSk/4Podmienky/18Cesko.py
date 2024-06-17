"""Vytvor program, ktorý podobne, ako v predchádzajúcej úlohe, nakreslí vlajku Českej republiky (bývalého Československa):"""
from logging import fatal
import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

for i in range(10000):
    x = random.randint(10, 350)
    y = random.randint(10, 250)
    if 275 - x > y and y > x:
        farba = 'blue'
    elif y > 130:
        farba = "red"
    else:
        farba = 'white'
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=farba, outline="")


tkinter.mainloop()

