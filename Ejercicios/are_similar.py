# 🧠 Ejercicio 14 — are_similar
# 📌 Enunciado (en español)

# Dadas dos listas de enteros a y b del mismo tamaño, determina si son similares.

# Dos arreglos son similares si:

# Son idénticos, o

# Puedes hacerlos idénticos intercambiando como máximo un par de elementos en uno de ellos

# 🔍 Ejemplos
# a = [1, 2, 3]
# b = [1, 2, 3]
# # True (ya son iguales)

# a = [1, 2, 3]
# b = [2, 1, 3]
# # True (con un swap)

# a = [1, 2, 2]
# b = [2, 1, 1]
# # False (ni con un swap)

def are_similar(a,b):
    #Primero comparo si son exactamente iguales regresamos True
    if a == b:
        return True

    #inicializamos un array para almacenar los diferentes
    diff = []

    #recorremos el array con range estableciendo el final
    for i in range(len(a)):
        #Comparamos los dos array en su posicion si es diferente lo agregamos las pociciones(indices) a la coleccion
        if a[i] != b[i]:
            diff.append(i)

    #Aqui es donde se aplica la regla intercambiando como máximo un par de elementos
    #si tiene mas de 2 elementos diferentes retornamos False
    if len(diff) != 2:
        return False

    #Aqui asiganmos los 2 indices de nuestra coleccion a variables
    i, j = diff

    #Aqui intercambiamos de lugar los valores y realizamos una comparacion que devuelve un boolean
    #es como si compararamos cruzando los 2 valores posicion a[0] == b[1] y posicion a[1] == a[0]
    return a[i] == b[j] and a[j] == b[i]

#a = [1, 2, 3]
#b = [1, 2, 3]
a = [1, 2, 3]
b = [2, 1, 3]
#a = [1, 2, 2]
#b = [2, 1, 1]
#-------------
#a = [1, 2, 3]
#b = [3, 1, 2]
print(are_similar(a,b))