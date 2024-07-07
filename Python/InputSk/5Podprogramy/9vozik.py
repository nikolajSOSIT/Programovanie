import tkinter

def koleso(x, y, r = 15, color="blue"):
    canvas.create_oval(x-r, y-r//3, x+r, y-r//3+r*2, fill=color)

def doska(x1,y1,x2 = 100,y2 = 20,color="red"):
    x2 = x2//2
    y2 = y2//2
    canvas.create_rectangle(x1-x2,y1-y2,x1+x2,y1+y2, fill=color)

def maly_vozik(x, y):
    doska(x, y)
    koleso(x - 30, y)
    koleso(x + 30, y)

def velky_vozik(x, y):
    doska(x, y, 150, 40, 'green')
    koleso(x - 35, y, 25, 'orange')
    koleso(x + 35, y, 25, 'orange')

canvas = tkinter.Canvas()
canvas.pack()

maly_vozik(200, 100)
velky_vozik(150, 200)
maly_vozik(300, 210)

tkinter.mainloop()