### Exceptions ###
try:
    x = 10/0
except ZeroDivisionError as error:
    print("No se puede dividir por cero")
finally:
    print("Esto se ejecuta siempre, independientemente de que falle o no")
    print(error)


try:
    x = 10/0
except Exception: #Controlamos todas las excepciones. (No es lo más optimo, ni recomendable) 
    print("Ha dado un error")