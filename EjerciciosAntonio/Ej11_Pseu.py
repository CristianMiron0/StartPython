#Primos

def principal():

    numero=input("Introduce un numero: ")

    n=int(numero)-1
    resultado=0
    primo=True
    #Se comprueba que sea un numero
    try:
            entero=int(numero)
    except ValueError:
            print("El numero debe ser un entero")
    #Se comprueba que sea primo
    while n>1 :
        resultado= int(numero) % n
        if resultado==0 :
            primo=False
            n=0
        else:
            n=n-1    
    #Se imprime
    if(primo==True):
        print("El numero es primo")       
    else:
        print("El numero no es primo") 

