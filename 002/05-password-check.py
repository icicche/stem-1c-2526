# 002/05
# Controllo password

# Memorizza una stringa inserita da tastiera
# nella variabile password
password = input("Inserisci una password: ")

# Questa è una variabile booleana che controlla se la
# seconda passord inserita coincide con la prima
is_correct = False

while not is_correct:

    check = input("Inserisci di nuovo la password: ")

    if check == password:
        print("OK")
        print("Password registrata con successo!")
        is_correct = True
    else:
        print("Le due password non coincidono!")