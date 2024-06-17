"""
Budeš vytvárať dlhý znakový reťazec podobne ako v predchádzajúcej úlohe. Namiesto úsekov hviezdičiek 
budeš do reťazca zapisovať čísla z nejakého intervalu (v tvare '<číslo>'). 
Schéma programu by mala byť podobná predchádzajúcej úlohe. Po spustení môžeš dostať takýto výstup:

zadaj od: 88
zadaj do: 100
<88> <89> <90> <91> <92> <93> <94> <95> <96> <97> <98> <99> <100>
"""

od = int(input("Zadaj od: "))
do = int(input("Zadaj do: "))
for i in range(od, do+1):
    print(f"<{i}>", end=" ")
