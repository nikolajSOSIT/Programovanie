"""
Napíš program, ktorý prečíta tri slová a vypíše všetkých 6 rôznych permutácií. Po spustení môžeš dostať:

zadaj 1. slovo: biela
zadaj 2. slovo: modrá
zadaj 3. slovo: červená

biela modrá červená
biela červená modrá
modrá biela červená
modrá červená biela
červená biela modrá
červená modrá biela

"""
slovo1 = input("Zadaj 1 slovo: ")
slovo2 = input("Zadaj 2 slovo: ")
slovo3 = input("Zadaj 3 slovo: ")

print(f"{slovo1} {slovo2} {slovo3}")
print(f"{slovo1} {slovo3} {slovo2}")
print(f"{slovo2} {slovo1} {slovo3}")
print(f"{slovo2} {slovo3} {slovo1}")
print(f"{slovo3} {slovo1} {slovo2}")
print(f"{slovo3} {slovo2} {slovo1}")