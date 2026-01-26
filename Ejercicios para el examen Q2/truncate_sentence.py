# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).

# For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
# You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.

 

# Example 1:

# Input: s = "Hello how are you Contestant", k = 4
# Output: "Hello how are you"
# Explanation:
# The words in s are ["Hello", "how" "are", "you", "Contestant"].
# The first 4 words are ["Hello", "how", "are", "you"].
# Hence, you should return "Hello how are you".
# Example 2:

# Input: s = "What is the solution to this problem", k = 4
# Output: "What is the solution"
# Explanation:
# The words in s are ["What", "is" "the", "solution", "to", "this", "problem"].
# The first 4 words are ["What", "is", "the", "solution"].
# Hence, you should return "What is the solution".
# Example 3:

# Input: s = "chopper is not a tanuki", k = 5
# Output: "chopper is not a tanuki"

# que es lo que quiere resolver?
# quiero cortar la horacion solo hasta el numero de paralabras que nos pasan en 4

# como lo resuelves?
#     pienso que la forma mas optima es hacer un split 
#     un range por k y ya no recorrera mas

def truncate_sentence(s, k):
    array = s.split(" ")
    output=""
    for i  in range(k):
        if i == 0:
            output += array[i]
        else:
            output += " "+array[i]
    
    return output
    

s = "Hello how are you Contestant"
k = 4
#s = "What is the solution to this problem"
#k = 4
#s = "chopper is not a tanuki"
#k = 5
print(truncate_sentence(s, k))