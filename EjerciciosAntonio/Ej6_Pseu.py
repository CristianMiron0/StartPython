#Cambiar de grados celsius a farenheit


grados=input("Introduce los grados en celsius: ")

if(float(grados)<0):
    print("Error, el radio no puede ser menor que 0")
else:
    resultado= float(grados) * (9/5) +32
    print("Grados Farenheit: {n:1.2f}".format(n=resultado))
    
