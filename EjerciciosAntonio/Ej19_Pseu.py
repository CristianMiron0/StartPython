#Dada una lista de numeros enteros, crea un algoritmo que elimine los números duplicados de la lista

def principal():
        
    lista_numeros=[]
    numero=0
    salida=False
    confirmacion=""
    encontrado=False

    sublista=[]

    numero=input("Introuzca un numero:")
    #Se comprueba que sea un numero
    try:
            entero=int(numero)
    except ValueError:
            print("El numero debe ser un entero")
    lista_numeros.append(int(numero))

    #El usuario introduce los valores de la lista
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

    sublista.append(None)

    #Se comprueban duplicados
    for i in range(0,len(lista_numeros)):
        for j in range(0,len(sublista)):
            if(lista_numeros[i]==sublista[j]):
                encontrado=True
            elif j==len(sublista)-1 and encontrado==False:
                sublista.append(lista_numeros[i])
        encontrado=False

    sublista.remove(sublista[0])
    print(sublista)

