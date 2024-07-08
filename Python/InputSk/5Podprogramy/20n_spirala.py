'''
Aj nasledovná funkcia n_spirala(n, x0, y0, r) 
vychádza z riešenia funkcie n_uholnik(n, x0, y0, r).
V tomto prípade sa nebude kresliť n-uholník, ale špirála. 
Každá úsečka tu bude spájať 
dva vrcholy lenže na stále sa zväčšujúcej kružnici so stredom (x0, y0). 
Začína sa na kružnici s polomerom 5. Prvý 
vrchol sa spojí s nasledujúcim ale na kružnici s polomerom o 2 väčším. 
Takto sa pokračuje, až kým by nebol polomer väčší ako r. 
Napríklad pre volanie:

n_spirala(3, 50, 50, 45)
n_spirala(4, 150, 50, 45)
n_spirala(5, 250, 50, 45)

n_spirala(6, 50, 150, 45)
n_spirala(7, 150, 150, 45)
n_spirala(8, 250, 150, 45)
'''
import tkinter
import math

canvas = tkinter.Canvas()
canvas.pack()

def n_spirala(n, x0, y0, r):
   r_sub = 5
   while r_sub < r:
      for i in range(n):
        canvas.create_line(x0 + r_sub*math.cos(i*(360/n)*math.pi/180), y0 + r_sub*math.sin(i*(360/n)*math.pi/180),
                    x0 + (r_sub+2)*math.cos((i+1)*(360/n)*math.pi/180), y0 + (r_sub+2)*math.sin((i+1)*(360/n)*math.pi/180))
        r_sub += 2


n_spirala(3, 50, 50, 45)
n_spirala(4, 150, 50, 45)
n_spirala(5, 250, 50, 45)

n_spirala(6, 50, 150, 45)
n_spirala(7, 150, 150, 45)
n_spirala(8, 250, 150, 45)

tkinter.mainloop()

