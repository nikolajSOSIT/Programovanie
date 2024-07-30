"""
Napíš funkciu stvorec(n, znak), ktorá vráti jeden dlhý znakový 
reťazec. Znakový reťazec by po vypísaní pomocou print vytvoril 
obvod štvorca z daného znaku. Môžeš predpokladať, že n nebude 
menšie ako 2. Napríklad:

r = stvorec(5, '#')
r
    '#####\n#   #\n#   #\n#   #\n#####'
print(r)
    #####
    #   #
    #   #
    #   #
    #####
Pokús sa to vyriešiť tak, že telo funkcie bude obsahovať jediný
riadok return:

def stvorec(n, znak):
    return ...
"""

def stvorec(n, znak):
    return znak * n + "\n" + (n-2) * (znak + (" " * (n-2)) + f'{znak}\n') + znak * n

print(stvorec(8, '#'))