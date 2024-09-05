"""
Napíš funkciu najdlhsi_riadok(meno_suboru), ktorá pre 
zadaný súbor vráti najdlhší riadok (aj s koncovým '\n'). 
Napríklad:
"""

def najdlhsi_riadok(meno_suboru):
    with open(meno_suboru, "r") as t:
        maxi = 0
        vysled = ""
        len_ = len(t.readline)
        if maxi > len(t.readline()):
            maxi = maxi
        else:
            vysled = repr(t.readline())
            maxi = len(vysled)
        t.close()
    return vysled


print(najdlhsi_riadok("Python\InputSk\\7TextovéSúbory\\text1.txt"))

        
