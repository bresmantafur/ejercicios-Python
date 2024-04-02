"""El Centro de Industria y Comercio del Sena regional Tolima,quiere implementar un sistema de control de ingresos
que permita contar los estudiantes que ingresan durante los seis dias de la semana 
como tambien el número de estudiantes por formacion 
Para el ejemplo vamos a tener en ceenta las siguientes formaciones:
a. ADSO
b. produccion multimedia 
c. Desarrollo de videojuegos
d. Sistemas
El algoritmo debe indicar el total de estudiantes clasificados por cada programa, por dia"""

registro_Estudiantes=0
dias=("lunes", "marteas", "miercoles", "jueves", "viernes", "sabado")
def dividir_numero(numero):
    partes=[numero / 4] *4
    return partes
registro_Estudiantes=int(input("ingrse un numero de estudiantes:"))
partes= dividir_numero(registro_Estudiantes)
print("el numero de estudiantes divididos en cada formacion es:", partes)