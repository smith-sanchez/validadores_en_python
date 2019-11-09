#INPUT
cliente=input("ingrese el nombre del cliente:")
cantidad=int(input("ingrese la cantidad de rodajes:"))
pu=float(input("ingrese el precio del rodaje:"))

#PROCESSING
total=(cantidad*pu)

#VERIFICADOR
buena_ganancia=(total>120)

#OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# cliente         :",cliente)
print("# cantidad        :",cantidad)
print("# precio unitario :s/",pu)
print("total             :s/",total)
print("#######################")
print("se obtiene buena ganancia?",buena_ganancia)
