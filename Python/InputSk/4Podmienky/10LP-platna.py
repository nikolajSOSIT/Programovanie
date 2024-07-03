"""
Napíš program, ktorý nakreslí gramofónovú LP platňu ako 
niekoľko sústredných kružníc.
Najväčšia z nich má polomer r a každá ďalšia je o 3 menšia.
Najmenšia kružnica by nemala mať menší polomer ako 15. 
Každú k-tu kružnicu nakresli šedou farbou (začni od najväčšej).
Napríklad pre premenné:

x, y = 190, 130
r = 120
k = 6
"""

import tkinter

x, y = 190, 130
r = 120
k = 6
color = "black"
pocet = 0

canvas = tkinter.Canvas()
canvas.pack()

while r >= 15:
    if pocet % k == 0:
        color = "gray"
    else:
        color = "black"
    canvas.create_oval(x-r, y-r, x+r, y+r, outline=color)
    r -= 3
    pocet += 1

tkinter.mainloop()