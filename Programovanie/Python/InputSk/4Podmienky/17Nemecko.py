"""
Vlajku Nemecka môžeš do štandardnej veľkosti grafickej plochy nakresliť tak, 
že pomocou cyklu vygeneruješ 10000 náhodných súradníc 
x z intervalu <10, 350> a y z intervalu <10, 250>. 
Na vygenerované súradnice nakreslíš farebnú bodku (kruh s polomerom 5 bez obrysu). 
Farbu bodky zvolíš podľa y-ovej súradnice:

ak je y < 90 kresli čierny krúžok,

inak, ak je y < 170 kresli červený krúžok,

inak nakresli žltý (môže byť 'gold') krúžok.

Mal by si dostať takýto obrázok:
"""
import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

for i in range(10000):
    x = random.randint(10, 350)
    y = random.randint(10, 250)
    if y < 90:
        farba = 'black'
    elif y < 170:
        farba ='red'
    else:
        farba = 'gold'
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=farba, outline="")


tkinter.mainloop()
