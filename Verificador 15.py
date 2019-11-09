#Verificador 15                           area lateral de una piramide
#INPUT
semiperimetro_de_la_base=float(input("ingrese el semiperimetro de la base de la piramide:"))
apotema=float(input("ingrese el apotema de la piramide:"))

#PROCESSING
areal_lateral_de_la_piramide=(semiperimetro_de_la_base*apotema)


#VERIFICADOR
areal_lateral=(areal_lateral_de_la_piramide>50)

#OUTPUT
print("el area lateral de la piramide es:",areal_lateral_de_la_piramide)
print("el area lateral de este solido es mayor a 50:",areal_lateral)
