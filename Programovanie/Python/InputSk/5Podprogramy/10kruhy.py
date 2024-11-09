"""
Napíš funkciu kruhy(x, y), ktorá nakreslí 
10 sústredných náhodne zafarbených kruhov, ich polomery budú 5, 10, 15, … 
Napríklad pre volanie:

for i in range(10):
    kruhy(random.randint(50, 330), random.randint(50, 210))
"""
import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

def kruhy(x,y):
    num = 50
    for i in range(10):
        canvas.create_oval(x-num,y-num, x+num, y + num, fill=f"#{random.randrange(256**3):06x}")
        num -= 5


for i in range(10):
    kruhy(random.randint(50, 330), random.randint(50, 210))

tkinter.mainloop()