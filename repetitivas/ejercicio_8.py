import random
valorCompra=int(input("se ingrasa el valor de la compra: "))
aleatorio = random.choice(["con la valota roja", "cion la balota verde", "con la balota azul", "con la balota amarrilla", "con la balota negra"])
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