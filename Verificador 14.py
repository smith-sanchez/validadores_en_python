#Verificador14
#INPUT   volumen de una uña cilindrica
radio_de_uña_cilindrica=float(input("ingrese el radio de la uña cilindrica es:"))
altura=float(input("ingrese altura de la uña cilindrica es:"))

#PROCESSING
volumen_de_la_uña_cilindrica=(2*altura*radio_de_uña_cilindrica**2)/3

#VERIFICADOR
volumen=(volumen_de_la_uña_cilindrica!=456)

#OUTPUT
print("el volumen de la uña cilindria es:",volumen_de_la_uña_cilindrica)
print("el volumen de este solido es diferente a 456:",volumen)
