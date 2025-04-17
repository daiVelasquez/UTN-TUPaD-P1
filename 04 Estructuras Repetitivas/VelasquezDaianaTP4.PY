# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for cont in range(1,101): #1 = valor Inicial ,    101= valor Final 0 al 100 
    print(cont)


 # --------  --------    --------    --------    --------    --------    --------    --------    --------  

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 

num = int(input("ingrese un numero entero: "))
cont=0
n = abs(num) #abs() vuelve positivo el integer 

while n > 0:
    n //=10 #Se va dividiendo y quitando los decimales que se encuantran detras del punto
    #ej: 123 --> 123:10 = 12.3 (12) -> 12:10= 1.2 (1) --> 1:10=0.1 (0)  #OBTUVIMOS 3 RESULTADOS(repetimos el bucle 3veces) = cont =3 
    cont= cont +1

if num == 0:
    cont=1
    
print(f"El número {num} contiene {cont} dígitos")



 # --------  --------    --------    --------    --------    --------    --------    --------    --------   

# 3)Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 

valor1= int(input("Ingrese el primer valor: "))
valor2= int(input("Ingrese el segundo valor: "))

if valor1 > valor2:
    aux = valor2
    valor2 = valor1
    valor1 = aux 


inicio= valor1 + 1
sum=0
for x in range(inicio,valor2):
    sum= sum + x
   
print(f"La suma de los números entre {valor1} y {valor2} (sin incluirlos) es: {sum}") 



 # --------  --------    --------    --------    --------    --------    --------    --------    -------- 


# 4)Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 

num = int(input("Ingresa un número entero (0 para terminar): "))
total = 0

while num != 0:
    total += num
    num = int(input("Ingresa otro número entero (0 para terminar): "))

print(f"La suma total es: {total}")


# --------  --------    --------    --------    --------    --------    --------    --------    --------

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random

num_secreto = random.randint(0, 9) #número aleatorio entre 0 y 9

intentos = 0
adivinanza = -1  # El bucle while solo se ejecuta mientras la adivinanza sea distinta al número secreto.
#-1 no se encuentra entre el 0 y 9 así ingresará al bucle.

while adivinanza != num_secreto:
    try:
        adivinanza = int(input("Adivina el número (entre 0 y 9): "))
        if 0 <= adivinanza <= 9:
            intentos += 1
        else:
            print("Por favor, ingresa un número dentro del rango.")
    except ValueError:
        print("Entrada inválida. Ingresa un número entero.")

print(f"¡Correcto! El número era {num_secreto}.")
print(f"Lo adivinaste en {intentos} intento(s).")


# --------  --------    --------    --------    --------    --------    --------    --------    --------


# 6)Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

for n in range(100, -1, -2):  # valorI= 100 , valorFinal= -1, valorActualización= -2
        print(n)


# --------  --------    --------    --------    --------    --------    --------    --------    --------

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

num = int(input("Introduce un número entero positivo: "))

if num < 0:
    print("El número debe ser positivo.")
else:
    suma = 0
    for i in range(0, num + 1):
        suma += i

    print(f"La suma de los números entre 0 y {num} es: {suma}")



# --------  --------    --------    --------    --------    --------    --------    --------    --------


# 8)Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

cant_numeros = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingrese {cant_numeros} números enteros:")


for i in range(cant_numeros):
    numero = int(input(f"Número {i+1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Verificar positivo o negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\n--- Resultados ---")
print(f"Números pares:      {pares}")
print(f"Números impares:    {impares}")
print(f"Números positivos:  {positivos}")
print(f"Números negativos:  {negativos}")

# --------  --------    --------    --------    --------    --------    --------    --------    --------


# 9)Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor). 

cant_numeros = 100 

suma_total = 0

print(f"Ingrese {cant_numeros} números enteros:")


for i in range(cant_numeros):
    num = int(input(f"Número {i+1}: "))
    suma_total += num

media = suma_total / cant_numeros # Calcular la media


print("\n--- Resultado ---")
print(f"La media de los números ingresados es: {media}")



# --------  --------    --------    --------    --------    --------    --------    --------    --------

# 10)Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingresa un número entero: "))

invertido = 0

n = abs(num) #si es negativo lo pasamo a positivo

while n != 0:
    digito = n % 10           # Tomamos el último dígito
    invertido = invertido * 10 + digito  # Lo agregamos al número invertido
    n //= 10                  # Quitamos el último dígito decimal al número original

# Si el número es negativo, al invertirlo debe seguir negativo
if num < 0:
    invertido = -invertido

print(f"Número invertido: {invertido}")