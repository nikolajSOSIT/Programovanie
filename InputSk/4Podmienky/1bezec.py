"""
Športovec prvý deň prebehol x kilometrov. Každý ďalší deň prebehol o 10% viac ako v predchádzajúci deň. 
Napíš program, ktorý pre dané y zistí, v ktorý deň športovec dokopy prebehne aspoň y kilometrov. 
Napríklad, po spustení môžeš dostať:

zadaj km pre prvý deň: 10
zadaj cieľové km: 20
na 9. deň prebehne 21.44 km

zadaj km pre prvý deň: 100
zadaj cieľové km: 121
na 3. deň prebehne 121.00 km
"""
x = int(input('zadaj km pre prvý deň: '))
y = int(input('zadaj cieľové km: '))
pocet_dni = 1
while x < y:
    x += x * 0.1
    pocet_dni += 1
print(f"na {pocet_dni}. deň prebehne {x:.2f} km")
