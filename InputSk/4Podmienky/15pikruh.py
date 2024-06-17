"""
Aj ďalšia verzia programu generuje náhodné bodky v 300 x 300. 
Bodiek teraz vygeneruj aspoň 10000 a zmenši ich na polomer 2. 
Červené bodky budú tie, pre ktoré platí x*x+y*y<=300*300, zvyšné budú modré. 
Program ma záver vypíše podiel počtu červených ku všetkým bodkám krát 4. 
Zamysli sa nad tým, prečo sa tento podiel blíži k číslu pi. 
Napríklad:
"""

import tkinter 
import random

canvas = tkinter.Canvas(height="300", width="300")
canvas.pack()

red = 0
blue = 0

for i in range(10000):
    x, y = random.randint(1, 300), random.randint(1, 300)
    if x*x + y*y <= 300*300:
        farba ='red'
        red += 1
    else: 
        farba = 'blue'
        blue += 1
    canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill=farba, outline="")
print(red/10000 * 4)

tkinter.mainloop()