"""
Budeme simulovať hádzanie dvomi hracími kockami. 
Zakaždým vypíšeme aj ich súčet. 
Napíš program, ktorý to simuluje n-krát. 
Môžeš dostať takýto výstup:
zadaj n: 4
na 1. kocke padla 1
na 2. kocke padla 4
ich súčet je 5
======================
na 1. kocke padla 4
na 2. kocke padla 5
ich súčet je 9
======================
na 1. kocke padla 6
na 2. kocke padla 1
ich súčet je 7
======================
na 1. kocke padla 4
na 2. kocke padla 1
ich súčet je 5
======================
"""
import random

n = int(input("Zadaj n: "))
for i in range(n):
    kocka1 = random.randint(1, 6)
    kocka2 = random.randint(1, 6)
    print(f"na {1}. kocke padla {kocka1}")
    print(f"na {2}. kocke padla {kocka2}")
    print(f"ich súčet je {kocka1+kocka2}")
    print("="*20)