#INPUT
nombre=input("ingrese el nombre del cliente:")
cantidad_docenas=int(input("ingrese la cantidad de docenas:"))
valor_por_docena=float(input("ingrese el valor por docena:"))

#PROCESSING
precio_total=(cantidad_docenas*valor_por_docena)

#VERIFICADOR
beneficia_la_compra=(precio_total==80)

#OUTPUT
print("###########################")
print("# BOLETA DE VENTA")
print("###########################")
print("#")
print("# nombre    :",nombre)
print("# cantidad  :",cantidad_docenas)
print("# valor     :s/",valor_por_docena)
print("total       :s/",precio_total)
print("###########################")
print("¿la compra es beneficiosa?",beneficia_la_compra)
