# 002/06
# Controllo password con numero limitato (5) di tentativi

password = input("Inserisci una password: ")
is_correct = False

n_tent = 5      # numero tentativi rimanenti

while not is_correct and n_tent > 0:

    check = input("Inserisci di nuovo la password (" + str(n_tent) + " tentativi rimasti): ")

    if check == password:
        print("\nOK")
        print("Password registrata con successo!")
        is_correct = True
    else:
        print("\nLe due password non coincidono!")
        n_tent = n_tent - 1

if n_tent == 0:
    print("\nHai esaurito il numero di tentativi")
    print("Operazione annullata")