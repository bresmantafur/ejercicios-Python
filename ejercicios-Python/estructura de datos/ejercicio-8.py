#.un grupo de 23 estudiantes presentan un examen de algoritmia. Hacer un
#algoritmo que lea por cada estudiante la calificación obtenida. Al finalizar calcule e
#imprima:

import random

qualification1 = 0
qualification2 = 0
qualification3 = 0
qualification4 = 0

for estudiante in range(23):

    estudiante = random.randint(1, 100);

    if estudiante <= 50 :
        qualification4 += 1
    elif estudiante >= 50 and estudiante <= 70: 
         qualification3 += 1
    elif estudiante >= 70 and estudiante <= 80 :
        qualification2 += 1
    elif estudiante >= 80 :
        qualification1 += 1

print(f'{qualification1} Obtuvieron una calificacion mayor a 80');
print(f'{qualification2} Obtuvieron una calificacion mayor a 70 y menor 80');
print(f'{qualification3} Obtuvieron una calificacion mayor a 50 y menor a 70');
print(f'{qualification4} Obtuvieron una calificacion menor a 50');