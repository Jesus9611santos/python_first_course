# 🔴 Ejercicio B — Longest Increasing Prefix

# Enunciado:
# Dado un arreglo nums, devuelve la longitud del prefijo creciente más largo
# (el arreglo debe ser estrictamente creciente desde el inicio).

# Entrada:

# nums = [1, 2, 3, 2, 5]


# Salida:

# 3

def longest_increasing_prefix(nums):
    count = 1
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            count += 1
        else:
            break
            
    return count

nums = [1, 2, 3, 2, 5]
nums = [1, 2, 3, 4, 2]
nums = [3, 1, 2, 3]
print(longest_increasing_prefix(nums))