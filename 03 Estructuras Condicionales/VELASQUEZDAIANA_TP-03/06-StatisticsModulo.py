#escribir un programa que tome la lista 
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 

import statistics
import random 

#crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria. 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 


media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)


print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)


# Compara y determina el sesgo
if media > mediana > moda:
    print("Sesgo positivo.")
elif media < mediana < moda:
    print("Sesgo negativo.")
else:
    print("No hay sesgo (distribución simétrica o no clara).")
