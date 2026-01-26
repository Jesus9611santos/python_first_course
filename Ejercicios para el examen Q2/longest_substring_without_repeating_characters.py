# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def length_of_longest_substring(s):
    left = 0
    setsito = set()
    maximum = 0

    for i in range(len(s)):
        while s[i] in setsito:
            setsito.remove(s[left])
            left += 1
        
        setsito.add(s[i])
        maximum = max(maximum, i - left + 1)

    return maximum

s = "abcabcbb"
#s = "bbbbb"
#s = "pwwkew"
print(length_of_longest_substring(s))