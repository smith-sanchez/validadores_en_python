#Verificador 12
#INPUT
area_de_la_seccion_recta=float(input("ingrese el area:"))
arista=float(input("ingrese la arista:"))

#PROCESSING
volumen_del_prisma_oblicuo=(area_de_la_seccion_recta*arista)

#VERIFICADOR
volumen=(volumen_del_prisma_oblicuo<=80)

#OUTPUT
print("el volumen del prisma oblicuo es:",volumen_del_prisma_oblicuo)
print("el volumen de este prisma es menor igual a 80:",volumen)

