"""En un supermercado, se ha implementado la estrategia de descuento, según el valor de la compra y la balota que el cliente saque de una bolsa secreta. Las condiciones se listan a continuación:
- si el valor de la compra es superior igual a 50.000 pesos y saca:
a. balota roja el descuento será del 10%
b. balota verde el descuento será del 15%
c. balota azul el descuento será del 20%
d. balota amarilla el descuento será del 50%
e. balota negra el descuento será del 100%
-Si la compra es inferior a 50.000 pesos no participará del sorteo, para este caso se muestra un mensaje y se  imprimirá solo el valor a pagar."""
#compra ejercicio
valorCompra=int(input("se ingrasa el valor de la compra: "))
balota=input("se ingresa el color de la balota: ")
if valorCompra>=50000 and balota=="rojo":
    descuento=0.10
    print(valorCompra*descuento)
elif valorCompra>=50000 and balota=="verde":
    descuento=0.15
    print(valorCompra*descuento)
elif valorCompra>=50000 and balota=="azul":
    descuento=0.20
    print(valorCompra*descuento)
elif valorCompra>=50000 and balota=="amarilla":
    descuento=0.50
    print(valorCompra*descuento)
elif valorCompra>=50000 and balota== "negra":
    descuento=100
    print(valorCompra*descuento)
elif valorCompra<=50000:
    print("no participas")