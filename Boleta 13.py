#INPUT
cliente=input("ingrese el nombre del cliente:")
cantidad=int(input("ingrese la cantidad laptops:"))
pu=float(input("ingrese el precio unitario de la laptop:"))

#PROCESSING
total=(cantidad*pu)

#VERIFICADOR
buena_ganacia=(total>200)

#OUTPUT
print("######################")
print("# BOLETA DE VENTA")
print("######################")
print("#")
print("# cliente             :",cliente)
print("# cantidad de laptops :",cantidad)
print("# precio unitario     :s/",pu)
print("total                 :s/",total)
print("######################")
print("¿se obtiene buena ganancia?",buena_ganacia)


