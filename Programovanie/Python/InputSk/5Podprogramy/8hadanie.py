"""
Napíš funkciu hadanie(od, do), pomocou ktorej sa budeš 
vedieť zahrať s počítačom takúto hru: 
počítač si náhodne pomyslí číslo z intervalu <od, do> (neprezradí nám ho) 
a my sa ho budeme na maximálne 10 pokusov snažiť uhádnuť. 
Po každom pokuse nám oznámi,
či náš typ je menší ako jeho číslo alebo väčší. 
Priebeh hry by mohol vyzerať, napríklad takto:

hadanie(1, 100)
    Myslím si číslo, uhádni ho!
    tvoj tip: 50
    *** pridaj
    tvoj tip: 75
    *** pridaj
    tvoj tip: 88
    *** uber
    tvoj tip: 81
    *** uber
    tvoj tip: 78
    *** uber
    tvoj tip: 77
    Uhádol si na 6. pokus. Gratulujem.


hadanie(1, 100)
    Myslím si číslo, uhádni ho!
    tvoj tip: 10
    *** pridaj
    tvoj tip: 20
    *** pridaj
    tvoj tip: 30
    *** pridaj
    tvoj tip: 40
    *** pridaj
    tvoj tip: 50
    *** pridaj
    tvoj tip: 60
    *** uber
    tvoj tip: 59
    *** uber
    tvoj tip: 58
    *** uber
    tvoj tip: 57
    *** uber
    tvoj tip: 56
    *** uber
    Neuhádol si ani na 10 pokusov.
    Myslel som si číslo 54.
"""
import random


def hadanie(od, do):
    cislo = random.randint(od, do)
    pokusy = 1
    x = int(input("tvoj tip: "))
    while (x != cislo):
        if x > cislo:
            print("*** uber")
        elif x < cislo:
            print("*** pridaj")
        x = int(input("tvoj tip: "))
        pokusy += 1
        if pokusy >= 10:
            print(f"Neuhadol si ani na 10 pokus\nMyslel som si cislo {cislo}.")
            break
    if cislo == x:
        print(f"Uhadol si na {pokusy}. pokus. Gratulujeme")
hadanie(1, 100)

