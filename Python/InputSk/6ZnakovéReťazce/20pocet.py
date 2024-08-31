"""
Metóda 'reťazec'.count(podreťazec) 
zisťuje počet výskytov podreťazca v reťazci.
Napíš funkciu pocet(retazec, podretazec),
ktorá robí to isté,
ale bez použitia tejto metódy. 
Napríklad:

pocet('mama ma emu a ema ma mamu', 'ma ')
    4
pocet('mama ma emu a ema ma mamu', 'am')
    2
"""

def pocet(retazec, podretazec):
    pocet = 0
    for i in range(len(retazec) - len(podretazec) + 1):
        if retazec[i:i + len(podretazec)] == podretazec:
            pocet += 1
    return pocet

print(pocet('mama ma emu a ema ma mamu', 'ma '))