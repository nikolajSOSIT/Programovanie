'''
Napíš funkciu vybodkuj_usecku(x1, y1, x2, y2, n), ktorá nakreslí úsečku 
z bodu (x1, y1) do bodu (x2, y2). Túto úsečku nekreslí 
pomocou create_line, 
ale pomocou n bodiek, t.j. malých modrých kruhov s polomerom 3. 
Parameter n je minimálne 2 a vtedy sa nakreslia len dve bodky  
v koncových vrcholoch úsečky. 
Pre kontrolu najprv vykreslíme originálnu úsečku šedou farbou. 
Otestuj, napríklad:
'''
import tkinter


def vybodkuj_usecku(x1, y1, x2, y2, n):
    x = x2-x1
    y = y2-y1
    for i in range(n+1):
        canvas.create_oval((x1 + round(i*(x/n))) - 3, (y1 + round(i*(y/n))) - 3, (x1 + round(i*(x/n))) + 3, (y1 + round(i*(y/n))) + 3, fill="blue")

canvas = tkinter.Canvas()
canvas.pack()

canvas.create_line(100, 80, 280, 120, fill='lightgray', width=11)
vybodkuj_usecku(100, 80, 280, 120, 20)
canvas.create_line(280, 120, 150, 200, fill='lightgray', width=11)
vybodkuj_usecku(280, 120, 150, 200, 10)
canvas.create_line(150, 200, 100, 80, fill='lightgray', width=11)
vybodkuj_usecku(150, 200, 100, 80, 8)

tkinter.mainloop()