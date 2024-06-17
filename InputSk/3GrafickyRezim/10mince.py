"""
Program nakreslí n náhodných mincí. Mincami sú farebné kruhy s 
polomerom 20, v ktorých sú veľké ('arial 30') náhodné číslice od 1 do 9. 
Napríklad pre n = 30 môžeš dostať niečo podobné:
"""

import tkinter
import random

n = int(input("počet mincí: ") )
r = 20

canvas = tkinter.Canvas(width=1920,height=1080)
canvas.pack()

for i in range(n):
    cislo = random.randint(1,9)
    x, y = random.randint(20,1900), random.randint(20,1060)
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=f"#{random.randrange(256**3):06x}", outline="black")
    canvas.create_text(x, y, text=f"{cislo}", fill="black", font="arial 30")

tkinter.mainloop()

