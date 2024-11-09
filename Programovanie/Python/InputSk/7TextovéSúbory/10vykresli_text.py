import tkinter



def vykresli_text(meno_suboru, velkost=16):
    with open(f"Python\\InputSk\\7TextovéSúbory\\{meno_suboru}", "r") as subor:
        text = subor.read()
    canvas = tkinter.Canvas()
    canvas.pack()
    canvas.create_text(200, 100, text=text, font=("consolas", velkost))
    tkinter.mainloop()

vykresli_text("text3.txt")