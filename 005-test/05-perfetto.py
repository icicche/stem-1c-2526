# 005/05
#
# Un numero naturale si dice perfetto se è la somma dei suoi divisori.
# Ad esempio, i primi due numeri perfetti sono
#
# 6  = 1 + 2 + 3
# 28 = 1 + 2 + 4 + 7 + 14
#
# Trovare i primi quattro numeri perfetti.

n = 1
totale = 0

while totale < 4:

    # Calcola la somma dei divisori di n
    somma_divisori = 0
    for d in range(1,n):
        if n % d == 0:
            somma_divisori += d
    
    # Se n è un numero perfetto,
    # stampalo e incrementa il totale
    if somma_divisori == n:
        print(n)
        totale += 1

    n += 1