#Crea un algoritmo que calcule el factorial de un número entero.
def principal():

        factorial=input("Introduce un numero: ")

        resultado=1
        #Se comprueba que sea un numero
        try:
                entero=int(factorial)
        except ValueError:
                print("El numero debe ser un entero")
        #Se realiza la operacion
        for n in range(1,int(factorial)+1):
                resultado=resultado*n


        print(resultado)
        
