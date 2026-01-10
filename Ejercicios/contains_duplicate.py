# 🧪 PROBLEMA 2 – Contains Duplicate

# Dado un arreglo de enteros nums,
# regresa True si algún valor aparece más de una vez,
# si no, regresa False.

def containsDuplicate(nums):
    numbers = set()

    for num in nums:
        if num in numbers:
            return True
        
        numbers.add(num)
    
    return False

nums1 = containsDuplicate([1, 2, 3, 1])
nums2 = containsDuplicate([1, 2, 3, 4])

print(nums1)
print(nums2)