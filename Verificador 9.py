#vereficador 9
#input
intensidad_de_corriente=float(input("ingrese la intensidad de corriente:"))
resistencia_electrica=float(input("ingrese la resistencia electrica:"))

#procesing
diferencia_de_potencial=(intensidad_de_corriente*resistencia_electrica)

#vereficador
potencial_adecuado=(diferencia_de_potencial==17)

#output
print("la diferencia de potencial es:",diferencia_de_potencial)
print("¿el potencial adecuado es 17?",potencial_adecuado)
