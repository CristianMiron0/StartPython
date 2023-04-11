#Anagrama
cadena1=input("Introduce la primera cadena")
cadena2=input("Introduce la segunda cadena")

temp=cadena2
cadena1=str(list).split()
temp=str(list).split()

for n in range(0, len(cadena1)):
    for l in range(0, len(cadena2)):
        if(cadena1[n]==temp[l]):
            temp.remove(temp[l])

if len(temp)==0:
    print("Son anagramas")
else:
    print("No son anagramas")            
    