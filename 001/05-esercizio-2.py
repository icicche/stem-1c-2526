# 001/05
# Esercizio
#
# Crea uno script python che
# 1. Chiede all'utente di inserire una stringa
# 2. Se la lunghezza è > 10 stampa "La stringa è lunga"
#    Se la lunghezza è < 5  stampa "La stringa è corta"
#    Altrimenti stampa "La stringa non è lunga né corta"

stringa = input("Inserisci una stringa: ")
lunghezza = len(stringa)

if lunghezza > 10:
    print("La stringa inserita è lunga")
elif lunghezza < 5:
    print("La stringa inserita è corta")
else:
    print("La stringa inserita non è lunga né corta")