"""
Výpočet pi podľa Liebnizovho vzorca je takýto súčet radu:

4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + 4/13 ...
Napíš program, ktorý vypočíta súčet tohto radu pre prvých n členov. Po spustení môžeš dostať:

zadaj počet: 10
pi = 3.0418396189294032

zadaj počet: 100000
pi = 3.1415826535897198

"""

n = int(input("Zadaj počet: "))
medzi = 1
pi = 0
for i in range(n):
    pi += (4/medzi)*(-1)**i
    medzi += 2
print(f"pi = {pi}")