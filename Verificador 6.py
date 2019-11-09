#Verificador 6
#Input
masa=float(input("ingrese la cantidad de masa"))
latente_de_fusion=float(input("ingrese el latente de fusion"))

#Procesing
calor_latente=(masa*latente_de_fusion)

#Verificador
calor_total=(calor_latente<523)

#ouput
print("el calor latente es:",calor_latente)
print("el calor latente es menor que 523:",calor_total)
