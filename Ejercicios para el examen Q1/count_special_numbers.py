# 🔴 Ejercicio C — Count Special Numbers

# Enunciado:
# Cuenta cuántos números cumplen ambas condiciones:

# el número es par

# es mayor que el promedio del arreglo

# Entrada:

# nums = [1, 4, 6, 2]

# Salida:

# 1

# recibo los datos
# creo cntador
# saco el promedio
# recorro con for normal
# comparo y sumo
# regreso contador

def count_special_numbers(nums):
    count = 0
    prom = sum(nums) / len(nums)

    for i in nums:
        if i % 2 == 0 and i > prom:
            count += 1
            
    return count

nums = [1, 4, 6, 2]
nums = [1, 2, 3, 4, 5]
print(count_special_numbers(nums))