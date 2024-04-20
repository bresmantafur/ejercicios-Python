"""Leer 21 números e imprimir cuantos son positivos, cuantos negativos y cuantos neutros"""

positivos=0
negativos=0 
neutros=0
for i in range (0, 21):
    numero=int(input("ingrese el numero: "))
    if numero>0:
        positivos+=1
    elif numero<0:
        negativos+=1
    elif numero==0:
        neutros+=1
print("los numeros negativos son:", negativos)
print("los numeros positivos son:", positivos)
print("los numeros neutros son:", neutros)