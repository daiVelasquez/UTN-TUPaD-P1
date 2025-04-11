 #Utilizando la información aportada en la siguiente tabla sobre las estaciones del año:

 #Periodo del año                       |     Estación en el hemisferio norte          |        Estación en el hemisferio sur
 #---------------------------------------------------------------------------------------------------------------------------
 #Desde el 21 de diciembre hasta        |     Invierno                                 |         Verano 
 #el 20 de marzo (incluidos)            |                                              |
 #-------------------------------------------------------------------------------------------------------------------------
 #Desde el 21 de marzo hasta el 20      |      Primavera                               |           Otoño
 #de junio (incluidos)                  |                                              | 
 #--------------------------------------------------------------------------------------------------------------------------
 #Desde el 21 de junio hasta el 20      |       Verano                                 |           Invierno
 #de septiembre (incluidos)             |                                              |
 #--------------------------------------------------------------------------------------------------------------------------
 #Desde el 21 de septiembre hasta       |       Otoño                                  |            Primavera
 #el 20 de diciembre (incluidos)        |                                              |
 #-------------------------------------------------------------------------------------------------------------------------
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano. 


hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ")
mes = input("¿Qué mes es? (ej. marzo): ")
dia = int(input("¿Qué día es? (número): "))

# Convertimos el mes a minúsculas
mes = mes.lower()


meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}


if mes not in meses:
    print("Mes inválido.")
else:
    mes_num = meses[mes]

  
    if hemisferio.upper() == "N":
        if (mes_num == 12 and dia >= 21) or (mes_num in [1, 2]) or (mes_num == 3 and dia < 21):
            estacion = "Invierno"
        elif (mes_num == 3 and dia >= 21) or (mes_num in [4, 5]) or (mes_num == 6 and dia < 21):
            estacion = "Primavera"
        elif (mes_num == 6 and dia >= 21) or (mes_num in [7, 8]) or (mes_num == 9 and dia < 23):
            estacion = "Verano"
        else:
            estacion = "Otoño"
    elif hemisferio.upper() == "S":
        if (mes_num == 6 and dia >= 21) or (mes_num in [7, 8]) or (mes_num == 9 and dia < 23):
            estacion = "Invierno"
        elif (mes_num == 9 and dia >= 23) or (mes_num in [10, 11]) or (mes_num == 12 and dia < 21):
            estacion = "Primavera"
        elif (mes_num == 12 and dia >= 21) or (mes_num in [1, 2]) or (mes_num == 3 and dia < 21):
            estacion = "Verano"
        else:
            estacion = "Otoño"
    else:
        estacion = "Hemisferio no válido"

 
    print("Estás en", estacion)
