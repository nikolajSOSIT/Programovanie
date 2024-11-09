def zlomky(meno_suboru):
    text = ""
    sucet = 0
    pocet = 0
    with open(f"Python/InputSk/7TextovéSúbory/{meno_suboru}", "r") as subor:
        text = subor.read().split()
    for i in text:
        if "/" in i:
            t = i.split("/")
            sucet += int(t[0])/int(t[1])
        else:
            sucet += float(i)
        pocet += 1
    print(f"pocet = {pocet}")
    print(f"sucet = {sucet:2.2f}")
    print(f"priemer = {sucet/pocet:2.2f}")

    
zlomky("cisla.txt")

        
    