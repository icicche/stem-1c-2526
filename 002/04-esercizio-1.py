# 002/04
# Esercizio
#
# Creare uno script che stampa i DIVISORI di un numero intero inserito
# da tastiera e riporta il numero totale di divisori

print("Questo script calcola i divisori di un numero.")

n = int(input("Inserisci un intero positivo: "))

d = 1
totale = 0

print("\nDivisori di " + str(n) + "\n---")

while d <= n:

    if n % d == 0:
    # se d è un divisore di n:
        print(d)
        totale = totale + 1

    d = d + 1

print("---\nTotale: " + str(totale))