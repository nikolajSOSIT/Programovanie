"""
Podobný príklad predchádzajúcemu, lenže teraz budeme hádzať ľubovoľným počtom kociek: 
Napíš program, ktorý si najprv vypýta n (počet hádzaní) a počet kociek. 
Potom n-krát vypíše čísla na kockách a ich súčet. 
Môžeš dostať takýto výstup:

zadaj n: 3
zadaj počet kociek: 4
na 1. kocke padla 3
na 2. kocke padla 2
na 3. kocke padla 2
na 4. kocke padla 2
ich súčet je 9
======================
na 1. kocke padla 4
na 2. kocke padla 6
na 3. kocke padla 1
na 4. kocke padla 5
ich súčet je 16
======================
na 1. kocke padla 1
na 2. kocke padla 4
na 3. kocke padla 6
na 4. kocke padla 3
ich súčet je 14
======================

"""
import random

n = int(input("Zadaj n: "))
pocet = int(input("Zadaj počet kociek: "))
sucet = 0
for i in range(n):
    for j in range(pocet):
        kocka = random.randint(1, 6)
        print(f"na {j+1}. kocke padla {kocka}")
        sucet += kocka
    print(f"ich súčet je {sucet}")
    print("="*20)
    sucet = 0