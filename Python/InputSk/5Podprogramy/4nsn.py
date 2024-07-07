"""
Na prednáške si sa zoznámil s funkciou nsd(a, b), 
ktorá počítala najväčší spoločný deliteľ dvoch čísel. 
Inšpiruj sa touto funkciou a napíš funkciu nsn(a, b), ktorá 
vypočíta najmenší spoločný násobok dvoch čísel. Napríklad pre volania:

a, b = 129, 162
print(f'nsn({a}, {b}) =', nsn(a, b))
a, b = 60, 168
print(f'nsn({a}, {b}) =', nsn(a, b))
dostaneme výstup:

nsn(129, 162) = 6966
nsn(60, 168) = 840

"""

def nsn(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           nsn = greater
           break
       greater += 1

   return nsn
    
a, b = 129, 162
print(f'nsn({a}, {b}) =', nsn(a, b))
a, b = 60, 168
print(f'nsn({a}, {b}) =', nsn(a, b))