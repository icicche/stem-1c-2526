# 003/05
# Esercizio
#
# Creare uno script che chiede all'utente di popolare una lista
# vuota inserendo gli elementi da tastiera uno per uno.
#
# Quando l'utente inserisce 'END' lo script termina e stampa la
# lista che è stata generata e la sua lunghezza.

stringhe_inserite = []

prompt = "Inserisci una stringa (oppure END per terminare): "
stringa = input(prompt)

while stringa != "END":
    stringhe_inserite.append(stringa)
    stringa = input(prompt)

print("Hai inserito", len(stringhe_inserite), "stringhe.")
print("---")
for p in stringhe_inserite:
    print(p)
print("---")