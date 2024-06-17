"""
Napíš program, ktorý prečíta nejaké (aspoň štvorciferné) celé číslo. Potom do štyroch riadkov postupne vypíše:

číslo celočíselne delené 10 a zvyšok po delení 10

číslo celočíselne delené 100 a zvyšok po delení 100

číslo celočíselne delené 1000 a zvyšok po delení 1000

číslo celočíselne delené 10000 a zvyšok po delení 10000

Takto vieme rozložiť dané číslo na dve časti. Po spustení môžeš dostať:

Očakávaný výsledok:

zadaj číslo: 98765
9876 5
987 65
98 765
9 8765

zadaj číslo: 2743
274 3
27 43
2 743
0 2743

slovo = input() - string("slovo")
cislo = int(input()) - input ako cislo, povolené znaky 0123456789.

celociselné delenie cislo // n (25 // 3) = 8 
zvyšok po delení % cislo % n (25 % 3) = 1

formátovanie pri výpise: print(f"{premenná}, abcedefcn, {premenná}")
"""
cislo = int(input("Zadaj cislo: "))

print(f"{cislo // 10} {cislo % 10}")   #9876 5

print(f"{cislo // 100} {cislo % 100}") #987 65

print(f"{cislo // 1000} {cislo % 1000}") #98 765

print(f"{cislo // 10000} {cislo % 10000}") #9 8765
