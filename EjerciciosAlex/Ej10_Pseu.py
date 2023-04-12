def leer(lista):
    stop = False
    while stop == False:
        if len(lista) == 0:
            lista.append(input("Introduce el primer valor de la lista: "))
        else:
            print("¿Desea continuar? s/n: ", end="")
            decision = input().upper()
            if decision == "S":
                lista.append(input("Introduzca el siguiente valor de la lista: "))
            else:
                stop = True

def principal():
    listaPalabras = []
    leer(listaPalabras)
    listaPalabras.sort()
    print(listaPalabras)