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
    retazec = retazec.split('+')
    x = 0
    for i in range(len(retazec)):
        x += int(retazec[i])
    return x

x = sucet('1+2+3+4+5+6')
print(x)