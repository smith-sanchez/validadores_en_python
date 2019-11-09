#Verificador 4
#Input
masa=float(input("ingrese la masa"))
volumen=float(input("ingrese el volumen"))

#Procesing
densidad=(masa/volumen)

#verificador
densidad_del_cuerpo=(densidad<10)

#Output
print("la densidad es:",densidad)
print("¿la densidad del cuerpo es menor de 10?", densidad_del_cuerpo)



