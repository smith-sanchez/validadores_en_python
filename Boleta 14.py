#INPUT
clientes=input("ingrese los nombres de los clientes:")
ne=int(input("ingrese el numero de entradas:"))
pe=float(input("ingrese el valor de cada entrada:"))

#PROCESSING
total=(ne*pe)

#VERIFICADOR
clientes_buenos=(total>200)

#OUTPUT
print("##################################")
print("# BOLETA DE VENTA")
print("##################################")
print("#")
print("# cliente           :",clientes)
print("# centidad          :",ne)
print("# precio unitario   :s/",pe)
print("total               :s/",total)
print("##################################")
print("¿son buenos clientes?",clientes_buenos)

