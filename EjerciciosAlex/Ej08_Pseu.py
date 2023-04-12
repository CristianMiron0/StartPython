def principal():
    while True:
        try:
            anyo = int(input("Otórgueme un año: "))
        except ValueError:
            print("El valor debe ser un año AD (número entero positivo)")
        else:
            break

    if anyo % 4 == 0:
        print(f"El año {anyo} es bisiesto")
    else:
        if anyo % 100 == 0 and anyo % 400 == 0:
            print("El año es bisiesto")
        else:
            print(f"El año {anyo} no es bisiesto")