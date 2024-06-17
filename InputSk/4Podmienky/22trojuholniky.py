"""
Pomocou polygónu nakresli farebný trojuholník 
zadaný tromi jeho vrcholmi a, b, c. 
Potom do neho nakresli vpísaný trojuholník 
(jeho vrcholy sú v stredoch strán). 
Toto opakuj, kým sú všetky dĺžky strán trojuholníka aspoň 30. 
Trojuholníky vyfarbuj náhodnými farbami. 
Napríklad pre:

a = 10, 100
b = 250, 10
c = 300, 250

Pomôcka: ak mám dva vrcholy (x1, y1) a (x2, y2), potom stred úsečky je 
x3, y3 = (x1+x2)/2, (y1+y2)/2 
"""
import tkinter
import random
from math import sqrt
canvas = tkinter.Canvas()
canvas.pack()

x1, y1 = 10, 100
x2, y2 = 250, 10
x3, y3 = 300, 250
xp, yp = 0, 0

while sqrt((x2-x1)**2 + (y2-y1)**2) >= 30 and sqrt((x3-x2)**2 + (y3-y2)**2) >= 30 and sqrt((x1-x3)**2 + (y1-y3)**2) >= 30:
    index = 1 - index
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=f"#{random.randrange(256**3):06x}")
    xp, yp = x1, y1
    x1, y1 = (x1+x2)/2, (y1+y2)/2
    x2, y2 = (x2+x3)/2, (y2+y3)/2
    x3, y3 = (x3+xp)/2, (y3+yp)/2

tkinter.mainloop()