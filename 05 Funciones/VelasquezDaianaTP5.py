 # 1. Crear una función llamada imprimir_hola_mundo que imprima por
 # pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
 # programa principal.

# Definición de la función
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

#  -------   -------   -------   -------   -------   -------   ------- 

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

# Definición de la función
def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

# Programa principal
nombre_usuario = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

#  -------   -------   -------   -------   -------   -------   ------- 

# 3.Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
# dir los datos al usuario y llamar a esta función con los valores in
# gresados

# Definición de la función
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("¿Dónde vivís?: ")

informacion_personal(nombre, apellido, edad, residencia)


#  -------   -------   -------   -------   -------   -------   ------- 

# 4.Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.

import math  # Importamos la librería para usar PI

# Definición de funciones
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


# Programa principal
radio_str = input("Ingrese el radio del círculo: ")
radio = float(radio_str)  # Convertimos a float por si el usuario ingresa decimales

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")


#  -------   -------   -------   -------   -------   -------   ------- 

# 5.Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.

# Definición de la función
def segundos_a_horas(segundos):
    return segundos / 3600  # 1 hora = 3600 segundos

# Programa principal
segundos_str = input("Ingrese la cantidad de segundos: ")
segundos = float(segundos_str)  # por si hay decimales

horas = segundos_a_horas(segundos)

print(f"{segundos} segundos equivalen a {horas} horas.")

#  -------   -------   -------   -------   -------   -------   ------- 


# 6.Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción

# Definición de la función
def tabla_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


# Programa principal
numero  = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#  -------   -------   -------   -------   -------   -------   -------

# 7.Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

# Definición de la función
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    if b != 0: # Evitamos la división por cero
        division = a / b
    else:
        division = "Error: División por cero"
    
    return (suma, resta, multiplicacion, division) # Devolvemos los resultados en una tupla


# Programa principal
valor1 = int(input("Ingrese el primer valor"))
valor2 = int(input("Ingrese el segundo valor"))
resultados = operaciones_basicas(valor1, valor2)


print(f"Los resultados de las operaciones son:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")


#  -------   -------   -------   -------   -------   -------   -------

# 8.Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.


# Definición de la función
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2) #elevar a la potencia de 2
    return imc

# Programa principal
peso = float(input("Introduce tu peso en kilogramos: "))#ya que peso y altura por lo general son condecimales usamos FLOAT()
altura = float(input("Introduce tu altura en metros: "))


resultado_imc = calcular_imc(peso, altura)

# Mostramos el resultado con dos decimales
print(f"Tu índice de masa corporal (IMC) es: {resultado_imc}")


#  -------   -------   -------   -------   -------   -------   -------


# 9.Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.


# Definimos la función
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


# Programa principal
celsius = float(input("Introduce la temperatura en grados Celsius: "))

resultado_fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius} grados Celsius equivalen a {resultado_fahrenheit} grados Fahrenheit.")


#  -------   -------   -------   -------   -------   -------   -------

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

# Definimos la función
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio


# Programa principal
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

resultado = calcular_promedio(num1, num2, num3)

print(f"El promedio de los tres números es: {resultado}")
