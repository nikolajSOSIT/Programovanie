'''
Napíš funkciu n_hviezda(n, x0, y0, r, k=2), ktorá pracuje na 
rovnakom princípe ako n_uholnik(n, x0, y0, r) z predchádzajúcej úlohy. 
V tomto prípade sa ale nespájajú 
úsečkami najbližšie vrcholy n-uholníka, ale parameter k určuje,
o koľko vrcholov sa presunieme pre každú úsečku. 
Napríklad n_hviezda(5, 50, 50, 45, 2) označuje,
že sa budú spájať vrcholy 5-uholníka takto: 
0. vrchol s 2., potom 2. vrchol s 4., potom 4. s 1., 1. 
vrchol so 3. a na koniec (piata úsečka) 3. vrchol s 0. 
Zrejme pre k=1 by sa kreslili pôvodné n-uholníky. 
Napríklad pre volanie:

n_hviezda(5, 50, 50, 45)
n_hviezda(7, 150, 50, 45)
n_hviezda(7, 250, 50, 45, 3)

n_hviezda(9, 50, 150, 45)
n_hviezda(9, 150, 150, 45, 4)
n_hviezda(11, 250, 150, 45, 4)
'''
import tkinter
import math


canvas = tkinter.Canvas()
canvas.pack()

def n_hviezda(n, x0, y0, r, k=2):
    for i in range(n):
        canvas.create_line(x0 + r*math.cos(i*(360/n)*math.pi/180), y0 + r*math.sin(i*(360/n)*math.pi/180),
                    x0 + r*math.cos((i+k)*(360/n)*math.pi/180), y0 + r*math.sin((i+k)*(360/n)*math.pi/180))

n_hviezda(5, 50, 50, 45)
n_hviezda(7, 150, 50, 45)
n_hviezda(7, 250, 50, 45, 3)

n_hviezda(9, 50, 150, 45)
n_hviezda(9, 150, 150, 45, 4)
n_hviezda(11, 250, 150, 45, 4)

tkinter.mainloop()
