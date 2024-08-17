### Sets ###
#Un set no es una estructura ordenada, y no admite valores repetidos

#Declaración de un set
my_set = set()
my_other_set = {}

my_other_set = {"Daniel", "Andres", 28, 1.83}

my_other_set.add("Rojo")

#Comprobar que existen elementos en las listas
print("Daniel" in my_other_set)

#Eliminar todos los valores del set
# my_other_set.clear()

#Recuerda que podemos convertir el set en otro tipo como una list o una tuple
my_list = list(my_other_set)

#Unir dos sets
my_simple_set = {"Java", "Python", "Daniel"}
print(my_other_set.union(my_simple_set))

print(my_other_set)