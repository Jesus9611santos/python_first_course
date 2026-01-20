# 4️⃣ Difference Between Even and Odd Sum

# Entrada:

# nums = [1, 2, 3, 4]


# Salida:

# 2

def difference(nums):
    total = 0
    for i in nums:
        if i % 2 == 0:
            total += i
        else:
            total -= i
    return total

nums = [1, 2, 3, 4]
print(difference(nums))