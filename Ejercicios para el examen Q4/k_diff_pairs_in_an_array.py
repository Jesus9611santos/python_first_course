# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

# 0 <= i, j < nums.length
# i != j
# |nums[i] - nums[j]| == k
# Notice that |val| denotes the absolute value of val.

 

# Example 1:

# Input: nums = [3,1,4,1,5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.
# Example 2:

# Input: nums = [1,2,3,4,5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
# Example 3:

# Input: nums = [1,3,1,5,4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
 
def fuerza_bruta(nums, k):
    pares = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if k > 0 and nums[i] != nums[j] and abs(nums[i] - nums[j]) == k:
                    a = min(nums[i], nums[j])
                    b = max(nums[i], nums[j])
                    pares.add((a,b))
            
            if k == 0 and nums[i] == nums[j] and abs(nums[i] - nums[j]) == k:
                    a = min(nums[i], nums[j])
                    b = max(nums[i], nums[j])
                    pares.add((a,b))

    return len(pares)

def hash_map(nums, k):
    count = {}
    suma = 0
    for i in nums:
        count[i] = count.get(i,0) + 1

    for i in count:
        if k > 0 and k + i  in count:
            suma += 1

        elif k == 0 and count[i] >= 2:
            suma += 1

    return suma

nums = [3,1,4,1,5]
k = 2
#nums = [1,2,3,4,5]
#k = 1
#nums = [1,3,1,5,4]
#k = 0
print(hash_map(nums, k))