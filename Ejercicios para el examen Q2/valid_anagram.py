# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false
# este hay que pensarlo como una bolsa de letras y sacar de una en una primero hay que contar 
# las letras y luego sacar de una en una

def is_anagram(s, t):
    count = {}

    if len(s) != len(t):
        return False
    
    for i in s:
        #vamos a cuantas veces aparece cada letra
        count[i] = count.get(i, 0) + 1

    #vamos a recorrer la segunda palabra para ver si tiene las mismas palabras
    for i in t:
        #le pregunto si existe esa palabra en el conteo si no se rompre no es un anagrama
        if i not in count:
            return False
        
        #le quito la plabra al contador
        count[i] -= 1

        #si al quitar se pone un numero negativo es que ya me termine las palabras entonces en la segunda hay mas por lo cual no es un anagrana
        if count[i] < 0:
            return False
    
    #si no se rompio entonces si es un anagrama
    return True

s = "anagram"
t = "nagaram"
s = "rat"
t = "car"
print(is_anagram(s, t))