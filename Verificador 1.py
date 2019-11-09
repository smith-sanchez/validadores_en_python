#verificadaor1
#INPUT

masa=float(input("ingrese la masa:"))
aceleracion=float(input("ingrese la acceleracion:"))

#PROCESSING
fuerza=masa*aceleracion

#VERIFICADOR
fuerza_regular=(fuerza>100)

#OUTPUT
print("La fuerza es:",fuerza)
print("¿tiene fuerza regular?:",fuerza_regular)
