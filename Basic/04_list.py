### List ###

#Declaración de listas
my_list = list()
my_other_list = []

#Podemos llenar listas con cualquier tipo de dato
my_list = [35, 32, 22, 35]
my_other_list = [28, 1.83, "Daniel", "Andres", True]

print(my_list)
print(len(my_list))

#Imprimir el primer valor de la lista
print(my_other_list[0])
#Imprimir el ultimo valor de la lista
print(my_other_list[-1])

#Podemos desempaquetar los valores de una lista en variables
age, size, name, surname, check = my_other_list

#Concatenar dos listas
print(my_list + my_other_list)

#Agregar el valor al final de la lista
my_other_list.append("Red")

#Cambiar el valor de una posición
my_other_list[0] = 30

#Cuenta cuantas veces aparece en la lista el valor que buscamos
print(my_other_list.count(28))

#Insertar un valor en una posición concreta, moviendo el resto de elementos a la derecha una posición más
my_other_list.insert(-2, "Bacho")

#Elimina el primer elemento que identifique
my_other_list.remove(True)

#Elimina el ultimo elemento de la lista y lo devuelve
delete_element = my_other_list.pop()
print("La variable que he eliminado es %s" %(delete_element))

#Si le ponemos una posición eliminaremos el indicado en la lista
my_other_list.pop(2)

print(my_other_list)