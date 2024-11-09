"""
Napíš funkciu postupnost(start, koniec), ktorá vytvorí znakový
reťazec z postupnosti čísel range(start, koniec). Čísla v tejto
postupnosti budú oddelené znakom medzera ' '. Napríklad:

p = postupnost(5, 13)
p
    '5 6 7 8 9 10 11 12'
Do funkcie pridaj ešte jeden parameter postupnost(start, koniec,
krok=1) tak, aby fungovalo napríklad:

p = postupnost(13, 5, -2)
p
    '13 11 9 7'
"""

def postupnost(start, koniec, krok=1):
    p = ''
    for i in range(start, koniec, krok):
        p += str(i) + ' '
    return p

p = postupnost(13, 5, -2)
print(p)