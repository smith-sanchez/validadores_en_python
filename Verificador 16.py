#Verificador 16
#INPUT
base_mayor=float(input("ingrese el tamaño de la base mayor:"))
base_menor=float(input("ingrese el tamaño de la base menor:"))

#PROCESSING
base_media_del_trapecio=(base_menor+base_mayor)/2

#VERIFICADOR
base_media=(base_media_del_trapecio==50)

#OUTPUT
print("la base media del trapecio es:",base_media_del_trapecio)
print("la base media de este trapecio es igual a 50:",base_media)
