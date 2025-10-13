# 002/03
# Sequenze di numeri con proprietà
# STAMPA e CONTEGGIO
#
# Questo script stampa tutti i multipli di 7 compresi
# tra due interi inseriti da tastiera

a = int(input("Inserisci primo numero: "))
b = int(input("Inserisci il secondo numero: "))

num = a
tot = 0

print("\nMultipli di 7 compresi tra " + str(a) + " e " + str(b))
print("---")

while num <= b:
    
    if num % 7 == 0:
        print(num)
        tot = tot + 1
    
    num = num + 1

print("---")
print("Totale: " + str(tot))