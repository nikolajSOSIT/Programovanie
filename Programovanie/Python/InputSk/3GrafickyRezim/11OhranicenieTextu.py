"""
Program najprv prečíta nejaký text zo vstupu (input) 
a potom postupne každé písmeno tohto textu zapíše ('arial 26') 
do jedného farebného štvorca veľkosti 30x30. 
Tieto štvorce sú umiestnené tesne vedľa seba. 
Farby štvorcov aj písmen zvoľ náhodne. 
Napríklad môžeš dostať niečo podobné:
"""
import tkinter
import random

text = input("text: ")
a = 15
x, y = 500, 100

canvas = tkinter.Canvas(width=1920,height=1080)
canvas.pack()
for i in text:
    canvas.create_rectangle(x-a, y-a, x+a, y+a, fill=f"#{random.randrange(256**3):06x}")
    canvas.create_text(x, y, text=i, fill=f"#{random.randrange(256**3):06x}", font="arial 26")
    x += a*2
tkinter.mainloop()

