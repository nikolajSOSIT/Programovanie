"""
V jednom starodávnom príbehu sa na políčka šachovnice kládli zrniečka ryže: na 1. políčko
1 zrnko ryže, na ďalšie 2, na každom ďalšom je dvojnásobok predchádzajúceho. 
Napíš program, ktorý vypíše, koľko zrniek bude na n-tom políčku. Po spustení môžeš dostať:
"""

n = int(input("Napíš kolkate policko tyneger: "))

pocet_zrniek = 2**(n-1)
print(f"{pocet_zrniek}")