"""El Centro de Industria y Comercio del Sena regional Tolima,quiere implementar un sistema de control de ingresos
que permita contar los estudiantes que ingresan durante los seis dias de la semana 
como tambien el número de estudiantes por formacion 
Para el ejemplo vamos a tener en ceenta las siguientes formaciones:
ADSO, produccion multimedia, Desarrollo de videojuegos, Sistemas
El algoritmo debe indicar el total de estudiantes clasificados por cada programa, por dia"""
    # Inicializar diccionario para almacenar el conteo de estudiantes por formación y día
conteo_estudiantes = {
        'ADSO': {'Lunes': 0, 'Martes': 0, 'Miércoles': 0, 'Jueves': 0, 'Viernes': 0, 'Sábado': 0},
        'Producción Multimedia': {'Lunes': 0, 'Martes': 0, 'Miércoles': 0, 'Jueves': 0, 'Viernes': 0, 'Sábado': 0},
        'Desarrollo de Videojuegos': {'Lunes': 0, 'Martes': 0, 'Miércoles': 0, 'Jueves': 0, 'Viernes': 0, 'Sábado': 0},
        'Sistemas': {'Lunes': 0, 'Martes': 0, 'Miércoles': 0, 'Jueves': 0, 'Viernes': 0, 'Sábado': 0}
    }
    # Solicitar ingreso de estudiantes por día y por formación
for formacion in conteo_estudiantes.keys():
        for dia in conteo_estudiantes[formacion].keys():
            cantidad = int(input(f"Ingrese la cantidad de estudiantes de {formacion} que ingresaron el día {dia}: "))
            conteo_estudiantes[formacion][dia] = cantidad

    # Generar reporte de ingresos por día y formación
print("\nReporte de ingresos por día y formación:")
for formacion, conteo_dias in conteo_estudiantes.items():
        print(f"\n{formacion}:")
        total_formacion = 0
        for dia, conteo in conteo_dias.items():
            print(f"{dia}: {conteo} estudiantes")
            total_formacion += conteo
        print(f"Total {formacion}: {total_formacion} estudiantes")

    # Calcular y mostrar el total de estudiantes ingresados en la semana
total_ingresos = sum(sum(conteo_dias.values()) for conteo_dias in conteo_estudiantes.values())
print(f"\nTotal de estudiantes ingresados en la semana: {total_ingresos}")