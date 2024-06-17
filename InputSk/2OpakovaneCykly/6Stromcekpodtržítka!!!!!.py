"""Aj v tejto úlohe treba napísať program, ktorý vytvorí pyramídu z hviezdičiek, 
len z hviezdičiek bude len obvod trojuholníka, vnútro trojuholníka bude zo znakov mínus ('-'). 
Môžeš dostať takýto výstup:


zadaj n: 7
      *
     *-*
    *---*
   *-----*
  *-------*
 *---------*
*************
"""

n = int(input("Zadaj n:"))

print(" "*(n) + "*")

index = 1
for i in reversed(range(n-1)):
    print(" "*(i+1) + "*" + "-"*index + "*")
    index +=2

print("*"*(n*2+1))