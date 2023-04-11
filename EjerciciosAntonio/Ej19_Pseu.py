lista_numeros=[]
numero=0
salida=False
confirmacion=""

sublista=[]

numero=input("Introuzca un numero:")
lista_numeros.append(int(numero))
mayor=int(numero)
menor=int(numero)

while salida!=True :

    confirmacion=input("Quiere introducir otro numero? S/N :")
    
    if(confirmacion=='n' or confirmacion=='N'):
        salida=True
    elif(confirmacion=='s' or confirmacion=='S'):
        numero=input("Introuzca un numero:")
        lista_numeros.append(int(numero))
    else:
        print("Opcion erronea")

for i in range(0,len(lista_numeros)):
    for j in range(0,len(sublista)):
        if(lista_numeros[i]==sublista[j]):
            lista_numeros.remove(lista_numeros[i])
        else:
            sublista.append(lista_numeros[i])
print(lista_numeros)

