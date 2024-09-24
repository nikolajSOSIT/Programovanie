"""
Reads the first 5 lines from the text3.txt file and prints them to the console.

t = open("Python\InputSk\\7TextovéSúbory\\text3.txt", "r")

for i in range(5):
    riadok = t.readline()
    print(riadok[:-1])

t.close()
"""

t = open("Python\InputSk\\7TextovéSúbory\\text1.txt", "r")
riadok = t.readline()
while riadok != '':
    print(riadok, end="")
    riadok = t.readline()
t.close()