"""
Budem hrať takúto hru: kladiem vedľa seba do radu
mince s náhodnými hodnotami z <1, 4>; skončím, 
keď ich súčet bude väčší alebo rovný danému k. 
Ak skončil so súčtom, ktorý je rovný k, 
vypíše text 'HURÁ' inak 'ŠKODA'. 
Napíš program, 
ktorý túto hru odsimuluje 10-krát a zakreslí to pod seba,
napríklad pre ˙˙k=21˙˙ môžeš dostať takýto obrázok:

"""
import random
import tkinter

k = 21
sucet = 0
x, y = 20, 20
r = 10

canvas = tkinter.Canvas()
canvas.pack() 

for i in range(10):
    while True:
        mince = random.randint(1, 4)
        canvas.create_oval(x-r, y-r, x+r, y+r, outline="black", fill="white")
        canvas.create_text(x, y, text=str(mince), fill="black", font="Arial 15")
        sucet += mince
        x += 25
        if sucet >= k:
            if sucet == k:
                canvas.create_text(350, y, text="HURÁ", fill="green", font="Arial 10")
                x = 20
                sucet = 0	
            else:
                canvas.create_text(350, y, text="ŠKODA", fill="red", font="Arial 10")
                x = 20
            sucet = 0	
            break
        
    y += 25

tkinter.mainloop()