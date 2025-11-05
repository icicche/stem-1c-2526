# 005/02
#
# Scrivere uno script in Python che
#
# 1. Prende in input una password inserita dall'utente.
#
# 2. Se la password è più corta di 5 caratteri lo script chiede
#    all'utente di inserire una password più lunga.
#
# 3. Altrimenti lo script termina e stampa a schermo un
#    messaggio di avvenuta registrazione.

success = False

while not success:
    password = input("Inserisci una password: ")
    if len(password) < 5:
        print("La password inserita è troppo corta!\nRiprova...\n")
    else:
        success = True
        print("------------------------------------")
        print("| Password registrata con successo |")
        print("------------------------------------")