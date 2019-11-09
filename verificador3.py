#Verificador 3
#input

masa=float(input("ingrese la masa"))
velocidad=float(input("ingrese la velocidad"))

#procesing
energia_cinetica=(masa*velocidad**2)/2

#vereficador
energia=(energia_cinetica!=100)
#input

print("la energia cinetica es:",energia_cinetica)
print("¿la energia cinetica es diferente de 100?",energia)
