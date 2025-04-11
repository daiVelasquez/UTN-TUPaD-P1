#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Por favor, ingresa tu edad: "))

if edad < 12 :
    print("Perteces a la categoría : Niño/a")

elif edad >= 12 and edad < 18: 
    print ("Perteneces a la categorí: Adolescente")

elif edad >= 18 and edad < 30:
    print ("Perteneces a la categoría : Adulto/a joven")
else: 
    print("Pertenece a la categoría Adulto/a")
