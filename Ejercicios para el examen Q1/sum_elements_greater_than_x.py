# 1️⃣ Sum Elements Greater Than X

# Entrada:

# nums = [1, 5, 3, 8, 2]
# x = 3

# Salida:

# 13

def sum_element(nums, x):
    result = 0
    for i in nums:
        if i > x:
            result += i
    return result

nums = [1, 5, 3, 8, 2]
x = 3
print(sum_element(nums, x))