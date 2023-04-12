def principal():
    while True:
        try:
            radio = float(input("¿Cuál es el radio del círculo?: "))
        except ValueError:
            print("Debes introducir un número positivo")
        else:
            break


    pi = 3.14159264

    area = round(radio * radio * pi, 2)
    perimetro = round(radio * pi * 2, 2)

    print(f"El área es {area} y el perímetro es {perimetro}")