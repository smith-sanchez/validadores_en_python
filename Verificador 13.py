#Verificador 13
#INPUT
semiperimetro_del_triangulo=float(input("ingrese el semiperimetro del triangulo:"))
radio_del_circulo=float(input("ingrese el radio del circulo:"))

#PROCESSING
area_del_triangulo=(semiperimetro_del_triangulo*radio_del_circulo)

#VERIFICADOR
area=(area_del_triangulo>75)

#OUTPUT
print("el area del triangulo que circunscribe a un circulo es:",area_del_triangulo)
print("el area de este triangulo es mayor a 75:",area)
