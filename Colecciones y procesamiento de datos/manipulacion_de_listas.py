to_do = [
    "Dirigirnos al hotel",
    "Ir almorzar",
    "Visitar un museo",
    "Volver al hotel"
]

print(type(to_do))
print(to_do)

numbers = [1,2,3,4,"cinco"]

print(type(numbers))
print(numbers)

mix = ["uno",2,3.14,True,[1,2,3]]
print(mix)

#Al igual que en las cadenas podemos consultar cuantos datos tenemos
print(len(mix))

#la indexacion sirve para rescatar elementos por posicion
print("primer elemento", mix[0])
print("segundo elemento", mix[1])
print("ultimo elemento", mix[-1])

#la indexacion tambien se puede hacer con cadenas
string = "Hola Mundo"
print("primer elemento", string[0])
print("segundo elemento", string[1])
print("ultimo elemento", string[-1])

#El slicing se puede hacer pasando 2 datos en diferentes posiciones
print(mix[0:2])#debemos tomar en cuenta que el segundo parametro le resta 1
print(mix[:2])#Es una buena practica dejar vacio si es 0
print(mix[2:])#En caso de que yo quisiera ir hasta el final dejo vacio el segundo parametro
print(mix[2:-2])

#Metodos
#append añade elementos a la lista aparte osea al final
print(mix)
mix.append(False)
print(mix)
mix.append(["a","b"])
print(mix)

#insert cuando queremos insertar un dato en una posicion
#posicion, elemento
mix.insert(1,["a","b"])
print(mix)

#index pregunta el indice del elemento
#["a","b"] existe 2 veces en esta lista pero index solo encontrara la primera
print(mix.index(["a","b"]))


#max es una funcion para obtener el numero mayor de una lista de datos numericos
numbers = [1,2,100.01,90.45,3,4,5]
print(numbers)
print("Mayor", max(numbers))

#min es para el menor
print("Menor", min(numbers))

#del con esta palabra reservada puedo eliminar una posicion de la lista
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
del numbers #elimina toda la lista
print(numbers)#aqui nos ejecuta un error porque en este punto ya no existe la lista