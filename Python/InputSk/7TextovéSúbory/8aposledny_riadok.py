def posledny_riadok(subor):
    with open(f"Python\\InputSk\\7TextovéSúbory\\{subor}", 'r') as f:
        return f.readlines()[-1]
    
print(posledny_riadok("text3.txt"))