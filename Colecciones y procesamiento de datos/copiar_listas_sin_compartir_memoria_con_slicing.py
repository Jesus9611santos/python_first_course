a = [1,2,3,4,5]
#b=a apunta al mismo lugar en memoria
b = a
print(a)
print(b)

#Solo quiero eliminar un elemento de la lista a pero la modificacion se hace en las 2
del a[0]
print(a)
print(b)

#preguntamos la informacion en memoria.
#id() muestra el identificador en memoria
print(id(a))
print(id(b))

#para no tener el mismo problema que ambas se almacenen en el mismo espacio
#c = a[:] con slicing apuntamos a otro espacio en memoria
c = a[:]
print(id(c))
#Ahora añadiremos un elemento con append para ver si la modificacion solo afecta la lista y no todas
#Esto agregara la modificacion en a y b pero no en c
a.append(6)

print(a)
print(b)
print(c)


