def principal():
    while True:
        try:
            num = input("Ingrese el número que desee comprobar si es capicúa o no: ")
        except ValueError:
            print("El número dado debe ser un entero")
        else:
            break

    reverso = "".join(reversed(num))

    if num == reverso:
        print("El número es capicúa")
    else:
        print("El número no es capicúa")