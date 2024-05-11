"""Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos.
Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja
de todo el grupo"""

estudiantes=int(input("ingrese la cantidad de notas:"))
suma=0
i=1
while (i<= estudiantes):
    print("ingrese el numero de la nota", i)
    nota=float(input())
    suma=suma+nota
    i+=1
prom =suma / estudiantes
print("el promedio de las notas es:", prom)
if estudiantes>=10:
    print("la nota mayor es de", estudiantes)
elif estudiantes <=5:
    print("la nota menor es de", estudiantes)
        