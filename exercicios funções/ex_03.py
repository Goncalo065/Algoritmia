def heartRate (num):
    """
    recebe freq cardiaca e return o nivel de esforço
    """
    if num<50:
        print ("no exercicio")
    elif 50<=num<=80:
        print ("Nível aeróbico") 
    elif 80<=num<=100:
        print("treino cardiovascular")
    elif 100<=num<=120:
        print("treino aeróbico ideal")

    else:
      return ("treino anaeróbico")

   
        
num=int(input("Indique a sua frequência cardíaca: "))