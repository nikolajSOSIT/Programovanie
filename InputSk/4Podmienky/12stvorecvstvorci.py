"""
Využi program z prednášky, v ktorom sa vykresľovalo 1000 farebných bodiek 
(malé krúžky s polomerom 5 bez obrysu) podľa toho či mali x-ovú, 
alebo y-ovú súradnicu menšiu alebo väčšiu ako 150. 
Veľkosť grafickej plochy bola 300x300. 
Zmeň v tomto programe sériu príkazov if tak, 
aby kreslené bodky vytvorili vnútorný červený štvorec s rozmermi 150x150. 
Vykresli s 4000 farebnými bodkami:

"""

import tkinter
import random

canvas = tkinter.Canvas(bg='white', width=300, height=300)
canvas.pack()

for i in range(4000):
    x = random.randint(1, 300)
    y = random.randint(1, 300)
    if 225 > x > 75  and 225 > y > 75:
        farba ='red'
    else: 
        farba = 'blue'
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=farba, width=0)

tkinter.mainloop()

