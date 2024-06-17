"""
Budeme konštruovať takúto postupnosť celých čísel:

začneme zadaným číslom n

ak je párne, vydelíme ho 2

inak sa vynásobí 3 a pripočíta 1

toto sa opakuje, kým nedostaneme číslo 1

Napíš program, ktorý pre dané štartové číslo vypíše takto skonštruovanú postupnosť. Napríklad:

zadaj číslo: 44
44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
"""

n = int(input('zadaj číslo: '))
while n!= 1:
    if n % 2 == 0:
        n /= 2
    else:
        n = n * 3 + 1
    print(n, end=', ')