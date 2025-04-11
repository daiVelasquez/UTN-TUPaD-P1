#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla. 

    
texto = input("Ingresa una frase o palabra: ")

# lower() pasamos el texto a minúscula
if texto[-1].lower() in 'aeiou': #devuelve true si el último caracter se encuentra en 'aeiou'
    texto += '!'  

print("Resultado:", texto)
