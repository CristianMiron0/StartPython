#Crea un algoritmo que determine si una cadena de texto es un anagrama de otra cadena de texto
def principal():
        
    cadena1=input("Introduce la primera cadena: ")
    cadena2=input("Introduce la segunda cadena: ")

    temp=[x for x in cadena1]
    temp2=[x for x in cadena2]

    for n in range(0, len(temp)):
        for l in range(0, len(temp2)):
            if(temp[n]==temp2[l]):
                temp2.remove(temp2[l])
                break

    if len(temp2)==0:
        print("Son anagramas")
    else:
        print("No son anagramas")            
        