"""  programa que peça ao utilizador a indicação de 2 números
inteiros (limite inferior e limite superior), calculando em seguida a
soma de todos os pares entre esse intervalo (incluindo os limites indicados).
"""

Limite_Inferior=int(input("Indique o limite inferior: "))
Limite_Superior=int(input("Indique o limite superior: "))

#soma

soma=0

#ver o intervalo
for number in range(Limite_Inferior, Limite_Superior +1):
    if number %2==0:  #ver se é par
     soma+=number #add à soma

print(f"A soma de todos os pares entre {Limite_Inferior} e {Limite_Superior} é {soma} ")

