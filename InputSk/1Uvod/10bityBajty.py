"""
Do jedného bajtu (8 bitov) môžeme zapísať čísla od 0 do 255. Keď máme dvojbajtovú pamäť, môžeme sem zapísať číslo od 0 až do 256*256-1.
Do trojbajtovej pamäte sa zmestí číslo do 256*256*256-1. Napíš program, ktorému zadáme počet bajtov a ten potom vypíše maximálne číslo,
ktoré sa dá zapísať do takejto pamäte. Program vyskúšaj pre rôzne počty bajtov, napríklad:

zadaj počet bajtov: 4
maximálna hodnota je 4294967295
"""

bajty = int(input("Pocet bajtov:" ))
maxbajt = 256**(bajty)-1
print(maxbajt)