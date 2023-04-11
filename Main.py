import os
from EjerciciosAlex import Ej01_Pseu
from EjerciciosAlex import Ej02_Pseu
from EjerciciosAlex import Ej03_Pseu
from EjerciciosAlex import Ej04_Pseu
from EjerciciosAntonio import Ej05_Pseu
from EjerciciosAntonio import Ej06_Pseu
from EjerciciosAntonio import Ej07_Pseu
from EjerciciosAlex import Ej08_Pseu
from EjerciciosAlex import Ej09_Pseu
from EjerciciosAlex import Ej10_Pseu
from EjerciciosAntonio import Ej11_Pseu
from EjerciciosAntonio import Ej12_Pseu
from EjerciciosAntonio import Ej13_Pseu
from EjerciciosAlex import Ej14_Pseu
from EjerciciosAlex import Ej15_Pseu
from EjerciciosAlex import Ej16_Pseu
from EjerciciosAntonio import Ej17_Pseu
from EjerciciosAntonio import Ej18_Pseu
from EjerciciosAntonio import Ej19_Pseu
from EjerciciosAlex import Ej20_Pseu
while True:
    os.system("cls")
    print("Bienvenidos")
    print("Menu principal")
    print("1-Calcular la letra del DNI Espanol")
    print("2-Calcular el salario de un empleado")
    print("3-Determinar la ruta para llegar a una ciudad por avion")
    print("4-Calcula el área y perímetro de un círculo dado su radio")
    print("5-A partir de una lista de números, determine cuál es el más grande y cuál es el más pequeño")
    print("6-Convierta grados Celsius a Fahrenheit")
    print("7-Codigo que determine si es par o impar")
    print("8-Codigo que determine si un año es bisiesto o no")
    print("9-Codigo que determine si una cadena de texto es un palindromo o no")
    print("10-Codigo que ordene la lista alfabeticamente")
    print("11-Codigo que calcule el factorial de un numero entero")
    print("12-Codigo que determine un numero entero si es primo o no")
    print("13-Codigo que calcule el area y volumen de un cubo dado su lado")
    print("14-Codigo que calcule la suma de todos los numeros pares de la lista")
    print("15-Codigo que determine si un numero es positivo, negativo o cero")
    print("16-Codigo que calcule la media de la lista")
    print("17-Codigo que genere un numero aleatorio entre 1 y 100, y le pida al usuario adivinarlo")
    print("18-Codigo que determine si una cadena de texto es un anagrama de otra cadena de texto")
    print("19-Codigo que elimine los numeros duplicados de la lista")
    print("20-Codigo que determine si un numero es capicua o no")
    print("0 -Salir")
    opcion = input("Seleccione una opción:")
    if opcion == "1":
        Ej01_Pseu.principal()
    elif opcion == "2":
        Ej02_Pseu.principal()
    elif opcion == "3":
        Ej03_Pseu.principal()
    elif opcion == "4":
        Ej04_Pseu.principal()
    elif opcion == "5":
        Ej05_Pseu.principal()
    elif opcion == "6":
        Ej06_Pseu.principal()
    elif opcion == "7":
        Ej07_Pseu.principal()
    elif opcion == "8":
        Ej08_Pseu.principal()
    elif opcion == "9":
        Ej09_Pseu.principal()
    elif opcion == "10":
        Ej10_Pseu.principal()
    elif opcion == "11":
        Ej11_Pseu.principal()
    elif opcion == "12":
        Ej12_Pseu.principal()
    elif opcion == "13":
        Ej13_Pseu.principal()
    elif opcion == "14":
        Ej14_Pseu.principal()
    elif opcion == "15":
        Ej15_Pseu.principal()
    elif opcion == "16":
        Ej16_Pseu.principal()
    elif opcion == "17":
        Ej17_Pseu.principal()
    elif opcion == "18":
        Ej18_Pseu.principal()
    elif opcion == "19":
        Ej19_Pseu.principal()
    elif opcion == "20":
        Ej20_Pseu.principal()
    elif opcion == "0":
        print("Que tenga un lindo día ^_^")
        break
    continuar=input("Presione enter para continuar...")