# 🔴 Ejercicio A — Alternating Sum

# Enunciado:
# Dado un arreglo nums, calcula la suma donde:

# los elementos en índices pares se suman

# los elementos en índices impares se restan

# Entrada:

# nums = [4, 2, 5, 3]


# Salida:

# 4 - 2 + 5 - 3 = 4

def alternating_sum(nums):
    total = 0

    for i in range(len(nums)):
        if i % 2 == 0:
            total += nums[i]
        else:
            total -= nums[i]
    return total

nums = [4, 2, 5, 3]
print(alternating_sum(nums))