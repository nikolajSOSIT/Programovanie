"""
Napíš program, ktorý zadané číslo rozloží na prvočinitele 
(vyjadrí ho ako súčin prvočísel). 
Tento rozklad zapíš v tvare rovnosti s násobením:

zadaj číslo: 60
60 = 2 * 2 * 3 * 5
zadaj číslo: 1001
1001 = 7 * 11 * 13

V programe bude while-cyklus, v ktorom budeš postupne 
skúšať deliť zadané číslo rôznymi deliteľmi: 
ak je číslo týmto deliteľom deliteľné, 
tak ho vypíšeš a samotné číslo vydelíš týmto deliteľom, 
inak deliteľ zvýšiš o 1 a celé sa to opakuje.
"""
delitel = 2
cislo = int(input("zadaj číslo: "))

print(f"{cislo} =", end=" ")
while cislo > 1:
    if cislo == delitel:
        print(cislo)
        break
    elif cislo % delitel == 0:
        print(f"{delitel} *", end=" ")
        cislo = cislo // delitel
    else:
        delitel += 1

