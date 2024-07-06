"""
Napíš funkciu riadok(n, text=''), ktorá vypíše n znakový reťazec 
hviezdičiek '*', stred ktorého nahradí zadaným textom. 
Ak je tento zadaný text neprázdny, vloží na jeho začiatok aj koniec medzeru. 
Napríklad pre volania:

sir = 40
riadok(sir)
riadok(sir, 'Ján Botto')
riadok(sir, 'Žltá ľalija')
riadok(sir, '-')
riadok(sir, 'Stojí stojí mohyla')
riadok(sir, 'Na mohyle zlá chvíľa')
riadok(sir, 'na mohyle tŕnie chrastie')
riadok(sir, 'a v tom tŕní chrastí rastie')
riadok(sir)
dostaneme výstup:

****************************************
************** Ján Botto ***************
************* Žltá ľalija **************
****************** - *******************
********** Stojí stojí mohyla **********
********* Na mohyle zlá chvíľa *********
******* na mohyle tŕnie chrastie *******
***** a v tom tŕní chrastí rastie ******
****************************************
"""
import math

def riadok(n, text=''):
    if text != '':
        text = ' ' + text + ' ' 
    n -= 2 + len(text)+1
    print(f"{'*' * (math.floor(n/2))}{text}{'*' * (math.ceil(n/2))}")

sir = 40
riadok(sir)
riadok(sir, 'Ján Botto')
riadok(sir, 'Žltá ľalija')
riadok(sir, '-')
riadok(sir, 'Stojí stojí mohyla')
riadok(sir, 'Na mohyle zlá chvíľa')
riadok(sir, 'na mohyle tŕnie chrastie')
riadok(sir, 'a v tom tŕní chrastí rastie')
riadok(sir)
