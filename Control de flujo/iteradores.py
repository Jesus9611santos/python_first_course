#ejemplo de iterador

#crear una lista
my_list = [1,2,3,4]

#Creamos el objeto iterador
my_iter = iter(my_list)

#usar el iterador
#next nos ayuda a visualizar cuales son los valores que se van guardando en memoria
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#tambien podemos iterar a travez de cadenas
text = "Hola Mundo"
iter_text = iter(text)
#print(next(iter_text))
#print(next(iter_text))
#print(next(iter_text))
#print(next(iter_text))

#otra forma de iterar puede ser con for
for char in iter_text:
    print(char)


#crear un iterador para los numero impares
#establecemos un limite
limit = 10
#creamos el iterador
#establecemos en range donde inicia el limite y los saltos
odd_itter = iter(range(1,limit+1,2))
for num in odd_itter:
    print(num)