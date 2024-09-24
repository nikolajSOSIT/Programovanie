"""
Napíš funkciu najdlhsi_riadok(meno_suboru), ktorá pre 
zadaný súbor vráti najdlhší riadok (aj s koncovým '\n'). 
Napríklad:
"""

def najdlhsi_riadok(meno_suboru):
    with open(meno_suboru, 'r') as subor:
        najdlhsi = subor.readline()
        for riadok in subor:
            if len(riadok) > len(najdlhsi):
                najdlhsi = riadok
    return repr(najdlhsi)


print(najdlhsi_riadok("Python\InputSk\\7TextovéSúbory\\text3.txt"))

        
