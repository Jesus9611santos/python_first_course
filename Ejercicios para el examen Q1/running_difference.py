# 🔴 Ejercicio D — Running Difference

# Enunciado:
# Devuelve un arreglo donde:

# en cada posición guardes
# (cantidad de pares vistos hasta ahora − cantidad de impares vistos hasta ahora)

# Entrada:

# nums = [2, 3, 4, 1]


# Salida:

# [1, 0, 1, 0]

#si es positivo sumo 1 si no es resto
#recibo
#declaro un count
#declaro un array
#recorro con for normal
#valido sies par o impar y manipulo la el count

def running_difference(nums):
    count = 0
    resut = []

    for i in nums:
        if i % 2 == 0:
            count += 1
            resut.append(count)
        else:
            count -= 1
            resut.append(count)

    return resut

nums = [2, 3, 4, 1]
nums = [2, 4, 6]
print(running_difference(nums))