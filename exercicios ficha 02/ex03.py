"""
Adivinhar o número
"""

import random

numero= random.randint(1,50)

print ("Adivinhe o numero de 1-50")

tentativa =0
max_tentativas =10


#Loop de tentativas 

while tentativa <max_tentativas: 
    player= int(input(f" Tentativa {tentativa+1} Insira o seu palpite: " ))
    tentativa+=1

    if player<numero:
     print("Mais alto...")

    elif player>numero:
     print("Mais baixo...")

    else :
     print(f"Acertou em {tentativa}tentativas ")
     break
else:
  print(f"Esgotaste as {max_tentativas} trys man :( ")