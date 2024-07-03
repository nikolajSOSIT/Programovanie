"""
Využi while-cyklus z predchádzajúcej úlohy a vypíš cifry 
do grafickej plochy (zrejme sprava do ľava). 
Program jednotlivé cifry vypíše do farebných štvorcov. 
Napríklad, pre číslo 510726 by si mal dostať:
"""
import tkinter

n = int(input("zadaj číslo: "))
sucet = 0

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

a = 20
x, y = 500-a, 250

while n > 0:
    canvas.create_rectangle(x+a, y+a, x - a, y - a, fill="blue")
    sucet += n % 10
    canvas.create_text(x, y, text=n%10, font="Arial 35")
    n = n // 10
    x -= 2*a+5
print(f"ciferný súčet = {sucet}")


tkinter.mainloop()