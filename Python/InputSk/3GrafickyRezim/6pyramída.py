"""
Napíš program, ktorý nakreslí pyramídu z kvádrov (obdĺžnikov) veľkosti: 200x50, 150x50, 100x50 a 50x50. 
Najväčší z nich má stred dolnej hrany (180, 250). Všetky zafarbi štyrmi rôznymi odtieňmi zelenej. 
Na kreslenie použi jeden for-cyklus, v ktorom premenná cyklu farba, 
bude nadobúdať 4 rôzne reťazce (mená farieb) a v cykle sa budú meniť premenné y a momentálna sirka kvádra. 
Mal by si dostať podobný výstup:
"""
import tkinter

x,y = 180,250
a,b = 200,50


canvas = tkinter.Canvas(width=1920,height=1080)
canvas.pack()

for farba in ["aquamarine4", "aquamarine3", "aquamarine2", "aquamarine1"]:
    canvas.create_rectangle(x-round(a/2),y,x+round(a/2),y+b, fill=farba, outline="")
    a -= 50
    y -= b
    print(a,b,x,y)

tkinter.mainloop()
