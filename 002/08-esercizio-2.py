# 002/08
# Esercizio
#
######################
# INDOVINA IL NUMERO #
######################
#
# Creare un gioco in cui l'utente cerca di indovinare
# un numero intero casuale compreso tra 0 e 20. Si hanno
# 5 tentativi a disposizione.
#
# Scrivere una variazione del gioco in cui a ogni tentativo
# inserito lo script comunica se il numero da indovinare è
# maggiore o minore del numero inserito

import random

num_segreto = random.randint(0,20)
max_tentativi = 5

print("Ho scelto casualmente un numero intero compreso tra 0 e 20.")
print("Hai " + str(max_tentativi) + " tentativi per indovinarlo...")

partita_vinta = False
tentativo = 1

while not partita_vinta and tentativo <= max_tentativi:
    n = int(input("\nTentativo " + str(tentativo) + ": "))

    if n < num_segreto:
        print("Il numero da indovinare è più grande.")
    elif n > num_segreto:
        print("Il numero da indovinare è più piccolo.")
    else:
        partita_vinta = True
    
    tentativo = tentativo + 1

if partita_vinta:
    print("\nCOMPLIMENTI, hai indovinato!")
else:
    print("\nGAME OVER, il numero da indovinare era " + str(num_segreto) + ".")