# 005/06
#
# Data la lista

parole = [
    "mela", "luna", "gatto", "casa", "mare", "vento", "sole", "pietra", "sogno", "tempo",
    "notte", "libro", "fiore", "montagna", "fiume", "ombra", "luce", "strada", "cielo", "musica",
    "amore", "sorriso", "voce", "sabbia", "pioggia", "cuore", "viaggio", "penna", "finestra", "neve",
    "stella", "foglia", "bosco", "campo", "ponte", "nuvola", "sale", "vino", "pane", "chiave",
    "porta", "gioco", "parola", "silenzio", "passo", "ricordo", "respiro", "viola", "lago", "pianta",
    "terra", "ombrello", "specchio", "segreto", "disegno", "treno", "ferro", "zucchero", "miele", "lampada",
    "giardino", "acqua", "ghiaccio", "deserto", "sentiero", "montagna", "fiore", "sogno", "vento", "sole",
    "tempo", "ombra", "mare", "notte", "cielo", "neve", "libro", "fiume", "porta", "pioggia",
    "cuore", "luce", "viaggio", "bosco", "campo", "pane", "vino", "sale", "ponte", "mela",
    "nuvola", "musica", "silenzio", "vento", "sorriso", "amore", "fiore", "stella", "luna", "gatto"
]

# Stampare a schermo il seguente resoconto:
#
# | n | Numero di parole di n caratteri |
# |---|---------------------------------|
# | 1 |
# | 2 |
# | 3 |
# | 4 |
#  ...

lunghezze = []

# La lista lunghezze ha questa proprietà:
# l'elemento di posto i è il numero di parole
# che hanno lunghezza i

for i in range(10):
    totale = 0
    for parola in parole:
        if len(parola) == i:
            totale += 1
    lunghezze.append(totale)

for i in range(1, 10):
    print("Parole di " + str(i) + " lettere: ", lunghezze[i])