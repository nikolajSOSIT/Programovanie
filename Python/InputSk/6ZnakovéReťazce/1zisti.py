"""
Ručne bez počítača zisti, čo sa vypíše:

x, y = 'Bratislava', 'Košice'
y[1] + x[4] + y[3] + x[-4] + y[-5]
    #oiilo
x[5:8] + 3 * x[3] + y[2:]
    #slatttšice
y[:2] + x[-2:]
    #Kova
x[1::2] + y[2::2] + x[2::3]
    ...
x.replace('a', 'e') + y.replace('ic', 'm')
    ...
(y + x).replace('i', '').replace('a', 'xa')
    ...
Potom to skontroluj pomocou Pythonu
"""