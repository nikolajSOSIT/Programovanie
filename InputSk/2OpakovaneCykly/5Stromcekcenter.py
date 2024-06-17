"""
Napíš program, ktorý z hviezdičiek vytvorí takúto pyramídu:

v prvom riadku je najprv n-1 medzier a potom jedna hviezdička

v každom ďalšom riadku je o jednu medzeru menej a o dve hviezdičky viac

Môžeš dostať takýto výstup:

zadaj n: 7
      *
     ***
    *****
   *******
  *********
 ***********
*************

"""

n = int(input("Zadaj n(počet hviezdičiek: "))
for i in range(1, n+1):
    print(f"{" " * (n-i)} {'*' * (2*i-1)}")