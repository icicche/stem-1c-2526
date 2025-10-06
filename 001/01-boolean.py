# 001/01
# Variabili booleane

a = 1
b = a > 3

# La variabile a è di tipo intero, mentre b è di tipo booleano
# Questo significa che b può assumere solo due valori possibili:
# b = True se a è maggiore di 3
# b = False sa non è maggiore di 3
#
# Altri possibili valori di b sono
# b = a == 5 (significa a uguale a 5)
# b = a <= 4
# b = a >= 2
# b = a != 1 (significa a diverso da 1)

print("Valore della variabile b:")
print(b) # False

c = a <= 5
print("Valore della variabile c:")
print(c) # True

# Le variabili booleane possono essere combinate con gli operatori
# and, or, not

a = False
b = True

a_e_b = a and b
a_oppure_b = a or b
non_a = not a

# Stampa il valore delle tre variabili definite nelle righe 31-32-33
# In che modo il loro valore dipende da quello di a e b?
