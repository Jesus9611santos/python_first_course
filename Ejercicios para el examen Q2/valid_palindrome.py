# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

#if i.isalnum():

def isPalindrome(s):
    word = ""

    for c in s:
        if c.isalnum():
            word += c

    new_s = word.lower()
    left = 0
    right = len(new_s)-1

    while left < right:
         
         if new_s[left] != new_s[right]:
             return False
        
         left += 1
         right -= 1
    
    return True

s = "A man, a plan, a canal: Panama"
s = "race a car"
s = " "
print(isPalindrome(s))