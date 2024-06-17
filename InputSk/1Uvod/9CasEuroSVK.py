"""
    Euro je zavedené na Slovensku od 1. januára 2009. Zisti, koľko 
    približne dní od vtedy uplynulo (do dnes uplynulo 12 rokov, 8 mesiacov a 21 dní).
    Predpokladaj, že každý rok má 365 dní a každý mesiac má 30 dní.
    Potom vypočítaj koľko je to hodín a aj sekúnd. Po spustení môžeš dostať:

    počet dní je ????
    počet hodín je ?????
    počet sekúnd je ?????????
"""
#dni = int(input("Vpíš pocet dní: "))
#hodiny = 24*dni
#minuty = hodiny*60
#print(f"Pocet dní: {dni}\n Pocet hodin {hodiny} \n Pocet minut: {minuty}") 


rok = int(input("Vpíš pocet rokov: "))
mesiace = int(input("Vpíš pocet mesiacov"))

mesiace2 = rok*12 + mesiace
dni = mesiace2*30
hodiny = dni *24
sekundy = hodiny*60*60 

print(f"{dni}\n {sekundy}\n {hodiny} ")                                 