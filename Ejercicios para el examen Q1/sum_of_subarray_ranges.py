# You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

# Return the sum of all subarray ranges of nums.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 4
# Explanation: The 6 subarrays of nums are the following:
# [1], range = largest - smallest = 1 - 1 = 0 
# [2], range = 2 - 2 = 0
# [3], range = 3 - 3 = 0
# [1,2], range = 2 - 1 = 1
# [2,3], range = 3 - 2 = 1
# [1,2,3], range = 3 - 1 = 2
# So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
# Example 2:

# Input: nums = [1,3,3]
# Output: 4
# Explanation: The 6 subarrays of nums are the following:
# [1], range = largest - smallest = 1 - 1 = 0
# [3], range = 3 - 3 = 0
# [3], range = 3 - 3 = 0
# [1,3], range = 3 - 1 = 2
# [3,3], range = 3 - 3 = 0
# [1,3,3], range = 3 - 1 = 2
# So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
# Example 3:

# Input: nums = [4,-2,-3,4,1]
# Output: 59
# Explanation: The sum of all subarray ranges of nums is 59.

def sub_array_ranges(nums):
    #para acumular la sumatoria
    total = 0
    #como el len lo ocupamos varias veces por eso definimos variable
    n = len(nums)
    #hacemos el loop de nums
    for i in range(n):
        #guardamos el valor maximo y minimo de i en realidad es el mismo
        min_val = nums[i]
        max_val = nums[i]

        #este segundo for anidado recorre de i en adelante y va cambiano de posision en cada loop
        for j in range(i, n):
            #obtenemos el minimo real comparando con cada posicion
            min_val = min(min_val, nums[j])
            #obtenemos el maximo real comparando con cada posicion
            max_val = max(max_val, nums[j])
            #sumamos el total
            total += max_val - min_val

    return total 

nums = [1,2,3]
#nums = [1,3,3]
#nums = [4,-2,-3,4,1]
print(sub_array_ranges(nums))