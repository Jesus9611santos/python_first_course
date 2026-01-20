# 🟢 Running Sum of Even Numbers
# 📝 Enunciado completo

# Dado un arreglo de enteros nums, devuelve un nuevo arreglo result del mismo tamaño, donde:

# result[i] es la suma acumulada de SOLO los números pares desde el inicio del arreglo hasta el índice i (incluyéndolo si es par).

# Si en una posición no hay números pares acumulados, el valor será 0.

# 📥 Entrada
# nums = [1, 2, 3, 4, 5]

# 📤 Salida
# [0, 2, 2, 6, 6]


def running_sum(nums):
    result = []
    suma = 0
    for i in nums:
        if i % 2 == 0:
            suma += i
        result.append(suma)
    
    return result

nums = [1, 2, 3, 4, 5]
print(running_sum(nums))