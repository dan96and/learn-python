### Functions ###
def my_function():
    print("Hola soy una función")

my_function()

#Función con parametros
def my_function_with_params(num1:int, num2:int):
    print(num1+num2)

my_function_with_params(1,1)

#Función con parametros que devuelve un valor
def my_function_with_params_and_return(num1: int, num2: int):
    return num1 + num2

result = my_function_with_params_and_return(2,3)
print(result)