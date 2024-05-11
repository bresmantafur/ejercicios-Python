#La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad
#de Ibagué, cuantos entran con calcomanía de cada color. Conociendo el ultimo
#dígito de la placa de cada carro, se puede determinar el color de la calcomanía
#utilizando la siguiente relación

import random
amarillo=0
rosa=0
roja=0
verde=0
azul=0

for i in range(30):
    etiqueta = random.randint(0,9)
    
    if etiqueta == 1 or etiqueta == 2:
        amarillo +=1
    elif etiqueta == 3 or etiqueta == 4:
        rosa +=1
    elif etiqueta == 5 or etiqueta == 6:
        roja +=1
    elif etiqueta == 7 or etiqueta == 8:
        verde +=1
    else:
        azul +=1
        
print(f'{amarillo} tiee etiqueta amarilla')   
print(f'{rosa} tiee etiqueta rosa')  
print(f'{roja} tiee etiqueta roja')  
print(f'{verde} tiee etiqueta verde')  
print(f'{azul} tiee etiqueta azul')      
        
        