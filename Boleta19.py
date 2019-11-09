#INPUT
nombre=input("ingrese el nombre del cliente:")
producto1=input("ingrese el nombre del producto:")
precio_p1=float(input("ingrese el precio del primer producto :"))
producto2=input("ingrese elnombre del segundo producto :")
precio_p2=float(input("ingrese el precio del producto 2:"))

#PROCESSING
total=(precio_p1+precio_p2)

#VEREFICADOR
total_suficiente=(total>200)

#OUTPUT
print("############################")
print("# BOLETA DE VENTA")
print("############################")
print("#")
print("# el nombre el ciente es:       :",nombre)
print("# producto 1 :",precio_p1," precio:",precio_p1)
print("# producto 2 :",precio_p2," precio:",precio_p2)
print("total                 :s/",total)
print("############################")
print("el total del precio es suficiente?",total_suficiente)
