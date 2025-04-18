def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio


# Programa principal
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

# Llamamos a la función para calcular el promedio
resultado = calcular_promedio(num1, num2, num3)


print(f"El promedio de los tres números es: {resultado}")
