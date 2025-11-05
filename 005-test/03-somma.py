# 005/03
#
# Scrivere uno script in Python che prende in input una sequenza di interi
# inseriti dall'utente e stampa la loro somma.
#
# L'inserimento dei dati termina quando l'utente inserisce la stringa "stop".

print("Inserisci una sequenza di numeri interi...")

n = input("> ")
totale = 0

while n != 'stop':
    totale += int(n)
    n = input("> ")

print("---")
print("La somma dei numeri inseriti è", totale)