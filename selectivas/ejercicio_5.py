"""• La cantidad de estudiantes que obtuvieron una calificación menor a 50. 
• La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 70.
• La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80. 
• La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
La calificación obtenida en el examen de algoritmia debe ser entre 1 y 100."""
#Declaracion de variables
#hacer un algoritmo que lea por cada estudiante la calificacion obtenida
contador1=0
contador2=0
contador3=0
contador4=0
calificacion1=int(input("ingrese la cantidad de nota del estudiante1 " ))
calificacion2=int(input("ingrese la cantidad de nota del estudiante2 " ))
calificacion3=int(input("ingrese la cantidad de nota del estudiante3 " ))
calificacion4=int(input("ingrese la cantidad de nota del estudiante4 " ))
calificacion5=int(input("ingrese la cantidad de nota del estudiante5 " ))
calificacion6=int(input("ingrese la cantidad de nota del estudiante6 " ))
calificacion7=int(input("ingrese la cantidad de nota del estudiante7 " ))
calificacion8=int(input("ingrese la cantidad de nota del estudiante8 " ))
calificacion9=int(input("ingrese la cantidad de nota del estudiante9 " ))
calificacion10=int(input("ingrese la cantidad de nota del estudiante10 " ))
if calificacion1< 50:
    contador1 +=1
if calificacion2< 50:
    contador1 +=1
if calificacion3< 50:
    contador1 +=1
if calificacion4< 50:
    contador1 +=1
if calificacion5< 50:
    contador1 +=1
if calificacion6< 50:
    contador1 +=1
if calificacion7< 50:
    contador1 +=1
if calificacion8< 50:
    contador1 +=1
if calificacion9< 50:
    contador1 +=1
if calificacion10< 50:
    contador1 +=1
if calificacion1<70 and calificacion1>=50 :
    contador2 +=1
if calificacion2<70 and calificacion2>=50 :
    contador2 +=1
if calificacion3<70 and calificacion3>=50 :
    contador2 +=1
if calificacion4<70 and calificacion4>=50:
    contador2 +=1
if calificacion5<70 and calificacion5>=50:
    contador2 +=1
if calificacion6<70 and calificacion6>=50:
    contador2 +=1
if calificacion7<70 and calificacion7>=50:
    contador2 +=1
if calificacion8<70 and calificacion8>=50:
    contador2 +=1
if calificacion9<70 and calificacion9>=50:
    contador2 +=1
if calificacion10<70 and calificacion10>=50:
    contador2 +=1
if calificacion1<80 and calificacion1>=70:
    contador3 +=1
if calificacion2< 80 and calificacion2>=70:
    contador3 +=1
if calificacion3<80 and calificacion3>=70:
    contador3 +=1
if calificacion4<80 and calificacion4>=70:
    contador3 +=1
if calificacion5<80 and calificacion5>=70:
    contador3 +=1
if calificacion6<80 and calificacion6>=70:
    contador3 +=1
if calificacion7<80 and calificacion7>=70:
    contador3 +=1
if calificacion8<80 and calificacion8>=70:
    contador3 +=1
if calificacion9<80 and calificacion9>=70: 
    contador3 +=1
if calificacion10<80 and calificacion10>=70:
    contador3 +=1
if calificacion1>=80:
    contador4 +=1
if calificacion2>=80:
    contador4 +=1
if calificacion3>=80:
    contador4 +=1
if calificacion4>=80:
    contador4 +=1
if calificacion5>=80:
    contador4 +=1
if calificacion6>=80:
    contador4 +=1
if calificacion7>=80:
    contador4 +=1
if calificacion8>=80:
    contador4 +=1
if calificacion9>=80:
    contador4 +=1
if calificacion10>=80:
    contador4 +=1
print("cantidad de estudiantes con calificaciones")
print("menor a 50", contador1)
print("igual a 50 o menor a 70", contador2)
print("igual a 70 o menor a 80",contador3)
print("igual a 80 o mas",contador4)
