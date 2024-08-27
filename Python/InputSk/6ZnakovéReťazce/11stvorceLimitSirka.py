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
    y = 80
    cele = 10
    retazec_ = retazec.split()
    farby = []
    parameter = []
    for i in range(len(retazec_)):
        if i % 2 == 0:
            parameter.append(retazec_[i])
        else:
            farby.append(retazec_[i])   
    i = 0
    while cele + int(parameter[i]) < sirka:
        canvas.create_rectangle(x, y, x + int(parameter[i]), y - int(parameter[i]), fill = farby[i])
        x += int(parameter[i]) + 5
        cele += int(parameter[i]) + 5 
        i += 1
        if i >= len(farby):
            i = 0
        
    
stvorce('40 red 20 blue 60 purple 40 red 30 gold')

tkinter.mainloop()