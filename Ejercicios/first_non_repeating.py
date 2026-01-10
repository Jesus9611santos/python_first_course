# 🧪 PROBLEMA 4 – firstNonRepeating

# Enunciado

# Dado un string s, encuentra el primer carácter que NO se repite.
# “Recorre el texto y encuentra el primer carácter que aparece una sola vez en todo el texto.
# Si todos aparecen más de una vez, regresa _.”

def firstNonRepeating(s):
    count = {}

    for ch in s:
        #“get me dice cuántas veces ya apareció antes; +1 cuenta esta aparición.”
        count[ch] = count.get(ch, 0) + 1

    for ch in s:
        if count[ch] == 1:
            return ch

    return '_'

str1 = firstNonRepeating("aabccbd")# → "b"
str2 = firstNonRepeating("aabbcc")# → "_"
str3 = firstNonRepeating("abac")# → "b"

print(str1)
print(str2)
print(str3)