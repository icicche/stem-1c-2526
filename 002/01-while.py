# 002/01
# Cicli while

a = 0

# Le istruzioni all'interno di un blocco while sono
# eseguite ripetutamente fintanto che la condizione
# in cima è vera

while a < 10:
    # Controlla che a sia minore di 10

    # Se la condizione è vera prosegue
    # con l'esecuzione dei comandi che
    # seguono

    print("Ciao")

    # Incrementa il valore di a di 1
    a = a + 1

    # Ripete tutti i comandi a partire
    # dalla riga 10

# Quando il valore di a diventa 10, esce dal blocco
# while ed esegue il resto dello script

print("Il programma è terminato")
print("Il valore della variabile a è " + str(a))