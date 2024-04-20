"""Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos números."""
suma=0
for i in range(1,11):
    num=int(input(f"ingrese los numeros negativos{i}: "))
    if num<0:
        num*=-1
        suma = suma + num
        print("imprimir los numeros positivos son:", num)
        print("el total de la suma es:", suma)

    
