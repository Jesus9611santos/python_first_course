# Ejercicio 2 – Primer elemento que se repite

# Problema:
# Dado un arreglo nums, regresa el primer número que se repite
# (el primero cuyo conteo llegue a 2 al recorrer de izquierda a derecha).

# Ejemplo
# nums = [3, 1, 4, 1, 5, 3]


# 3 → aparece 1 vez

# 1 → aparece 1 vez

# 4 → aparece 1 vez

# 1 → aparece 2 veces ← primer repetido

# Salida: 1

def first_repeated(nums):
    seen = set()

    for i in nums:
        if i in seen:
            return i
        seen.add(i)

    return None

nums = [3, 1, 4, 1, 5, 3]
#nums = [1, 1, 2, 3, 4]
#nums = [5, 3, 2, 4, 1, 3]
#nums = [10, 20, 30, 40]
print(first_repeated(nums))