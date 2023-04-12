def principal():
    cadena = input("Ingrese el texto que desee comprobar si es palíndromo o no: ")

    cadena = cadena.lower().replace(" ","")

    reverso = cadena[::-1]

    if cadena == reverso:
        print("El texto es palíndromo")
    else:
        print("El texto no es palíndromo")