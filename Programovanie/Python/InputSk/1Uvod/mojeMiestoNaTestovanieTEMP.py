"""simonove"""
def jedna(cislo):
    delitel = 10
    text = str(cislo)
    for i in range(len(text)-1):
        print(cislo//delitel, cislo%delitel)
        delitel *= 10
#jedna(51731456)

def tri(text):
    print((text+"\n")*10)
#tri("(.)(.)")

def styri(input):
    datum = [1,1,2009] 
    print(f"ms od: {(input[2]-datum[2])*(input[1]-datum[1])*(input[0]-datum[0])*24*60*60*1000}") # :(
    print(f"sekund od: {(input[2]-datum[2])*(input[1]-datum[1])*(input[0]-datum[0])*24*60*60}")
    print(f"minut od: {(input[2]-datum[2])*(input[1]-datum[1])*(input[0]-datum[0])*24*60}")
    print(f"hodin od: {(input[2]-datum[2])*(input[1]-datum[1])*(input[0]-datum[0])*24}")
    print(f"dni od: {input[0]-datum[0]}")
    print(f"mesiacov od: {input[1]-datum[1]}")
    print(f"rokov od: {input[2]-datum[2]}")
    
styri([23,4,2024])