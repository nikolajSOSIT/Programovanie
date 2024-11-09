"""
Napíš program, ktorý vypíše cifry zadaného čísla postupným 
delením desiatimi, teda vo while-cykle vypíšeš 
poslednú cifru (číslo % 10) a pritom ešte samotné číslo vydelíš 10. 
Súčasne každú túto cifru pripočítaš do počítadla cs (ciferný súčet). 
Môžeš dostať takýto výstup:

zadaj číslo: 4132
2
3
1
4
ciferný súčet = 10
"""

n = int(input("zadaj číslo: "))
sucet = 0

while n > 0:
    print(n % 10)
    sucet += n % 10
    n = n // 10
print(f"ciferný súčet = {sucet}")