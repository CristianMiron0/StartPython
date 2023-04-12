def principal():
    salarioBase = input("¿Cuál es el salario base mensual?: ")
    pagasExtras = input("¿Cuánto corresponde de pagas extras en total?: ")
    complementos = input("¿Cuánto corresponde de complementos al mes?: ")
    otrosConceptosRetributivos = input("Indica el valor total de otros conceptos retributivos: ")
    IRPF = input("Indica el porcentaje de IRPF: ")
    segSocial = input("Indica cuánto debe pagar de Seg Social: ")

    salarioBruto = salarioBase + (pagasExtras/12) + complementos + otrosConceptosRetributivos
    deducciones = (salarioBase/100*IRPF) + segSocial
    salarioNeto = salarioBruto - deducciones

    print("El salario bruto es: " + salarioBruto)
    print("El salario Neto es:" + salarioNeto)