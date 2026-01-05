#Son funciones anonimas que solo necesitan parametros y una operacion

add = lambda a, b: a + b
print(add(2,2))

multiply = lambda a, b: a * b
print(multiply(3,3))

#cuadrado de cada numero
numbers = range(11)
#map aplica una funcion a cada elemento de una lista
# list() consume el iterador y guarda sus valores en una lista
squared_numbers = list(map(lambda x: x**2, numbers))
print("Cuadrados:",squared_numbers)

#Pares
#filter(función, iterable)
#Recorre un iterable y se queda solo con los elementos
#No transforma el valor (como map), solo decide si pasa o no.
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print("Pares:",even_numbers)