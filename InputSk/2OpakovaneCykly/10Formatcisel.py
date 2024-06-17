"""
Napíš program, ktorý vypíše naformátovanú tabuľku mocnín celých čísel z nejakého daného intervalu. 
Prvý stĺpec tabuľky obsahuje číslo, 
v druhom je druhá mocnina tohto čísla,
v treťom tretia,
vo štvrtom štvrtá. 
Môžeš dostať takýto výstup:

zadaj od: 95
zadaj do: 103
 95   9025   857375   81450625
 96   9216   884736   84934656
 97   9409   912673   88529281
 98   9604   941192   92236816
 99   9801   970299   96059601
100  10000  1000000  100000000
101  10201  1030301  104060401
102  10404  1061208  108243216
103  10609  1092727  112550881
"""

od = int(input("Zadaj od: "))
do = int(input("Zadaj do: "))
for i in range(od, do+1):
    print(f"{i:3}  {i**2:6}  {i**3:9}  {i**4:12}")