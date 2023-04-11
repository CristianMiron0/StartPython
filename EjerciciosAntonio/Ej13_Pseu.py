#Cubo
def principal():

    volumen=0
    area=0
    lado=input("Introduce el lado: ")
    #Se comprueba que sea un numero
    try:
            entero=int(lado)
    except ValueError:
            print("El numero debe ser un entero")

    if(int(lado)<0):
        print("Error, el radio no puede ser menor que 0")
    else:
        #Se calcula el area y el volumen
        area=int(lado)*int(lado)*6
        volumen=int(lado)*int(lado)*int(lado)
        print("Area: {n:1.2f}".format(n=area))
        print("Volumen: {n:1.2f}".format(n=volumen))
        
