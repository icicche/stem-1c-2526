# 003/02
# Cicli for

lista_parole = ["come", "quando", "fuori", "piove"]

# Possiamo usare un ciclo while per stampare ciascun
# elemento di una lista:
####################################################
i = 0       # i rappresenta l'indice dell'elemento

while i < len(lista_parole):
    print(lista_parole[i])
    i = i + 1
####################################################

# Lo stesso risultato si può ottenere più rapidamente
# utilizzando un ciclo for:

for parola in lista_parole:
    print(parola)