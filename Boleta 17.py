#INPUT
cliente=(input("ingrese el nommbre del cliente: "))
precio_mochila=float(input("ingrese el precio de la mochila:"))
numero=int(input("numero de mochilas:"))

#procesing
total=(precio_mochila*numero)

#vereficador
cliente_necesario=(total>120)

#OUTPUT
print("############################")
print("# BOLETA DE VENTA")
print("############################")
print("#")
print("# el nombre el ciente es:       :",cliente)
print("# precio de la mochila es :s/",precio_mochila)
print("# numero de mochilas    :",numero)
print("total                 :s/",total)
print("############################")
print("cliente necesariopara el negocio?",cliente_necesario)
