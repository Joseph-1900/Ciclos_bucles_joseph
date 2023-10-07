"""Escriba un programa para encontrar la suma de los primeros 20 números naturales. El total es 210. """

suma = 0
for i in range(1, 21):  
    suma += i  

if suma == 210:
    print("La suma de los primeros 20 números naturales es igual a 210.")
else:
    print("La suma de los primeros 20 números naturales no es igual a 210.")

print("La suma de los primeros 20 números naturales es:", suma)

