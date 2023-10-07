"""Escriba un programa para hacer un patrón como una pirámide con números aumentados en 1."""

altura = int(input("Ingrese la altura de la pirámide: "))

numero_actual = 1

for i in range(1, altura + 1):
   
    for z in range(altura - i):
        print(" ", end=" ")
    for x in range(i):
        print(numero_actual, end=" ")
        numero_actual += 1

    print()
    
    #la piramide no sale bien, sale toda chueca profesor :(
