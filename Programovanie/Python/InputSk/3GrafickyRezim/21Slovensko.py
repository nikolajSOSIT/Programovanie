import tkinter

x, y = 30, 30
sir, vys = 325, 216
modra, cervena = '#0b4ea2', '#ee1c25'
farba1, farba2, farba3 = '#ffffff', '#0000ff', '#ff0000'
canvas = tkinter.Canvas()
canvas.pack()
vys = vys/3

image = tkinter.PhotoImage(file='InputSk/3GrafickyRezim/sk.png')

for i in range(3):
    canvas.create_rectangle(x, y, x+sir, y+vys, fill=farba1, outline="")
    y = y+vys
    farba1, farba2, farba3 = farba2, farba3, farba1


canvas.create_image(x+100, y-108, image=image)

tkinter.mainloop()