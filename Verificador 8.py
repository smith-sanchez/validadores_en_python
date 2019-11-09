#verficador 8
#input
carga_electrica_acumulada=float(input("ingrese la carga electrica acumulada:"))
diferencia_de_potencial=float(input("registre la diferencia de potencial:"))

#procesing
capacitancia=(carga_electrica_acumulada/diferencia_de_potencial)

#vereficadores
capacitancia_adecuada=(capacitancia==4)

#output
print("la capacitancia es",capacitancia)
print("¿la capacitancia adecuada es 4?",capacitancia_adecuada)
