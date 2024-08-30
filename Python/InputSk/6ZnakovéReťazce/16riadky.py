"""
Napíš funkciu riadky(retazec), ktorá vypíše daný viacriadkový reťazec, 
ale pritom každý riadok očísluje číslami od 1 do počet riadkov. 
Napríklad:

riadky('prvy riadok\n\ntreti je posledny')
    1. prvy riadok
    2.
    3. treti je posledny
riadky('len \\n jeden riadok')
    1. len \n jeden riadok
"""


def riadky(retazec):
    riadky = retazec.split('\n')
    for i in range(len(riadky)):
        print(f'{i+1}. {riadky[i]}')

riadky('len \\n jeden riadok')
