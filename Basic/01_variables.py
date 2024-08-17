#Variables
#Para escribir las variables se utiliza la nomemclatura snake case y en minusculas
variable = 2

my_string_variable= "My String variable"
print(my_string_variable)

my_int_variable= 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

#Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Hola soy una variable", my_string_variable, "Me gusta imprimir cosas concatenadas")

#Declarar varias variables en una sola linea
name, surname, age = "Daniel", "Andrés", 28
print("Me llamo", name, surname, "y tengo", age, "años")

#Python es un lenguaje de typado debil, podemos "tiparlo" pero solo seria visual, 
#podriamos cambiar el contenido por otro tipo y no daria ningun error
address: str = "Daniel"
address = 32
print(type(address))

#Funciones del sistema
# str() -> Convierte un tipo de dato a str
my_int_to_str_variable = str(my_int_variable)
print(type(my_int_to_str_variable))

#len() -> Indica el tamaño del contenido de la variable
print(len(my_string_variable))

#input() -> Pedir datos por consola
first_name = input("Cual es tu nombre?")
print("Tu nombre es", first_name)
