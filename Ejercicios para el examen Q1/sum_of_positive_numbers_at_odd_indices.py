# 🟢 Sum of Positive Numbers at Odd Indices

# Enunciado:
# Dado un arreglo de enteros nums, devuelve la suma de los valores que están en índices impares y son positivos.

# Entrada: nums = [3, -2, 5, 1, -7, 4]

# Salida: 5

# Explicación corta:
# Índices impares → -2, 1, 4
# Positivos → 1 + 4 = 5

#primero recibo datos
#declaro una variable de sum
#recorro con range
#veo si la posicion es impar 
#veo si el numero es positiv
#lo sumo

def find_numbers(nums):
    suma = 0
    for i in range(len(nums)):
        if i % 2 == 1 and nums[i] > 0:
            suma += nums[i]
    return suma
    

nums = [3, -2, 5, 1, -7, 4]
print(find_numbers(nums))