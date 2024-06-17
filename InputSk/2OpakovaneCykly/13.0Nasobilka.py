"""
Napíš program, ktorý vytvorí tabuľku násobenia, podobnú malej násobilke. 
Násobiť sa budú čísla z nejakého daného intervalu: 
v prvom riadku (aj stĺpci) sú násobky prvého čísla, v druhom druhého, atď. 
Môžeš dostať takýto výstup:

zadaj od: 8
zadaj do: 13
  64   72   80   88   96  104
  72   81   90   99  108  117
  80   90  100  110  120  130
  88   99  110  121  132  143
  96  108  120  132  144  156
 104  117  130  143  156  169

"""

od = int(input("Zadaj od: "))
do = int(input("Zadaj do: "))
for i in range(od, do+1):
    for j in range(od, do+1):
        print(f"{i*j:3}", end=" ")
    print()