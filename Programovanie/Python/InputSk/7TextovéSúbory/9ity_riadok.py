def ity_riadok(meno_suboru, index):
    with open(f"Python\\InputSk\\7TextovéSúbory\\{meno_suboru}", "r") as subor:
        cele = subor.readlines()
        print(cele)
        if len(cele) > index >= 0:
            return repr(cele[index])
        else:
            return "''"
        

print(ity_riadok("text3.txt", 3))