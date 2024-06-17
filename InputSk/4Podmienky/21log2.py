"""
Dvojkový logaritmus môžeme počítať pomocou funkcie math.log2(cislo), ale vieme na to použiť aj 
algoritmus z prednášky, ktorý delením intervalu na polovice počítal druhú odmocninu. 
Napíš program, ktorý to s nejakou presnosťou vypočíta takýmto algoritmom. Napríklad po spustení:

zadaj číslo: 1000
logaritmus 1000.0 je 9.965784382075071
"""

#Simon

logaritmus = int(input())
index = 0
while 2 ** index <= logaritmus:
    index += 0.0001
print(f"log2 {logaritmus} = {index}")

#Nikolaj

cislo = int(input('zadaj číslo: '))
x = 0
while 2 ** x < cislo:
    x += 0.0001
print('log', cislo, 'je', x)