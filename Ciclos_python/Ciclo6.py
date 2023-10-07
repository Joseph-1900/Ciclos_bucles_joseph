"""Escriba un programa para mostrar el patrón como triángulo con un asterisco"""

altura = int(input("Ingrese la mitad de la altura del triángulo: "))

for i in range(1, altura + 1):
    print('*' * i)
for i in range(altura - 1, 0, -1):
    print('*' * i)

