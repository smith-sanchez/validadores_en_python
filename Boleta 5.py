#INPUT
comprador=input("ingrese el nombre del comprador:")
cajas_de_chocolate=int(input("ingrese el numero de cajas de chocolate:"))
precio_por_caja=float(input("ingrese el precio por caja de chocolate:"))

#PRECESSING
total=(cajas_de_chocolate*precio_por_caja)

#VERIFICADOR
mucha_ganancia=(total>1500)

#OUTPUT
print("###################################")
print("# BOLETA DE VENTA")
print("###################################")
print("#")
print("# comprador          :",comprador)
print("# cajas de chocolate :",cajas_de_chocolate)
print("# precio por caja    :s/",precio_por_caja)
print("total                :s/",total)
print("###################################")
print("¿se obtiene mucha ganancia?",mucha_ganancia)













