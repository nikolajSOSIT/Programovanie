def vypis_do_ramiku(meno_suboru):
    with open(f"Python/InputSk/7TextovéSúbory/{meno_suboru}", "r") as subor:
        riadokList = subor.readlines()
    maxLen = len(max(riadokList, key=len))
    print("*" * int(maxLen+3))
    for i in riadokList:
        veta = i.replace("\n", "")
        pocet_medzier = maxLen - len(i)
        print(f"* {veta}{pocet_medzier*" "}*")
    print("*" * int(maxLen+3)) 

vypis_do_ramiku("text1.txt")
