"""
Napíš funkciu rozsekaj(text, sirka), ktorá vypíše zadaný
text do viacerých riadkov, pričom každý (možno okrem posledného)
má presne sirka znakov. Napríklad:

ret = rozsekaj('Anicka dusicka, kde si bola', 10)
ret
    'Anicka dus\nicka, kde \nsi bola'
print(ret)
    Anicka dus
    icka, kde
    si bola
"""

def rozsekaj(text, sirka):
    ret = ''
    for i in range(len(text)):
        if i % sirka == 0 and i!= 0:
            ret += '\n'
        ret += text[i]
    return ret

print(rozsekaj('Anicka dusicka, kde si bola', 10))
