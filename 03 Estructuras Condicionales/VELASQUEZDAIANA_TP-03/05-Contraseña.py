#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string.

contraseña = input("Ingrese una contraseña (entre 8 y 14 caracter): ")

if len(contraseña) >=8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else: 
     print("Por favor, ingrese una contraseña de entre 8 a 14 caracteres")

#El comando len() se usa para obtener la longitud de un bojeto.
# En cadenas: Cuenta los caracteres.   ----> ej: print(len("Hola"))  -> salida:4
# Listas, tulplas: cuenta los elementos.  -----> ej: print(len([1,2,3,4]))   -> salida:4
# Diccionarios: cuenta las claves.   -----> ej: print(len({'a': 1, 'b':2, 'c':3 }))   -> salida:3 