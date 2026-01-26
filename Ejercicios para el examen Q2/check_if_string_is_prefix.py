# Given a string s and an array of strings words, determine whether s is a prefix string of words.

# A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.length.

# Return true if s is a prefix string of words, or false otherwise.

 

# Example 1:

# Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
# Output: true
# Explanation:
# s can be made by concatenating "i", "love", and "leetcode" together.
# Example 2:

# Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
# Output: false
# Explanation:
# It is impossible to make s using a prefix of arr.

def isPrefixString(s, words):
    string = ""
    for i in range(len(words)):
        string += words[i]
        if s == string:
            return True
        
    return False

s = "iloveleetcode"
words = ["i","love","leetcode","apples"]
s = "iloveleetcode"
words = ["apples","i","love","leetcode"]
s = "hello"
words = ["he","llo","world"]
s = "hello"
words = ["he","world","llo"]
s = "a"
words =["aa","aaaa","banana"]
print(isPrefixString(s, words))