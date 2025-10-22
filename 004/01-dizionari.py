# 004/01
# Dizionari

# Questa è una lista che contiene nome, cognome
# ed età di una persona:

lista_dati_utente = ["Mario", "Rossi", 18]
# Indice             0        1        2

# Un dizionario è sostanzialmente è una lista in
# cui al posto degli indici numerici abbiamo delle
# CHIAVI numeriche

dict_dati_utente = {
    "nome": "Mario",
    "cognome": "Rossi",
    "età": 18
}

# CHIAVE        VALORE
# --------------------
# "nome"    --> "Mario"
# "cognome" --> "Rossi"
# "età"     --> 18

print(dict_dati_utente["nome"])     # "Mario"

dict_dati_utente["età"] = 19
print(dict_dati_utente["età"])      # 19

# A differenza delle lista possiamo aggiungere
# direttamente nuovi valori

dict_dati_utente["città"] = "Torino"

print(dict_dati_utente)

# A ogni dizionario sono associate due liste
lista_chiavi = dict_dati_utente.keys()
lista_valori = dict_dati_utente.values()

print(lista_chiavi)   # ['nome', 'cognome', 'età', 'città']
print(lista_valori)   # ['Mario', 'Rossi', 19, 'Torino']

# Possiamo scorrere le coppie chiave-valore di un dizionario
# in questo modo:
for chiave, valore in dict_dati_utente.items():
    print(chiave, "-->", valore)