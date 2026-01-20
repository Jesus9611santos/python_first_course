# 3️⃣ Replace Negatives with Zero

# Entrada:

# nums = [-1, 3, -5, 7]


# Salida:

# [0, 3, 0, 7]

def replace_negatives(nums):
    result = []
    for i in nums:
        if i < 0:
            result.append(0)
        else: 
            result.append(i)

    return result 

nums = [-1, 3, -5, 7]
print(replace_negatives(nums))