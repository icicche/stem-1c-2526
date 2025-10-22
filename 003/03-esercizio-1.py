# 003/03
# Esercizio

lista_parole = [
    "tavolo",
    "sedia",
    "asciugamano",
    "muraglia",
    "zebra",
    "matematica",
    "intersezione",
    "eco",
    "allora",
    "cane",
    "gatto"
    ]

lista_parole_corte = [] # lista vuota

# Popolare la lista lista_parole_corte con gli elementi
# di lista_parole che hanno meno di 6 caratteri. Infine
# stampare il numero di parole corte trovate.

for parola in lista_parole:
    if len(parola) < 6:
        lista_parole_corte.append(parola)

# Stampa
for parola in lista_parole_corte:
    print(parola)