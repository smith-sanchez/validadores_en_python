#Verificador 11
#INPUT
perimetro_de_la_base=float(input("ingrese el perimetro:"))
altura=float(input("ingrese la atura:"))

#PROCESSING
area_lateral_del_prisma=(perimetro_de_la_base*altura)

#VERIFICADOR
area_lateral=(area_lateral_del_prisma!=125)

#OUTPUT
print("el area lateral del prisma es:",area_lateral_del_prisma)
print("¿el area lateral es diferente a 125?:",area_lateral)

