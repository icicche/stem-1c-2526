# 001/02
# Istruzioni di controllo

a = 12

# IF semplice
if a > 0:
  print("Il numero è positivo")    # eseguito solo se a è positivo
print("Ciao a tutti!")             # eseguito sempre perché si trova fuori dal blocco if

# IF-ELSE
if a > 0:
  print("Il numero è positivo")      # eseguito solo se a è positivo
else:
  print("Il numero non è positivo")  # eseguito solo se a NON è positivo

# IF-ELIF-ELSE
if a > 0:
  print("Il numero è positivo")    # eseguito solo se a è positivo
elif a < 0:
  print("Il numero è negativo")    # eseguito se a NON è positivo ed è negativo
else:
  print("Il numero è zero")        # eseguito se a NON è positivo e NON è negativo

# In alternativa è possibile definire una variabile booleana di controllo

b = 5
b_is_positive = b > 0    # variabile booleamna di controllo

if b_is_positive:
  print("Il numero è positivo")
elif not b_is_positivo:
  print("Il numero è negativo")
else:
  print("Il numero è zero")
