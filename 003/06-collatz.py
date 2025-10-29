# 003/05
# Sequenza di Collatz
#
# Si parte da un numero intero positivo n.
#   Se n è pari, il numero successivo nella sequenza è n/2
#   Altrimenti, se n è dispari, il numero successivo è 3n + 1
#
# https://it.wikipedia.org/wiki/Congettura_di_Collatz
#
# La sequenza termina quando raggiunge il valore 1.

n = int(input("Inserisci un numero intero positivo: "))

collatz = [n]   # Inizialmente la lista contiene solo il valore iniziale n
ultimo = n      # In questa situazione l'ultimo valore della lista è n stesso

while ultimo != 1:

    # Calcoliamo il numero successivo nella sequenza di Collatz
    if ultimo % 2 == 0:
        nuovo = int(ultimo/2)
    else:
        nuovo = 3 * ultimo + 1

    # Aggiungiamo il nuovo valore trovato alla lista
    collatz.append(nuovo)

    # Aggiorniamo l'ultimo valore della lista
    ultimo = nuovo

print("Partendo da", n, "la sequenza termina dopo", len(collatz) - 1, "iterazioni:")

for i in collatz:
    print(i)