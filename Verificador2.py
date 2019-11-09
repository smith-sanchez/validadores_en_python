#Verificador 2
#input
fuerza=float(input("ingrese la fuerza:"))
area=float(input("sigue el area:"))
#procesing
presion=fuerza/area

#verificador
presion_maxima=(presion>500)

#output
print("fuerza=",presion)
print("¿la presion es maxima?",presion_maxima)
