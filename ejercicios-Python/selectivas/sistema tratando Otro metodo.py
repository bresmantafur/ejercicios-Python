"""El Centro de Industria y Comercio del Sena regional Tolima,quiere implementar un sistema de control de ingresos
que permita contar los estudiantes que ingresan durante los seis dias de la semana 
como tambien el número de estudiantes por formacion 
Para el ejemplo vamos a tener en ceenta las siguientes formaciones:
a. ADSO
b. produccion multimedia 
c. Desarrollo de videojuegos
d. Sistemas
El algoritmo debe indicar el total de estudiantes clasificados por cada programa, por dia"""

registro_estudiantes = {}
contador = 1
#muestra los 6 dias de la semana
while contador <= 6:
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

# divide el número total de estudiantes en las cuatro formaciones
adso_estudiantes = total_estudiantes // partes
produccion_multimedia_estudiantes = total_estudiantes // partes
desarrollo_de_videojuegos_estudiantes = total_estudiantes // partes
sistemas_estudiantes = total_estudiantes // partes

# Imprime el número de estudiantes divididos en cada formacion
print("Número de estudiantes dividido en las cuatro formaciones:")
print("ADSO:", adso_estudiantes)
print("Producción Multimedia:", produccion_multimedia_estudiantes)
print("Desarrollo de Videojuegos:", desarrollo_de_videojuegos_estudiantes)
print("Sistemas:", sistemas_estudiantes)

# Registra los estudiantes por formación
registro_adso = {}
registro_produccion_multimedia = {}
registro_desarrollo_de_videojuegos = {}
registro_sistemas = {}

for dia, cantidad in registro_estudiantes.items():
    registro_adso[dia] = adso_estudiantes
    registro_produccion_multimedia[dia] = produccion_multimedia_estudiantes
    registro_desarrollo_de_videojuegos[dia] = desarrollo_de_videojuegos_estudiantes
    registro_sistemas[dia] = sistemas_estudiantes

print("Reporte de estudiantes que ingresaron:")
for dia, cantidad in registro_estudiantes.items():
    print(f"{cantidad} estudiantes ingresaron el día {dia}.")

#El Total de estudiantes clasificados por cada formación
total_adso = sum(registro_adso.values())
total_produccion_multimedia = sum(registro_produccion_multimedia.values())
total_desarrollo_de_videojuegos = sum(registro_desarrollo_de_videojuegos.values())
total_sistemas = sum(registro_sistemas.values())

print("Total de estudiantes clasificados por cada programa:")
print("ADSO:", total_adso)
print("Producción Multimedia:", total_produccion_multimedia)
print("Desarrollo de Videojuegos:", total_desarrollo_de_videojuegos)
print("Sistemas:", total_sistemas)