# 003/04
# Esercizio
#
# Il comando range(a,b) è un modo rapido di generare la lista
# dei numeri interi compresi tra a e b-1

lista_numeri = range(2,9)
print(lista_numeri)         # [2, 3, 4, 5, 6, 7, 8]

# Generare la stessa lista SENZA utilizzare il comando range

lista_numeri = []

n = 2

while n < 9:
    lista_numeri.append(n)
    n += 1

print(lista_numeri)