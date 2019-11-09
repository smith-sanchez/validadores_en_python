#INPUT
frecuentador=input("ingrese el nombre del frecuentador:")
pm=float(input("ingrese el precio de la memoria de 16gb:"))
pc=float(input("ingrese el precio del chip:"))

#PROCESSING
total=(pm+pc)

#VERIFICADOR
frecuentador_comprensible=(total>15.5)

#OUTPUT
print("############################")
print("# BOLETA DE VENTA")
print("############################")
print("#")
print("# fecuentador         :",frecuentador)
print("# precio de memoria   :s/",pm)
print("# precio del chip     :s/",pc)
print("total                 :s/",total)
print("############################")
print("el frecuentador es comprensible?",frecuentador_comprensible)
