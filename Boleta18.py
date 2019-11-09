#input
cliente=input("ingrese el nombre del cliente:")
precio=float(input("ingrese el precio del libro: "))
numero_producto=int(input("ingrese el numero del libro"))
#procesing
total=(numero_producto*precio)
#vereficador
gasto_necesario=(total>50)
#OUTPUT
print("############################")
print("# BOLETA DE VENTA")
print("############################")
print("#")
print("# el nombre el ciente es:       :",cliente)
print("# precio del libro es :s/",precio)
print("# numero de libros    :",numero_producto)
print("total                 :s/",total)
print("############################")
print("el clientegasto lo necesario?",gasto_necesario)
