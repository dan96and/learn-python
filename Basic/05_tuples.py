### Tuples ###
#Es como una lista pero inmutable no se puede editar, añadir o eliminar los elementos

#Declaración
my_tuple = tuple()
my_other_tuple = (35, 1.83, "Daniel", "Andres")

#Podemos cambiar el tipo de dato de una tupla a una lista, y poder manipularla
my_tuple = list(my_other_tuple)

print(my_other_tuple)