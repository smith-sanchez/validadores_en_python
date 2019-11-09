#INPUT
nombre=input("ingrese el nombre del cliente:")
marca_reloj=input("ingrese la marca del reloj:")
precio_reloj=float(input("ingrese el precio del reloj:"))
cantidad=int(input("ingrese la cantidad de reloj:"))

#PROCESSING
total=(cantidad*precio_reloj)

#VERIFICADOR
cliente_rendible=(total>60)

#OUTPUT
print("###################################")
print("# BOLETA DE VENTA")
print("###################################")
print("#")
print("# nombre del cliente        :",nombre)
print("# marca del reloj           :",marca_reloj)
print("# precio por cada reloj     :s/",precio_reloj)
print("total                       :s/",total)
print("###################################")
print("¿cliente es rendible?",cliente_rendible)
