# You are given two strings: pattern and source. The first string pattern contains only the symbols 0 and 1, and the second string source contains only lowercase English letters.

# Your task is to calculate the number of substrings of source that match pattern. 

# We’ll say that a substring source[l..r] matches pattern if the following three conditions are met:
# – The pattern and substring are equal in length.  
# – Where there is a 0 in the pattern, there is a vowel in the substring. 
# – Where there is a 1 in the pattern, there is a consonant in the substring. 

# Vowels are ‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘, and ‘y‘. All other letters are consonants.

# Example

# For pattern = "010" and source = "amazing", the output should be solution(pattern, source) = 2.
# – “010” matches source[0..2] = "ama". The pattern specifies “vowel, consonant, vowel”. “ama” matches this pattern: 0 matches a, 1 matches m, and 0 matches a. 
# – “010” doesn’t match source[1..3] = "maz" 
# – “010” matches source[2..4] = "azi" 
# – “010” doesn’t match source[3..5] = "zin" 
# – “010” doesn’t match source[4..6] = "ing"

# So, there are 2 matches. For a visual demonstration, see the example video. 

# For pattern = "100" and source = "codesignal", the output should be solution(pattern, source) = 0.
# – There are no double vowels in the string "codesignal", so it’s not possible for any of its substrings to match this pattern.

# Guaranteed constraints:
# 1 ≤ source.length ≤ 103
# 1 ≤ pattern.length ≤ 103
# This is a pattern-matching question where instances of a pattern need to be found inside of a larger array. It has the advantage of testing several fundamental programming skills at once: traversing multiple arrays with nested loops, working with subarrays, and performing basic collections/string operations.

# Note that the guaranteed constraints in this question indicate that the candidate shouldn’t worry about optimizing their solution. 

#patron donde 0 es vocal y 1 es consonante retornar el numero de coincidencias
def funcion(pattern,source):
    count = 0
    k = len(pattern)
    vowels =  ['a','e','i','o','u','y']

    for i in range(len(source) - k + 1):
        sub = source[i:i+k]
        valid = True

        for j in range(k):
            if (sub[j] in vowels and pattern[j] != '0') or (sub[j] not in vowels and pattern[j] != '1'):
                valid = False
                break

        if valid:
            count += 1
    
    return count


pattern = "010"
source = "amazing"
pattern = "0"
source = "aeiouy"
pattern = "1"
source = "bcdfg"
pattern = "01"
source = "abab"
pattern = "0"
source = "y"
pattern = "010"
source = "aba"
pattern = "010"
source = "abb"
pattern = "010"
source = "ab"
pattern = "000"
source = "bbbba"
pattern = "10"
source = "bababa"
print(funcion(pattern,source))