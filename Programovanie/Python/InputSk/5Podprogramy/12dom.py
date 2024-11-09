"""
Napíš funkciu dom(x, y, vel1, vel2), ktorá nakreslí domček:
štvorec má ľavý dolný roh (x, y) a veľkosť strany je vel1,
trojuholník má výšku vel2 a základňu vel1. 
Oba sú zafarbené rôznymi náhodnými farbami. 
Napríklad pre volanie:

"""
import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

def dom(x, y, vel1, vel2):
    canvas.create_rectangle(x, y, x+vel1, y-vel1, fill=f"#{random.randrange(256**3):06x}")
    y -= vel1
    canvas.create_polygon(x, y, x+vel1, y, x+vel1/2, y-vel2, fill=f"#{random.randrange(256**3):06x}")

x, y = 10, 150
while x < 330:
    v = random.randint(20, 50)
    dom(x, y, v, random.randint(v // 2, v))
    x += v

tkinter.mainloop()
