"""Escriba un programa para mostrar un patrón como Z con asteriscos. """


tamaño = int(input("Ingrese el tamaño de la letra Z (un número impar mayor o igual a 3): "))


if tamaño < 3 or tamaño % 2 == 0:
    print("El tamaño ingresado no es válido. Debe ser un número impar mayor o igual a 3.")
else:
    for i in range(tamaño):
        for j in range(tamaño):
          
            if i == 0 or i == tamaño - 1:
                print("*", end=" ")
           
            elif i + j == tamaño - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
