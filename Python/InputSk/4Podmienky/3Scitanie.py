"""
Napíš program,
ktorý číta desatinné čísla zo vstupu a keď zadáme 0,
čítanie čísel zo vstupu skončí
a program vypíše súčet všetkých týchto čísel. 
Použi while-cyklus. 
Napríklad po spustení:

zadaj 1. číslo: 17
zadaj 2. číslo: 3.14
zadaj 3. číslo: -9.8
zadaj 4. číslo: 6
zadaj 5. číslo: 0
súčet všetkých prečítaných čísel je 16.34

"""

sucet = 0 
pocet = 1
cislo = 1

while cislo!= 0:
    cislo = float(input(f"zadaj {pocet}. číslo: "))
    sucet += float(cislo)
    pocet += 1
print("súčet všetkých prečítaných čísel je", sucet)