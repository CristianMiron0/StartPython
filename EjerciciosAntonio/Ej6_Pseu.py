#Cambiar de grados celsius a farenheit

def principal():

    grados=input("Introduce los grados en celsius: ")
    #Se comprueba que sea un numero 
    try:
            entero=int(grados)
    except ValueError:
            print("El numero debe ser un entero")
    #Se hacen las operaciones
    resultado= float(grados) * (9/5) +32
    print("Grados Farenheit: {n:1.2f}".format(n=resultado))
        
