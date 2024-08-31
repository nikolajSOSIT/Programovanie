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
    abeceda = 'abcdefghijklmnopqrstuvwxyz'
    for i in text:
        print(i)
        if i.islower():
            retazec += abeceda[(abeceda.index(i) + posun) % 26]
        else:
            retazec += i

    return retazec

print(zakoduj('pyThon', 10))
print(zakoduj('ziTryx', -10))