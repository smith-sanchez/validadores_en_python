#INPUT
pasajero=input("ingrese el nombre del pasajero:")
na=int(input("ingrese el numero de asientos:"))
va=float(input("ingrese el valor por asiento:"))

#PROCESSING
total=(na*va)

#VERIFICADOR
pasajero_comprensible=(total<50)

#OUTPUT
print("########################")
print("# BOLETA DE VENTA")
print("########################")
print("#")
print("# pasajero              :",pasajero)
print("# numero de asientos    :",na)
print("# valor de cada asiento :s/",va)
print("# total                 :s/",total)
print("########################")
print("¿pasajero comprensible?:",pasajero_comprensible)
