"""
Program pre dané n a dĺžku strany a nakreslí pravidelný n-uholník so stranou a. 
Využi body na kružnici so stredom x a y a polomerom r budeš musieť vypočítať. 
Napríklad pre x, y = 180, 130 a n = 7 a a = 100 nakreslíš:



canvas = tkinter.Canvas()
canvas.pack()

x0, y0 = 150, 130
r = 110

n = int(input('zadaj n: '))
x, y = x0 + r, y0

for i in range(1, n+1):
    x1 = x0 + r * cos(radians(i * 360 / n))
    y1 = y0 + r * sin(radians(i * 360 / n))
    farba = f'#{random.randrange(256**3):06x}'
    canvas.create_line(x, y, x1, y1, fill=farba, width=3)
    x, y = x1, y1


"""
import math
import tkinter


canvas = tkinter.Canvas()
canvas.pack()

x0, y0 = 180, 130
r = 100

n = int(input('zadaj n: '))
x, y = x0 + r, y0

for i in range(1, n+1):
    x1 = x0 + r * math.cos(math.radians(i * 360 / n))
    y1 = y0 + r * math.sin(math.radians(i * 360 / n))
    canvas.create_line(x, y, x1, y1, width=3)
    for j in range(1, n+1):
        x2 = x0 + r * math.cos(math.radians(j * 360 / n))
        y2 = y0 + r * math.sin(math.radians(j * 360 / n))
        canvas.create_line(x, y, x2, y2)
        #canvas.create_oval(x2-5, y2-5, x2+5, y2+5, fill='white', outline='black', width=1)
        #x, y = x2, y2
    x, y = x1, y1

tkinter.mainloop()