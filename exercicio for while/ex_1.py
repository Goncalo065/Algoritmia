#leia 10 numeros e indique media e o maior e ignora maiores que 20

import math
maior =-math.inf

maior=0
soma=0
i=0
while i<10:
    numero=int(input("Indique o {:n}º número: ".format(i+1)))
    if numero>20:
        continue

    soma+=numero
    i+=1

    if numero> maior:
      maior=numero

print("A média é {:n}".format(soma/10))
print("O maior é {:n}".format(maior))