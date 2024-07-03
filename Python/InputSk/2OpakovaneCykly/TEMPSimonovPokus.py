n = int(input("Zadaj n:"))

print(" "*(n) + "*")

index = 1
for i in reversed(range(n-1)):
    print(" "*(i+1) + "*" + "-"*index + "*")
    index +=2

print("*"*(n*2+1))



"""""
n = int(input("Zadaj n(počet hviezdičiek: "))
for i in range(1, n+1):
    print(f"{" " * (n-i)} {'*' * (2*i-1)}")
"""