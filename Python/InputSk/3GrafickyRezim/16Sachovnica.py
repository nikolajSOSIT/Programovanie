"""
Napíš program, ktorý nakreslí farebnú šachovnicu. Program si najprv pomocou dvoch input vypýta počet stĺpcov a počet riadkov. V premenných:

vel = 30
farba1, farba2 = 'maroon', 'gold'
má nastavenú veľkosť štvorčeka a dve farby, ktoré sa majú na šachovnici striedať. Medzi nakreslenými štvorčekmi je ešte medzera veľkosti 3. Môžeš dostať takýto výstup:

"""



import tkinter

canvas = tkinter.Canvas(width=300, height=300)
canvas.pack()
x,y=10,10
a=30
farba1, farba2 = 'maroon', 'gold'

for i in range(8):
    for j in range(8):
        canvas.create_rectangle(x,y,x+30,y+30,fill=farba1)
        x+=35
        farba1, farba2 = farba2, farba1
    y+=35
    x = 10
    farba1, farba2 = farba2, farba1

tkinter.mainloop()