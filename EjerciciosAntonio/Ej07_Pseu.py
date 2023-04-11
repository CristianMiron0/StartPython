#Dado un numero entero, determinar si es par o impar
def principal():
    #Se comprueba que sea un numero    
    parimpar=input("Introduce numero: ")
    try:
            entero=int(parimpar)
    except ValueError:
            print("El numero debe ser un entero")


    if(int(parimpar)%2!=0):
        print("El numero es impar")
    else:
        print("El numero es par")
