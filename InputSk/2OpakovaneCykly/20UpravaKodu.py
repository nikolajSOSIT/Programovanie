
"""
Oprav tento program tak, aby vypísal túto tabuľku trikrát vedľa seba, napríklad takto:

zadaj n: 5
 1  2  3  4  5     1  2  3  4  5     1  2  3  4  5
 6  7  8  9 10     6  7  8  9 10     6  7  8  9 10
11 12 13 14 15    11 12 13 14 15    11 12 13 14 15
16 17 18 19 20    16 17 18 19 20    16 17 18 19 20
21 22 23 24 25    21 22 23 24 25    21 22 23 24 25
"""

n = int(input('Zadaj n: '))

print()
for i in range(n):
    for j in range(3):
        for k in range(n):
            print(f'{i*n + k + 1:2}', end=' ')
        print('  ', end='')
    print()
print()

