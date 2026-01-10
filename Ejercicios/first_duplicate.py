#🧪 Problema 1: firstDuplicate

#Dado un arreglo de enteros a, encuentra el primer valor que aparece al menos dos veces, 
#donde la segunda aparición tiene el índice más pequeño.

#Si no hay duplicados, regresa -1.

def firstDuplicate(a):
    #set crea una colección de valores únicos, sin llaves (claves) y sin elementos repetidos.
    seen = set()
    
    #recorremos el array
    for num in a:
        
        #verificamos si el numero que estamos recorriendo existe en la coleccion
        if num in seen:
            #si existe este será nuestro resultado
            return num
        
        #si no existe lo agregamos a la coleccion para compararlo en la siguiete corrida
        seen.add(num)

    return -1

response = firstDuplicate([2, 1, 3, 5, 3, 2])
print(response)