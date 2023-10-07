"""Escribe un programa para leer 10 números del teclado y encontrar su suma y promedio."""

suma = 0
contador = 0

while True:
    numero = float(input("Ingrese un número (ingresar 0 para salir): "))
    
    if numero == 0:
        break  
    
    suma += numero
    contador += 1

if contador >= 10:
    promedio = suma / contador
    print(f"La suma de los números ingresados es: {suma}")
    print(f"El promedio de los números ingresados es: {promedio:.2f}" )
else:
    print("No se ingresaron suficientes números para calcular la suma y el promedio.")

