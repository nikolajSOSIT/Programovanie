"""
Napíš program, ktorý prečíta polomer kruhu
a vypíše obvod a obsah tohto kruhu. 
Môžeš predpokladať, že pi = 3.14159. 
Po spustení môžeš dostať:

zadaj polomer: 10
obvod je 62.8318
obsah je 314.159
"""

pi = 3.14159

r = int(input("Zadaj polomer: "))
print(f"obvod je {2 * pi * r}\nobsah je {pi * r ** 2}")