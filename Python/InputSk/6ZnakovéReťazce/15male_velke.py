"""
Napíš funkcie male(retazec, i) a velke(retazec, i),
ktoré i-te písmeno v reťazci prerobia na malé (resp. veľké).
Napríklad:

r = male('PYTHON', 3)
r
    'PYThON'
r = velke('python', 5)
r
    'pythoN'
"""

def male(retazec, i):
    return retazec[:i] + retazec[i].upper() + retazec[i+1:]

def velke(retazec, i):
    return retazec[:i] + retazec[i].lower() + retazec[i+1:]

r = velke('PYTHON', 3)
print(r)

r = male('python', 5)
print(r)