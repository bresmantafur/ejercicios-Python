import random 
valorCompra=int(input("ingresa el valor de la compra: "))
aleatorio = random.choice(["con la balota roja", "con la balota verde", "con la balota azul", "con la balota amarrilla", "con la balota negra"])

print(aleatorio)
if aleatorio == "con la balota roja":
    balotaRoja = valorCompra*0.10 
    print("El descuento total a pagar seria de: ",balotaRoja)
elif aleatorio == "con balota verde":
    balotaVerde = valorCompra*0.15
    print("El descuento total a pagar seria de: ", balotaVerde)

elif aleatorio == "con la balota azul":
    balotaAzul = valorCompra * 0.20
    print("El descuento total a pagar seria de: ", balotaAzul)
elif aleatorio == "con la balota amarilla":
    balotaAmarilla = valorCompra*0.50
    print("el decuento a pagar seria de:", balotaAmarilla)
elif aleatorio == "con la balota negra":
    balotaNegra = valorCompra*1.0
    print("el valor a pagar seria de: ", balotaNegra)

