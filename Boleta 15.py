#INPUT
consumidores=input("ingrese los nombres de los consumidores:")
cantidad=int(input("ingrese la cantidad de tickets:"))
pt=float(input("ingrese el precio del tickets:"))

#PROCESSING
total=(cantidad*pt)

#VERIFICADOR
disponibilidad_de_los_consumidores=(total<30)

#OUTPUT
print("######################")
print("# BOLETA DE VENTA")
print("######################")
print("#")
print("# consumidores     :",consumidores)
print("# cantidad         :",cantidad)
print("# precio unitario  :s/",pt)
print("total              :s/",total)
print("######################")
print("¿la venta esta disponible?",disponibilidad_de_los_consumidores)
