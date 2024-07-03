"""
Napíš program, ktorý pod seba vygeneruje n bankoviek s náhodnými hodnotami.
Na generovanie náhodnej hodnoty použi zápis:

hodnota = random.choice((1, 2, 5, 10, 20, 50))

pomocou ktorého sa náhodne vyberie jedno číslo zo zadanej postupnosti.
Program na záver spočíta výslednú sumu. Veľkosť obdĺžnikov nech je 50x20.
Napríklad pre zadané n=10 môžeš dostať takýto výstup:

"""

import tkinter
import random


n = int(input("počet bankoviek: ") )
a, b = 25, 10
x,y = 150, 100
spolu = 0
canvas = tkinter.Canvas(width=1920,height=1080)
canvas.pack()

for i in range(n):
    canvas.create_rectangle(x-a, y-b, x+a, y+b, fill="white")
    hodnota = random.choice((1, 2, 5, 10, 20, 50))
    canvas.create_text(x, y, text=f"{hodnota} €", fill="black", font="Times 15")
    y += b*2+5
    spolu += hodnota

canvas.create_text(250, y/2, text=f"suma: {spolu} €", fill="black", font="Times 15")

tkinter.mainloop()