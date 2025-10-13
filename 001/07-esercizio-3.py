# 001/07
# Esercizio
#
# Scrivere uno script che
# 1. Legge un numero intero da tastiera
# 2. Controlla se è un multiplo di 8 oppure se è un multiplo di 13
#
# Esempi di funzionamento:
#
# Se inseriamo il numero 416, lo script deve stampare:
# "Il numero 416 è un multiplo di 8 e di 13"
#
# Se inseriamo il numero 16, lo script deve stampare:
# "Il numero 16 è un multiplo di 8 ma non di 13"
#
# Se inseriamo il numero 92, lo script deve stampare:
# "Il numero 92 non è un multiplo di 8 né di 13"

n = input("Inserisci un numero: ")

is_mul_8 = int(n) % 8 == 0
is_mul_13 = int(n) % 13 == 0

if is_mul_8 and is_mul_13:
    print("Il numero " + n + " è multiplo di 8 e di 13")
elif is_mul_8:
    print("Il numero " + n + " è multiplo di 8 ma non di 13")
elif is_mul_13:
    print("Il numero " + n + " è multiplo di 13 ma non di 8")
else:
    print("Il numero " + n + " non è multiplo di 8 né di 13")