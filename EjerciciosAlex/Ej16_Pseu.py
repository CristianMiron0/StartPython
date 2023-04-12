def leer():
    lista = []
    stop = False
    while stop == False:
        if len(lista) == 0:
            while True:
                try:
                    lista.append(int(input("Introduce el primer valor de la lista: ")))
                except ValueError:
                    print("El valor debe ser un número entero")
                else:
                    break
        else:
            print("¿Desea continuar? s/n: ", end="")
            decision = input().upper()
            if decision == "S":
                while True:
                    try:
                        lista.append(int(input("Introduce el siguiente valor de la lista: ")))
                    except ValueError:
                        print("El valor debe ser un número entero")
                    else:
                        break
            elif decision == "N":
                stop = True
    return lista

def principal():
    listaNum = leer()
    sumatorio = 0

    for num in listaNum:
        sumatorio += num

    media = round(sumatorio/len(listaNum), 2)

    print(f"La media de la lista otorgada es: {media}")