#INPUT
cliente=input("ingrese el nombre del cliente:")
cantidad=int(input("ingrese la cantidad de rectificadores:"))
pu=float(input("ingrese el precio unitario por rectificador:"))

#PROCESSING
total=(cantidad*pu)

#VERIFICADOR
disponibilidad_del_comprador=(total<300)

#OUTPUT
print("########################")
print("# BOLETA DE VENTA")
print("########################")
print("#")
print("# cliente:",cliente)
print("# cantidad de rectificadores  :",cantidad)
print("# precio de cada rectificador :s/",pu)
print("# total                       :s/",total)
print("########################")
print("¿disponibilidad del comprador?",disponibilidad_del_comprador)
