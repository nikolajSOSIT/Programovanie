"""
Napíš funkciu usporiadaj(h1, h2, h3),
ktorá z troch zadaných hodnôt
(všetky tri sú rovnakého typu, napríklad reťazce) 
vytvorí reťazec (vráti ho ako výsledok funkcie)
zlepením týchto troch hodnôt v utriedenom poradí:
najprv najmenšia (napríklad reťazec prvý v abecede),
potom väčšia a na koniec najväčšia.
Medzi zlepené reťazce vloží medzeru.
Napríklad:

x = usporiadaj('python', 'pytliak', 'pytagoras')
x
    'pytagoras python pytliak'
usporiadaj(345, 123, 234)
    '123 234 345'
"""

def usporiadaj(h1, h2, h3):
    foo = sorted([h1, h2, h3])
    x = " ".join(foo)
    return x

x = usporiadaj('python', 'pytliak', 'pytagoras')
print(x)