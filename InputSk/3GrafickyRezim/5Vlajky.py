"""
Napíš program, ktorý nakreslí vlajky týchto štátov: Nemecko, Taliansko, Francúzsko a Ukraina. 
Všetky nech majú rozmery 135 x 90. Môže to vyzerať, napríklad takto 
(všimni si, že medzi farebnými pruhmi nie je čierna čiara):"""

import tkinter

x, y = 20,20
a,b = 135,90
canvas = tkinter.Canvas()
canvas.pack()


canvas.create_rectangle(x,y,x+a,y+b)
b = b/3 #premenná už je vydelená tromi, čiže je možné ju znovu použiť
canvas.create_rectangle(x+1, y,x+a, y+b, fill="black", outline="")
y = y+b
canvas.create_rectangle(x+1, y,x+a, y+b, fill="red", outline="")
y = y+b
canvas.create_rectangle(x+1, y,x+a, y+b, fill="yellow", outline="")


# [x,y]
x, y = 20, 160
b = 90
canvas.create_rectangle(x,y,x+a,y+b)
a = a/3
canvas.create_rectangle(x, y+1, x+a, y+b, fill = "blue", outline="")
x = x+a
canvas.create_rectangle(x, y+1, x+a, y+b, fill = "white", outline="")
x = x+a
canvas.create_rectangle(x, y+1, x+a, y+b, fill = "red", outline="")

x, y = 200,20
a, b = 135,90
canvas.create_rectangle(x,y,x+a,y+b)
a = a/3
canvas.create_rectangle(x, y+1, x+a, y+b, fill = "green", outline="")
x = x+a
canvas.create_rectangle(x, y+1, x+a, y+b, fill = "white", outline="")
x = x+a
canvas.create_rectangle(x, y+1, x+a, y+b, fill = "red", outline="")

x, y = 200,160
a, b = 135,90
canvas.create_rectangle(x,y,x+a,y+b)
b = b/2 #premenná už je vydelená tromi, čiže je možné ju znovu použiť
canvas.create_rectangle(x+1, y,x+a, y+b, fill="blue", outline="")
y = y+b
canvas.create_rectangle(x+1, y,x+a, y+b, fill="yellow", outline="")


tkinter.mainloop()
