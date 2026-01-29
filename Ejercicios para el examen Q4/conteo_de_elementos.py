# 🔹 Ejercicio 1 (fácil) – Conteo de elementos

# Problema:

# Se te da un arreglo nums.
# Tu tarea: contar cuántas veces aparece cada número y devolverlo como un diccionario.

# Ejemplo
# nums = [1, 2, 2, 3, 1, 2]


# Salida esperada:

# {1: 2, 2: 3, 3: 1}

def count_elements(nums):
    count = {}

    for i in nums:
        count[i] = count.get(i, 0) + 1

    return count
    
nums = [1, 2, 2, 3, 1, 2]
print(count_elements(nums))