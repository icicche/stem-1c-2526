# 003/01
# Liste

# Una lista (chiamata anche "array") è un tipo di variabile che
# può contenere a sua volta altre variabili, di qualsiasi tipo

mia_lista = ["Ciao", 23, True, "parola"]
print(mia_lista)

# La lunghezza di una lista è il numero di elementi che contiene

print(len(mia_lista))   # 4

# Gli elementi di una lista sono indicizzati a partire da zero

print(mia_lista[0])     # "Ciao"
print(mia_lista[1])     # 23

# Gli elementi di una lista possono essere modificati direttamente

mia_lista[1] = 14
print(mia_lista)        # ["Ciao", 14, True, "parola"]

# Possiamo aggiungere elementi con .append()

mia_lista.append("ultimo")
print(mia_lista)        # ["Ciao", 14, True, "parola", "ultimo"]

# Possiamo rimuovere elementi con del

del mia_lista[2]
print(mia_lista)        # ["Ciao", 14, "parola", "ultimo"]

# Possiamo controllare se un certo elemento fa parte di una lista

if "esempio" in mia_lista:
    print("L'elemento 'esempio' è nella lista")
else:
    print("L'elemento 'esempio' non è nella lista")