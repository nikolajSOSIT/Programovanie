"""
Na prednáške si sa zoznámil s funkciou fibonacci(n), 
ktorá počítala n-tý člen fibonacciho postupnosti. 
Napíš funkciu fibonacci_medzi(od, do), ktorá vypíše (pomocou print) 
všetky fibonacciho čísla z daného intervalu <od, do>. 
Táto funkcia by mala obsahovať len jeden while-cyklus
(okrem priradení a if). 
Napríklad pre volania:

fibonacci_medzi(10, 100)
fibonacci_medzi(1000, 3000)
dostaneme výstup:

13 21 34 55 89
1597 2584
"""

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end = ' ')
        a, b = b, a + b

def fibonacci_medzi(od, do):
    a, b = 0, 1
    while(a <= do):
        if(a >= od):
            print(a, end = ' ')
        a, b = b, a + b
    print()

fibonacci_medzi(10, 100)
fibonacci_medzi(1000, 3000)