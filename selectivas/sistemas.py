#permite saber el registro de los estudiantes
registro_estudiantes={}
contador=1
while contador <= 6:
    dia = ""
    if contador == 1:
        dia = "lunes"
    elif contador == 2:
        dia = "martes"
    elif contador == 3:
        dia = "miércoles"
    elif contador == 4:
        dia = "jueves"
    elif contador == 5:
        dia = "viernes"
    elif contador == 6:
        dia = "sábado"

    cantidad_de_estudiantes = int(input(f"Ingrese la cantidad de estudiantes registrados para el día {dia}: "))
    registro_estudiantes[dia] = cantidad_de_estudiantes
    contador += 1

print("Registro de estudiantes por día:")
for dia, cantidad in registro_estudiantes.items():
    print(f"El número de estudiantes que ingresaron el día {dia} es: {cantidad}")

total_estudiantes = sum(registro_estudiantes.values())
partes = 4
ADSO = total_estudiantes // partes
print("El total de estudiantes que ingresaron a la formación de ADSO es:", ADSO)

produccion_multimedia = total_estudiantes // partes
print("El valor de la variable Producción Multimedia es:", produccion_multimedia)

desarrollo_de_videojuegos = total_estudiantes // partes
print("El valor de la variable Desarrollo de Videojuegos es:", desarrollo_de_videojuegos)

sistemas = total_estudiantes // partes
print("El valor de la variable Sistemas es:", sistemas)