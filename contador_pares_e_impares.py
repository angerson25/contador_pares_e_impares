#INPUT
numero = int(input("\nDigite un numero: "))
cant_impares=0
cant_pares=0

#PROCESSING
while numero != 0:
    residuo=numero % 2
    if residuo==1:
        cant_impares = cant_impares + 1
    else:
        cant_pares = cant_pares + 1

    numero = int(input("\nDigite un numero: "))
    
#OUTPUT
print("\nLa cantidad de numeros pares es "+str(cant_pares))
print("\nLa cantidad de numeros impares es "+str(cant_impares))
        





