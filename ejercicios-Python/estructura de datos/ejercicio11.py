"""
Pedir los datos de los alumnos, estos son: sexo, edad y altura. Al final del programa
se deberá mostrar la cantidad de hombres, la cantidad de mujeres, la altura promedio
,la cantidad de alumnos que tienen una altura mayor a 1.70 cm, la cantidad de alumnos
que tiene una altura menor o igual a 1.50 cm. El programa debe finalizar cuando la edad
sea igual a 0.
"""
# Inicializamos las variables para contar hombres, mujeres y alturas
cantidad_hombres = 0
cantidad_mujeres = 0
altura_total = 0
cantidad_altura_mayor_170 = 0
cantidad_altura_menor_150 = 0

# Bucle para ingresar los datos de los alumnos
while True:
    sexo = input("Ingrese el sexo del alumno (H/M): ").upper()
    if sexo == 'H':
        cantidad_hombres += 1
    elif sexo == 'M':
        cantidad_mujeres += 1
    else:
        print("Sexo no válido. Por favor ingrese 'H' para hombre o 'M' para mujer.")
        continue
    
    edad = int(input("Ingrese la edad del alumno (0 para salir): "))
    if edad == 0:
        break
    
    altura = float(input("Ingrese la altura del alumno en centímetros: "))
    
    # Actualizamos la altura total
    altura_total += altura
    
    # Verificamos las alturas
    if altura > 170:
        cantidad_altura_mayor_170 += 1
    elif altura <= 150:
        cantidad_altura_menor_150 += 1

# Calculamos la altura promedio
altura_promedio = altura_total / (cantidad_hombres + cantidad_mujeres)

# Mostramos los resultados
print("\nResultados:")
print("Cantidad de hombres:", cantidad_hombres)
print("Cantidad de mujeres:", cantidad_mujeres)
print("Altura promedio:", altura_promedio, "cm")
print("Cantidad de alumnos con altura mayor a 170 cm:", cantidad_altura_mayor_170)
print("Cantidad de alumnos con altura menor o igual a 150 cm:", cantidad_altura_menor_150)
