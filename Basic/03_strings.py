### Strings ###

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con un tab"
print(my_tab_string)

#Format
name, surname, age = "Daniel", "Andres", 28
#Al lenguaje le cuesta mucho menos ejecutar esto, que el clasico de concatenar que conociamos
print("Mi nombre es %s %s y mi edad es %d años" %(name, surname, age))
print("Mi nombre es {} {} y mi edad es {} años" .format(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age} años")

#Imprimir caracteres de un String
lenguage = "python"
print(lenguage[0])   #P
print(lenguage[0:3]) #Pyt

#Funciones de los Strings
print(lenguage.capitalize()) #Pone la primera en mayuscula
print(lenguage.upper())      #Pone el String en mayuscula
print(lenguage.lower())      #Pone el texto en minuscula
print(lenguage.count("t"))   #Cuanta cuantos caracteres hay en el String
print(lenguage.isnumeric())  #Devuelve un True si el String es un numero
print("1".isnumeric())