# 005/05
#
# Un numero naturale si dice perfetto se è la somma dei suoi divisori.
# Ad esempio, i primi due numeri perfetti sono
#
# 6  = 1 + 2 + 3
# 28 = 1 + 2 + 4 + 7 + 14
#
# Trovare i primi cinque numeri perfetti.

n = 1
count = 0

while(count <= 5):
    somma = 0
    for i in range(1,n):
        if n % i == 0:
            somma += i
    if somma == n:
        print(n)
        count += 1
    n += 1