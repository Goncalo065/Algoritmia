def somatorio(num1,num2):
    """
    recebe 2 argumentos e imprime o somatorio do intervalo
    """
    #primeiro ordenar os numeros
    ini=min (num1,num2)
    fim=max (num1,num2)

    #faz o somatorio 

    final=sum(range(ini, fim+1))

    print(final)

#ex.:
somatorio(1,3) #sera 6
somatorio(4,2) # sera 9