#Numero Aleatorio
import random

aleatorio=random.randint(0,100)
numero=101

while numero!=aleatorio:
    numero=input("Introduce el numero:")
    if(int(numero)>100 or int(numero)<0):
        print("Fuera de rango")
    elif(int(numero) < aleatorio):
        print("El numero que buscas es mayor")
    elif(int(numero) > aleatorio):
        print("El numero que buscas es menor")
    elif(int(numero) == aleatorio):
        print("Lo has encontrado!!")


