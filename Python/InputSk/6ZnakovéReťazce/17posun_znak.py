"""
Napíš funkciu posun_znak(znak, posun), 
ktorá posunie daný znak v abecede 
o p znakov vpravo (resp. vľavo, ak je záporné). 
Na konci abecedy sa pokračuje od začiatku. Funkcia 
posúva len písmená malej abecedy, ostatné znaky nemení. 
Napríklad:

posun_znak('c', 4)
    'g'
posun_znak('g', -4)
    'c'
posun_znak('x', 10)
    'h'
posun_znak('A', 10)
    'A'
"""

def posun_znak(znak, posun):
    abeceda = 'abcdefghijklmnopqrstuvwxyz'
    if znak.islower():
        return abeceda[(abeceda.index(znak) + posun) % 26]
    else:
        return znak


print(posun_znak('c', 4),
posun_znak('g', -4),
posun_znak('x', 10),
posun_znak('A', 10),
)