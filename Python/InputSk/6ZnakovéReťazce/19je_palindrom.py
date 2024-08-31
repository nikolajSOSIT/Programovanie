"""
Napíš funkciu je_palindrom(reťazec),ktorá 
zistí (vráti True alebo False),
či je zadaný reťazec palindróm. 
Funkcia ignoruje medzerya nerozlišuje medzi
malými a veľkými písmenami. 
Napríklad:


"""

def je_palindrom(reťazec):
    reťazec = reťazec.lower()
    reťazec = reťazec.replace(" ", "")
    return reťazec == reťazec[::-1]

print(je_palindrom('Jelenovi Pivo Nelej'))