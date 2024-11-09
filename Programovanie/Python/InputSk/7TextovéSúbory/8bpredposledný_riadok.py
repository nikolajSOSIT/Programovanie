def predposledny_riadok(nazov_suboru):
    with open(f"Python\\InputSk\\7TextovéSúbory\\{nazov_suboru}", 'r') as f:
        return f.readlines()[-2]
    
print(predposledny_riadok("text3.txt"), end="")