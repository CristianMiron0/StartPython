def principal():
    while True:
        try:
            num = float(input("Dame un número: ").replace(",","."))
        except ValueError:
            print("El valor debe ser un número")
        else:
            break

    if num < 0:
        print("El número es negativo")
    elif num > 0:
        print("El número es positivo")
    else:
        print("El número es 0")