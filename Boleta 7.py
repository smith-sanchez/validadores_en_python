#INPUT
consumidor=input("ingrese el nombre del consumidor:")
numero_de_galones=int(input("ingrese el numero de galones de gasolina:"))
precio_por_galon=float(input("ingrese el valor por galon de gasolina:"))

#PROCESSING
total=(numero_de_galones*precio_por_galon)

#VERIFICADOR
precio_bajo=(total<=12)

#OUTPUT
print("##########################")
print("# BOLETA DE VENTA")
print("##########################")
print("#")
print("# consumidor          :",consumidor)
print("# cantidad de galones :",numero_de_galones)
print("# precio por galon    :s/",precio_por_galon)
print("total                 :s/",total)
print("##########################")
print("¿se vendio a bajo precio?",precio_bajo)

