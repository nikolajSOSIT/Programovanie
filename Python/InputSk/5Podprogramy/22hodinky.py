'''
Napíš funkcie rucicka(uhol, dlzka, hrubka, farba) a hodinky(hod, min, sek),
pomocou ktorých nakreslíme ručičkové hodinky. Funkcia rucicka nakreslí len
jednu ručičku ako úsečku z bodu (190, 130) pod daným uhlom,
danej farby a hrúbky (podobne ako sa kreslil vektor v 15. úlohe). 
Funkcia hodinky nakreslí ciferník (stačí kruh s polomerom 100)
tri ručičky pre hodiny (dĺžka 60, hrúbka 10, farba 'gray'),
pre minúty (dĺžka 70, hrúbka 6, farba 'black'),
pre sekundy (dĺžka 80, hrúbka 2, farba 'red'). 
Napríklad volanie:

hodinky(8, 55, 10)
by nakreslilo:
'''
import tkinter
import math
import time

canvas = tkinter.Canvas()
canvas.pack()

def rucicka(uhol, dlzka, hrubka, farba):
    canvas.create_line(190, 130, 190 + dlzka*math.cos(uhol*math.pi/180), 130 + dlzka*math.sin(uhol*math.pi/180), width=hrubka, fill=farba, arrow='last')

def hodinky(hod, min, sek):
    canvas.create_oval(90, 30, 290, 230, fill='white')
    hod -= 3
    min -= 15
    sek -= 15
    rucicka(hod*30, 60, 10, 'gray')
    rucicka(min*6, 70, 6, 'black')
    rucicka(sek*6, 80, 2, 'red')

while True:
    canvas.delete('all')
    h, m, s = time.localtime()[3:6]
    hodinky(h, m, s)
    canvas.update()
    canvas.after(1000)


tkinter.mainloop()