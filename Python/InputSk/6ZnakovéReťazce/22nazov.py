"""
Napíš funkciu nazov(n), pomocou ktorej sa bude dať
vygenerovať názov hudobnej skupiny. Chceme, aby toto meno
začínalo a končilo rovnakou samohláskou a medzi týmito 
samohláskami by sa malá n krát objaviť nejaká spoluhláska.
Prvé písmeno mena by malo byť veľké ostatné malé.
Zrejme využiješ ideu z 2. prednášky,
pomocou ktorej sa náhodne generovali písmená. 
Môžeš dostať napríklad:

for i in range(5):
    print(nazov(2))
    print(nazov(3))
Uxxu
Uxxxu
Ippi
Idddi
Atta
Ottto
Yggy
Odddo
Aqqa
Ibbbi
"""
import random


def nazov(n):
    samohlasky = "aeiou"
    spoluhlasky = "bcdfghjklmnpqrstvwxyz"
    vysledok = ""
    samohlaska_ = random.choice(samohlasky)
    vysledok += samohlaska_
    spoluhlaska_ = random.choice(spoluhlasky)	
    vysledok += spoluhlaska_ * n
    vysledok += samohlaska_
    return vysledok.capitalize()


for i in range(5):
    print(nazov(2))
    print(nazov(3))