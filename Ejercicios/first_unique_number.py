# 🧪 PROBLEMA 5 – firstUniqueNumber
# Enunciado

# Dado un arreglo de enteros nums, encuentra el primer número que aparece solo una vez.
# Si todos se repiten → devuelve -1
# Debes respetar el orden original del arreglo.

# [4, 5, 1, 2, 0, 4] → 5
# [1, 2, 3, 2, 1, 3] → -1
# [7, 8, 7, 8, 9] → 9

def firstUniqueNumber(numbers):
    count = {}

    for num in numbers:
        #“get me dice cuántas veces ya apareció antes; +1 cuenta esta aparición.”
        count[num] = count.get(num, 0) + 1

    for num in numbers:
        if count[num] == 1:
            return num

    return -1

nums1 = firstUniqueNumber([4, 5, 1, 2, 0, 4])
nums2 = firstUniqueNumber([1, 2, 3, 2, 1, 3])
nums3 = firstUniqueNumber([7, 8, 7, 8, 9])
print(nums1)
print(nums2)
print(nums3)