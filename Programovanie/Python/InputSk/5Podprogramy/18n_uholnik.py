'''
Napíš funkciu n_uholnik(n, x0, y0, r), ktorá nakreslí pravidelný n-uholník. 
Tento n-uholník bude vpísaný v myslenej kružnici
so stredom (x0, y0) a s polomerom r. 
Napríklad pre volanie:

n_uholnik(3, 50, 50, 45)
n_uholnik(4, 150, 50, 45)
n_uholnik(5, 250, 50, 45)

n_uholnik(6, 50, 150, 45)
n_uholnik(7, 150, 150, 45)
n_uholnik(8, 250, 150, 45)
'''
import tkinter
import math

canvas = tkinter.Canvas()
canvas.pack()

def n_uholnik(n, x0, y0, r):
    for i in range(n):
        canvas.create_line(x0 + r*math.cos(i*(360/n)*math.pi/180), y0 + r*math.sin(i*(360/n)*math.pi/180),
                    x0 + r*math.cos((i+1)*(360/n)*math.pi/180), y0 + r*math.sin((i+1)*(360/n)*math.pi/180))

n_uholnik(3, 50, 50, 45)
n_uholnik(4, 150, 50, 45)
n_uholnik(5, 250, 50, 45)

n_uholnik(6, 50, 150, 45)
n_uholnik(7, 150, 150, 45)
n_uholnik(8, 250, 150, 45)

tkinter.mainloop()