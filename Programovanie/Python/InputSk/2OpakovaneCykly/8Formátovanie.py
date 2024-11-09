"""
Napíš program, ktorý vyrobí jeden dlhý znakový reťazec, zložený z úsekov hviezdičiek oddelených medzerami: 
na začiatku je 1 hviezdička (znak '*'), za ňou medzera, potom 2 hviezdičky a medzera, 3 hviezdičky a medzera … 
Počet hviezdičkových úsekov je n. Program by mal mať takúto schému:

n = ...
retazec = ''
for ...:
    ...
print(retazec)

zadaj n: 10
* ** *** **** ***** ****** ******* ******** ********* **********
"""
n = int(input("Zadaj n: "))
for i in range(1, n+1):
    print(f"{"*" * i}", end=" ")
    
