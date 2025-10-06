# 001/03
# Input da tastiera

n_str = input("Inserisci un numero intero: ")
# Lo script chiede all'utente di inserire una stringa da tastiera
# e il suo valore viene assegnato alla variabile n_str

# ATTENZIONE!
# La variabile n_str costruita in questo modo è di tipo stringa
# Per convertirla in una variabile di tipo intero si usa il
# cosiddetto CASTING:
n_int = int(n_str)

# A questo punto possiamo trattare n_int come numero intero

succ = n_int + 1

print("Il successore del numero " + n_str + " è il numero:")
print(succ)

# Cosa sarebbe successo se nella riga 18 avessimo usato la variabile
# n_int al posto di n_str?
