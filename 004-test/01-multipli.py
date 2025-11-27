# 005/01
#
# Consideriamo tutti i numeri interi compresi tra 123458 e 232502,
# estremi inclusi.
#
# Quanti di questi sono multipli di 719?
#
# Scrivere uno script in Python per trovare la risposta.

conteggio = 0

for n in range(123458, 232503):
    if n % 719 == 0:
        conteggio += 1

print(conteggio)        # 152