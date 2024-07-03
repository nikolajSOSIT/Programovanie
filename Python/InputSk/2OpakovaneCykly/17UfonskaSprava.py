"""
Dostali sme správu od mimozemšťanov, ktorá je zložená zo znakov 'O' a '-'. 
Správa obsahuje istý počet riadkov a stĺpcov takýchto znakov. 
Napíš program, ktorým náhodne vygeneruješ podobnú správu. 
Môžeš dostať takýto výstup:

zadaj počet riadkov: 5
zadaj počet stĺpcov: 28
O-OOO----OO-OOO---O---OOOO-O
OOO-OOOO----OO----O-OOOOO-O-
O-OO-OO-OOO--O-OOO--O----OOO
---OO--OO-O-O--OO----OOOO--O
-O-----O--OOOO-OO-OOO-OO---O
"""

import random

riadky = int(input("Zadaj počet riadkov: "))
stlpce = int(input("Zadaj počet stĺpcov: "))
for j in range(riadky):
    for i in range(stlpce):
        print(f"{random.choice("O-")}", end="")
    print()
    