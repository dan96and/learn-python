### Dictionaries ###
#Son listas de clave : valor

my_dict = dict()
my_other_dict = {}

my_other_dict = {
    "Nombre": "Daniel",
    "Apellido": "Andres",
    "Edad": 28,
    1: "Python",
    "Lenguajes":{"Python", "Kotlin", "Java"}
    }

#Acceder a una clave del diccionario
print(my_other_dict["Nombre"])

#Cambiar el valor de una clave del diccionario
my_other_dict["Nombre"] = "Pedro"

#Eliminar una clave del diccionario
my_other_dict.pop(1)

#Comprueba por clave no por valor
print("Nombre" in my_other_dict)


print(my_other_dict.items())
print(my_other_dict.values())
print(my_other_dict.keys())

my_new_list = list(my_other_dict)
print(my_new_list)
print(my_other_dict)