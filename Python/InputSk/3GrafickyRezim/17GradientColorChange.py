"""
Program nakreslí 25 obdĺžnikov veľkosti 15x250, 
ktoré sú uložené tesne vedľa seba. Tieto obdĺžniky postupne menia farby od červenej k modrej:
čím je väčšie x obdĺžnika tým menej červenej a viac modrej. 
Mohlo by to vyzerať takto:
"""

import tkinter


canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()
x = 15

for i in range(25):
    cervena = 255 -(i * (255 // 25))
    modra = 0 + (i * (255 // 25))
    canvas.create_rectangle(x, 15, x+15, 15+250, fill=f"#{cervena:02x}{0:02x}{modra:02x}", outline="")
    x += 15

tkinter.mainloop()