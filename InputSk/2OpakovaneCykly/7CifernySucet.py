"""
Celé číslo môžeme rozobrať na jednotlivé cifry tak, že ho najprv prevedieme na reťazec 
a potom vo for-cykle každú cifru (ako znak) zvlášť prevedieme na číslo. 
Napíš program, ktorý prečíta celé číslo, rozoberie ho na cifry,
tieto vypíše aj s poradovým číslom a zistí ich súčet. Takýto súčet voláme ciferný súčet. 
Po spustení dostaneš, napríklad:

zadaj číslo: 784
1. cifra 7
2. cifra 8
3. cifra 4
ciferný súčet je 19

zadaj číslo: 1003
1. cifra 1
2. cifra 0
3. cifra 0
4. cifra 3
ciferný súčet je 4

"""

cif_sucet = 0
cislo = input("Zadaj číslo: ")
poradie = 1
for i in cislo:
    print(f"{poradie}. cifra {i}")
    poradie += 1
    cif_sucet += int(i)
print(f"Ciferný súčet je {cif_sucet}")