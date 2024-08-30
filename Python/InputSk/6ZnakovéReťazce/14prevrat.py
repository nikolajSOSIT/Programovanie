"""
Znakový reťazec vieme prevrátiť pomocou zápisu retazec[::-1]. 
Napíš funkciu prevrat(retazec), ktorá len pomocou cyklu a
zreťazovania prevráti zadaný reťazec. Napríklad:
"""

def prevrat(retazec ):
    prevrateny = ''
    for i in range(len(retazec)-1,-1,-1):
        prevrateny += retazec[i]
    return prevrateny

x = prevrat('tseb eht si nohtyP')
print(x)