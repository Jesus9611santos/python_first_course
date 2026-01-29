# Problema

# Se te da un arreglo de enteros nums y un entero k.

# Tu tarea es contar cuántos pares únicos (i, j) existen tales que:

# i < j

# abs(nums[i] - nums[j]) == k

# 👉 Sin usar doble loop (esa es la clave del ejercicio).

# Ejemplo 1
# nums = [1, 5, 3, 4, 2]
# k = 2
# output = 3

#Ejemplo 2
# nums = [1, 2, 2, 3]
# k = 1
# output = 2

#Ejemplo 3
# nums = [1, 1, 1, 2, 2, 3]
# k = 0
# output = 2

#primer paso es entender el problema 
#que quiere hacer? la tarea es contar cuantos pares unicos existen entre todos los numero del array
#nos da la formula para saber si son pares unicos abs(nums[i] - nums[j]) == k
#sabemos que i < j evitar contar el mismo par 2 veces 0,1 bien 1,0 no

# como lo resuelves?
# con fuerza doble loop y voy aplicando la formula a ver?

def fuerza_bruta(nums,k):
    pares = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                a = min(nums[i], nums[j])
                b = max(nums[i], nums[j])
                pares.add((a, b))
    return len(pares)

def hash_map(nums,k):
    suma = 0
    count = {}
    for i in nums:
        count[i] = count.get(i,0) + 1

    for i in count:
        if k + i in count:
            if k > 0:
                suma += 1
            else:
                if count[i] >= 2:
                    suma += 1

    return suma

nums = [1, 5, 3, 4, 2]
k = 2
#3
#nums = [1, 2, 2, 3]
#k = 1
#2
#nums = [1, 1, 1, 2, 2, 3]
#k = 0
#2
print(hash_map(nums,k))