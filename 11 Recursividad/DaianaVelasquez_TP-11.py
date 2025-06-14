## 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función 
# para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que 
# indique el usuario.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar número al usuario
limite = int(input("Ingresá un número para calcular los factoriales desde 1 hasta ese número: "))

print("\nFactoriales:")
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")


## ////////////////////////////////////////////////////////////////

##2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique. 

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

# Solicitar número al usuario
hasta = int(input("\n¿Hasta qué posición querés mostrar la serie de Fibonacci?: "))

print("\nSerie de Fibonacci:")
for i in range(hasta + 1):
    print(f"Posición {i}: {fibonacci(i)}")


##//////////////////////////////////////////////////////////////

## 3)	Crea una función recursiva que calcule la potencia de un número base 
# elevado a un exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). 
# Prueba esta función en un algoritmo general. 

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Solicitar base y exponente al usuario
base = int(input("\nIngresá la base: "))
exponente = int(input("Ingresá el exponente: "))

resultado = potencia(base, exponente)
print(f"\n{base}^{exponente} = {resultado}")

##//////////////////////////////////////////////////////////////

## 4)	Crear una función recursiva en Python que reciba un número entero positivo 
# en base decimal y devuelva su representación en binario como una cadena de texto. 
#Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) 
# y unos (1), en base 2. Para convertir un número decimal a binario, 
# se puede seguir este procedimiento: 
#1.	Dividir el número por 2. 
#2.	Guardar el resto (0 o 1). 
#3.	Repetir el proceso con el cociente hasta que llegue a 0. 
#4.	Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario. 

#Convertir el número 10 a binario: 
#10 ÷ 2 = 5     resto: 0   
# 5 ÷ 2 = 2     resto: 1   
# 2 ÷ 2 = 1     resto: 0   
# 1 ÷ 2 = 0     resto: 1   
# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010". 

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Solicitar número al usuario
numero = int(input("Ingresá un número entero positivo para convertir a binario: "))

if numero == 0:
    print("El binario de 0 es: 0")
else:
    binario = decimal_a_binario(numero)
    print(f"El binario de {numero} es: {binario}")


##/////////////////////////////////////////////////////////////////

##5)	Implementá una función recursiva llamada es_palindromo(palabra) que 
# reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un 
# palíndromo o False si no lo es. 
# Requisitos: 
#La solución debe ser recursiva. 
#No se debe usar [::-1] ni la función reversed(). 

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

# Solicitar palabra al usuario
texto = input("Ingresá una palabra sin espacios ni tildes para verificar si es un palíndromo: ").lower()

if es_palindromo(texto):
    print(f"'{texto}' es un palíndromo.")
else:
    print(f"'{texto}' no es un palíndromo.")

    
##////////////////////////////////////////////////////////////////

##6)	Escribí una función recursiva en Python llamada suma_digitos(n) que 
# reciba un número entero positivo y devuelva la suma de todos sus dígitos. 
#  Restricciones: 
#No se puede convertir el número a string. 
#Usá operaciones matemáticas (%, //) y recursión. 
#Ejemplos: suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) suma_digitos(9)      → 9 
#suma_digitos(305)    → 8   (3 + 0 + 5) 

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Solicitar número al usuario
numero = int(input("Ingresá un número entero positivo para sumar sus dígitos: "))

if numero < 0:
    print("Por favor ingresá un número positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")

##///////////////////////////////////////////////////////////////////////////

##7)	Un niño está construyendo una pirámide con bloques. En el nivel más bajo
#  coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente 
# hasta llegar al último nivel con un solo bloque. 
 
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques
# en el nivel más bajo y devuelva el total de bloques que necesita para construir 
# toda la pirámide. 

#  Ejemplos: 
#contar_bloques(1)   → 1         (1)
# contar_bloques(2)   → 3         (2 + 1)
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1) 


def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

nivel_inferior = int(input("Ingresá el número de bloques en el nivel más bajo de la pirámide: "))

if nivel_inferior < 1:
    print("El número debe ser mayor o igual a 1.")
else:
    total = contar_bloques(nivel_inferior)
    print(f"Para construir la pirámide se necesitan {total} bloques en total.")

##////////////////////////////////////////////////////////////////////

##8)	Escribí una función recursiva llamada contar_digito(numero, digito) que }
# reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva
# cuántas veces aparece ese dígito dentro del número. 
#  Ejemplos: 
# contar_digito(12233421, 2)   → 3   
# contar_digito(5555, 5)       → 4   
# contar_digito(123456, 7)     → 0   


def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

# Pedir los datos al usuario
numero = int(input("Ingresá un número entero positivo: "))
digito = int(input("Ingresá el dígito que querés contar (entre 0 y 9): "))

# Validación básica
if numero < 0 or digito < 0 or digito > 9:
    print("Datos inválidos. Asegurate de que el número sea positivo y el dígito esté entre 0 y 9.")
else:
    resultado = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")
