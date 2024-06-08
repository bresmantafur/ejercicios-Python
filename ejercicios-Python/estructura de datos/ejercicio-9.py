 #Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos. 
import random

edadHombre = 0
numHombre = 0 

edadMujer=0
numMujer=0

for i in range(40):
    sexo = random.choice(['hombre' , 'mujer'])
     
    if sexo == 'hombre':
         edad = random.randint(15, 50)
         numHombre +=1
         edadHombre += edad
    else:
        edad=random.randint(15, 50)
        numMujer +=1
        edadMujer += edad
        
edadPromedioHombre = int(edadHombre / numHombre)
edadPromedioMujer = int(edadMujer / numMujer)

print(f'la edad promedio de los hombres es: {edadPromedioHombre}')
print(f'la edad promedio de las mujeres es: {edadPromedioMujer}')
        
 