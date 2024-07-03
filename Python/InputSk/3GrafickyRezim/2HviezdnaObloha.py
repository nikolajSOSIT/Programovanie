"""
Na tmavomodré pozadie (napríklad 'navy') nakresli na náhodné pozície n žltých hviezdičiek (create_text) znak '*' - 
skús ich kresliť rôznymi veľkosťami fontu (napr. veľkosť fontu nech je náhodne číslo od 10 do 20). 
Napríklad, pre n = 200 môžeš dostať niečo podobné:
"""

import tkinter
import random

n = 500

canvas = tkinter.Canvas(bg='navy')
canvas.pack()

for i in range(n):
    x = random.randint(0, 400)
    y = random.randint(0, 300)
    font_size = random.randint(10, 20)
    canvas.create_text(x, y, text='*', fill='yellow', font=('Helvetica', font_size))
tkinter.mainloop()