"""Escriba un programa para mostrar n términos de número natural y su suma (Fibonacci)."""


n = int(input("Ingrese la cantidad de términos de la secuencia de Fibonacci que desea mostrar: "))

a, b = 0, 1

suma = 0
print("Secuencia de Fibonacci de", n, "términos:")
for i in range(n):
    print(a, end=" ")  
    suma += a  
    a, b = b, a + b 

print("\nLa suma de los primeros", n, "térmimos de la secuencia de Fibonacci es: ", suma)
