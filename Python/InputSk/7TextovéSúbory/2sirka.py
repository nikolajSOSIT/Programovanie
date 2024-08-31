"""
Napíš funkciu sirka(meno_suboru), ktorá pre zadaný 
súbor zistí dĺžku 
najdlhšieho riadku (aj s koncovym '\n'). Napríklad:
"""

def sirka(meno_suboru):
    subor = open(f"Python\InputSk\\7TextovéSúbory\{meno_suboru}", 'r')
    riadok = subor.readline()
    max = 0
    while riadok:
        if len(riadok) > max:
            max = len(riadok)
        riadok = subor.readline()
    print(max)