"""Escriba un programa para calcular el factorial de un número dado."""

numero = int(input("Digite porfa un número entero no negativo: "))
factorial = 1

if numero < 0:
    print("El factorial no está definido para números negativos.")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:

    for i in range(1, numero + 1):
        factorial *= i

    print("El factorial de", numero, "es:", factorial)
