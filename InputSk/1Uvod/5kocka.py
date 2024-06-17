"""
Napíš program, ktorý prečíta veľkosť strany kocky
a vypíše dĺžku stenovej a telesovej uhlopriečky
- obe tieto dĺžky zaokrúhli na 2 desatinné miesta
(využiješ funkciu round). Po spustení môžeš dostať:

zadaj veľkosť strany kocky: 18
stenová uhlopriečka je 25.46
telesová uhlopriečka je 31.18

"""

a = int(input("Zadaj veľkosť strany kocky: "))
ts = round(2 **(1/2) * a, 2)
tu = round(3 ** (1/2) * a, 2)
print(f"stenová uhlopriečka je {ts}\ntelesová uhlopriečka je {tu}")

