# 🟢 Count Increasing Pairs
# 📝 Enunciado completo

# Dado un arreglo de enteros nums, cuenta cuántos pares consecutivos (i, i+1) cumplen que:

# nums[i] < nums[i + 1]

# 📥 Entrada
# nums = [1, 3, 2, 4]

# 📤 Salida
# 2

# recibo los datos
# ConnectionAbortedError
# recorro range
# hago la formula 
# valido el extremo para que no se rompa

def count_increasing_pairs(nums):
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            count += 1
    return count

nums = [1, 3, 2, 4]
print(count_increasing_pairs(nums))