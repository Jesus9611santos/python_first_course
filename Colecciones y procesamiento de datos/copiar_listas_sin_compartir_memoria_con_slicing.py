a = [1,2,3,4,5]
b = a
print(a)
print(b)

#Solo quiero eliminar un elemento de la lista a pero la modificacion se hace en las 2
del a[0]
print(a)
print(b)

#preguntamos la informacion en memoria.
print(id(a))
print(id(b))

#para no tener el mismo problema que ambas se almacene 