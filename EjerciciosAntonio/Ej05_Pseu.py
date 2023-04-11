#Dada una lista de numeros enteros, determinar cual es mayor o menor

def principal():
    lista_numeros=[]
    numero=0
    salida=False
    confirmacion=""

    numero=input("Introuzca un numero:")
    #Se comprueba que sea un numero 
    try:
            entero=int(numero)
    except ValueError:
            print("El numero debe ser un entero")
    
    lista_numeros.append(int(numero))
    mayor=int(numero)
    menor=int(numero)

    #El usuario introduce los elementos de la lista
    while salida!=True :

        confirmacion=input("Quiere introducir otro numero? S/N :")
        
        if(confirmacion=='n' or confirmacion=='N'):
            salida=True
        elif(confirmacion=='s' or confirmacion=='S'):
            numero=input("Introuzca un numero:")
            try:
                entero=int(numero)
            except ValueError:
                print("El numero debe ser un entero")
            lista_numeros.append(int(numero))
        else:
            print("Opcion erronea")
    #Se comprueba los numeros mayores y menores
    for n in lista_numeros:
        if n > mayor:
            mayor=n
        elif n < menor:
            menor=n

    print(mayor)
    print (menor)