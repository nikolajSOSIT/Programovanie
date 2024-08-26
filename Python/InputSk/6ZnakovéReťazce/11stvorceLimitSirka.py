"""
Úloha bude podobná predchádzajúcej: napíš funkciu stvorce(retazec),
ktorá dostáva v reťazci informáciu o veľkosti a farbe štvorcov.
Funkcia bude tieto štvorce kresliť vedľa seba, ale len dovtedy,
kým by nasledovný nevypadol z grafickej plochy 
(tento reťazec sa stále opakuje od začiatku). 
Do premennej sirka nastav nejakú šírku grafickej plochy a zavolaj funkciu
"""

import tkinter

sirka = 450
canvas = tkinter.Canvas(width=sirka)
canvas.pack()

def stvorce(retazec):
    x = 10
    y = 60
    cele = 0
    farby = retazec.split()
    for i in range(len(farby)//2):
        canvas.create_rectangle(x, y, x + int(farby[i]), y + 50, fill = farby[i+1])
        x += int(farby[i])
        cele += int(farby[i])
        if cele > sirka:
            break

    
stvorce('40 red 20 blue 60 purple 40 red 30 gold')

tkinter.mainloop()