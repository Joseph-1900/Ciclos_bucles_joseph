#en este archivo solo voy a agregar unas placticas


tamaño = int(input("Digita el tamaño de las letras, y debe ser impar: "))

if tamaño < 3 or tamaño % 2 == 0:
    print("El tamaño ingresado no es válido. recuerde ,debe ser impar.")
else:
    
    for i in range(tamaño):
    
        for j in range(tamaño):
            if j == i or j == tamaño - i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print(" ", end=" ")
        
       
        for j in range(tamaño):
            if j == i or j == tamaño - i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print(" ", end=" ")
        
        
        for j in range(tamaño):
            if j == i or j == tamaño - i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        
        print()  

