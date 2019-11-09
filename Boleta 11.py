#INPUT
consumidor=input("ingrese el nombre del consumidor:")
precio_moto=float(input("ingrese el precio de la moto:"))
precio_auto=float(input("ingrese el precio del auto:"))

#PROCESSING
total=(precio_moto+precio_auto)

#VERIFICADOR
buena_compra=(total>50000)

#OUTPUT
print("################################")
print("# BOLETA DE VENTA")
print("################################")
print("#")
print("# consumidor         :",consumidor)
print("# precio de la moto  :s/",precio_moto)
print("# precio del auto    :s/",precio_auto)
print("total                :s/",total)
print("################################")
print("¿se da una buena compra?",buena_compra )




