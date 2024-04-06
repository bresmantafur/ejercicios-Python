dias_semana=[" lunes "," martes ", "miercoles", " jueves ", " viernes ", " sabado "]
registro_estudiantes={}
for dia in dias_semana:
    cantidad_de_estudiantes= int(input(f"indrese la cantidad de estudiantes registrados para el dia{ dia }: "))
    registro_estudiantes[dia] = cantidad_de_estudiantes

print("registro de estudiantes por dia:")
for dia, cantidad in registro_estudiantes.items():
    print(f"el numero de estudiantes que ingrsaron el dia {dia} es: {cantidad}" )
total_estudiantes=sum(registro_estudiantes.values())
partes=4
ADSO=total_estudiantes//partes
print("El total de estudiates que ingresaron a la formacion de ADSO es:", ADSO)

produccion_multimedia =total_estudiantes//partes
print("El total de estudiates que ingresaron a la formacion de produccion Multimedia es:", produccion_multimedia)

Desarrollo_de_videojuegos=total_estudiantes//partes
print("El total de estudiates que ingresaron a la formacion de Videojuegos es:", Desarrollo_de_videojuegos)

Sistemas=total_estudiantes//partes
print("El total de estudiates que ingresaron a la formacion de sistemas es:", Sistemas)
