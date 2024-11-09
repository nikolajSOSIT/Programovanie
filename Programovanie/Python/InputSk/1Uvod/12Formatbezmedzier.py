"""
Napíš program, ktorý prečíta dve celé čísla (napríklad 27 a 342) a vypíše ich v tvare takejto 
rovnosti: 27+342=369, teda bez medzier. Použi na to formátovaciu šablónu 
f'...{hodnota}...'. Po spustení teda môžeš dostať:



zadaj 1. číslo: 27
zadaj 2. číslo: 342
27+342=369


alebo

zadaj 1. číslo: 8
zadaj 2. číslo: 999997
8+999997=1000005


"""
cislo1 = int(input("zadaj cislo prve: "))
cislo2 = int(input("Zadaj cislo dva: "))
cisloX = cislo1 + cislo2
print(f"{cislo1}+{cislo2}={cisloX}")