'''
Napíš dve funkcie horna(x0, y0, r) a dolna(x0, y0, r), 
ktoré nakreslia len polovicu kružnice so stredom (x0, y0) a s polomerom r. 
Funkcia horna by mala nakresliť len hornú polovicu a dolna len dolnú.
Kružnicu kresli ako 36-uholník, a teda polovica označuje 18 úsečiek. 
Napríklad volania:

horna(30, 100, 30)
dolna(90, 100, 30)
horna(150, 100, 30)
dolna(210, 100, 30)
horna(270, 100, 30)
dolna(330, 100, 30)

for i in range(6):
    horna(30+60*i, 200, 30)
by nakreslili:

'''
import tkinter
import math

canvas = tkinter.Canvas()
canvas.pack()

def horna(x0, y0, r):
    for i in range(18):
        canvas.create_line(x0 + r*math.cos(i*(360/36)*math.pi/180), y0 - r*math.sin(i*(360/36)*math.pi/180),
                    x0 + r*math.cos((i+1)*(360/36)*math.pi/180), y0 - r*math.sin((i+1)*(360/36)*math.pi/180))


def dolna(x0, y0, r):
    for i in range(18):
        canvas.create_line(x0 + r*math.cos(i*(360/36)*math.pi/180), y0 + r*math.sin(i*(360/36)*math.pi/180),
                    x0 + r*math.cos((i+1)*(360/36)*math.pi/180), y0 + r*math.sin((i+1)*(360/36)*math.pi/180))

horna(30, 100, 30)
dolna(90, 100, 30)
horna(150, 100, 30)
dolna(210, 100, 30)
horna(270, 100, 30)
dolna(330, 100, 30)

for i in range(6):
    horna(30+60*i, 200, 30)

tkinter.mainloop()