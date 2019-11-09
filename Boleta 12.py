#INPUT
comprador=input("ingrese el nombre del comprador:")
cantidad_de_pantalones=int(input("ingrese la cantidad de pantalones comprados:"))
precio_por_pantalon=float(input("ingrese el precio por pantalon:"))

#PROCESSING
total=(cantidad_de_pantalones*precio_por_pantalon)

#VERIFICADOR
exelente_comprador=(total>600)

#OUTPUT
print("##########################")
print("# BOLETA DE VENTA")
print("##########################")
print("#")
print("# comprador              :",comprador)
print("# cantidad de pantalones :",cantidad_de_pantalones)
print("# precio por pantalon    :s/",precio_por_pantalon)
print("total                    :s/",total)
print("##########################")
print("¿es un exelente comprador?",exelente_comprador)
