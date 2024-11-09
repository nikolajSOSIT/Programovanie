import tkinter

def kresli(retazec):
    x, y = 100, 100
    nasobok = 1
    farba = 'black'
    for znak in retazec:
        x1, y1 = x, y
        if znak == 's':
            y1 -= 10 * nasobok
        elif znak == 'v':
            x1 += 10 * nasobok
        elif znak == 'j':
            y1 += 10 * nasobok
        elif znak == 'z':
            x1 -= 10 * nasobok
        elif znak == 'h':
            farba = ""
        elif znak == 'd':
            farba = "black"
        elif znak.isdigit():
            nasobok = int(znak)
        elif not znak.isdigit():
            print('nerozumiem "' + znak + '"')  
            return
        canvas.create_line(x, y, x1, y1, fill=farba)
        x, y = x1, y1

canvas = tkinter.Canvas()
canvas.pack()

kresli('4v4j4z4sh5vd'*5)

tkinter.mainloop()
