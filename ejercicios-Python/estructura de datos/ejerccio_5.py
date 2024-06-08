"""Una persona debe realizar un muestreo con 50 personas para determinar el
promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona.
Las categorías se determinar de acuerdo a la siguiente tabla:

joven=13-29
adulto=30-59
niños=0-12
ancianos=60
"""
#muestreo 50 personas 
# determinar el promedio
# determinar las categorias 

"Contadores "
pesoNiños = 0
pesoJovenes = 0
pesoAdultos = 0
pesoAncianos = 0

cantidadNiños = 0
cantidadJovenes = 0
cantidadAdultos = 0
cantidadAncianos = 0
for i in range(50):
    edad= int(input("ingresa la edad"))
    peso= int(input("ingresa el peso"))
if 0<= edad <= 12:
    pesoNiños +=peso
    cantidadNiños +=1
elif 13 <= edad <=29:
    pesoJovenes += peso
    cantidadJovenes +=1
elif 30 <= edad <= 59:
    pesoAdultos +=peso
    cantidadAdultos +=1
else:
    pesoAncianos +=peso
    cantidadAncianos +=1
promedioNiños = pesoNiños / cantidadNiños if cantidadNiños > 0 else 0    
promedioJovenes = pesoJovenes / cantidadJovenes if cantidadJovenes > 0 else 0
promedioAdultos = pesoAdultos / cantidadAdultos if cantidadAdultos > 0 else 0
promedioAncianos = pesoAncianos / cantidadAncianos if cantidadAncianos > 0 else 0

print("Promedio de peso de niños:", promedioNiños)
print("Promedio de peso de jóvenes:", promedioJovenes)
print("Promedio de peso de adultos:", promedioAdultos)
print("Promedio de peso de ancianos:", promedioAncianos)