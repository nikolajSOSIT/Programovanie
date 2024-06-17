"""
Napíš program, ktorý vygeneruje na číselnej osi dva náhodné body (v intervale <0, 100>) a vypočíta ich vzdialenosť. 
Toto urobí n-krát.
Môžeš dostať takýto výstup:
zadaj n: 6

Prvý bod na priamke je 32, druhý bod 10. Ich vzdialenosť je 22
Prvý bod na priamke je 61, druhý bod 12. Ich vzdialenosť je 49
Prvý bod na priamke je 62, druhý bod 35. Ich vzdialenosť je 27
Prvý bod na priamke je 9, druhý bod 78. Ich vzdialenosť je 69
Prvý bod na priamke je 5, druhý bod 82. Ich vzdialenosť je 77
Prvý bod na priamke je 16, druhý bod 20. Ich vzdialenosť je 4

"""
import random

n = int(input("Zadaj n: "))
for i in range(n):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    print(f"Prvý bod na priamke je {a}, druhý bod {b}. Ich vzdialenosť je {abs(a-b)}")