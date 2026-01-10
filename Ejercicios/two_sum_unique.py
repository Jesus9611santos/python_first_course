# 🧪 PROBLEMA 6 – twoSumUnique
# Enunciado

# Dado un arreglo de enteros nums y un número objetivo target, encuentra dos números distintos en el arreglo que sumen exactamente target.
# Devuelve una tupla con esos dos números (num1, num2)
# Si hay múltiples pares, devuelve el primero que aparezca en orden de izquierda a derecha
# Si no hay ningún par → devuelve None

# Ejemplos
# nums = [2, 7, 11, 15], target = 9 → (2, 7)
# nums = [3, 2, 4], target = 6 → (2, 4)
# nums = [1, 2, 3], target = 7 → None

def twoSumUnique(numbers, target):
    numbers_checked = set()
    for num in numbers:
        if target - num in numbers_checked:
            return (target - num, num)
        numbers_checked.add(num)
    return None

first = twoSumUnique([2, 7, 11, 15], 9)
second = twoSumUnique([3, 4, 2, 4], 8)
third = twoSumUnique([1, 2, 3], 7)
print(first)
print(second)
print(third)