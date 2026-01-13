# 🧪 EJERCICIO 12 — count_pairs
# 📌 Enunciado

# Dado un arreglo de números enteros nums, cuenta cuántos pares de números iguales existen.

# 👉 Un número puede formar solo un par.
# 👉 Si sobra un número sin pareja, no cuenta.

# 🧠 Ejemplo 1
# nums = [1, 2, 3, 1, 2, 3]
# resultado = 3

def count_pairs(nums):
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    pairs = 0
    for value in count:
        pairs += count[value] // 2

    return pairs

nums = [1, 2, 3, 1, 2, 3]
print(count_pairs(nums))