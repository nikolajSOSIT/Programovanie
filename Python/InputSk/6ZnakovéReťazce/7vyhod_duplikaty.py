"""
Napíš funkciu vyhod_duplikaty(retazec), ktorá z daného reťazca vyhodí všetky za sebou idúce opakujúce sa znaky (nechá len jeden z nich). Napríklad:

x = vyhod_duplikaty('Braatisssllavaaaaa')
x
    'Bratislava'
"""

def vyhod_duplikaty(retazec):
    ret = ""
    for i in range (len(retazec)-1):
        if retazec[i]!= retazec[i+1]:
            ret += retazec[i]
        else:
            continue
    ret += retazec[-1]
    return ret


print(vyhod_duplikaty("marrrrtinnnaaaammm"))