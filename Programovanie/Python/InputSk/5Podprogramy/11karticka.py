"""
Napíš funkciu karticka(x, y, text), ktorá nakreslí bledošedý obdĺžnik a do jeho stredu vypíše zadaný text. Stred kartičky má súradnice (x, y) a jej strany majú dĺžky 100 a 40. Font písma môže byť, napríklad 'arial 14'. Otestuj náhodným vygenerovaním 10 kartičiek, napríklad:

for i in range(10):
    karticka(random.randint(50, 300), random.randint(50, 200), 'Python')
"""
import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

def karticka(x,y, text):
    canvas.create_rectangle(x-50, y-20, x+50, y+20, fill='gray')
    canvas.create_text(x,y, text=text, font='Arial 14')

for i in range(10):
    karticka(random.randint(50, 300), random.randint(50, 200), 'Python')

tkinter.mainloop()