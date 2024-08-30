"""
Napíš funkciu zakoduj(text, posun), ktorá posunie 
v abecede všetky znaky (pomocou funkcie posun_znak). 
Napríklad:

x = zakoduj('pyThon', 10)
x
    'ziTryx'
zakoduj(x, -10)
    'pyThon'
zakoduj(x, 16)
    'pyThon'
"""

def zakoduj(text, posun):
    retazec = ""
    for i in text:
        retazec += str(ord(i) + posun) + " "
        print(retazec)
    return retazec

print(zakoduj('pyThon', 10))
    