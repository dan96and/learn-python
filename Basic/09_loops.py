### Loops ###
for i in range (2,5):
    print (i)

#Recorrer una lista:
frutas = ["Manzana", "Pera", "Melón", "Platano"]

#Recorrer una lista con un for
for fruta in frutas:
    if fruta == "Pera":
        continue #Continue: Salta a la siguiente iteración
    elif fruta == "Melón":
        break #Break: Sale del bucle
    print(fruta)

#Bucle usando while
contador = 0
while contador <= 5:
    print("Contador es: ", contador)
    contador+=1

print("END")