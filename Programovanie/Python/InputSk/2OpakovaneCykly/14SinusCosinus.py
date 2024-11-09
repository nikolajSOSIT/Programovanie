"""
Napíš program, ktorý vytvorí takúto tabuľku: pre všetky uhly (v stupňoch) z nejakého daného intervalu 
a kroku vypíše druhé mocniny príslušných sínusov a kosínusov a aj ich súčet. 
Druhé mocniny vypíše na šírku 6 a 4 desatinné miesta, súčet bez udania šírky a počtu desatinných miest. 
Môžeš dostať takýto výstup:

zadaj od: 0
zadaj do: 90
zadaj krok: 10
  0 sin**2=0.0000 cos**2=1.0000 súčet=1.0
 10 sin**2=0.0302 cos**2=0.9698 súčet=0.9999999999999999
 20 sin**2=0.1170 cos**2=0.8830 súčet=1.0
 30 sin**2=0.2500 cos**2=0.7500 súčet=1.0
 40 sin**2=0.4132 cos**2=0.5868 súčet=0.9999999999999999
 50 sin**2=0.5868 cos**2=0.4132 súčet=1.0
 60 sin**2=0.7500 cos**2=0.2500 súčet=1.0
 70 sin**2=0.8830 cos**2=0.1170 súčet=0.9999999999999999
 80 sin**2=0.9698 cos**2=0.0302 súčet=0.9999999999999999
 90 sin**2=1.0000 cos**2=0.0000 súčet=1.0
"""

import math
od = int(input("Zadaj od: "))
do = int(input("Zadaj do: "))
krok = int(input("Zadaj krok: "))

for i in range(od, do+1, krok):
    print(f"{i:3} sin**2={math.sin(i)**2:6.4f} cos**2={math.cos(i)**2:6.4f} súčet={math.sin(i)**2+math.cos(i)**2:6.12f}")