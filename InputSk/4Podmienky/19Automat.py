"""
Hrací automat mi pri každom zatlačení (hodil som do neho 1 euro) dá 3 náhodné čísla z intervalu <1, 20>. 
Ak sú medzi týmito tromi číslami dve rovnaké, vyhrávam 5 euro, ak sú všetky tri rovnaké vyhrávam 100 euro. 
Začal som s nejakou sumou a hral som maximálne 1000 zatlačení, prípadne som skončil skôr, keď som všetko prehral. 
Napíš program, ktorý to všetko odsimuluje: 
pri každom zatlačení vypíše '+5' alebo '+100', ak som niečo vyhral, alebo '-1', ak som nič nevyhral. 
Napríklad:

začínam so sumou: 20
štart -1-1-1-1-1-1-1+5-1-1-1-1+5-1-1-1-1-1-1-1-1+5-1+5-1-1-1-1-1-1+5-1+5
-1-1-1-1-1-1-1-1-1+5+5-1-1-1-1+5-1-1-1+5-1-1-1+5+5-1-1+5+5-1-1+5-1-1-1-1
-1-1-1-1+5-1-1-1+5-1+5-1-1-1-1+5-1+5-1-1+5-1-1-1-1-1-1-1+5-1+5-1-1-1-1-1
+5-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1+5-1-1-1-1-1+5-1
-1-1-1+5-1-1+5-1-1-1-1-1-1-1-1-1-1-1-1
zostalo mi 0 euro
"""
import random

n = int(input("začínam so sumou: "))
print("štart ", end=" ")

for i in range(1000):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    c = random.randint(1, 20)
    if a == b or a == c or b == c:
        print("+5", end="")
        n += 5
    elif a == b == c:
        print("+100", end="")
        n += 100
    elif a != b!= c:
        print("-1", end="")
        n -= 1
    if n == 0:
        break