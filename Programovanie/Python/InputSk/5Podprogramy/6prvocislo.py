"""
Na prednáške si sa zoznámil s funkciou je_prvocislo(cislo), ktorá pomocou 
funkcie pocet_delitelov(cislo) zisťovala, či je dané cislo prvočíslo. 
Oprav funkciu je_prvocislo(cislo) tak, 
aby nevyužívala pocet_delitelov(cislo), ale vo while-cykle zisťovala, 
či neexistuje aspoň jeden deliteľ v intervale <2, odmocnina>. 
Funkcia sa bude postupne snažiť nájsť takého deliteľa daného čísla, 
ktorého druhá mocnina nie je väčšia ako dané číslo. 
Napríklad, číslo 25 bude postupne deliť 2, 3, 4, 5 
(pre všetky ich druhá mocnina nie je väčšia ako 25) 
a na 5 skončí, lebo delí 25. Číslo 37 sa tiež pokúsi 
deliť 2, 3, 4, 5, 6 (žiadne z nich nie je deliteľom) a keďže pre všetky 
väčšie je ich druhá mocnina väčšia ako 37, vyhlásime 37 za prvočíslo. 
Okrem funkcie je_prvocislo(cislo) 
napíš aj funkciu dvojicky(od, do), ktorá v danom intervale <od, do> 
nájde všetky prvočíselné dvojičky (ich rozdiel je 2). 
Napríklad:
"""

def je_prvocislo(cislo):
    delitel = 1
    pocet = 0
    while (delitel <= cislo**(1/2)):
        if cislo % delitel == 0:
            pocet += 1
        delitel += 1
    return pocet == 1

def dvojicky(od, do):
    for i in range(od, do):
        for j in range(od+2, do):
            if je_prvocislo(i) and je_prvocislo(j) and j-i == 2:
                print(i, j)

dvojicky(3, 50)