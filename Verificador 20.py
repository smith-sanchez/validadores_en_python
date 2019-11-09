#Verificador 20
#Esta calculadora realizara el calculo de la energia de un cuerpo en reposo
masa=float(input("ingrese la masa:"))
velocidad_de_la_luz=float(input("ingrese la velocidad de la luz:"))

#PROCESSING
energia_del_cuerpo=(masa*velocidad_de_la_luz**2)

#VERIFICADOR
energia=(energia_del_cuerpo>15)

#OUTPUT
print("la energia del cuerpo es:",energia_del_cuerpo)
print("la energia de este cuerpo es mayor a 15:",energia)
