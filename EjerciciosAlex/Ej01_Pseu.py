tablaLetrasDNI = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']

dni = 0

while len(str(dni)) != 8 or not isinstance(dni, int):
    try:
        dni = int(input("Escribe un DNI: "))
    except:
        if len(str(dni)) != 8 or not isinstance(dni, int):
            print("DNI Inválido")

def principal():
    resultadoResto = dni % 23

    for i in range(0, len(tablaLetrasDNI)):
        if resultadoResto == i:
            resultado = tablaLetrasDNI[i]
            print("La letra de este DNI es " + resultado)
