"""
Napíš program, ktorý najprv nakreslí dva štvorce vedľa seba (prvý má ľavý horný (x, y), veľkosť 100, druhý je o 10 odsunutý). Potom postupne:

zafarbí ich tak, že prvý bude červený a druhý modrý (parameter fill='...')

do stredu prvého vypíšeš text 'červený' a druhého 'modrý'

písmo oboch textov zväčšíš (napríklad parameter font='arial 20') a zafarbíš na žlto (parameter fill='...')

Ak budú premenné x, y = 50, 50, mal by si dostať takýto výstup:


"""

import tkinter

x, y = 120, 10
velkost = 100

canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(x, y, x+velkost, y+velkost, fill='red')
x_ = x + velkost + 10
canvas.create_rectangle(x_, y, x_+velkost, y+velkost, fill='blue')
x_text = x + velkost / 2
y_text = y + velkost / 2
canvas.create_text(x_text, y_text, text='červená', font='arial 20', fill='yellow')
canvas.create_text(x_text + velkost + 10, y_text, text='modrá', font='arial 20', fill='yellow')

tkinter.mainloop()