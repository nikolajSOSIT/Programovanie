"""
Máme mince a bankovky s hodnotami 1, 2, 5, 10, 20, 50, 100. Napíš program, ktorý zistí, 
ako sa dá poskladať ľubovoľná suma peňazí minimálnym počtom kusov peňazí. 
Použi len jeden for-cyklus, v ktorom bude jeden if, nejaké priradenia a tiež print. 
Napríklad po spustení:

zadaj cislo: 346
3 krát hodnota 100
2 krát hodnota 20
1 krát hodnota 5
1 krát hodnota 1
"""

suma = int(input("zadaj cislo: "))
for i in [100, 50, 20, 10, 5, 2, 1]:
    pocet = suma // i
    if pocet > 0:
        print(f"{pocet} krát hodnota {i}")
        suma -= pocet * i