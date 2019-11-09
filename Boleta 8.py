#INPUT
cliente=input("ingrese el nombre del cliente:")
cl=int(input("ingrese la cantidad de lapiceros:"))
pl=float(input("ingrese el precio de cada lapicero:"))
cb=int(input("ingrese la cantidad de borradores:"))
pb=float(input("ingrese el precio de cada borrador:"))

#PROCESSING
total=(cl*pl+cb*pb)

#VERIFICADOR
buena_venta=(total>800)

#OUTPUT
print("############################")
print("# BOLETA DE VENTA")
print("############################")
print("#")
print("# cliente                :",cliente)
print("# cantidad de lapiceros  :",cl)
print("# precio por lapicero    :s/",pl)
print("# cantidad de borradores :",cb)
print("# precio por borrador    :s/",pb)
print("total    :s/",total)
print("############################")
print("¿se da una buena venta?",buena_venta)
