#Crea un algoritmo que calcule el factorial de un número entero.


factorial=input("Introduce un numero: ")

resultado=1

try:
        entero=int(factorial)
except ValueError:
        print("El numero debe ser un entero")

for n in range(1,int(factorial)+1):
        resultado=resultado*n


print(resultado)
    
