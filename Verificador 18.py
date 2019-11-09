#Verificador 18
#INPUT
coeficiente_estatico=float(input("ingrese el coeficiente estatico:"))
normal=float(input("ingrese la normal que se le ejerce al cuepo:"))

#PROCESSING
fuerza_rozamiento=(coeficiente_estatico*normal)

#VERIFICADOR
fuerza=(fuerza_rozamiento>20)

#OUTPUT
print("la fuerza de rozamiento es:",fuerza_rozamiento)
print("esta fuerza que se le ejerce es mayor a 20:",fuerza)
