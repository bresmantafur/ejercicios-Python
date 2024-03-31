#desarrollar condocionales 
#elaborar un algoritmo que basado en el valor de una compra
#si la compra es mayor a 50000 el descuento sera de 10%
#si la compra es menor que 50000 el descuento sera de 5%
#si la compra es igual a 50000 el descuento sera de 7%
#si la compra es cero no tendra descuento
precio=int(input("digite el valor para el precio:"))
descuento=0.10
if precio>50000:
    compraTotal=precio-(precio*0.10)
    print("descuento",(compraTotal*descuento), "Valor a pagar es: ",compraTotal)
elif precio<50000:
    descuento=0.05
    compraTotal=precio-(precio*0.05)
    print("descuento",(compraTotal*descuento), "valor a pagar es: ", compraTotal)    
elif precio==50000:
    descuento=0.07
    compraTotal=precio-(precio*0.07)
print("descuento",(compraTotal*descuento), "valor a pagar es: ", compraTotal)
if precio==0:
    print("sin descuento", "valor es ", compraTotal)
