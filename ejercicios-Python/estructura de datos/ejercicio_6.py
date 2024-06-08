"""Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un
total de n personas"""



"contadores"
catidadHombres=0
cantidadMujeres=0
hombres=0
mujeres=0
while True:
    genero=input("ingrese (m) para hombres y ingrese (f) para mujeres para terminar(salir): " )
    if genero.lower()=="salir":
        break

    if genero=="f":
        cantidadMujeres+=1
    if genero=="m":
        catidadHombres+=1

    totalCantidad=cantidadMujeres+catidadHombres
print("la cantidad total es :", totalCantidad)
print ("el promedio de mujeres es:", cantidadMujeres)
print("el promedio de hombres es:", catidadHombres)
