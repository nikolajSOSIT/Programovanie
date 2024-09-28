"""
Napíš funkciu tri_slova(meno_suboru), ktorá pre zadaný súbor 
vypíše všetky tie riadky súboru, ktoré obsahujú práve tri slová.
V každom riadku je niekoľko slov, ktoré sú oddelené jednou medzerou. 
Napríklad:

tri_slova('text1.txt')
    Od ucenia este
tri_slova('text2.txt')
tri_slova('text3.txt')
    Stoji stoji mohyla
    na mohyle trnie
    rastie kvety rozvija
    jedna zlta lalija

"""

def tri_slova(meno_suboru):
    t = open(meno_suboru, "r")
    riadok = t.readline()
    while riadok != '':
        slova = riadok.split()
        if len(slova) == 3:
            print(riadok, end="")
        riadok = t.readline()
    t.close()

tri_slova("Python/InputSk/7TextovéSúbory/text3.txt")