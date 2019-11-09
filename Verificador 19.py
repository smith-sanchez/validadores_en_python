#Verificador 19
#INPUT
peso_atomico=float(input("ingrese el peso atomico:"))
numero_de_avogadros=float(input("ingrese el numero de avogadros:"))

#PROCESSING
peso_de_un_atomo=(peso_atomico/numero_de_avogadros)

#VERIFICADOR
peso=(peso_de_un_atomo<0.2)

#OUTPUT
print("el peso de un atomo es:",peso_de_un_atomo)
print("el peso es menor a 0.2:",peso)
