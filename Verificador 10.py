#vereficador 10
#input
velocidad=float(input("ingrese la velocidad del movil:"))
tiempo=float(input("ingrese el tiempo:"))

#procesing
espacio=(velocidad*tiempo)

#vereficador
espacio_adecuado=(espacio>=100)

#output
print("la distncia del movil es:",espacio)
print("¿el espacio es adecuado?",espacio_adecuado)
