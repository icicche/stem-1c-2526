# 005/04
#
# Scrivere uno script in Python che calcola il minimo comune multiplo
# di due numeri interi positivi inseriti dall'utente.

print("Inserisci due numeri interi positivi")
print("---")

a = int(input("Primo numero: "))
b = int(input("Secondo numero: "))

if a < b:
    max_num = b
    min_num = a
else:
    max_num = a
    min_num = b

mcm = 0
trovato = False

while not trovato:
    mcm += max_num
    if mcm % min_num == 0:
        trovato = True

print("---")
print("Il minimo comune multiplo dei numeri inseriti è", mcm)