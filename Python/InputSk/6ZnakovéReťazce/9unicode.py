"""
Unicode 0x2654 a ďalších päť za ním sú obrázky šachových figúrok.
Napíš program, ktorý do grafickej plochy nakresli vedľa seba
všetkých 6 figúrok náhodnými farbami väčším fontom 
(napríklad 'arial 50'). Môžeš dostať takýto obrázok:
"""

import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()


def figurky():
    
    x, y = 30, 100
    for i in range(6):
        canvas.create_text(x, y, text=chr(0x2654 + i), font='arial 50', fill=f"#{random.randrange(256**3):06x}")
        x += 60
    

figurky()


tkinter.mainloop()