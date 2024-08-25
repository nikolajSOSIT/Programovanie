"""
Napíš funkciu ozatvorkuj(retazec, podretazec), ktorá v zadanom reťazci retazec všetky výskyty daného podreťazca ozátvorkuje. Napríklad:

b = ozatvorkuj('Bratislava', 'a')
b
    'Br(a)tisl(a)v(a)'
ozatvorkuj('prospešné programovanie v prologu', 'pro')
    '(pro)spešné (pro)gramovanie v (pro)logu'
"""

def ozatvorkuj(retazec, podretazec):
    return retazec.replace(podretazec, '(' + podretazec + ')')

print(ozatvorkuj('Bratislava', 'a'))