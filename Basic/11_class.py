### Class ###

class Person:
    #Constructor
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    #Función
    def saludar(self):
        print(f"Hola! Soy {self.name}")
    
my_person = Person("Daniel", "Andres", 28)

print(my_person.name)
my_person.saludar()
