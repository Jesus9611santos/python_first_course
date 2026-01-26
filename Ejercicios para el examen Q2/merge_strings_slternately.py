# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 
# ok lo primero es entender el problema que debo hacer?
# debo combinar las 2 palabras iterando una y una y si ya no hay mas para convinar poner todas de la que sobren

# ahora como lo hago?
# primero recibo las 2 palabras 
# el problema dice que siempre comience con la palabra uno pero esto no me limita a iterar la mas larga
# veo cual es mayor y esa itero si no la primera 
# despues voy adjuntando a mi variable almacenadora
# y valido si sigue habiando posiciones en la que se termina para que no me marque error la duda es como?

def merge_alternately(word1, word2):
    output = ""
    n1 = len(word1)
    n2 = len(word2)
    iterate_word = max(n1,n2)

    for i in range(iterate_word):
        if i < n1 :
            output += word1[i]

        if i < n2 :
            output += word2[i]
        
    return output

word1 = "abc"
word2 = "pqr"
#word1 = "ab"
#word2 = "pqrs"
#word1 = "abcd"
#word2 = "pq"
print(merge_alternately(word1, word2))