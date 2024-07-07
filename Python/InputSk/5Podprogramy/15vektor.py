"""
Vektor si môžeme predstaviť ako úsečku, 
ktorá je daná jedným vrcholom (x, y), dĺžkou a uhlom. Uvedom si,
že koncové body takéhoto vektora ležia na kružnici s polomerom 
dĺžka a daným stredom (bodom (x, y)). Úsečku nakreslíme tak, aby mala 
tvar šípky (do create_line pridáme pomenovaný parameter arrow='last'). 
Napíš funkciu vektor(x, y, dlzka, uhol). 
Otestuj, napríklad takto:

for i in range(10):
    vektor(random.randint(50, 300), random.randint(50, 200),
           random.randint(10, 80), random.randint(0, 359))
a môžeš dostať:

"""
import math
import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

def vektor(x, y, dlzka, uhol):
    canvas.create_line(x, y, x + dlzka * math.cos(uhol * math.pi / 180), y + dlzka * math.sin(uhol * math.pi / 180), arrow='last')

for i in range(10):
    vektor(random.randint(50, 300), random.randint(50, 200),
           random.randint(10, 80), random.randint(0, 359))

tkinter.mainloop()