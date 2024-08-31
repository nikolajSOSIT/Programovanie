"""
Napíš program, ktorý si vypýta meno súboru a z tohto 
súboru vypíše druhý riadok uzavretý v apostrofoch. Z tohto
riadku ešte vypíše prvé slovo (je ukončené medzerou) 
a počet výskytov medzier v tomto riadku. Napríklad:
"""

def fun(nazov):
    subor = open(f"Python\InputSk\\7TextovéSúbory\{nazov}", 'r')
    for i in range(2):
        riadok = subor.readline()
        if i == 1:
            print(f"'{riadok.strip()}'")
            riadok = riadok.strip()
            slova = riadok.split(' ')
            print(slova[0])
            print(riadok.count(' '))


nazov = input('Zadaj meno suboru: ')
fun(nazov)