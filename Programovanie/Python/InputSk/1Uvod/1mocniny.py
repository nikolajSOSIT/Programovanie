"""
Pomocou operácie ** vieme vypočítať mocniny čísel. Ak je exponentom, napríklad zlomok 1/2, vypočítame takto druhú odmocninu čísla. Zapíš v Pythone:

do premennej a1 priraď druhú odmocninu z 3

do premennej a2 priraď tretinu tretej odmocniny z 5

do premennej a3 priraď piatu mocninu piatej odmocniny z 1024

do premennej a4 priraď desiatu odmocninu z dvadsiatej mocniny 2

Hodnoty týchto štyroch premenných potom vypíš v tvare:

a1 = 1.7320508075688772
"""

a1 = 3 ** (1/2)
a2 = 5 ** (1/3) * (1/3)
a3 = (1024 ** (1/5)) ** 5
a4 = (2 ** 20) ** (1/10)

print(f"a1 = {a1}\na2 = {a2}\na3 = {a3}\na4 = {a4}")