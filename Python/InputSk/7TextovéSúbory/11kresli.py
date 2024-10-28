import tkinter

canvas = tkinter.Canvas()
canvas.pack()

def kresli(meno_suboru):
    with open(f'Python\\InputSk\\7TextovéSúbory\\{meno_suboru}') as subor:
        x1,y1,x2,y2 = 0,0,0,0
        for riadok in subor:
            i = riadok.find(' ')
            x, y = int(riadok[:i]), int(riadok[i:])
            if x1 == 0:
                x1, y1 = x, y
            else:   
                x2, y2 = x, y
                canvas.create_line(x1, y1, x2, y2)
            x1, y1 = x, y
            canvas.create_oval(x-2, y-2, x+2, y+2)



kresli('body.txt')
tkinter.mainloop()