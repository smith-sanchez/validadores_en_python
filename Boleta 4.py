#INPUT
consumidor=input("ingrese el nombre del consumidor:")
articulo1=input("ingrese el primer articulo:")
precio1=float(input("precio del primer articulo:"))
articulo2=input("ingrese el segundo articulo:")
precio2=float(input("precio segundo articulo:"))

#PROCESSING
precio_total=(precio1+precio2)

#VERIFICADOR
consumidor_rendible=(precio_total>500)

#OUTPUT
print("##############################")
print("# BOLETA DE VENTA")
print("##############################")
print("#")
print("# consumidor   :",consumidor)
print("# articulo 1   :",articulo1, "precio: s/",precio1)
print("# articulo 2   :",articulo2, "precio: s/",precio2)
print("total          :s/",precio_total)
print("##############################")
print("¿el consumidor es rendible?",consumidor_rendible)
