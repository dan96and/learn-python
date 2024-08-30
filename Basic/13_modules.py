### Modules ###
import module #Importar un modulo entero
from module import despedir #Importar SOLO una función del modulo
from math import pi as PI_VALUE #Importar SOLO una variable y renombrarla
import random
import reflex as rx

module.saludar()
despedir()

x = random.randint(0,10)
print(x)

print(PI_VALUE)