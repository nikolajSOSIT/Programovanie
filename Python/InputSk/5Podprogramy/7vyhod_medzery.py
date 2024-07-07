"""
Napíš funkciu vyhod_medzery(text), 
ktorá zo zadaného textu vyhodí všetky medzery. 
Nepoužívaj žiadne funkcie ani operácie s reťazcami, 
ktoré sme sa ešte neučili. 
Funkcia nič nevypisuje, ale pomocou return vráti nový reťazec. 
Otestuj ju s rôznymi hodnotami parametrov. Napríklad:

vyhod_medzery('  mám   rád Python ')
    'mámrádPython'
vyhod_medzery('      ')
    ''
"""

def vyhod_medzery(text):
    product = ""
    for x in text:
        if x == " ":
            product += ""
        else:
            product += x
    print(product)

vyhod_medzery('  mám   rád Python ')
vyhod_medzery('      ')
