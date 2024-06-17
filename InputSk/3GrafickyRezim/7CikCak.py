"""
Napíš program, ktorý nakreslí cikcakovú čiaru zloženú z n úsečiek. V premenných:

x, y = 10, 100
d = 20

má nastavené súradnice najľavejšieho bodu prvej úsečky a v d je posunutie 
pre x aj y každého ďalšieho bodu čiary. 
Zrejme k y sa to raz pripočíta a raz odpočíta. 
Napríklad pre n=16 by si mohol dostať:
"""

import tkinter

x, y = 10, 100
d = 20

n = int(input("počet zlomov: ") )

canvas = tkinter.Canvas(width=1920,height=1080)
canvas.pack()

for i in range(n):
    canvas.create_line(x, y, x+d, y+d*(-1)**i, fill="blue", width=5)
    x += d
    y += d*(-1)**i

tkinter.mainloop()