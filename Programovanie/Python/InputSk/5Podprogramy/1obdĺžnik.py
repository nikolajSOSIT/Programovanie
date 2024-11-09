"""
Napíš funkciu obdlznik(sirka, znak='*'), ktorá z daného znaku znak 
vypíše do troch riadkov výstupu obdĺžnik zadanej šírky. 
Napríklad pre volania:

obdlznik(30, '#')
obdlznik(6)
obdlznik(19, 'O')

dostaneme výstup:

##############################
#                            #
##############################

******
*    *
******

OOOOOOOOOOOOOOOOOOO
O                 O
OOOOOOOOOOOOOOOOOOO
"""

def obdlznik(sirka, znak='*'):
    for i in range(sirka):
        print(znak, end="")
    print()
    print(f"{znak}{(sirka-2) * ' '}{znak}")
    for i in range(sirka):
        print(znak, end="")

obdlznik(30)
