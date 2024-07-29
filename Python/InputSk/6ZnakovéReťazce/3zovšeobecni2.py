"""
Napíš funkciu sucet(retazec), ktorá dostáva znakový reťazec
s dvomi celými číslami oddelenými znakom '+'. Funkcia vráti
(nič nevypisuje) celé číslo, ktoré je súčtom dvoch čísel v 
reťazci. Použi rezy, metódu retazec.find('+') a funkciu int().
Napríklad:

x = sucet('12+9')
x
    21
sucet('987654321+99999')
    987754320

"""

def sucet(retazec):
    x = retazec.find('+')
    y = int(retazec[:x]) + int(retazec[x+1:])
    print(y)