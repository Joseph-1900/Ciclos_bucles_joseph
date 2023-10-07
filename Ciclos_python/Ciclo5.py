"""Escriba un programa para mostrar la tabla de multiplicar de un entero dado."""

numero = int(input("Ingrese un número entero para ver su tabla de multiplicar: "))

print("Tabla de multiplicar de", numero)
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
