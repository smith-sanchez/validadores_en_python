#Verificador 5
#Input
angulo=float(input("ingrese el angulo:"))
tiempo=float(input("ingrese el tiempo:"))

#Procesing
velocidad_angular=(angulo/tiempo)

#Verificador
velocidad=(velocidad_angular==9)

#output
print("la velocidad angular es:",velocidad_angular)
print("¿la velocidad angular es igual que 9?:",velocidad)
