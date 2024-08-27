import tkinter

canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(50,50,100,100, outline="red", fill="blue", width=5)

tkinter.mainloop()