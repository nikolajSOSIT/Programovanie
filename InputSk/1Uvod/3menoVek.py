"""
Napíš program, ktorý pomocou príkazu input 
prečíta meno študenta a jeho vek. 
Potom to vypíše pomocou príkazu print a tiež 
vypíše informáciu jeho veku o rok a aj o 10 rokov. 
Po spustení programu môžeš dostať takýto výpis:

zadaj meno: Ema
zadaj vek: 17
Ema má 17 rokov
Ema bude mať o rok 18
Ema bude mať o 10 rokov 27

"""
meno = input("Zadaj meno: ")
vek = int(input("Zadaj vek: "))
print(f"{meno} má {vek} rokov")
print(f"{meno} bude mať o rok {vek + 1}")
print(f"{meno} bude mať o 10 rokov {10 + vek}")
