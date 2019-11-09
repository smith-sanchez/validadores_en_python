#vereficador 7
#input
numero_de_electrones=float(input("ingrese el numero de electrones:"))
carga_del_electron=float(input("ingrese el numreo de eleectrones:"))

#procesing
carga_electrica=(numero_de_electrones*carga_del_electron)

#vereficador
carga_electrica_regular=(carga_electrica>3.20)

#output
print("la carga electrica es ",carga_electrica)
print("¿la carga electrica es regular? ",carga_electrica_regular)
