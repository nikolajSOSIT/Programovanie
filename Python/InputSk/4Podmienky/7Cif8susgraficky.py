"""
Uprav predchádzajúci program tak, 
aby sa číslo vypísalo v osmičkovej sústave 
(zrejme namiesto delenia 10 budeš deliť 8). 
Pre číslo 1753 by si mal dostať:
"""

import tkinter

n = int(input("zadaj číslo: "))
sucet = 0

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

a = 20
x, y = 500-a, 250

while n > 0:
    canvas.create_rectangle(x+a, y+a, x - a, y - a, fill="blue")
    sucet += n % 8
    canvas.create_text(x, y, text=n%8, font="Arial 35")
    n = n // 8
    x -= 2*a+5
print(f"ciferný súčet = {sucet}")


tkinter.mainloop()