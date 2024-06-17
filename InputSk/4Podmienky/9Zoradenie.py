"""
Žiaci sú v rade zoradení podľa veľkosti (od najmenšieho). 
Napíš program, ktorému najprv postupne oznamujeme (pomocou input) 
výšky žiakov a ten na záver (zadali sme „prázdnu“ výšku) vypíše, 
či boli zoradení správne. 
Použi príkaz while (dopredu nepoznáme počet žiakov), 
v ktorom bude príkaz if. 
Mali by fungovať takéto spustenia programu:

zadávaj výšky žiakov
   výška 1. žiaka: 100
   výška 2. žiaka: 110
   výška 3. žiaka: 110
   výška 4. žiaka: 120
   výška 5. žiaka:
všetci žiaci sú zoradení správne
zadávaj výšky žiakov
   výška 1. žiaka: 100
   výška 2. žiaka: 120
   výška 3. žiaka: 110
   výška 4. žiaka: 140
   výška 5. žiaka: 145
   výška 6. žiaka:
žiaci nie sú správne zoradení
zadávaj výšky žiakov
   výška 1. žiaka: 180
   výška 2. žiaka:
všetci žiaci sú zoradení správne
"""
oldMaxH = 0
pocet = 1
sorted = True

print("zadávaj výšky žiakov")

while True:
    vyska = input(f"   Zadaj {pocet}. vysku: ")
    if vyska.isnumeric():
        vyska = int(vyska)
    else:
        break
    if vyska >= oldMaxH:
        oldMaxH = vyska
    else:
        sorted = False
    pocet += 1

if sorted:
    print("žiaci sú zoradení správne")
else:
    print("žiaci nie sú zoradení správne")  