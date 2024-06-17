"""
Napíš program, ktorý najprv nakreslí dva štvorce: prvý štvorec má ľavý horný roh (x, y) a 
veľkosť strany a1. Druhý štvorec má rovnaký stred ale veľkosť a2 (menšiu od a1). Potom postupne:

zafarbí ich na niektorý odtieň červenej a bledomodrej (napríklad 'indian red' a 'light blue')

k vrcholom vonkajšieho štvorca pripíše pomenovania A, B, C, D

k pravej zvislej hrane väčšieho štvorca pripíše veľkosť tohto štvorca

k spodnej hrane menšieho štvorca pripíše veľkosť tohto menšieho štvorca

Malo by to fungovať aj vtedy, keď zmeníme hociktorú z premenných x, y, a1, a2. Napríklad pre premenné:
"""

import tkinter

x1,y1 = 50, 50
a1, a2 = 180, 100
x2, y2 = ((a1 - a2) /2) + x1, ((a1 - a2) /2) + y1
x1_text, y1_text = x1 + a1 + 15, y1 + a1/2
x2_text, y2_text = x2 + a2/2, y2 + a2 - 15
x1_A, y1_A = x1-10 , y1-10
x1_B, y1_B = x1 + a1 + 10, y1 - 10
x1_C, y1_C = x1 + a1 + 10, y1 + a1 + 10
x1_D, y1_D = x1 - 10, y1 + a1 + 10

canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(x1, y1, x1 + a1, y1 + a1, fill='indian red')
canvas.create_text(x1_text, y1_text, text=a1, font=('Helvetica', 12))
canvas.create_rectangle(x2, y2, x2 + a2, y2 + a2, fill='light blue')
canvas.create_text(x2_text, y2_text, text=a2, font=('Helvetica', 12))
canvas.create_text(x1_A, y1_A, text='A', font=('Helvetica', 12))
canvas.create_text(x1_B, y1_B, text='B', font=('Helvetica', 12))
canvas.create_text(x1_C, y1_C, text='C', font=('Helvetica', 12))
canvas.create_text(x1_D, y1_D, text='D', font=('Helvetica', 12))

tkinter.mainloop()