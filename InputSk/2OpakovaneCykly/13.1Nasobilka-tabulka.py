"""
Do výpisu tabuľky pridaj prvý stĺpec aj riadok navyše s číslami z daného intervalu, napríklad v takomto tvare:

zadaj od: 8
zadaj do: 13
     |    8    9   10   11   12   13
=====|===============================
   8 |   64   72   80   88   96  104
   9 |   72   81   90   99  108  117
  10 |   80   90  100  110  120  130
  11 |   88   99  110  121  132  143
  12 |   96  108  120  132  144  156
  13 |  104  117  130  143  156  169

"""




od = int(input("Zadaj od: "))
do = int(input("Zadaj do: "))
print(4*" ", end="|")
for u in range(od, do+1):
    print(f"{u:3}", end=" ")
print()
print("====|" + od*"=")
for i in range(od, do+1):
    print(f"{i:3} ", end="|")
    for j in range(od, do+1):
        print(f"{i*j:3}", end=" ")
    print()