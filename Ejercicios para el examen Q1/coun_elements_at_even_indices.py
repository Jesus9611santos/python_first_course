# 2️⃣ Count Elements at Even Indices

# Entrada:

# nums = [4, 7, 1, 9, 2]

# Salida:

# 3

def count_elements(nums):
    total = 0
    
    for i in range(len(nums)):
        if i % 2 == 0:
            total += 1
    return total

nums = [4, 7, 1, 9, 2]
print(count_elements(nums))