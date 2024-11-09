def pocet_slov(meno_suboru):
    t = open(f"Python/InputSk/7TextovéSúbory/{nazov}")
    print(len(t.read().split()))

def vypis_slova(meno_suboru):
    t = open(f"Python/InputSk/7TextovéSúbory/{nazov}")
    print(t.read().replace(" ", "\n"))


vypis_slova("text3.txt")