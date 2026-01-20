# 🔹 BLOQUE 1 – PENSAMIENTO (SIN CÓDIGO)

# Ejercicio mental:

# Dado un arreglo de enteros, devuelve la suma de todos los elementos anteriores a cada posición.
# En la posición 0, el valor debe ser 0.

# Ejemplo:

# input: [3, 1, 4, 2]
# output: [0, 3, 4, 8]

#ok resivo el array
#lo recorro
#valido que si es la posicion 0 agregre 0 en la primer posicion
#si no es 0 hago un tipo de slicing window para obtene las demas pociciones
#retorno el array

def array_sum(numbers):
    result = []
    suma = 0

    for num in numbers:
        result.append(suma)
        suma += num

    return result

print(array_sum([3, 1, 4, 2]))


# 🧠 PLANTILLA MENTAL (GUÁRDALA)

# Cuando veas:

# “suma de elementos anteriores”

# Piensa automáticamente:

# acumulador