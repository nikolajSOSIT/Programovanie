import tkinter

def kresli(meno_suboru):
    with open(f'Python\\InputSk\\7TextovéSúbory\\{meno_suboru}', 'r') as subor:
        x0 = None
        for riadok in subor:
            i = riadok.find(' ')
            if i < 0:             # ak v riadku nie je medzera, riadok je asi prázdny
                x0 = None
            else:
                x, y = int(riadok[:i]), int(riadok[i:])
                canvas.create_oval(x - 3, y - 3, x + 3, y + 3)
                if x0 != None:
                    canvas.create_line(x0, y0, x, y)
                x0, y0 = x, y

canvas = tkinter.Canvas()
canvas.pack()

kresli('body1.txt')

tkinter.mainloop()