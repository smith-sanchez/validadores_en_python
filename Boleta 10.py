#INPUT
cliente=input("ingrese el nombre del cliente:")
precio_polo=float(input("ingrese el precio del polo:"))
precio_pantalon=float(input("ingrese el precio del pantalon:"))

#PROCESSING
precio_total=(precio_polo+precio_pantalon)

#VERIFICADOR
cliente_favorable=(precio_total>400)

#OUTPUT
print("###################################")
print("# BOLETA DE VENTA")
print("###################################")
print("#")
print("# nombre del cliente        :",cliente)
print("# precio del polo           :",precio_polo)
print("# precio del  pantalon      :s/",precio_pantalon)
print("#total                      :s/",precio_total)
print("###################################")
print("¿cliente es rendible?",cliente_favorable)
