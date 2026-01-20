# 🟢 Transform Array by Parity

# Enunciado:
# Dado un arreglo nums, construye un nuevo arreglo donde:

# si el número es par, guarda su cuadrado

# si el número es impar, guarda el número original

# Entrada: nums = [1, 2, 3, 4]

# Salida: [1, 4, 3, 16]

def transform_array(nums):
    output = []
    for i in nums:
        if i % 2 == 0:
            output.append(i*i)
        else: 
            output.append(i)

    return output

nums = [1, 2, 3, 4]
print(transform_array(nums))