"""
Ludolfovo číslo pi rôzni matematici v histórii počítali podľa zaujímavých magických vzorcov.

predpokladaj, že

pi = 3.141592653589793
zisti, ktorý so vzorcov sa k tomuto číslu pi priblížil najviac:

    podiel 223 a 71

    súčet zlomkov 22/17, 37/47 a 88/83

    druhá mocnina 99 lomeno súčin 2206 krát druhá odmocnina z 2

    druhá odmocnina z 5, k tomu plus 6, to celé druhá odmocnina, k tomu plus 7 a to celé opäť druhá odmocnina

    10 na 100 lomeno 11222.11122 a to celé 193 odmocnina

Napríklad podiel 223 a 71 sa od pi líši o 0.0007475831672580924.
"""

pi = 3.141592653589793

pi_1 = 223 / 71
pi_2 = 22/17 + 37/47 + 88/83
pi_3 = (99 ** 2) / (2206 * (2 ** (1/2)))
pi_4 = (((5 ** (1/2) + 6) ** (1/2) + 7) ** (1/2))
pi_5 = (10 ** 100 / 11222.11122) ** (1/193) #Toto je najbližšie

print(f"pi_1 = {pi_1}\npi_2 = {pi_2}\npi_3 = {pi_3}\npi_4 = {pi_4}\npi_5 = {pi_5}")
#odčítanie pi_n od pi
print(f"pi_1 - pi = {pi_1 - pi}\npi_2 - pi = {pi_2 - pi}\npi_3 - pi = {pi_3 - pi}\npi_4 - pi = {pi_4 - pi}\npi_5 - pi = {pi_5 - pi}")