#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas. 

nombre = input("Por favor, ingresa tu nombre: ")


print("\nElige una opción:")
print("1. Convertir el nombre a MAYÚSCULAS")
print("2. Convertir el nombre a minúsculas")
print("3. Convertir el nombre con la primera letra en mayúscula")


opcion = input("Ingresa el número de la opción (1, 2 o 3): ")


if opcion == "1":
    print("\nTu nombre en MAYÚSCULAS es:", nombre.upper()) #Todas las letras a mayúsculas
elif opcion == "2":
    print("\nTu nombre en minúsculas es:", nombre.lower()) #Todo el texto a minúsculas
elif opcion == "3":
    print("\nTu nombre con la primera letra en mayúscula es:", nombre.title()) #Sólo la pirmera letra la convierte a mayúscula
else:
    print("\nOpción no válida. Por favor, elige 1, 2 o 3.")
