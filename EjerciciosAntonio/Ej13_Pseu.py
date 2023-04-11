#Cubo


volumen=0
area=0
lado=input("Introduce el lado: ")

if(int(lado)<0):
    print("Error, el radio no puede ser menor que 0")
else:
    area=int(lado)*int(lado)*6
    volumen=int(lado)*int(lado)*int(lado)
    print("Area: {n:1.2f}".format(n=area))
    print("Volumen: {n:1.2f}".format(n=volumen))
    
