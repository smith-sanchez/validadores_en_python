#INPUT
clientes=input("ingrese los nombres de los clientes:")
cantidad_de_platos=int(input("ingrese la cantidad de platos:"))
precio_por_plato=float(input("ingrese el precio por plato:"))

#PROCESSING
total=(cantidad_de_platos*precio_por_plato)

#VERIFICADOR
poca_ganancia=(total<=50)

#OUTPUT
print("#########################")
print("# BOLETA DE VENTA")
print("#########################")
print("#")
print("# clientes           :",clientes)
print("# cantidad de platos :",cantidad_de_platos)
print("# precio por plato   :s/",precio_por_plato)
print("total                :s/",total)
print("#########################")
print("¿se obtiene poca ganancia?",poca_ganancia)
